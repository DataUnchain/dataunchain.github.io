---
layout: default
title: "AI Document Processing Architecture for Enterprise Systems — DataUnchain"
lang: en
categories: blog
date: 2026-03-15
author: Antonio Trento
description: "Deep technical dive into AI document processing architecture: ingestion, parsing, vision AI extraction, validation, and enterprise integration layers with diagrams."
---

<article class="pt-36 pb-20 px-6">
  <div class="max-w-3xl mx-auto">

    <span class="text-brand-tealLight text-xs font-bold uppercase tracking-widest">Architecture · 2026</span>
    <h1 class="text-4xl lg:text-5xl font-black font-display mt-4 mb-6">AI Document Processing Architecture for Enterprise Systems</h1>
    <p class="text-gray-400 text-lg leading-relaxed">A technical reference for architects and engineers building production-grade AI document processing systems. Covers the complete architecture from multi-channel ingestion through vision AI inference, mathematical validation, enterprise integration, and deployment — with diagrams and design rationale for each decision.</p>

    <div class="prose prose-invert prose-lg max-w-none text-gray-300 leading-relaxed space-y-6">

      <h2 class="text-2xl font-black font-display text-white mt-12 mb-4">1. Overview: Why Architecture Matters</h2>

      <p>Document processing systems fail in predictable ways. They fail when a corrupted PDF crashes the entire pipeline because exception handling was bolted on as an afterthought. They fail when the AI inference output goes directly to the ERP because there was no validation layer in the design. They fail when authentication tokens expire mid-batch because the integration layer didn't account for session management. They fail when document volume triples and the system has no queue backpressure mechanism.</p>

      <p>These are not AI problems. They are architecture problems. The AI model is one component — typically a small fraction of the total codebase and the most reliable part of the stack. The failures happen in the plumbing: the reception logic, the error routing, the retry semantics, the validation rules, the adapter configuration, the deployment topology.</p>

      <p>This document describes the architecture of a production AI document processing system as actually built and deployed. Every design decision described here was made in response to a real problem encountered in real deployments. Where there are multiple valid approaches, this document explains the tradeoffs and the reasoning behind the chosen approach.</p>

      <div class="bg-brand-teal/10 border border-brand-teal/20 rounded-2xl p-6 my-8">
        <strong class="text-brand-tealLight">KEY INSIGHT:</strong>
        <p class="text-gray-300 mt-2">The hard constraint shaping every architectural decision in DataUnchain is this: no document leaves the on-premise environment. The AI model runs locally. The storage is local. The integrations go outbound to target systems, but no document content travels to any cloud service. This constraint eliminates entire categories of simpler cloud-native architectures and forces every component to be deployable and maintainable on-premise.</p>
      </div>

      <h2 class="text-2xl font-black font-display text-white mt-12 mb-4">2. System Architecture Diagram</h2>

      <div class="bg-brand-surface rounded-2xl p-6 my-8 font-mono text-sm text-gray-300 overflow-x-auto"><pre>
┌─────────────────────────────────────────────────────────────────────┐
│                        RECEPTION LAYER                              │
│                                                                     │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────────────┐  │
│  │  Email   │  │  REST    │  │ Folder   │  │  Telegram Bot    │  │
│  │  (IMAP)  │  │  API     │  │  Watch   │  │  (attachment)    │  │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘  └────────┬─────────┘  │
│       └─────────────┴─────────────┴─────────────────┘            │
│                              │                                      │
│                    ┌─────────▼──────────┐                          │
│                    │   Intake Receiver   │  ← assigns doc_id,       │
│                    │  (async, Celery)    │    stores original,       │
│                    └─────────┬──────────┘    records metadata       │
└──────────────────────────────┼──────────────────────────────────────┘
                               │
┌──────────────────────────────▼──────────────────────────────────────┐
│                        PARSING LAYER                                │
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────┐  │
│  │   Format Normalizer                                          │  │
│  │   PDF / DOCX / Image / Email body → canonical PDF           │  │
│  └────────────────────┬────────────────────────────────────────┘  │
│                        │                                            │
│  ┌─────────────────────▼──────────────────────────────────────┐   │
│  │   PDF Renderer (poppler/pdftoppm)                           │   │
│  │   → [ page_001.png, page_002.png, ... ] at 200 DPI          │   │
│  └────────────────────┬────────────────────────────────────────┘   │
│                        │                                            │
│  ┌─────────────────────▼──────────────────────────────────────┐   │
│  │   Quality Assessor                                          │   │
│  │   DPI check, contrast check, rotation detection            │   │
│  │   → quality_score, preprocessing_flags                     │   │
│  └────────────────────┬────────────────────────────────────────┘   │
└───────────────────────┼────────────────────────────────────────────┘
                         │
┌───────────────────────▼────────────────────────────────────────────┐
│                     AI UNDERSTANDING LAYER                          │
│                                                                     │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │   Prompt Builder                                             │  │
│  │   doc_type + page_images + extraction_schema → prompt        │  │
│  └────────────────────┬─────────────────────────────────────────┘  │
│                        │                                            │
│  ┌─────────────────────▼──────────────────────────────────────┐   │
│  │   Qwen 2.5-VL (via Ollama, local GPU)                      │   │
│  │   Vision-Language Model, 7B or 72B parameters              │   │
│  └────────────────────┬────────────────────────────────────────┘   │
│                        │                                            │
│  ┌─────────────────────▼──────────────────────────────────────┐   │
│  │   JSON Schema Enforcer                                     │   │
│  │   raw LLM output → validated JSON (Pydantic model)         │   │
│  └────────────────────┬────────────────────────────────────────┘   │
└───────────────────────┼────────────────────────────────────────────┘
                         │
┌───────────────────────▼────────────────────────────────────────────┐
│                      VALIDATION LAYER                               │
│                                                                     │
│  ┌───────────────┐  ┌────────────────┐  ┌──────────────────────┐  │
│  │   Math        │  │   Format       │  │   Confidence         │  │
│  │   Validator   │  │   Validator    │  │   Scorer             │  │
│  └───────┬───────┘  └───────┬────────┘  └──────────┬───────────┘  │
│           └────────────────┬┘                       │              │
│                            └───────────┬────────────┘              │
│                                        │                            │
│                         ┌──────────────▼───────────────────────┐   │
│                         │   Audit Status Resolver              │   │
│                         │   VALIDATED / NEEDS_REVIEW /         │   │
│                         │   PENDING_REVIEW                     │   │
│                         └──────────────┬───────────────────────┘   │
└──────────────────────────────────────── ─┼──────────────────────────┘
                                           │
             ┌─────────────────────────────┤
             │                             │
    ┌────────▼─────────┐      ┌────────────▼────────────────────────┐
    │  Human Review    │      │        INTEGRATION LAYER             │
    │  Dashboard       │      │                                      │
    │  (NEEDS_REVIEW)  │      │  ┌──────────┐  ┌────────────────┐  │
    └────────┬─────────┘      │  │  Router  │  │  Dead-Letter   │  │
             │ approved       │  └────┬─────┘  │  Queue         │  │
             └────────────────┤       │        └────────────────┘  │
                              │  ┌────▼──────────────────────────┐ │
                              │  │  Adapter Dispatcher           │ │
                              │  │  (parallel dispatch)          │ │
                              │  └────┬──────────────────────────┘ │
                              │       │                             │
                              │  ┌────▼────────────────────────┐  │
                              │  │  Adapters (18 total)        │  │
                              │  │  SAP B1 / Salesforce /      │  │
                              │  │  FatturaPA / Webhook / ...  │  │
                              │  └─────────────────────────────┘  │
                              └──────────────────────────────────────┘
</pre></div>

      <h2 class="text-2xl font-black font-display text-white mt-12 mb-4">3. The Ingestion Layer</h2>

      <h3 class="text-xl font-bold font-display text-white mt-8 mb-3">Multi-Channel Input</h3>

      <p>Enterprise documents arrive through several channels simultaneously. The ingestion layer must handle all of them without preferencing one over another — a document arriving by email at the same time as one arriving via the REST API must enter the same queue and receive equal processing priority (or configurable priority if business rules require otherwise).</p>

      <p>Email ingestion connects to an IMAP mailbox, polls at a configured interval (typically 60 seconds), and processes all unread messages. For each message, it extracts attachments, handles inline images (some suppliers embed invoice images directly in HTML email bodies), and handles multi-attachment emails by creating one document record per attachment. It marks processed messages as read and optionally moves them to a processed folder. IMAP IDLE is supported for near-real-time processing when polling latency is unacceptable.</p>

      <p>REST API ingestion exposes a FastAPI endpoint at <code class="text-brand-tealLight">/api/v1/documents/upload</code> accepting multipart form data. It supports single file upload, batch upload (up to 50 files per request), and base64-encoded file content for integrations that cannot use multipart. It returns a document ID immediately (accepting the document into the queue) and provides a separate status endpoint for polling progress.</p>

      <p>Folder watch uses the <code class="text-brand-tealLight">watchdog</code> library to monitor one or more filesystem paths for new files. It handles: new file creation events (including slow file transfers where the file is written over several seconds), rename events (files written to a temp path and renamed when complete), and polling fallback for network-mounted filesystems where inotify events may not propagate reliably.</p>

      <h3 class="text-xl font-bold font-display text-white mt-8 mb-3">Format Normalization</h3>

      <p>All documents entering the pipeline are normalized to PDF before parsing. Email text parts are rendered to PDF using a headless browser (Playwright). DOCX files are converted via LibreOffice in headless mode. Images (JPEG, PNG, TIFF) are wrapped in a PDF envelope. This normalization ensures that the parsing layer deals with exactly one format: PDF.</p>

      <p>The normalization step also handles: extracting PDFs from ZIP archives, detecting password-protected PDFs (routed to dead-letter with status <code class="text-brand-tealLight">ENCRYPTED</code>), detecting zero-byte or malformed files (routed with status <code class="text-brand-tealLight">INVALID</code>), and deduplication (SHA-256 hash of the original file content, checked against recent documents to prevent double-processing of the same file arriving via multiple channels).</p>

      <h3 class="text-xl font-bold font-display text-white mt-8 mb-3">Multi-Page Handling</h3>

      <p>Multi-page documents present a specific challenge: which pages contain the information to extract? The system uses two strategies. For known document types with predictable structure (invoices — totals always on the first or last page), the extraction prompt focuses on specific pages. For unknown document types or long contracts, all pages are rendered and passed to the model with instructions to locate relevant information across the full document.</p>

      <p>Practical limit: Qwen 2.5-VL reliably handles up to approximately 10 page images in a single prompt. For documents longer than 10 pages, the system uses a two-pass approach: a first pass to identify which pages contain the relevant information, followed by a focused extraction pass on those pages only.</p>

      <h2 class="text-2xl font-black font-display text-white mt-12 mb-4">4. The Document Parsing Layer</h2>

      <h3 class="text-xl font-bold font-display text-white mt-8 mb-3">PDF to Image Conversion</h3>

      <p>PDF rendering uses <code class="text-brand-tealLight">poppler</code> (via <code class="text-brand-tealLight">pdf2image</code> Python wrapper) at 200 DPI in RGB color space. The choice of 200 DPI is deliberate: it provides sufficient resolution for the model to read 8pt text reliably while keeping image file sizes (and therefore prompt sizes and inference latency) manageable. A single-page invoice at 200 DPI produces an approximately 1.5–3 MB PNG depending on content density.</p>

      <p>The alternatives considered and rejected: 150 DPI is too low for small-font text common in European invoices (8–9pt font for legal notices, tax references, payment terms). 300 DPI doubles file size without proportionate accuracy improvement on electronic PDFs (where the source has infinite resolution). For scanned documents with original resolution below 150 DPI, no amount of upscaling recovers information not present in the scan — the system detects this case and assigns low confidence accordingly.</p>

      <h3 class="text-xl font-bold font-display text-white mt-8 mb-3">Image Preprocessing</h3>

      <p>Quality assessment runs on each rendered page image. It checks: estimated DPI of the original scan (for scanned PDFs, using frequency analysis of text stroke widths), contrast ratio (mean luminance of text pixels vs background pixels), rotation angle (using Hough line transform), and skew angle (using horizontal projection profile analysis).</p>

      <p>When quality flags are raised, preprocessing is applied adaptively:</p>

      <div class="bg-brand-surface rounded-2xl p-6 my-8 font-mono text-sm text-gray-300 overflow-x-auto"><pre>
# Quality-adaptive preprocessing decision logic

def preprocess_page(image: np.ndarray, flags: QualityFlags) -> np.ndarray:
    result = image.copy()

    if flags.rotation_angle != 0:
        result = rotate(result, -flags.rotation_angle)

    if flags.skew_angle > 0.5:  # degrees
        result = deskew(result, flags.skew_angle)

    if flags.contrast_ratio < 3.0:  # low contrast threshold
        result = enhance_contrast(result, method="CLAHE")

    if flags.estimated_dpi < 150:
        # Upscale using Lanczos resampling
        scale_factor = 200 / flags.estimated_dpi
        result = upscale(result, scale_factor, method="LANCZOS")

    return result

# Only preprocess if quality is below threshold
# Avoids unnecessary latency on good-quality documents
</pre></div>

      <p>Preprocessing is never applied to the stored original. The original file, exactly as received, is archived. Preprocessing happens on the copy passed to the AI model.</p>

      <h2 class="text-2xl font-black font-display text-white mt-12 mb-4">5. The AI Understanding Layer</h2>

      <h3 class="text-xl font-bold font-display text-white mt-8 mb-3">How Vision-Language Models Work</h3>

      <p>Qwen 2.5-VL is a transformer model with two input modalities: text tokens and image patch embeddings. When a document image is passed to the model, it is divided into fixed-size patches (typically 14x14 or 16x16 pixels), each patch is encoded into a dense vector embedding, and these visual embeddings are interleaved with the text token embeddings from the prompt. The transformer then attends across both modalities — text and visual — allowing it to answer questions that require understanding both the content and the layout of the document.</p>

      <p>This is fundamentally different from OCR + LLM pipelines (which extract text first, losing all layout information, then process the text) and from template OCR (which looks for content at fixed pixel coordinates). The vision-language model sees the whole page as a human would — understanding that a number in the bottom-right corner of a table is likely a total, that text in a smaller font below the main content area is likely legal fine print, that a bold label followed by a value is a labeled field.</p>

      <h3 class="text-xl font-bold font-display text-white mt-8 mb-3">Prompt Engineering for Structured Extraction</h3>

      <p>The extraction prompt is the most important tunable parameter in the system. A poor prompt produces inconsistent output. A well-engineered prompt produces structured JSON that reliably conforms to the extraction schema.</p>

      <p>The prompt structure used in production:</p>

      <div class="bg-brand-surface rounded-2xl p-6 my-8 font-mono text-sm text-gray-300 overflow-x-auto"><pre>
SYSTEM:
You are a document extraction assistant. Extract information from the
document image provided and return it as JSON conforming exactly to the
schema below. Return only valid JSON — no explanations, no markdown code
blocks, no text before or after the JSON object.

EXTRACTION SCHEMA:
{
  "document_type": "invoice | credit_note | delivery_note | contract | other",
  "supplier_name": "string | null",
  "supplier_vat_number": "string | null",
  "invoice_number": "string | null",
  "invoice_date": "YYYY-MM-DD | null",
  "due_date": "YYYY-MM-DD | null",
  "subtotal_amount": "number | null",
  "vat_rate": "number | null",
  "vat_amount": "number | null",
  "total_amount": "number | null",
  "currency": "EUR | USD | GBP | string",
  "line_items": [
    {
      "description": "string",
      "quantity": "number | null",
      "unit_price": "number | null",
      "line_total": "number"
    }
  ],
  "payment_terms": "string | null",
  "notes": "string | null"
}

RULES:
- Numbers must be extracted as numeric values, not strings.
  "1.000,00" in Italian format → 1000.00
  "1,000.00" in English format → 1000.00
- Dates must be in ISO 8601 format (YYYY-MM-DD).
- If a field is not present in the document, return null.
- Do not infer or calculate values not present in the document.

USER:
[IMAGE: page_001.png]
[IMAGE: page_002.png]  (if multi-page)

Extract all fields from this document.
</pre></div>

      <h3 class="text-xl font-bold font-display text-white mt-8 mb-3">JSON Schema Enforcement</h3>

      <p>LLMs do not always produce valid JSON. The model might include markdown code fences, trailing commas, comments, or simply produce malformed JSON when uncertain. The JSON schema enforcer applies a series of recovery strategies before raising an extraction failure:</p>

      <p>1. Try direct JSON parse. If it succeeds, validate against the Pydantic schema. 2. If parse fails, attempt to extract JSON from markdown code blocks (strip ``` delimiters). 3. If still failing, attempt to fix common JSON errors (trailing commas, unquoted keys) using a lenient JSON parser. 4. If all repair attempts fail, route to NEEDS_REVIEW with extraction_status: PARSE_FAILED. The raw model output is stored for debugging.</p>

      <p>The Pydantic validation step after parsing applies type coercion and constraint checking. A field declared as <code class="text-brand-tealLight">float | None</code> in the schema that receives the string <code class="text-brand-tealLight">"1000.00"</code> is coerced to <code class="text-brand-tealLight">1000.0</code>. A date field that receives <code class="text-brand-tealLight">"01/06/2026"</code> is parsed and normalized to <code class="text-brand-tealLight">"2026-06-01"</code>. Fields that cannot be coerced are set to null and flagged for confidence score reduction.</p>

      <h2 class="text-2xl font-black font-display text-white mt-12 mb-4">6. The Validation Layer</h2>

      <h3 class="text-xl font-bold font-display text-white mt-8 mb-3">Mathematical Validation</h3>

      <p>Mathematical validation implements the accounting relationships that must hold for financial documents. For invoices:</p>

      <div class="bg-brand-surface rounded-2xl p-6 my-8 font-mono text-sm text-gray-300 overflow-x-auto"><pre>
class InvoiceMathValidator:
    TOLERANCE = Decimal("0.02")  # €0.02 rounding tolerance

    def validate(self, doc: InvoiceExtraction) -> list[ValidationError]:
        errors = []

        # Rule 1: subtotal + vat_amount == total_amount
        if all(v is not None for v in [doc.subtotal, doc.vat_amount, doc.total]):
            subtotal = Decimal(str(doc.subtotal))
            vat = Decimal(str(doc.vat_amount))
            total = Decimal(str(doc.total))
            computed = subtotal + vat
            if abs(computed - total) > self.TOLERANCE:
                errors.append(ValidationError(
                    field="total_amount",
                    rule="MATH_TOTAL",
                    expected=str(computed),
                    found=str(total),
                    severity="ERROR"
                ))

        # Rule 2: subtotal * (vat_rate/100) ≈ vat_amount
        if all(v is not None for v in [doc.subtotal, doc.vat_rate, doc.vat_amount]):
            subtotal = Decimal(str(doc.subtotal))
            rate = Decimal(str(doc.vat_rate)) / 100
            vat = Decimal(str(doc.vat_amount))
            computed_vat = subtotal * rate
            if abs(computed_vat - vat) > self.TOLERANCE:
                errors.append(ValidationError(
                    field="vat_amount",
                    rule="MATH_VAT",
                    expected=str(computed_vat.quantize(Decimal("0.01"))),
                    found=str(vat),
                    severity="ERROR"
                ))

        # Rule 3: sum(line_items.line_total) ≈ subtotal
        if doc.line_items and doc.subtotal is not None:
            line_sum = sum(Decimal(str(item.line_total)) for item in doc.line_items)
            subtotal = Decimal(str(doc.subtotal))
            if abs(line_sum - subtotal) > self.TOLERANCE:
                errors.append(ValidationError(
                    field="subtotal_amount",
                    rule="MATH_LINES",
                    expected=str(line_sum),
                    found=str(subtotal),
                    severity="WARNING"  # Lines may not always be complete
                ))

        return errors
</pre></div>

      <p>Note the use of Python's <code class="text-brand-tealLight">Decimal</code> type throughout. Floating-point arithmetic cannot represent monetary values exactly — <code class="text-brand-tealLight">0.1 + 0.2 != 0.3</code> in IEEE 754. Using Decimal for all monetary validation eliminates false positives caused by floating-point rounding.</p>

      <h3 class="text-xl font-bold font-display text-white mt-8 mb-3">Format Validation</h3>

      <p>Format validators check that extracted strings conform to known patterns. Italian-specific validators are included because Italy is a primary deployment market, but the validator registry is extensible:</p>

      <div class="bg-brand-surface rounded-2xl p-6 my-8 font-mono text-sm text-gray-300 overflow-x-auto"><pre>
import re
from luhn import verify as luhn_verify  # third-party

VALIDATORS = {
    "IT_VAT": {
        "pattern": r"^(IT)?(\d{11})$",
        "checksum": lambda digits: it_vat_checksum(digits),
        "error": "Italian VAT number must be 11 digits with valid checksum"
    },
    "IT_FISCAL_CODE": {
        "pattern": r"^[A-Z]{6}\d{2}[A-Z]\d{2}[A-Z]\d{3}[A-Z]$",
        "error": "Italian fiscal code does not match expected format"
    },
    "IBAN": {
        "pattern": r"^[A-Z]{2}\d{2}[A-Z0-9]{4}\d{7}([A-Z0-9]?){0,16}$",
        "checksum": lambda iban: iban_modulo_97_check(iban),
        "error": "IBAN does not pass modulo-97 check"
    },
    "INVOICE_DATE": {
        "check": lambda d: not (d > date.today() or d.year < 2000),
        "error": "Invoice date is in the future or unrealistically old"
    }
}
</pre></div>

      <h3 class="text-xl font-bold font-display text-white mt-8 mb-3">Confidence Scoring Algorithm</h3>

      <p>Confidence scoring aggregates multiple signals into a single score per field and per document. The algorithm:</p>

      <div class="bg-brand-surface rounded-2xl p-6 my-8 font-mono text-sm text-gray-300 overflow-x-auto"><pre>
def compute_document_confidence(
    extraction: dict,
    math_errors: list,
    format_errors: list,
    quality_score: float,
    supplier_history: SupplierHistory | None
) -> float:

    base_score = 1.0

    # Deduct for each math error (major deduction)
    base_score -= len([e for e in math_errors if e.severity == "ERROR"]) * 0.25
    base_score -= len([e for e in math_errors if e.severity == "WARNING"]) * 0.10

    # Deduct for each format error
    base_score -= len(format_errors) * 0.15

    # Deduct for null values in required fields
    required_fields = ["supplier_name", "invoice_number", "invoice_date", "total_amount"]
    null_required = sum(1 for f in required_fields if extraction.get(f) is None)
    base_score -= null_required * 0.10

    # Deduct for poor document quality
    if quality_score < 0.5:
        base_score -= 0.15
    elif quality_score < 0.7:
        base_score -= 0.05

    # Bonus if supplier is known and total matches historical range
    if supplier_history and supplier_history.matches_expected_range(extraction):
        base_score += 0.05

    return max(0.0, min(1.0, base_score))
</pre></div>

      <h3 class="text-xl font-bold font-display text-white mt-8 mb-3">Audit Status Assignment</h3>

      <p>The audit status resolver maps confidence score and validation results to a disposition:</p>

      <div class="bg-brand-surface rounded-2xl p-6 my-8 font-mono text-sm text-gray-300 overflow-x-auto"><pre>
def assign_audit_status(
    confidence: float,
    has_math_errors: bool,
    has_format_errors: bool,
    manual_review_policy: bool
) -> AuditStatus:

    if manual_review_policy:
        return AuditStatus.PENDING_REVIEW

    if has_math_errors:
        # Math errors are always NEEDS_REVIEW — never auto-dispatch
        return AuditStatus.NEEDS_REVIEW

    if has_format_errors:
        return AuditStatus.NEEDS_REVIEW

    if confidence >= 0.85:
        return AuditStatus.VALIDATED

    return AuditStatus.NEEDS_REVIEW
</pre></div>

      <p>The 0.85 confidence threshold is configurable per deployment. Conservative deployments (medical, financial audit) may set it to 0.95. Deployments with high document volumes and lower stakes may set it to 0.75. The threshold should be calibrated against the labeled test set: what confidence score corresponds to what actual error rate on your specific documents?</p>

      <h2 class="text-2xl font-black font-display text-white mt-12 mb-4">7. The Routing and Integration Layer</h2>

      <h3 class="text-xl font-bold font-display text-white mt-8 mb-3">Adapter Pattern</h3>

      <p>The integration layer is built around the adapter pattern. A base abstract class defines the interface — every adapter must implement the same <code class="text-brand-tealLight">dispatch(document: ProcessedDocument) -> DispatchResult</code> method. Each adapter encapsulates the authentication, data mapping, API calls, and error handling specific to its target system.</p>

      <div class="bg-brand-surface rounded-2xl p-6 my-8 font-mono text-sm text-gray-300 overflow-x-auto"><pre>
# Base adapter interface
class BaseAdapter(ABC):
    @abstractmethod
    async def dispatch(self, document: ProcessedDocument) -> DispatchResult:
        """Send document data to the target system."""
        ...

    @abstractmethod
    async def test_connection(self) -> ConnectionStatus:
        """Verify the adapter can reach its target system."""
        ...

# Example adapter implementation: SAP Business One
class SAPBusinessOneAdapter(BaseAdapter):
    def __init__(self, config: SAPConfig):
        self.service_layer_url = config.service_layer_url
        self.company_db = config.company_db
        self._session_token: str | None = None
        self._session_expires: datetime | None = None

    async def _ensure_session(self):
        if self._session_token and datetime.now() < self._session_expires:
            return
        # Authenticate and obtain new session token
        response = await self._client.post(
            f"{self.service_layer_url}/Login",
            json={
                "CompanyDB": self.company_db,
                "UserName": self.config.username,
                "Password": self.config.password
            }
        )
        self._session_token = response.json()["SessionId"]
        self._session_expires = datetime.now() + timedelta(minutes=28)

    async def dispatch(self, document: ProcessedDocument) -> DispatchResult:
        await self._ensure_session()
        payload = self._map_to_sap_invoice(document.extracted_data)
        response = await self._client.post(
            f"{self.service_layer_url}/PurchaseInvoices",
            json=payload,
            headers={"B1SESSION": self._session_token}
        )
        if response.status_code == 201:
            return DispatchResult(success=True, external_id=response.json()["DocNum"])
        return DispatchResult(success=False, error=response.text)
</pre></div>

      <h3 class="text-xl font-bold font-display text-white mt-8 mb-3">Dead-Letter Queue</h3>

      <p>Any document where all configured adapters fail dispatch is moved to the dead-letter queue. The dead-letter queue is not a bin — it is a recoverable error state. Each entry records: which adapters were attempted, what errors were returned, and how many times retry has been attempted. An alerting rule fires when the dead-letter queue grows beyond a configurable threshold, notifying the operations team that integration targets may be down or that credentials need refresh.</p>

      <p>Dead-letter documents are retried on a configurable schedule (default: exponential backoff, starting at 5 minutes, up to 24 hours, maximum 10 retries). After maximum retries are exhausted, the document remains in the dead-letter queue indefinitely — waiting for manual intervention or a manual retry trigger.</p>

      <h3 class="text-xl font-bold font-display text-white mt-8 mb-3">Parallel vs Sequential Dispatch</h3>

      <p>When a document is configured to dispatch to multiple adapters (e.g., create a vendor invoice in SAP B1 and simultaneously post a notification to Slack), the dispatcher sends to all configured adapters in parallel using asyncio gather. Adapter failures are independent — if the Slack notification fails but SAP B1 succeeds, the SAP dispatch is not rolled back. Each adapter's result is recorded independently in the audit log.</p>

      <p>For adapters where order matters (e.g., create a supplier record before creating an invoice for that supplier), sequential dispatch with dependency ordering is configured explicitly. The adapter configuration includes an optional <code class="text-brand-tealLight">depends_on</code> field.</p>

      <h2 class="text-2xl font-black font-display text-white mt-12 mb-4">8. Data Persistence</h2>

      <h3 class="text-xl font-bold font-display text-white mt-8 mb-3">SQLite Schema Design</h3>

      <p>For deployments processing up to several thousand documents per month, SQLite provides sufficient performance with zero infrastructure overhead. The schema:</p>

      <div class="bg-brand-surface rounded-2xl p-6 my-8 font-mono text-sm text-gray-300 overflow-x-auto"><pre>
-- Core documents table
CREATE TABLE documents (
    id              TEXT PRIMARY KEY,          -- UUID
    received_at     TEXT NOT NULL,             -- ISO 8601 datetime
    channel         TEXT NOT NULL,             -- email | api | folder | telegram
    original_path   TEXT NOT NULL,             -- path to archived original file
    filename        TEXT NOT NULL,
    file_hash       TEXT NOT NULL,             -- SHA-256 of original
    page_count      INTEGER,
    doc_type        TEXT,                      -- classified document type
    audit_status    TEXT NOT NULL DEFAULT 'PENDING',
    confidence      REAL,
    reviewed_by     TEXT,                      -- user id if human reviewed
    reviewed_at     TEXT,
    created_at      TEXT NOT NULL DEFAULT (datetime('now'))
);

-- Extracted fields (JSON stored as text for flexibility)
CREATE TABLE extractions (
    id              TEXT PRIMARY KEY,
    document_id     TEXT NOT NULL REFERENCES documents(id),
    extracted_at    TEXT NOT NULL,
    model_name      TEXT NOT NULL,             -- qwen2.5-vl:7b
    raw_output      TEXT,                      -- raw LLM output before parsing
    parsed_data     TEXT,                      -- JSON string of parsed extraction
    parse_status    TEXT NOT NULL,             -- SUCCESS | PARSE_FAILED
    inference_ms    INTEGER                    -- latency tracking
);

-- Validation results
CREATE TABLE validations (
    id              TEXT PRIMARY KEY,
    document_id     TEXT NOT NULL REFERENCES documents(id),
    validated_at    TEXT NOT NULL,
    math_errors     TEXT,                      -- JSON array of ValidationError
    format_errors   TEXT,                      -- JSON array of ValidationError
    confidence      REAL NOT NULL,
    audit_status    TEXT NOT NULL
);

-- Dispatch records
CREATE TABLE dispatches (
    id              TEXT PRIMARY KEY,
    document_id     TEXT NOT NULL REFERENCES documents(id),
    adapter_name    TEXT NOT NULL,
    dispatched_at   TEXT NOT NULL,
    success         INTEGER NOT NULL,          -- 1 | 0
    external_id     TEXT,                      -- ID in target system
    error_message   TEXT,
    retry_count     INTEGER DEFAULT 0
);

-- Human review audit trail
CREATE TABLE review_events (
    id              TEXT PRIMARY KEY,
    document_id     TEXT NOT NULL REFERENCES documents(id),
    event_type      TEXT NOT NULL,             -- OPENED | CORRECTED | APPROVED | REJECTED
    user_id         TEXT NOT NULL,
    occurred_at     TEXT NOT NULL,
    field_name      TEXT,                      -- if CORRECTED
    old_value       TEXT,                      -- if CORRECTED
    new_value       TEXT                       -- if CORRECTED
);
</pre></div>

      <p>For deployments exceeding approximately 100,000 documents, migrating to PostgreSQL is appropriate. The SQLAlchemy ORM layer used throughout the codebase makes this migration straightforward — change the connection string, run Alembic migrations, and the application is running on PostgreSQL without code changes.</p>

      <h3 class="text-xl font-bold font-display text-white mt-8 mb-3">File Archiving</h3>

      <p>Every original document is archived at the path <code class="text-brand-tealLight">/data/archive/{year}/{month}/{document_id}/{original_filename}</code>. This archive is write-once — files are never modified after creation. Rendered page images and preprocessing outputs are stored at <code class="text-brand-tealLight">/data/processing/{document_id}/</code> and may be deleted after successful processing (configurable — some deployments retain them for debugging).</p>

      <h2 class="text-2xl font-black font-display text-white mt-12 mb-4">9. The Human Review Interface</h2>

      <h3 class="text-xl font-bold font-display text-white mt-8 mb-3">Review Dashboard Architecture</h3>

      <p>The review dashboard is a single-page application served by the FastAPI backend. It presents documents with NEEDS_REVIEW or PENDING_REVIEW status in a queue sorted by arrival time. For each document, the reviewer sees:</p>

      <ul class="list-disc pl-6 text-gray-300 space-y-2">
        <li>The original document rendered in the browser (PDF.js viewer or page images)</li>
        <li>The extracted data in editable form fields, side by side with the original</li>
        <li>Validation errors highlighted in red with explanations</li>
        <li>The confidence score and which factors reduced it</li>
        <li>Approve, Reject, and Save &amp; Continue buttons</li>
      </ul>

      <p>The reviewer corrects any extraction errors directly in the form fields. Each correction is recorded in the <code class="text-brand-tealLight">review_events</code> table with the before and after values. When the reviewer approves the document, it is dispatched to the integration layer using the corrected data, and the audit record notes that the data was human-reviewed.</p>

      <h3 class="text-xl font-bold font-display text-white mt-8 mb-3">Approval Workflow</h3>

      <p>For deployments with compliance requirements, a two-person approval workflow is available: a first reviewer corrects and marks as "ready for approval", a second reviewer (typically a finance manager or compliance officer) sees the corrected document and either approves or sends back for further review. This workflow is optional and configured per document type.</p>

      <h2 class="text-2xl font-black font-display text-white mt-12 mb-4">10. Deployment Architecture</h2>

      <div class="bg-brand-surface rounded-2xl p-6 my-8 font-mono text-sm text-gray-300 overflow-x-auto"><pre>
# docker-compose.yml (simplified)

services:
  ollama:
    image: ollama/ollama:latest
    volumes:
      - ollama_models:/root/.ollama
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: 1
              capabilities: [gpu]
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:11434/api/tags"]
      interval: 30s
      timeout: 10s
      retries: 3

  api:
    build: ./api
    ports:
      - "8000:8000"
    volumes:
      - ./data:/data        # document archive and SQLite database
      - ./config:/config    # adapter configuration files
    environment:
      - OLLAMA_HOST=http://ollama:11434
      - DATABASE_URL=sqlite:////data/dataunchain.db
    depends_on:
      ollama:
        condition: service_healthy

  worker:
    build: ./worker
    volumes:
      - ./data:/data
      - ./config:/config
    environment:
      - OLLAMA_HOST=http://ollama:11434
      - DATABASE_URL=sqlite:////data/dataunchain.db
    depends_on:
      - ollama
      - api
    deploy:
      replicas: 2   # scale workers independently from API

  dashboard:
    build: ./dashboard
    ports:
      - "3000:3000"
    environment:
      - API_URL=http://api:8000
    depends_on:
      - api

volumes:
  ollama_models:
</pre></div>

      <p>The services are: <code class="text-brand-tealLight">ollama</code> (AI inference), <code class="text-brand-tealLight">api</code> (FastAPI, REST endpoints, queue management), <code class="text-brand-tealLight">worker</code> (document processing workers, scalable independently), and <code class="text-brand-tealLight">dashboard</code> (review UI). The shared <code class="text-brand-tealLight">/data</code> volume holds the SQLite database and file archive, mounted by both the API and worker services.</p>

      <h2 class="text-2xl font-black font-display text-white mt-12 mb-4">11. Scaling Considerations</h2>

      <h3 class="text-xl font-bold font-display text-white mt-8 mb-3">The Bottleneck Is AI Inference</h3>

      <p>AI inference is the bottleneck in every document processing deployment, by a large margin. PDF rendering takes ~0.3 seconds. Validation takes ~0.05 seconds. Integration dispatch takes ~0.8 seconds. AI inference takes 4–10 seconds per document (with GPU). Every scaling strategy must address inference throughput first.</p>

      <div class="bg-brand-surface rounded-2xl p-6 my-8 font-mono text-sm text-gray-300 overflow-x-auto"><pre>
Throughput scaling options:

┌──────────────────────────────────────────────────────────────────┐
│  Single GPU (RTX 3090)                                           │
│  ~660 docs/hour (single-page invoices)                          │
│  ~6,000 docs/8-hour workday                                     │
│  Suitable for: up to ~120,000 docs/month                        │
├──────────────────────────────────────────────────────────────────┤
│  Two GPUs (2x RTX 3090)                                         │
│  ~1,300 docs/hour                                               │
│  Suitable for: up to ~250,000 docs/month                        │
│  Config: 2x ollama instances, 2x worker containers              │
├──────────────────────────────────────────────────────────────────┤
│  Enterprise GPU (A100 40GB)                                     │
│  ~3,000 docs/hour (larger batch size possible)                  │
│  Suitable for: up to ~600,000 docs/month                        │
│  Config: single ollama instance, multiple workers               │
└──────────────────────────────────────────────────────────────────┘
</pre></div>

      <h3 class="text-xl font-bold font-display text-white mt-8 mb-3">Vertical vs Horizontal Scaling</h3>

      <p>Vertical scaling (bigger GPU in the same machine) is simpler and maintains data locality. Horizontal scaling (multiple machines) requires a shared queue (Redis or RabbitMQ), a shared database (PostgreSQL), and a shared filesystem (NFS or S3-compatible object storage). For most enterprise deployments, vertical scaling to a single high-end GPU is sufficient and significantly simpler to operate.</p>

      <p>Horizontal scaling is appropriate when: single-machine GPU capacity is exhausted, geographic redundancy is required, or documents must be processed in isolated environments (e.g., different business units with strict data separation).</p>

      <h2 class="text-2xl font-black font-display text-white mt-12 mb-4">12. Security Architecture</h2>

      <h3 class="text-xl font-bold font-display text-white mt-8 mb-3">Network Isolation</h3>

      <p>The Docker Compose network is internal by default. Only the API service and dashboard expose ports to the host network — and through the host network, to the office network. Ollama and the database are not accessible from outside the Docker network. This limits the attack surface: even if the office network is compromised, the AI model and database are not directly reachable.</p>

      <p>For high-security deployments, the dashboard is placed behind an authentication reverse proxy (nginx with OAuth2-proxy, or Authentik) and only accessible over VPN. The API is accessible only from known source IPs (the email server, specific integration hosts).</p>

      <h3 class="text-xl font-bold font-display text-white mt-8 mb-3">Credential Management</h3>

      <p>Adapter credentials (ERP passwords, API keys, OAuth tokens) are stored in environment variables or a secrets manager (HashiCorp Vault in enterprise deployments), not in configuration files committed to version control. The adapter configuration file contains only the credential reference (e.g., <code class="text-brand-tealLight">api_key: "$SAP_API_KEY"</code>), and the actual value is injected at runtime from the environment.</p>

      <h3 class="text-xl font-bold font-display text-white mt-8 mb-3">File Access Controls</h3>

      <p>The <code class="text-brand-tealLight">/data/archive</code> directory is readable only by the service account running the API and worker processes. It is not writable by those processes after initial write — a separate archiver process with broader permissions handles the initial write and then removes its write permission. This implements write-once semantics at the filesystem level.</p>

      <h2 class="text-2xl font-black font-display text-white mt-12 mb-4">13. Monitoring and Observability</h2>

      <h3 class="text-xl font-bold font-display text-white mt-8 mb-3">Metrics That Matter</h3>

      <div class="overflow-x-auto my-8">
        <table class="w-full text-sm text-left">
          <thead>
            <tr class="border-b border-white/10 text-gray-400">
              <th class="pb-3 pr-8 font-medium">Metric</th>
              <th class="pb-3 pr-8 font-medium">Normal range</th>
              <th class="pb-3 font-medium">Alert threshold</th>
            </tr>
          </thead>
          <tbody class="text-gray-300">
            <tr class="border-b border-white/5 hover:bg-white/5">
              <td class="py-3 pr-8">Queue depth</td>
              <td class="py-3 pr-8">0–20 documents</td>
              <td class="py-3">&gt;100 for &gt;10 minutes</td>
            </tr>
            <tr class="border-b border-white/5 hover:bg-white/5">
              <td class="py-3 pr-8">VALIDATED rate (7-day rolling)</td>
              <td class="py-3 pr-8">85–95%</td>
              <td class="py-3">&lt;75% (model or quality issue)</td>
            </tr>
            <tr class="border-b border-white/5 hover:bg-white/5">
              <td class="py-3 pr-8">Dead-letter queue size</td>
              <td class="py-3 pr-8">0–5 documents</td>
              <td class="py-3">&gt;20 (integration target issue)</td>
            </tr>
            <tr class="border-b border-white/5 hover:bg-white/5">
              <td class="py-3 pr-8">AI inference p95 latency</td>
              <td class="py-3 pr-8">&lt;15s</td>
              <td class="py-3">&gt;30s (GPU overloaded)</td>
            </tr>
            <tr class="border-b border-white/5 hover:bg-white/5">
              <td class="py-3 pr-8">Dispatch success rate</td>
              <td class="py-3 pr-8">98–100%</td>
              <td class="py-3">&lt;90% (adapter failures)</td>
            </tr>
          </tbody>
        </table>
      </div>

      <p>Metrics are exposed via a Prometheus-compatible <code class="text-brand-tealLight">/metrics</code> endpoint and visualized in a Grafana dashboard. For simpler deployments without Prometheus infrastructure, the same metrics are available via the dashboard UI and written to a time-series log file.</p>

      <h2 class="text-2xl font-black font-display text-white mt-12 mb-4">14. Conclusion</h2>

      <p>The architecture described here has been designed around real constraints: no cloud, no data leaving the network, real enterprise integration targets, real document quality variation, and real human reviewers who need a usable interface. Every component — reception, parsing, AI inference, validation, integration, review, monitoring — has a defined responsibility and a defined failure mode that is handled gracefully.</p>

      <p>The result is a system where the AI model is neither the hero nor the single point of failure. It is one layer in a defense-in-depth architecture where documents that cannot be processed automatically are not silently dropped but routed to a human who can handle them — and where every decision, correction, and dispatch is recorded in an immutable audit trail.</p>

      <h2 class="text-2xl font-black font-display text-white mt-12 mb-4">Frequently Asked Questions</h2>

      <h3 class="text-xl font-bold font-display text-white mt-8 mb-3">Why SQLite instead of PostgreSQL?</h3>
      <p>For deployments processing up to approximately 100,000 documents per month, SQLite is simpler to operate (no separate database server), has no network overhead (file-based access), and is sufficient for the query patterns of a document processing system. SQLite with WAL mode handles concurrent reads from multiple workers without locking issues. The migration path to PostgreSQL is straightforward when volume requires it.</p>

      <h3 class="text-xl font-bold font-display text-white mt-8 mb-3">Why Ollama instead of calling the model API directly?</h3>
      <p>Ollama handles model loading, GPU memory management, request queuing, and model hot-swapping. It exposes a clean REST API that is compatible with the OpenAI API format, making it easy to swap models without changing application code. The alternative — managing the model lifecycle directly in the application — adds significant complexity for little gain.</p>

      <h3 class="text-xl font-bold font-display text-white mt-8 mb-3">Can the system process documents in real time?</h3>
      <p>With GPU acceleration, typical end-to-end latency (receipt to dispatch) is 6–15 seconds for single-page documents. This qualifies as real-time for most business process purposes — an invoice received by email is dispatched to the ERP within 15 seconds of arrival. For applications requiring sub-second latency (interactive use cases), this architecture is not appropriate.</p>

      <h3 class="text-xl font-bold font-display text-white mt-8 mb-3">How are adapter credentials stored securely?</h3>
      <p>In the standard deployment, adapter credentials are stored as environment variables injected at container startup. For higher-security deployments, integration with HashiCorp Vault is supported — the adapter fetches its credentials from Vault at runtime and refreshes them on expiry. Credentials are never stored in the database or in configuration files on disk.</p>

      <h3 class="text-xl font-bold font-display text-white mt-8 mb-3">What is the disaster recovery strategy?</h3>
      <p>The critical data to protect is the SQLite database and the document archive. The recommended backup strategy: daily snapshot of the <code class="text-brand-tealLight">/data</code> volume to a separate disk or NAS, with retention of 90 days. For higher criticality, continuous WAL archiving of the database provides point-in-time recovery. Ollama model weights can be re-pulled from the Ollama registry if lost — they are not business data.</p>

    </div>

    <div class="mt-16 pt-8 border-t border-white/10">
      <div class="bg-gradient-to-r from-brand-teal/20 to-brand-emerald/20 border border-brand-teal/30 rounded-3xl p-8 text-center">
        <h3 class="text-2xl font-black font-display text-white mb-3">Ready to automate your document workflows?</h3>
        <p class="text-gray-400 mb-6">DataUnchain processes your documents locally. No cloud, no data exposure, no subscriptions.</p>
        <a href="mailto:info@dataunchain.com?subject=Demo Request — DataUnchain" class="inline-flex items-center gap-2 px-8 py-3 bg-gradient-to-r from-brand-teal to-brand-emerald text-white font-bold rounded-full hover:opacity-90 transition-opacity">Request a Demo →</a>
      </div>
    </div>

  </div>
</article>
