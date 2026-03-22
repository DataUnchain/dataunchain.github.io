---
layout: default
title: "The Enterprise Document AI Stack (2026) — DataUnchain"
lang: en
categories: blog
date: 2026-03-15
author: Antonio Trento
description: "Complete breakdown of the enterprise document AI stack in 2026: ingestion, storage, extraction, orchestration, and integration layers with tool recommendations."
---

<article class="pt-36 pb-20 px-6">
  <div class="max-w-3xl mx-auto">

    <span class="text-brand-tealLight text-xs font-bold uppercase tracking-widest">Architecture · 2026</span>
    <h1 class="text-4xl lg:text-5xl font-black font-display mt-4 mb-6">The Enterprise Document AI Stack (2026)</h1>
    <p class="text-gray-400 text-lg leading-relaxed">Every enterprise receives documents — invoices, contracts, delivery notes, purchase orders, pay slips. The question is no longer whether to automate document processing, but how to build a stack that is accurate, resilient, and auditable at scale. This guide breaks down every layer of the 2026 enterprise document AI stack, what tools exist at each layer, and how they connect.</p>

    <div class="prose prose-invert prose-lg max-w-none text-gray-300 leading-relaxed space-y-6">

      <h2 class="text-2xl font-black font-display text-white mt-12 mb-4">Why the Stack Framing Matters</h2>
      <p>Most document automation projects fail not because the AI is bad, but because the surrounding infrastructure is fragile. A team pilots a cloud OCR API, it works on the first 50 invoices, and they ship to production. Then a vendor sends a slightly different template, the API returns a confidence of 0.4, there is no validation layer, no review queue, no retry logic — and the wrong values land in the ERP.</p>
      <p>The stack framing forces you to think in layers. Each layer has a specific responsibility. Each layer can be swapped independently. And crucially, failure at one layer should not silently corrupt data at the next. This is the architecture discipline that separates a robust document AI system from a brittle proof of concept.</p>
      <p>In 2026, the baseline expectation for enterprise document AI is: 90%+ straight-through processing rates, sub-5-second extraction latency, full audit trails, and zero data leaving the company perimeter. Meeting all four simultaneously requires a well-designed stack.</p>

      <h2 class="text-2xl font-black font-display text-white mt-12 mb-4">Overview: The 7-Layer Document AI Stack</h2>
      <p>The complete stack has seven layers. Documents flow top-to-bottom. Each layer transforms the representation of the document — from raw bytes to structured business data.</p>

      <div class="bg-brand-surface rounded-2xl p-6 my-8 font-mono text-sm text-gray-300 overflow-x-auto"><pre>
┌─────────────────────────────────────────────────────┐
│  Layer 1: Document Sources & Ingestion               │
│  Email · API · Watchdog · EDI/SDI · Messaging        │
├─────────────────────────────────────────────────────┤
│  Layer 2: Document Parsing & Preprocessing           │
│  PDF rendering · Image normalization · Format conv.  │
├─────────────────────────────────────────────────────┤
│  Layer 3: AI Understanding & Extraction              │
│  VLM inference · Prompt engineering · JSON schema    │
├─────────────────────────────────────────────────────┤
│  Layer 4: Validation & Quality Assurance             │
│  Math checks · Format validation · Confidence score  │
├─────────────────────────────────────────────────────┤
│  Layer 5: Orchestration & Routing                    │
│  Workflow engine · Conditional routing · DLQ         │
├─────────────────────────────────────────────────────┤
│  Layer 6: Integration & Delivery                     │
│  CRM · ERP · Files · Notifications · Webhooks        │
├─────────────────────────────────────────────────────┤
│  Layer 7: Storage & Archiving                        │
│  Document store · Results DB · Feedback loop         │
└─────────────────────────────────────────────────────┘</pre></div>

      <h2 class="text-2xl font-black font-display text-white mt-12 mb-4">Layer 1: Document Sources & Ingestion</h2>
      <p>The ingestion layer is where documents enter the system. It is often underestimated — teams focus on the AI and ignore the ingestion plumbing, then discover production documents arrive via five different channels, each with its own quirks.</p>

      <h3 class="text-xl font-bold font-display text-white mt-8 mb-3">Email Gateways (IMAP Monitoring)</h3>
      <p>Email is the dominant channel for B2B document exchange. Invoices, contracts, and purchase orders arrive as PDF attachments. A robust email ingestion component connects to a dedicated mailbox via IMAP, polls at configurable intervals (or uses IMAP IDLE for push-based notifications), extracts attachments matching defined MIME types, and enqueues them for processing. The sender address, subject line, and email body are metadata worth preserving — they provide context that can improve classification and routing downstream.</p>
      <p>Key considerations: handling multipart MIME messages, deduplication (same invoice forwarded twice), and archiving raw emails for audit purposes before any processing occurs.</p>

      <h3 class="text-xl font-bold font-display text-white mt-8 mb-3">Messaging Platforms</h3>
      <p>WhatsApp Business API and Telegram bots are increasingly used as document submission channels, particularly in SME-to-enterprise supply chains in southern Europe and emerging markets. Documents arrive as photos or files. The ingestion layer must handle image quality that is substantially lower than scanner output — blurry, skewed, and poorly lit photos of physical invoices are common. This makes the preprocessing layer (Layer 2) especially critical for messaging-channel input.</p>

      <h3 class="text-xl font-bold font-display text-white mt-8 mb-3">REST API Uploads</h3>
      <p>For integrations with supplier portals, ERP systems, or custom applications, a REST API endpoint provides a programmatic ingestion channel. The API accepts multipart/form-data uploads or base64-encoded document payloads, returns a job ID for async processing, and exposes a status endpoint for polling. Webhook callbacks on completion eliminate polling overhead for real-time integrations.</p>

      <h3 class="text-xl font-bold font-display text-white mt-8 mb-3">Folder Watchdog</h3>
      <p>Network shares (SMB/NFS mounts) and local directories remain common in on-premise environments where scanners deposit files. A folder watchdog uses filesystem event APIs (inotify on Linux, ReadDirectoryChangesW on Windows) or periodic polling to detect new files, moves them to a processing staging area atomically, and triggers the pipeline. Atomic moves prevent processing of partially written files — a common race condition bug in naive implementations.</p>

      <h3 class="text-xl font-bold font-display text-white mt-8 mb-3">EDI / SDI Channels (Italian E-Invoicing)</h3>
      <p>Italy's Sistema di Interscambio (SDI) is the world's most mature national e-invoicing infrastructure. Every B2B and B2G invoice must transit through SDI as an XML file conforming to the FatturaPA schema. The ingestion layer for Italian enterprises must connect to a certified intermediary (intermediario accreditato) or to the SDI API directly, receive incoming XML invoices, validate their digital signatures, and feed them into the processing pipeline. Similar mandates are expanding across the EU under PEPPOL and the ViDA (VAT in the Digital Age) directive.</p>

      <div class="bg-brand-surface rounded-2xl p-6 my-8 font-mono text-sm text-gray-300 overflow-x-auto"><pre>
Ingestion Layer Tools (2026):

DataUnchain     — Email, API, watchdog, Telegram ingestion (on-premise)
AWS S3 triggers — Lambda-based ingestion from S3 buckets (cloud)
Apache Kafka    — High-throughput event-driven ingestion at scale
Custom webhooks — Point-to-point API integration with any source system
Zapier/n8n      — No-code ingestion routing for SME environments</pre></div>

      <h2 class="text-2xl font-black font-display text-white mt-12 mb-4">Layer 2: Document Parsing & Preprocessing</h2>
      <p>Raw document files — PDFs, images, Word documents — must be converted into a format suitable for AI inference. This is not a trivial step. A poorly rendered PDF page fed to a vision model produces systematically worse extraction than a well-rendered one.</p>

      <h3 class="text-xl font-bold font-display text-white mt-8 mb-3">PDF Rendering Engines</h3>
      <p>PDFs are not images — they are structured containers that may hold vector graphics, embedded fonts, and image objects. Rendering them to images for vision models requires a PDF rendering engine. The de facto standard is Poppler (via pdf2image in Python), which produces accurate renders at configurable DPI. For digitally native PDFs (not scans), pdfplumber offers an alternative approach: extract the text layer directly, bypassing image rendering entirely. This is faster and preserves exact character positions, but fails on scanned documents where the text layer is absent or is OCR-generated.</p>
      <p>DPI selection matters significantly. 150 DPI is fast but loses fine print. 300 DPI is the standard for document AI workloads. 600 DPI is needed for very dense tables or small fonts. Higher DPI increases inference cost proportionally.</p>

      <h3 class="text-xl font-bold font-display text-white mt-8 mb-3">Image Preprocessing</h3>
      <p>For scanned documents and photos, preprocessing dramatically improves AI extraction accuracy. Key transformations include: deskewing (correcting rotation from imperfect scanner placement), denoising (removing scanner artifacts), contrast enhancement (for faded or low-contrast documents), and binarization (for handwritten content). OpenCV and Pillow provide the primitives; production systems typically build a preprocessing pipeline that applies transformations adaptively based on detected image quality metrics.</p>

      <h3 class="text-xl font-bold font-display text-white mt-8 mb-3">Multi-Page Document Handling</h3>
      <p>A purchase order might be 1 page. A construction contract might be 80 pages. The preprocessing layer must split multi-page PDFs into individual page images, process them, and re-associate extracted data with page numbers for audit and review purposes. For long documents, context management across pages is a Layer 3 concern — but the physical splitting and sequencing is a Layer 2 responsibility.</p>

      <div class="bg-brand-surface rounded-2xl p-6 my-8 font-mono text-sm text-gray-300 overflow-x-auto"><pre>
Preprocessing Layer Tools (2026):

pdf2image      — PDF → image conversion via Poppler
PyMuPDF (fitz) — Fast PDF rendering + text extraction
pdfplumber     — Text-layer extraction with positional info
Pillow         — Image transformations (resize, crop, enhance)
OpenCV         — Advanced image processing (deskew, denoise)
Tesseract 5    — OCR pre-pass for text-heavy scanned docs</pre></div>

      <h2 class="text-2xl font-black font-display text-white mt-12 mb-4">Layer 3: AI Understanding & Extraction</h2>
      <p>This is the layer that differentiates the 2026 stack from its predecessors. Vision-Language Models (VLMs) can look at a document image and understand it the way a human would — reading text, interpreting tables, understanding layout context, and extracting structured data according to a schema.</p>

      <h3 class="text-xl font-bold font-display text-white mt-8 mb-3">Vision-Language Models for Document Understanding</h3>
      <p>VLMs accept both image and text inputs. For document AI, the workflow is: render document page to image → construct a prompt asking for specific field extraction → feed image + prompt to the model → receive structured JSON output. The model does not need to be trained on your specific document types. Zero-shot performance — extracting fields from a document type the model has never explicitly seen — is the defining capability of modern VLMs that makes them dramatically more flexible than template-based or form-recognizer approaches.</p>
      <p>The leading open-weight VLMs for document AI in 2026 are our proprietary VLM (72B and 7B variants), LLaMA 3.2-Vision (11B and 90B), and Mistral Pixtral. Each offers different accuracy/speed/size tradeoffs. our proprietary VLM performs particularly well on dense tables and multilingual documents, making it well-suited to European enterprise contexts.</p>

      <h3 class="text-xl font-bold font-display text-white mt-8 mb-3">Prompt Engineering for Structured Extraction</h3>
      <p>The quality of extraction is heavily influenced by prompt design. Effective prompts for document extraction specify: (1) the document type being processed, (2) a complete list of target fields with their expected data types, (3) instructions for handling missing or ambiguous fields, (4) the output format (JSON schema). Few-shot prompting — including 2-3 examples of correctly extracted documents in the prompt — improves accuracy on unusual document layouts at the cost of increased token usage.</p>

      <h3 class="text-xl font-bold font-display text-white mt-8 mb-3">JSON Schema Enforcement</h3>
      <p>Raw model output is text. Converting it to validated structured data requires JSON parsing and schema validation. Models sometimes hallucinate field names, omit required fields, or return malformed JSON. Robust Layer 3 implementations use constrained decoding (grammar-based sampling) to guarantee syntactically valid JSON output, then apply JSON Schema validation to verify semantic correctness. Invalid outputs trigger a retry with a corrective prompt before escalating to human review.</p>

      <div class="bg-brand-surface rounded-2xl p-6 my-8 font-mono text-sm text-gray-300 overflow-x-auto"><pre>
AI Extraction Layer Tools (2026):

Ollama         — Local model runtime (CPU/GPU inference)
our proprietary VLM    — Best-in-class open VLM for documents
LLaMA 3.2-Vision — Meta's vision model (11B / 90B)
Mistral Pixtral — Mistral's document-capable VLM
GPT-4o         — Cloud VLM (OpenAI) — highest accuracy
Gemini 1.5 Pro — Cloud VLM (Google) — long context
vLLM           — High-throughput inference server (on-premise)
DataUnchain    — Orchestrated Ollama inference with schema enforcement</pre></div>

      <div class="bg-brand-teal/10 border border-brand-teal/20 rounded-2xl p-6 my-8">
        <strong class="text-brand-tealLight">KEY INSIGHT:</strong>
        <p class="text-gray-300 mt-2">The choice between cloud VLMs (GPT-4o, Gemini) and on-premise VLMs (our proprietary VLM via Ollama) is not just about cost — it is about data sovereignty. Every document sent to a cloud API is a document that has left your perimeter. For invoices containing supplier terms, contracts with NDAs, and medical records, this is a compliance issue, not just a preference.</p>
      </div>

      <h2 class="text-2xl font-black font-display text-white mt-12 mb-4">Layer 4: Validation & Quality Assurance</h2>
      <p>AI extraction output should never flow directly into business systems without validation. Models make mistakes — they misread digits, confuse fields, hallucinate values not present in the document. The validation layer catches these errors before they corrupt downstream systems.</p>

      <h3 class="text-xl font-bold font-display text-white mt-8 mb-3">Mathematical Validation</h3>
      <p>Invoices have a precise mathematical structure. Line item amounts must equal unit price multiplied by quantity. The sum of all line items must equal the subtotal. Tax amounts must equal the subtotal multiplied by the applicable tax rate. The total must equal subtotal plus tax. Checking these relationships costs microseconds and catches the most common AI extraction errors — digit transpositions, decimal point misplacement, and merged-cell table misreading.</p>

      <h3 class="text-xl font-bold font-display text-white mt-8 mb-3">Format Validation</h3>
      <p>Extracted values must conform to expected formats. Italian fiscal codes (codice fiscale) follow a deterministic algorithm that can be validated checksum-style. VAT numbers (partita IVA) have country-specific formats and check digits. Dates must be parseable and within plausible ranges (an invoice dated in 1987 or 2089 is almost certainly a misread). IBAN numbers have a standard structure verifiable by modulo-97 checksum. Bank account numbers, postal codes, and phone numbers all have format constraints that can be checked without calling external services.</p>

      <h3 class="text-xl font-bold font-display text-white mt-8 mb-3">Confidence Scoring</h3>
      <p>Not all extractions are equally reliable. A clear, high-resolution, digitally-native PDF produces more reliable extractions than a blurry photo of a handwritten receipt. Confidence scores — derived from model log-probabilities, cross-field consistency checks, and image quality metrics — enable the orchestration layer to route low-confidence documents to human review without rejecting them outright. The goal is to maximize straight-through processing for high-confidence documents while ensuring human oversight for uncertain cases.</p>

      <h3 class="text-xl font-bold font-display text-white mt-8 mb-3">Audit Trail</h3>
      <p>Every extraction must produce an immutable audit record: which document was processed, at what time, by which model version, with what prompt, and what output was produced before and after validation. This is not optional for enterprise use — auditors, finance teams, and regulators expect to be able to reconstruct exactly what happened to any given invoice or contract.</p>

      <div class="bg-brand-surface rounded-2xl p-6 my-8 font-mono text-sm text-gray-300 overflow-x-auto"><pre>
Validation Layer Tools (2026):

DataUnchain    — Built-in math validation, format checks, confidence scoring
Custom Python  — Bespoke validation rules for domain-specific documents
Great Expectations — Data quality framework (for high-volume pipelines)
Cerberus       — Lightweight Python schema validation
Pydantic       — Type-safe data validation with Python models</pre></div>

      <h2 class="text-2xl font-black font-display text-white mt-12 mb-4">Layer 5: Orchestration & Routing</h2>
      <p>The orchestration layer is the nervous system of the document AI stack. It coordinates execution across all other layers, handles failures gracefully, and routes documents to the right destination based on their type, content, and processing outcome.</p>

      <h3 class="text-xl font-bold font-display text-white mt-8 mb-3">Conditional Routing</h3>
      <p>Documents are not homogeneous. An invoice from supplier A goes to accounting. An invoice from supplier B (under a different cost center) goes to a different accounting code. A credit note triggers a different workflow than a standard invoice. A contract above a certain value threshold requires legal review. The orchestration layer evaluates routing rules against extracted document data and directs documents to the appropriate downstream handler. Rules may be expressed as decision trees, rule engines, or simple if/else logic depending on complexity.</p>

      <h3 class="text-xl font-bold font-display text-white mt-8 mb-3">Dead-Letter Queue & Retry Logic</h3>
      <p>Processing can fail for many reasons: the AI model is temporarily unavailable, an ERP API returns a 503, a validation rule throws an unexpected exception. The orchestration layer must handle these failures without losing documents. Dead-letter queues hold failed documents for inspection and reprocessing. Exponential backoff retry logic handles transient failures (network timeouts, API rate limits) without human intervention. Persistent failures alert operators and move documents to a human review queue.</p>

      <div class="bg-brand-surface rounded-2xl p-6 my-8 font-mono text-sm text-gray-300 overflow-x-auto"><pre>
Orchestration Layer Tools (2026):

DataUnchain    — Built-in orchestration with rule-based routing
Apache Airflow — DAG-based workflow orchestration (heavyweight)
Prefect        — Modern Python-native workflow orchestration
n8n            — Visual workflow builder (self-hosted)
Temporal       — Durable execution engine for complex workflows
Celery + Redis — Task queue for Python-based pipelines</pre></div>

      <h2 class="text-2xl font-black font-display text-white mt-12 mb-4">Layer 6: Integration & Delivery</h2>
      <p>Extracted, validated, and routed data must reach the business systems that act on it. This layer is where the business value is realized — data moving from a PDF into a live system is the moment that eliminates manual data entry.</p>

      <h3 class="text-xl font-bold font-display text-white mt-8 mb-3">CRM Connectors</h3>
      <p>Contracts and purchase orders extracted by the AI system often contain counterparty data — company names, contact persons, addresses — that belongs in the CRM. Adapters for Salesforce (REST API with bulk write support), HubSpot (Contacts and Deals API), Airtable (REST API), and Notion (Blocks API) enable automatic CRM enrichment from document data. The integration must handle deduplication — matching extracted company names against existing CRM records and updating rather than creating duplicates.</p>

      <h3 class="text-xl font-bold font-display text-white mt-8 mb-3">ERP Connectors</h3>
      <p>Invoice data belongs in the accounting module of an ERP. The specific API varies dramatically by ERP vendor. SAP Business One uses the Service Layer (REST) or DI API (COM). Odoo uses XML-RPC or the newer JSON-RPC interface. Italian ERPs — Zucchetti, TeamSystem, Mexal — each have proprietary APIs or file-based import interfaces. A complete enterprise document AI stack must have adapters for the ERPs in use across the organization. These adapters handle authentication, payload formatting, error handling, and idempotency (ensuring the same invoice is not created twice).</p>

      <h3 class="text-xl font-bold font-display text-white mt-8 mb-3">File Outputs</h3>
      <p>Not every integration target has an API. Legacy systems, batch processing workflows, and accounting software that predates REST APIs often import data via CSV or Excel files. The integration layer must support generating structured file outputs — including FatturaPA XML for Italian e-invoicing — and depositing them in designated locations (SFTP, network share, S3 bucket).</p>

      <h3 class="text-xl font-bold font-display text-white mt-8 mb-3">Notification Channels</h3>
      <p>Humans need to be notified when documents require review, when high-value invoices are processed, or when exceptions occur. Adapters for Slack (Incoming Webhooks), Microsoft Teams (Adaptive Cards), and email (SMTP) provide a notification layer that keeps staff informed without requiring them to poll a dashboard.</p>

      <div class="bg-brand-surface rounded-2xl p-6 my-8 font-mono text-sm text-gray-300 overflow-x-auto"><pre>
Integration Layer — DataUnchain Adapters (2026):

CRM:           Salesforce · HubSpot · Airtable · Notion
ERP:           SAP B1 · Odoo · Zucchetti · TeamSystem · Mexal
Files:         CSV · Excel · FatturaPA XML
Notifications: Email (SMTP) · Slack · Microsoft Teams
Automation:    Webhook (generic) · RPA Playwright · Microsoft 365
Sheets:        Google Sheets</pre></div>

      <h2 class="text-2xl font-black font-display text-white mt-12 mb-4">Layer 7: Storage & Archiving</h2>
      <p>Everything produced by the stack must be persisted — original documents, intermediate representations, extraction results, validation outcomes, and integration logs. Storage is the foundation for auditability, debugging, and future model improvement.</p>

      <h3 class="text-xl font-bold font-display text-white mt-8 mb-3">Document Archiving</h3>
      <p>Original documents must be stored in their original form, unmodified, with a complete chain of custody record. A structured folder hierarchy — organized by date, document type, and counterparty — makes manual retrieval practical. For regulated industries, document retention policies (7 years for accounting documents in Italy) must be enforced programmatically.</p>

      <h3 class="text-xl font-bold font-display text-white mt-8 mb-3">Results Database</h3>
      <p>Extraction results, validation outcomes, and processing metadata belong in a structured database. SQLite is appropriate for single-machine deployments processing hundreds of documents per day. PostgreSQL handles multi-node deployments and provides the query capabilities needed for reporting and audit. The schema should store extraction results as JSONB (or equivalent) to accommodate the variable structure of different document types while enabling efficient querying.</p>

      <h3 class="text-xl font-bold font-display text-white mt-8 mb-3">Feedback Storage for Model Improvement</h3>
      <p>Human corrections to AI extraction errors are gold. When a reviewer corrects a misread invoice total, that correction — original extraction, correct value, document image — is a training signal. Storing corrections in a structured feedback database enables future fine-tuning of the extraction model on domain-specific data, progressively improving accuracy over time on the specific document types the system processes most frequently.</p>

      <h2 class="text-2xl font-black font-display text-white mt-12 mb-4">The Build vs. Buy Decision at Each Layer</h2>

      <div class="overflow-x-auto my-8">
        <table class="w-full text-sm text-left">
          <thead>
            <tr class="border-b border-white/10 text-gray-400">
              <th class="pb-3 pr-8 font-medium">Layer</th>
              <th class="pb-3 pr-8 font-medium">Build Cost</th>
              <th class="pb-3 pr-8 font-medium">Buy Option</th>
              <th class="pb-3 font-medium">Recommendation</th>
            </tr>
          </thead>
          <tbody class="text-gray-300">
            <tr class="border-b border-white/5 hover:bg-white/5">
              <td class="py-3 pr-8">Ingestion</td>
              <td class="py-3 pr-8">2-4 weeks</td>
              <td class="py-3 pr-8">DataUnchain</td>
              <td class="py-3">Buy unless custom channels needed</td>
            </tr>
            <tr class="border-b border-white/5 hover:bg-white/5">
              <td class="py-3 pr-8">Preprocessing</td>
              <td class="py-3 pr-8">1-2 weeks</td>
              <td class="py-3 pr-8">DataUnchain</td>
              <td class="py-3">Buy — low differentiation</td>
            </tr>
            <tr class="border-b border-white/5 hover:bg-white/5">
              <td class="py-3 pr-8">AI Extraction</td>
              <td class="py-3 pr-8">4-8 weeks</td>
              <td class="py-3 pr-8">DataUnchain / cloud APIs</td>
              <td class="py-3">Buy runtime; own prompts</td>
            </tr>
            <tr class="border-b border-white/5 hover:bg-white/5">
              <td class="py-3 pr-8">Validation</td>
              <td class="py-3 pr-8">2-4 weeks</td>
              <td class="py-3 pr-8">DataUnchain</td>
              <td class="py-3">Hybrid — buy base, extend rules</td>
            </tr>
            <tr class="border-b border-white/5 hover:bg-white/5">
              <td class="py-3 pr-8">Orchestration</td>
              <td class="py-3 pr-8">4-12 weeks</td>
              <td class="py-3 pr-8">DataUnchain / Airflow</td>
              <td class="py-3">Buy unless complex custom logic</td>
            </tr>
            <tr class="border-b border-white/5 hover:bg-white/5">
              <td class="py-3 pr-8">Integration</td>
              <td class="py-3 pr-8">2-8 weeks/adapter</td>
              <td class="py-3 pr-8">DataUnchain adapters</td>
              <td class="py-3">Buy standard adapters</td>
            </tr>
            <tr class="border-b border-white/5 hover:bg-white/5">
              <td class="py-3 pr-8">Storage</td>
              <td class="py-3 pr-8">1-2 weeks</td>
              <td class="py-3 pr-8">DataUnchain / custom</td>
              <td class="py-3">Build if complex requirements</td>
            </tr>
          </tbody>
        </table>
      </div>

      <p>A full custom build across all 7 layers requires 6-12 months and a team of 3-5 engineers. DataUnchain covers all 7 layers out of the box, enabling an IT team to focus on configuration and domain-specific rules rather than infrastructure engineering.</p>

      <h2 class="text-2xl font-black font-display text-white mt-12 mb-4">Total Cost of Ownership Comparison</h2>

      <div class="overflow-x-auto my-8">
        <table class="w-full text-sm text-left">
          <thead>
            <tr class="border-b border-white/10 text-gray-400">
              <th class="pb-3 pr-8 font-medium">Scenario</th>
              <th class="pb-3 pr-8 font-medium">Year 1 Cost</th>
              <th class="pb-3 pr-8 font-medium">Year 3 Cost</th>
              <th class="pb-3 font-medium">Data Risk</th>
            </tr>
          </thead>
          <tbody class="text-gray-300">
            <tr class="border-b border-white/5 hover:bg-white/5">
              <td class="py-3 pr-8">Custom build (5 engineers)</td>
              <td class="py-3 pr-8">€400K–€600K</td>
              <td class="py-3 pr-8">€900K–€1.4M</td>
              <td class="py-3">Low (on-premise)</td>
            </tr>
            <tr class="border-b border-white/5 hover:bg-white/5">
              <td class="py-3 pr-8">Cloud APIs (GPT-4o scale)</td>
              <td class="py-3 pr-8">€20K–€100K</td>
              <td class="py-3 pr-8">€60K–€300K</td>
              <td class="py-3">High (cloud exposure)</td>
            </tr>
            <tr class="border-b border-white/5 hover:bg-white/5">
              <td class="py-3 pr-8">DataUnchain (on-premise)</td>
              <td class="py-3 pr-8">Low / fixed</td>
              <td class="py-3 pr-8">Low / fixed</td>
              <td class="py-3">Zero (no cloud)</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="bg-yellow-500/10 border border-yellow-500/20 rounded-2xl p-6 my-8">
        <strong class="text-yellow-400">IMPORTANT:</strong>
        <p class="text-gray-300 mt-2">Cloud API costs scale linearly with document volume. An enterprise processing 50,000 invoices per month with GPT-4o vision (at approximately €0.01–€0.03 per page) faces a significant and growing API bill. On-premise VLM inference via Ollama has near-zero marginal cost — the hardware is a fixed capital expense, not a per-document operating cost.</p>
      </div>

      <h2 class="text-2xl font-black font-display text-white mt-12 mb-4">How DataUnchain Covers All 7 Layers</h2>
      <p>DataUnchain is designed as a complete, on-premise document AI platform that implements all 7 layers of the stack described in this guide. Rather than requiring an engineering team to assemble 7 different tools and integrate them, DataUnchain ships as a single deployable system.</p>
      <p>The ingestion layer handles email (IMAP), REST API uploads, folder watchdog, and messaging platforms. The preprocessing layer renders PDFs via Poppler and applies image normalization. The AI extraction layer runs our proprietary VLM via Ollama with schema-enforced JSON output. The validation layer checks mathematical consistency, format compliance, and assigns confidence scores. The orchestration layer provides rule-based routing and dead-letter queue handling. The integration layer ships 18 production adapters covering CRM, ERP, files, and notifications. The storage layer persists documents, results, and feedback in local SQLite or PostgreSQL.</p>
      <p>Everything runs on your infrastructure. No document leaves your perimeter. No subscription fee scales with volume.</p>

      <h2 class="text-2xl font-black font-display text-white mt-12 mb-4">Frequently Asked Questions</h2>

      <h3 class="text-xl font-bold font-display text-white mt-8 mb-3">What hardware is required to run the full stack on-premise?</h3>
      <p>For DataUnchain VLM 7B (suitable for most enterprise document volumes): a server with 16GB RAM and a modern CPU (no GPU required) can process 50-100 pages per minute. For higher throughput, a GPU with 8-16GB VRAM (NVIDIA RTX 4090 or A-series) increases throughput to 200-500 pages per minute. The 72B model variant requires a multi-GPU setup or a high-end workstation with 48GB+ VRAM.</p>

      <h3 class="text-xl font-bold font-display text-white mt-8 mb-3">Can the stack handle documents in multiple languages?</h3>
      <p>our proprietary VLM has strong multilingual capabilities and performs well on Italian, German, French, Spanish, English, and most major European languages. Mixed-language documents (common in international trade) are handled by specifying the expected language in the extraction prompt or allowing the model to detect language automatically.</p>

      <h3 class="text-xl font-bold font-display text-white mt-8 mb-3">How does the stack handle document types it has not seen before?</h3>
      <p>This is the key advantage of VLMs over template-based systems. A new document type requires writing a new extraction prompt and defining the JSON schema for the target fields. It does not require retraining a model or building a new template. For most new document types, a working extraction configuration can be built and tested in hours rather than weeks.</p>

      <h3 class="text-xl font-bold font-display text-white mt-8 mb-3">What accuracy rates are realistic?</h3>
      <p>On clean, digitally-native PDFs (invoices, contracts from modern software): 95-99% field-level accuracy. On good-quality scans: 90-96%. On photos taken in poor conditions: 75-88%. The validation layer catches a significant fraction of errors in the lower-accuracy categories, and the confidence scoring system routes low-quality documents to human review before they reach business systems.</p>

      <h3 class="text-xl font-bold font-display text-white mt-8 mb-3">Is the stack suitable for regulated industries (healthcare, finance, legal)?</h3>
      <p>On-premise deployment is a prerequisite for regulated industries in Europe. Healthcare documents (containing personal health information) cannot legally be processed by most cloud AI APIs under GDPR and sector-specific regulations. Financial documents may contain information subject to banking secrecy. Legal documents are typically subject to attorney-client privilege. All of these use cases require the data to remain on-premise — which is precisely what this stack architecture provides.</p>

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
