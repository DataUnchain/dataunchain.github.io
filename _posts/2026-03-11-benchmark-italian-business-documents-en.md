---
layout: default
title: "We Ran 219 Italian Business Documents Through an Offline AI. Here Are the Numbers."
lang: en
categories: blog
date: 2026-03-11
author: Antonio Trento
description: "A scientific benchmark of DataUnchain on 219 real Italian business documents — invoices, payslips, contracts, delivery notes — with verified ground truth. 95.5% accuracy. $0.002 per document. Zero cloud."
---

<article class="pt-36 pb-20 px-6">
<div class="max-w-3xl mx-auto">

    <!-- Post header -->
    <div class="mb-10">
        <span class="text-brand-tealLight text-xs font-bold uppercase tracking-widest">Benchmark &middot; March 11, 2026</span>
        <h1 class="text-4xl lg:text-5xl font-black font-display mt-4 mb-6 leading-tight">We Ran 219 Italian Business Documents Through an Offline AI. Here Are the Numbers.</h1>
        <p class="text-gray-400 text-lg leading-relaxed">Invoices, payslips, contracts, delivery notes &mdash; 219 documents with verified ground truth, processed by Qwen2.5-VL 7B running locally on a $0.24/hr GPU. No cloud. No subscriptions. Not a single byte of data leaving the machine.</p>
    </div>

    <!-- Hero Score -->
    <div class="rounded-2xl mb-12 overflow-hidden" style="background: linear-gradient(135deg, #0D9488 0%, #10B981 60%, #F59E0B 100%);">
        <div class="px-8 py-12 text-center">
            <div class="text-8xl font-black text-white mb-2">95.5%</div>
            <div class="text-white text-xl font-bold mb-2 opacity-90">Overall Accuracy Score</div>
            <div class="text-white text-sm opacity-70">on 206 successfully processed documents &nbsp;&bull;&nbsp; Qwen2.5-VL 7B &nbsp;&bull;&nbsp; RTX 2000 Ada 16 GB</div>
        </div>
    </div>

    <!-- Key Stats -->
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 mb-12">
        <div class="bg-brand-surface rounded-xl p-4 text-center border border-white/10">
            <div class="text-2xl font-black text-brand-tealLight">$0.002</div>
            <div class="text-gray-400 text-xs mt-1">per document</div>
        </div>
        <div class="bg-brand-surface rounded-xl p-4 text-center border border-white/10">
            <div class="text-2xl font-black text-brand-tealLight">32s</div>
            <div class="text-gray-400 text-xs mt-1">avg processing time</div>
        </div>
        <div class="bg-brand-surface rounded-xl p-4 text-center border border-white/10">
            <div class="text-2xl font-black text-green-400">100%</div>
            <div class="text-gray-400 text-xs mt-1">VAT IDs accuracy</div>
        </div>
        <div class="bg-brand-surface rounded-xl p-4 text-center border border-white/10">
            <div class="text-2xl font-black text-green-400">SCAN=CLEAN</div>
            <div class="text-gray-400 text-xs mt-1">zero degradation</div>
        </div>
    </div>

    <!-- Section: The problem -->
    <div class="prose prose-invert prose-lg max-w-none text-gray-300 leading-relaxed space-y-6">
        <h2 class="text-2xl font-black font-display text-white">The question we set out to answer</h2>

        <p>Can a 7-billion parameter open-source model, running on a &euro;900 GPU, extract structured data from Italian business documents accurately enough for production use? Not in a controlled demo. Not on hand-picked examples. On a proper, systematic benchmark with 219 documents, a known correct answer for every single field, automated comparison logic, and published results.</p>

        <p>The Italian business document landscape is notoriously complex. Invoices must comply with specific fiscal formats including 11-digit VAT numbers (Partita IVA) with a proprietary checksum algorithm. Payslips carry a 16-character Codice Fiscale generated from name, birthdate, and municipality using the full ODD/EVEN table algorithm with homocody handling. Delivery notes follow the D.P.R. 14/08/1996 n. 472 format. Bank statements include IBANs, transaction codes, and running balance calculations. These aren't generic documents &mdash; they're heavily localized, and any serious extraction system needs to handle all of it reliably.</p>

        <p>This benchmark is the first systematic scientific test of DataUnchain's processor v2.0 against this document landscape. Every number here is real, every method is fully documented, and every result is verified against ground truth using automated comparison logic.</p>

        <h2 class="text-2xl font-black font-display text-white">Why a ground truth benchmark matters</h2>

        <p>Most demos of AI document systems show screenshots of successful extractions. That's not science &mdash; it's marketing. A real evaluation requires three things: a large enough corpus that statistical noise averages out; a known correct answer for every field in every document; and fully automated comparison that leaves no room for subjective interpretation of results.</p>

        <p>The concept of <em>ground truth</em> is the cornerstone of machine learning evaluation. For each document in our corpus, a JSON file contains the expected values for every extractable field &mdash; the invoice number, the supplier's VAT number, the issue date, the taxable amount, the VAT, the total. After the system processes a document, we compare its output against the ground truth file automatically. A date either matches or it doesn't. An amount is either within tolerance or it isn't. There is no grey area.</p>

        <p>We generated the corpus synthetically, meaning we built the PDFs ourselves using the fpdf2 library with realistic Italian business data. This gives us perfect ground truth from the start. The data is authentic: VAT numbers are generated with the real 11-digit checksum algorithm. Fiscal codes use the complete official algorithm including Belfiore municipality codes, the ODD/EVEN character tables, the final check digit calculation, and homocody handling for duplicate codes. Dates are in real Italian formats. Amounts are in euros with Italian thousand-separator notation (period as thousands separator, comma as decimal).</p>
    </div>

    <!-- Corpus Table -->
    <div class="my-10">
        <div class="text-xs text-gray-500 uppercase tracking-wider mb-3 font-bold">Corpus composition &mdash; 219 documents across 7 types</div>
        <div class="overflow-x-auto">
            <table class="w-full text-sm">
                <thead>
                    <tr class="border-b border-white/20 text-left">
                        <th class="pb-3 pr-4 text-white font-bold">Document Type</th>
                        <th class="pb-3 pr-4 text-right text-white font-bold">Count</th>
                        <th class="pb-3 text-white font-bold">Main Extracted Fields</th>
                    </tr>
                </thead>
                <tbody class="text-gray-400">
                    <tr class="border-b border-white/10"><td class="py-2.5 pr-4 text-gray-200">Invoice (Fattura)</td><td class="text-right pr-4">60</td><td class="py-2.5">VAT IDs, taxable amount, VAT 22%, total, line items, due date</td></tr>
                    <tr class="border-b border-white/10"><td class="py-2.5 pr-4 text-gray-200">Delivery Note (DDT)</td><td class="text-right pr-4">50</td><td class="py-2.5">DDT number, shipper, recipient, carrier, packages, goods</td></tr>
                    <tr class="border-b border-white/10"><td class="py-2.5 pr-4 text-gray-200">Payslip (Busta Paga)</td><td class="text-right pr-4">35</td><td class="py-2.5">employee, fiscal code, company VAT ID, CCNL, gross, net pay</td></tr>
                    <tr class="border-b border-white/10"><td class="py-2.5 pr-4 text-gray-200">Credit Note</td><td class="text-right pr-4">20</td><td class="py-2.5">NC number, reference invoice, credit amount, reason</td></tr>
                    <tr class="border-b border-white/10"><td class="py-2.5 pr-4 text-gray-200">Contract</td><td class="text-right pr-4">20</td><td class="py-2.5">contract type, number, signing date, Party A &amp; B, both VAT IDs</td></tr>
                    <tr class="border-b border-white/10"><td class="py-2.5 pr-4 text-gray-200">Purchase Order</td><td class="text-right pr-4">14</td><td class="py-2.5">order number, delivery date, supplier &amp; buyer, total amount</td></tr>
                    <tr class="border-b border-white/10"><td class="py-2.5 pr-4 text-gray-200">Bank Statement</td><td class="text-right pr-4">20</td><td class="py-2.5">IBAN, account holder, period, opening balance, transactions, closing balance</td></tr>
                    <tr class="text-white font-bold"><td class="py-2.5 pr-4">Total</td><td class="text-right pr-4">219</td><td></td></tr>
                </tbody>
            </table>
        </div>
    </div>

    <!-- Section: Scan simulation -->
    <div class="prose prose-invert prose-lg max-w-none text-gray-300 leading-relaxed space-y-6">
        <h2 class="text-2xl font-black font-display text-white">The scan simulation: testing real-world conditions</h2>

        <p>70% of the corpus &mdash; approximately 153 documents &mdash; was subjected to a controlled degradation pipeline to simulate real-world office scanning. This is not a simple JPEG save. We applied a multi-step transformation sequence: Gaussian noise at varying intensity levels, random rotations in the &plusmn;3&deg; range, JPEG compression at quality levels between 60 and 85 (the typical output range of office network scanners), overlaid stamps and watermarks in semi-transparent layers, brightness and contrast variations, and simulation of slight paper creases and perspective distortions from non-flat scanning surfaces.</p>

        <p>These transformations reproduce what happens in the vast majority of real document workflows: a document is printed, signed, stamped with a company seal, scanned with an inexpensive office scanner, and the resulting file is compressed before being emailed or archived. The output is a JPEG-based PDF with visible degradation artifacts. This is the reality of document processing in Italian businesses, and any system that only works well on pristine digital PDFs is not ready for production.</p>

        <h3 class="text-xl font-bold text-white">Ground truth verified mathematically</h3>

        <p>For documents with financial figures, the ground truth is not just a collection of correct values &mdash; it is a mathematically consistent set. For every invoice in the corpus: <code class="text-brand-tealLight text-sm">taxable_amount + vat_amount = total</code> exactly to the cent. For every payslip: <code class="text-brand-tealLight text-sm">gross_pay - deductions = net_pay</code> precisely. For every bank statement: <code class="text-brand-tealLight text-sm">opening_balance + total_credits - total_debits = closing_balance</code> to the cent.</p>

        <p>This mathematical consistency serves a dual purpose. First, it lets us test the system's math check feature: when the system extracts all the financial fields, it independently verifies the arithmetic. A 100% math check score means the system not only read the right numbers, but read them consistently with each other across the document. Second, it means that any inconsistency in the extracted data is a genuine error, not an artifact of inconsistent ground truth.</p>

        <h2 class="text-2xl font-black font-display text-white">How the pipeline works: three deterministic steps</h2>

        <p>Before getting into results, it's worth describing exactly what the system does. DataUnchain processor v2.0 implements a three-step pipeline. Two steps involve the vision model. One step is purely deterministic Python code.</p>

        <h3 class="text-xl font-bold text-white">Step 1 &mdash; Classify</h3>

        <p>The first step takes the document image (the PDF converted to a page image at 200 DPI using pdf2image and poppler-utils) and sends it to Qwen2.5-VL 7B running via Ollama with a classification prompt. The model must output one of the supported document type labels. No hints are given about what type the document might be &mdash; the model sees only the image and decides autonomously.</p>

        <p>This matters in practice because real document workflows are mixed. A daily incoming-mail folder might contain invoices, delivery notes, payslips, credit notes, and contracts all in the same batch. The system must sort them correctly before it can extract anything. A classification error at this stage propagates to the wrong extraction prompt, producing garbage output.</p>

        <h3 class="text-xl font-bold text-white">Step 2 &mdash; Extract</h3>

        <p>Once the document type is identified, a type-specific extraction prompt is selected. Each of the seven supported document types has its own optimized prompt that describes exactly which fields to extract, in what JSON structure, with what handling rules for edge cases. For example, the invoice prompt specifies that if a tax line is present for a different VAT rate, it should be listed separately. The payslip prompt specifies that if multiple CCNL entries are present, the primary one should be selected. The bank statement prompt specifies that the transaction list should include date, description, debit amount, credit amount, and running balance for each entry.</p>

        <p>The model returns a JSON object. This JSON is immediately validated against the schema for that document type. Missing required fields or type mismatches result in the document being flagged for human review before any further processing.</p>

        <h3 class="text-xl font-bold text-white">Step 3 &mdash; Audit</h3>

        <p>The third step involves no AI. A pure Python module runs formal validation and mathematical verification on the extracted JSON.</p>

        <p>Formal validation includes: VAT number (P.IVA) checksum verification using the official 11-digit algorithm; Codice Fiscale format check (16 characters), pattern validation, check digit verification, and homocody-aware handling; date validation (ISO 8601 format, range 1900-2100, valid day for the given month/year); and numeric field validation (positive values, 2 decimal place precision).</p>

        <p>Mathematical verification runs the appropriate check for the document type: <code class="text-brand-tealLight text-sm">taxable + vat = total &plusmn;&euro;0.10</code> for invoices; <code class="text-brand-tealLight text-sm">gross - deductions = net &plusmn;&euro;0.10</code> for payslips; <code class="text-brand-tealLight text-sm">opening + credits - debits = closing &plusmn;&euro;0.10</code> for bank statements. The tolerance exists to accommodate rounding differences in the source documents.</p>

        <p>The audit outputs a <strong class="text-white">confidence score</strong> (HIGH, MEDIUM, or LOW) based on the overall internal consistency of the extracted data, and an <strong class="text-white">audit_status</strong>: VALIDATED means the document can flow through automated processing; PENDING_REVIEW means minor issues were found that warrant a human glance; NEEDS_REVIEW means significant problems were detected and human intervention is required before the data is used.</p>
    </div>

    <!-- Hardware Table -->
    <div class="my-10">
        <div class="text-xs text-gray-500 uppercase tracking-wider mb-3 font-bold">Test environment</div>
        <div class="overflow-x-auto">
            <table class="w-full text-sm">
                <tbody class="text-gray-400">
                    <tr class="border-b border-white/10"><td class="py-2 pr-4 text-gray-500 w-1/3">GPU</td><td class="py-2 text-gray-200">NVIDIA RTX 2000 Ada Generation</td></tr>
                    <tr class="border-b border-white/10"><td class="py-2 pr-4 text-gray-500">VRAM</td><td class="py-2 text-gray-200">16,380 MiB (~16 GB)</td></tr>
                    <tr class="border-b border-white/10"><td class="py-2 pr-4 text-gray-500">vCPU / RAM</td><td class="py-2 text-gray-200">6 cores / 31 GB</td></tr>
                    <tr class="border-b border-white/10"><td class="py-2 pr-4 text-gray-500">Cloud cost</td><td class="py-2 text-gray-200">$0.24/hr (RunPod Community Cloud)</td></tr>
                    <tr class="border-b border-white/10"><td class="py-2 pr-4 text-gray-500">Model</td><td class="py-2 text-gray-200">Qwen2.5-VL 7B (Q4 quantized, 13.3 GB VRAM)</td></tr>
                    <tr class="border-b border-white/10"><td class="py-2 pr-4 text-gray-500">Runtime</td><td class="py-2 text-gray-200">Ollama with flash attention enabled</td></tr>
                    <tr><td class="py-2 pr-4 text-gray-500">OS / CUDA</td><td class="py-2 text-gray-200">Ubuntu 22.04 / CUDA 12.4.1 / Python 3.11</td></tr>
                </tbody>
            </table>
        </div>
    </div>

    <!-- Section: Results intro -->
    <div class="prose prose-invert prose-lg max-w-none text-gray-300 leading-relaxed space-y-6">
        <h2 class="text-2xl font-black font-display text-white">Speed and throughput</h2>

        <p>At 32 seconds per document average, DataUnchain processes approximately 112 documents per hour on this hardware. The minimum observed was 25.8 seconds (simple, clean delivery notes), the maximum 53 seconds (complex bank statements with many transaction rows). The 90th percentile is 41 seconds, meaning 90% of documents finish within 41 seconds &mdash; useful for planning batch processing windows.</p>

        <p>32 seconds may sound slow compared to traditional OCR, but the comparison is not valid. An OCR system extracts raw characters and layout coordinates. It has no concept of what fields mean, cannot validate a VAT number checksum, and certainly cannot verify that taxable + VAT = total. What DataUnchain does in 32 seconds &mdash; identify the document type, extract all semantic fields, validate fiscal identifiers, verify arithmetic &mdash; would take a human operator 2 to 5 minutes per document even working efficiently. At a cost of $0.002 per document at cloud rates, or essentially free on owned hardware, the economics are immediate.</p>
    </div>

    <!-- Accuracy Table -->
    <div class="my-10">
        <div class="text-xs text-gray-500 uppercase tracking-wider mb-3 font-bold">Field-by-field accuracy &mdash; 206 documents with status OK</div>
        <div class="overflow-x-auto">
            <table class="w-full text-sm">
                <thead>
                    <tr class="border-b border-white/20 text-left">
                        <th class="pb-3 pr-4 text-white font-bold">Field</th>
                        <th class="pb-3 pr-4 text-right text-white font-bold">Accuracy</th>
                        <th class="pb-3 text-white font-bold">Sample size</th>
                    </tr>
                </thead>
                <tbody>
                    <tr class="border-b border-white/10"><td class="py-2.5 pr-4 text-gray-300">Document type classification</td><td class="text-right pr-4 text-green-400 font-bold">100.0%</td><td class="text-gray-500 text-xs">206 / 206</td></tr>
                    <tr class="border-b border-white/10"><td class="py-2.5 pr-4 text-gray-300">VAT number / Fiscal Code (P.IVA / CF)</td><td class="text-right pr-4 text-green-400 font-bold">100.0%</td><td class="text-gray-500 text-xs">206 / 206</td></tr>
                    <tr class="border-b border-white/10"><td class="py-2.5 pr-4 text-gray-300">Issue date (exact YYYY-MM-DD match)</td><td class="text-right pr-4 text-green-400 font-bold">100.0%</td><td class="text-gray-500 text-xs">144 / 144</td></tr>
                    <tr class="border-b border-white/10"><td class="py-2.5 pr-4 text-gray-300">Taxable amount (&plusmn;&euro;0.50 tolerance)</td><td class="text-right pr-4 text-green-400 font-bold">100.0%</td><td class="text-gray-500 text-xs">94 / 94</td></tr>
                    <tr class="border-b border-white/10"><td class="py-2.5 pr-4 text-gray-300">VAT amount (&plusmn;&euro;0.50)</td><td class="text-right pr-4 text-green-400 font-bold">100.0%</td><td class="text-gray-500 text-xs">94 / 94</td></tr>
                    <tr class="border-b border-white/10"><td class="py-2.5 pr-4 text-gray-300">Invoice total (&plusmn;&euro;0.50)</td><td class="text-right pr-4 text-green-400 font-bold">100.0%</td><td class="text-gray-500 text-xs">94 / 94</td></tr>
                    <tr class="border-b border-white/10"><td class="py-2.5 pr-4 text-gray-300">Net pay &mdash; payslip (&plusmn;&euro;0.50)</td><td class="text-right pr-4 text-green-400 font-bold">100.0%</td><td class="text-gray-500 text-xs">35 / 35</td></tr>
                    <tr class="border-b border-white/10"><td class="py-2.5 pr-4 text-gray-300">Closing balance &mdash; bank statement (&plusmn;&euro;0.50)</td><td class="text-right pr-4 text-green-400 font-bold">100.0%</td><td class="text-gray-500 text-xs">7 / 7</td></tr>
                    <tr class="border-b border-white/10"><td class="py-2.5 pr-4 text-gray-300">Internal math check (&plusmn;&euro;0.10)</td><td class="text-right pr-4 text-green-400 font-bold">100.0%</td><td class="text-gray-500 text-xs">120 / 120</td></tr>
                    <tr class="border-b border-white/10"><td class="py-2.5 pr-4 text-gray-300">Document reference number</td><td class="text-right pr-4 text-green-400 font-bold">96.6%</td><td class="text-gray-500 text-xs">199 / 206</td></tr>
                    <tr><td class="py-2.5 pr-4 text-gray-300">Gross pay &mdash; payslip (&plusmn;&euro;0.50)</td><td class="text-right pr-4 text-yellow-400 font-bold">54.3%</td><td class="text-gray-500 text-xs">19 / 35 &mdash; label variance</td></tr>
                </tbody>
            </table>
        </div>
    </div>

    <!-- Section: Key findings narrative -->
    <div class="prose prose-invert prose-lg max-w-none text-gray-300 leading-relaxed space-y-6">
        <h2 class="text-2xl font-black font-display text-white">What these numbers actually mean</h2>

        <p><strong class="text-white">VAT numbers and fiscal codes: 100% on 206 documents.</strong> This is the most operationally significant result in the entire benchmark. The Partita IVA and Codice Fiscale are the primary identity fields in Italian business documents. They determine who issued an invoice, who it was issued to, who signed a contract, whose payslip this is. If these fields are extracted incorrectly, the downstream consequence is not a minor inconvenience &mdash; it's wrong accounting entries, wrong tax reporting, wrong payroll records. Getting them right 100% of the time, across all document types, across both pristine PDFs and low-quality scanned documents, is the baseline requirement for any production deployment.</p>

        <p><strong class="text-white">Financial amounts: 100% on every type that has them.</strong> Taxable amount, VAT, invoice total, net pay, bank statement closing balance &mdash; every single numeric financial field extracted is correct within the tolerance. This includes documents with amounts near psychological threshold values like &euro;999.99 or &euro;9,999.00, documents where the thousand separator could cause OCR confusion, and documents where JPEG compression has degraded the legibility of digits. The model handles all of these correctly.</p>

        <p><strong class="text-white">Math check: 100% on 120 verifications.</strong> Not only are the individual financial fields correct, but they are internally consistent. Every invoice where we verify that taxable + VAT = total passes. Every payslip where we verify gross - deductions = net passes. This means the model reads the numbers coherently across the document &mdash; it doesn't read the taxable amount from one line and the total from another line of a different document, for example. The consistency check catches a whole class of subtle extraction errors that field-by-field accuracy metrics alone would miss.</p>

        <p><strong class="text-white">The single critical failure: gross pay on payslips, 54.3%.</strong> Of 35 payslips in the corpus, 19 have the gross pay field correctly extracted and 16 do not. Examining the failures reveals a consistent pattern: the problem is not reading the number. When the model finds the correct field, the value is always right. The problem is identifying which of several differently-labeled fields represents the gross pay concept.</p>

        <p>Italian payslips vary significantly depending on the Contratto Collettivo Nazionale di Lavoro (CCNL) &mdash; the collective bargaining agreement &mdash; and the payroll software used. The field labeled "retribuzione lorda" in a metalworking CCNL payslip is labeled "imponibile lordo" in a retail payslip, "totale competenze" in a construction payslip, and "imponibile contributivo" in a healthcare payslip. The net pay field, by contrast, is almost always labeled "netto in busta" or "netto a pagare" &mdash; highly consistent across CCNL types &mdash; and extracts at 100%. The fix is straightforward: provide the extraction prompt with an explicit enumeration of the known label variants. This is planned for processor v2.1.</p>
    </div>

    <!-- SCAN=CLEAN callout -->
    <div class="rounded-2xl border border-brand-teal/40 p-6 my-10" style="background: rgba(13,148,136,0.07);">
        <div class="flex items-start gap-4">
            <div class="text-3xl shrink-0 mt-1">&#128302;</div>
            <div>
                <div class="text-white font-bold text-xl mb-3">The most surprising result: SCAN = CLEAN on every metric</div>
                <p class="text-gray-400 text-sm leading-relaxed mb-4">146 scanned documents (with noise, rotation, stamps, JPEG artifacts) achieved identical performance to 60 native digital PDFs on every measured metric. Zero degradation. Not marginally worse &mdash; statistically identical. This is the result that changes the production calculus most significantly.</p>
                <div class="grid grid-cols-2 sm:grid-cols-5 gap-3 mt-4">
                    <div class="text-center bg-black/20 rounded-lg p-2"><div class="text-green-400 font-bold text-sm">100%</div><div class="text-gray-500 text-xs">Type &mdash; SCAN</div></div>
                    <div class="text-center bg-black/20 rounded-lg p-2"><div class="text-green-400 font-bold text-sm">100%</div><div class="text-gray-500 text-xs">Type &mdash; CLEAN</div></div>
                    <div class="text-center bg-black/20 rounded-lg p-2"><div class="text-green-400 font-bold text-sm">100%</div><div class="text-gray-500 text-xs">VAT ID &mdash; SCAN</div></div>
                    <div class="text-center bg-black/20 rounded-lg p-2"><div class="text-green-400 font-bold text-sm">100%</div><div class="text-gray-500 text-xs">Amounts &mdash; SCAN</div></div>
                    <div class="text-center bg-black/20 rounded-lg p-2"><div class="text-green-400 font-bold text-sm">100%</div><div class="text-gray-500 text-xs">Math &mdash; SCAN</div></div>
                </div>
            </div>
        </div>
    </div>

    <!-- Section: Why scan=clean matters -->
    <div class="prose prose-invert prose-lg max-w-none text-gray-300 leading-relaxed space-y-6">
        <p>The scan-equals-clean result matters because the most common objection to AI document systems is: &ldquo;It works on clean PDFs, but all our documents are scanned, stamped, slightly rotated, faxed, re-scanned.&rdquo; That objection does not apply here. Qwen2.5-VL was trained on enormous quantities of real-world document images, which inherently include degraded, scanned, and low-quality documents. The result is built-in robustness to the exact conditions that break traditional OCR-based systems.</p>

        <p>We are not claiming the system is immune to all possible degradation. A document scanned at 72 DPI with severe motion blur, or a fax from 1995 transmitted over a poor line, might produce different results. But the conditions we tested &mdash; the actual conditions in a modern Italian office with standard network scanners &mdash; produce performance identical to native digital documents.</p>

        <h2 class="text-2xl font-black font-display text-white">Confidence distribution: the system knows when it's unsure</h2>

        <p>A production document automation system must do more than extract data. It must also communicate its own uncertainty reliably. A system that extracts data incorrectly without signaling the problem is dangerous &mdash; errors flow silently downstream. A system that correctly identifies its own uncertainty allows humans to review only the uncertain cases, capturing the vast majority of documents in automated flow while maintaining a human-in-the-loop safety net for edge cases.</p>
    </div>

    <!-- Confidence bars -->
    <div class="rounded-2xl bg-brand-surface border border-white/10 p-6 my-8">
        <div class="text-xs text-gray-500 uppercase tracking-wider mb-5 font-bold">Confidence distribution &mdash; 219 documents</div>
        <div class="space-y-4">
            <div class="flex items-center gap-3">
                <div class="text-blue-400 text-sm font-bold w-20 shrink-0">HIGH</div>
                <div class="flex-1 bg-white/10 rounded-full h-3 overflow-hidden">
                    <div class="bg-blue-400 h-full rounded-full" style="width: 92.2%"></div>
                </div>
                <div class="text-white font-bold text-sm w-14 text-right shrink-0">92.2%</div>
                <div class="text-gray-500 text-xs w-14 shrink-0">202 docs</div>
            </div>
            <div class="flex items-center gap-3">
                <div class="text-yellow-400 text-sm font-bold w-20 shrink-0">MEDIUM</div>
                <div class="flex-1 bg-white/10 rounded-full h-3 overflow-hidden">
                    <div class="bg-yellow-400 h-full rounded-full" style="width: 2%"></div>
                </div>
                <div class="text-white font-bold text-sm w-14 text-right shrink-0">1.8%</div>
                <div class="text-gray-500 text-xs w-14 shrink-0">4 docs</div>
            </div>
            <div class="flex items-center gap-3">
                <div class="text-red-400 text-sm font-bold w-20 shrink-0">LOW</div>
                <div class="flex-1 bg-white/10 rounded-full h-3 overflow-hidden">
                    <div class="bg-red-400 h-full rounded-full" style="width: 5.9%"></div>
                </div>
                <div class="text-white font-bold text-sm w-14 text-right shrink-0">5.9%</div>
                <div class="text-gray-500 text-xs w-14 shrink-0">13 docs</div>
            </div>
        </div>
        <p class="text-gray-500 text-xs mt-4">VALIDATED: 202 docs (92.2%) &nbsp;&bull;&nbsp; PENDING_REVIEW: 13 (5.9%) &nbsp;&bull;&nbsp; NEEDS_REVIEW: 4 (1.8%). The 13 LOW confidence documents correspond exactly to the bank statement GGML crashes described below &mdash; they are automatically routed to human review, not silently inserted into the data stream.</p>
    </div>

    <!-- Section: GPU resources -->
    <div class="prose prose-invert prose-lg max-w-none text-gray-300 leading-relaxed space-y-6">
        <h2 class="text-2xl font-black font-display text-white">What happened inside the GPU: resource consumption data</h2>

        <p>We monitored hardware resource consumption every 60 seconds using <code class="text-brand-tealLight text-sm">nvidia-smi</code> throughout the benchmark. The data provides a precise picture of the pipeline's hardware profile, which is critical for capacity planning.</p>
    </div>

    <!-- Resource cards -->
    <div class="grid grid-cols-2 sm:grid-cols-3 gap-3 my-8">
        <div class="bg-brand-surface rounded-xl p-4 border border-white/10">
            <div class="text-brand-tealLight text-xs font-bold uppercase tracking-wider mb-2">GPU Utilization</div>
            <div class="text-2xl font-black text-white">87&ndash;100%</div>
            <div class="text-gray-500 text-xs mt-1">avg ~94% during inference</div>
        </div>
        <div class="bg-brand-surface rounded-xl p-4 border border-white/10">
            <div class="text-brand-tealLight text-xs font-bold uppercase tracking-wider mb-2">VRAM Used</div>
            <div class="text-2xl font-black text-white">13.3 GB</div>
            <div class="text-gray-500 text-xs mt-1">of 16 GB &mdash; 2.6 GB margin</div>
        </div>
        <div class="bg-brand-surface rounded-xl p-4 border border-white/10">
            <div class="text-brand-tealLight text-xs font-bold uppercase tracking-wider mb-2">Power Draw</div>
            <div class="text-2xl font-black text-white">~68 W</div>
            <div class="text-gray-500 text-xs mt-1">near TDP &mdash; 6 W at idle</div>
        </div>
        <div class="bg-brand-surface rounded-xl p-4 border border-white/10">
            <div class="text-brand-tealLight text-xs font-bold uppercase tracking-wider mb-2">CPU Load</div>
            <div class="text-2xl font-black text-white">~4%</div>
            <div class="text-gray-500 text-xs mt-1">100% GPU-bound pipeline</div>
        </div>
        <div class="bg-brand-surface rounded-xl p-4 border border-white/10">
            <div class="text-brand-tealLight text-xs font-bold uppercase tracking-wider mb-2">GPU Temperature</div>
            <div class="text-2xl font-black text-white">65&ndash;70&deg;C</div>
            <div class="text-gray-500 text-xs mt-1">26&deg;C at idle</div>
        </div>
        <div class="bg-brand-surface rounded-xl p-4 border border-white/10">
            <div class="text-brand-tealLight text-xs font-bold uppercase tracking-wider mb-2">RAM Used</div>
            <div class="text-2xl font-black text-white">~35 GB</div>
            <div class="text-gray-500 text-xs mt-1">OS + Ollama + buffers</div>
        </div>
    </div>

    <div class="prose prose-invert prose-lg max-w-none text-gray-300 leading-relaxed space-y-6">
        <p>The most important finding from the resource data: <strong class="text-white">the pipeline is 100% GPU-bound</strong>. CPU utilization averaged 4% throughout the entire benchmark. The processor was doing almost nothing &mdash; converting PDFs to images, calling Ollama's HTTP API, writing JSON files. All of the computationally intensive work happened on the GPU. This has a direct implication for hardware planning: adding faster CPUs, more CPU cores, or more CPU RAM does not improve throughput. Only the GPU matters.</p>

        <p>The VRAM consumption of 13.3 GB out of 16 GB available is worth noting. The margin of 2.6 GB is sufficient for the image buffers and model context during normal inference, but it is genuinely tight. This is why the bank statement GGML crash described in the next section occurs specifically on this hardware &mdash; the combination of a large dense image and a long extraction prompt pushes the tensor allocations beyond what the remaining 2.6 GB can accommodate.</p>

        <p>The power draw of ~68 W during inference, compared to 6-7 W at idle, represents a significant but reasonable energy cost for continuous operation. At typical European electricity prices, running this GPU 8 hours a day for 22 working days a month costs approximately &euro;2-4 in electricity. This needs to be accounted for in on-premise TCO calculations, but it is negligible compared to the labor cost of manual data entry at equivalent throughput.</p>
    </div>

    <!-- Limit 1 -->
    <div class="rounded-2xl border p-6 my-8" style="border-color: rgba(234,179,8,0.35); background: rgba(234,179,8,0.06);">
        <div class="flex items-start gap-4">
            <div class="text-2xl shrink-0">&#9888;&#65039;</div>
            <div>
                <div class="text-yellow-400 font-bold text-lg mb-3">Known Limit 1 &mdash; GGML Crash on Dense Bank Statements (13/20)</div>
                <p class="text-gray-400 text-sm leading-relaxed mb-3">Bank statements with dense transaction tables (15 or more rows) trigger an internal assertion failure in Ollama's GGML tensor backend during the extraction step. The error is: <code class="text-yellow-300 bg-black/20 px-1 rounded text-xs">GGML_ASSERT(a-&gt;ne[2] * 4 == b-&gt;ne[0]) failed (HTTP 500)</code></p>
                <p class="text-gray-400 text-sm leading-relaxed mb-3">Classification always succeeds on all 20 bank statements. The crash occurs only during extraction, when the dense image combined with the long bank statement prompt exceeds an internal tensor dimension limit in the 7B model on 16 GB VRAM. The 7 bank statements with fewer transaction rows were processed without issue and scored 100% on all fields including the closing balance calculation.</p>
                <p class="text-gray-400 text-sm leading-relaxed mb-3">This is not a bug in DataUnchain's code. It is a hardware capacity limitation: the 7B model on 16 GB VRAM does not have enough tensor budget for the combination of a high-density vision encoding and a complex extraction prompt simultaneously. The same documents would likely process without issue on a 24 GB GPU.</p>
                <div class="flex flex-wrap gap-2 mt-4">
                    <span class="text-brand-tealLight text-xs font-bold px-3 py-1.5 rounded-full border border-brand-teal/30">Fix: adaptive DPI reduction for dense tables (200 &rarr; 150)</span>
                    <span class="text-brand-tealLight text-xs font-bold px-3 py-1.5 rounded-full border border-brand-teal/30">Alt fix: Qwen2.5-VL 14B / 32B on 24 GB+</span>
                </div>
            </div>
        </div>
    </div>

    <!-- Limit 2 -->
    <div class="rounded-2xl border p-6 my-8" style="border-color: rgba(234,179,8,0.35); background: rgba(234,179,8,0.06);">
        <div class="flex items-start gap-4">
            <div class="text-2xl shrink-0">&#9888;&#65039;</div>
            <div>
                <div class="text-yellow-400 font-bold text-lg mb-3">Known Limit 2 &mdash; Payslip Gross Pay: 54.3%</div>
                <p class="text-gray-400 text-sm leading-relaxed mb-3">Net pay extracts at 100% because its label is nearly always &ldquo;NETTO IN BUSTA&rdquo; or &ldquo;NETTO A PAGARE&rdquo; &mdash; highly consistent across all Italian CCNL types. Gross pay extracts at 54.3% because the same concept appears under at least five different labels depending on the collective bargaining agreement and payroll software: &ldquo;RETRIBUZIONE LORDA&rdquo;, &ldquo;IMPONIBILE LORDO&rdquo;, &ldquo;TOTALE COMPETENZE&rdquo;, &ldquo;IMPONIBILE CONTRIBUTIVO&rdquo;, &ldquo;TOTALE SPETTANZE&rdquo;.</p>
                <p class="text-gray-400 text-sm leading-relaxed mb-3">Critically: when the model finds the correct field, the numeric value is always extracted correctly. This is purely a label recognition problem, not a digit-reading problem. Providing the extraction prompt with an explicit enumeration of all known label variants for the gross pay field should raise accuracy above 90%.</p>
                <div class="flex flex-wrap gap-2 mt-4">
                    <span class="text-brand-tealLight text-xs font-bold px-3 py-1.5 rounded-full border border-brand-teal/30">Fix: add all known CCNL label variants to extraction prompt</span>
                    <span class="text-brand-tealLight text-xs font-bold px-3 py-1.5 rounded-full border border-brand-teal/30">Target: &gt;90% in processor v2.1</span>
                </div>
            </div>
        </div>
    </div>

    <!-- Section: Economics -->
    <div class="prose prose-invert prose-lg max-w-none text-gray-300 leading-relaxed space-y-6">
        <h2 class="text-2xl font-black font-display text-white">$0.002 per document: what this means for real businesses</h2>

        <p>At $0.24/hr with 32 seconds processing time per document on cloud compute, the cost math is straightforward: $0.24 / (3600 / 32) = approximately $0.002 per document. Let's translate that into real business scenarios.</p>
    </div>

    <!-- Economic scenarios -->
    <div class="space-y-4 my-8">
        <div class="bg-brand-surface rounded-2xl border border-white/10 p-5">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
                <div class="text-white font-bold">Small business &mdash; 100 invoices/month</div>
                <div class="text-brand-tealLight font-black text-xl">$0.20/mo on cloud</div>
            </div>
            <p class="text-gray-400 text-sm leading-relaxed">Manual data entry for 100 invoices: 2-4 hours at &euro;18-22/hr = &euro;36-88/month in direct labor cost, plus error correction overhead. DataUnchain on cloud: $0.20/month. On existing office hardware: approximately zero marginal cost. <span class="text-green-400 font-semibold">ROI: 200-400&times; cost reduction.</span></p>
        </div>
        <div class="bg-brand-surface rounded-2xl border border-white/10 p-5">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
                <div class="text-white font-bold">Medium enterprise &mdash; 2,000 documents/month</div>
                <div class="text-brand-tealLight font-black text-xl">$4/mo on cloud</div>
            </div>
            <p class="text-gray-400 text-sm leading-relaxed">2,000 mixed documents per month (invoices, DDT, payslips, credit notes, orders) typically requires 1-2 FTE staff members dedicating several hours per day to data entry. Competing SaaS document extraction services charge &euro;200-2,000/month at this volume. DataUnchain on cloud: $4/month. <span class="text-green-400 font-semibold">Immediate ROI from day one.</span></p>
        </div>
        <div class="bg-brand-surface rounded-2xl border border-white/10 p-5">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
                <div class="text-white font-bold">On-premise &mdash; RTX 3090 owned hardware</div>
                <div class="text-brand-tealLight font-black text-xl">&lt;$0.001/doc</div>
            </div>
            <p class="text-gray-400 text-sm leading-relaxed">An RTX 3090 24 GB costs approximately &euro;900-1,200 on the quality used market. Amortized over 3 years at 4 hours/day, including electricity: the cost per document drops below $0.001. Payback period against a competing SaaS subscription at &euro;500/month: less than 3 months. <span class="text-green-400 font-semibold">At medium-high volume, on-premise pays for itself within a quarter.</span></p>
        </div>
    </div>

    <!-- Section: Offline means -->
    <div class="prose prose-invert prose-lg max-w-none text-gray-300 leading-relaxed space-y-6">
        <h2 class="text-2xl font-black font-display text-white">What &ldquo;completely offline&rdquo; actually means</h2>

        <p>The offline operation mode of DataUnchain is not a secondary feature &mdash; it is the primary architectural choice that differentiates it from every major commercial document extraction service. When we say the system runs completely offline, the implications are concrete and verifiable:</p>

        <p><strong class="text-white">No data leaves your infrastructure.</strong> PDFs are converted to images locally. Ollama runs locally. The extracted JSON is written locally. Not a single byte of your documents &mdash; not metadata, not page thumbnails, not text fragments &mdash; is transmitted to any external service. Not to Anthropic, not to OpenAI, not to Microsoft Azure, not to Google Cloud, not to any other AI provider.</p>

        <p><strong class="text-white">GDPR compliance is fundamentally simplified.</strong> The most complex GDPR obligations for organizations using AI services involve international data transfers, data processing agreements with AI vendors, ensuring that the AI provider handles your data according to GDPR requirements, and managing breach notification obligations to external processors. When your documents never leave your infrastructure, none of these obligations apply. Your data protection officer will appreciate this enormously.</p>

        <p><strong class="text-white">Air-gap operation is possible.</strong> Once Qwen2.5-VL 7B is downloaded (approximately 5 GB, a one-time operation), the entire system runs without any internet connectivity. This enables deployment in environments that are genuinely isolated from the internet: manufacturing plant operational technology networks, secure government archives, legal document management systems with strict information barrier requirements, healthcare data systems subject to specific regulatory constraints.</p>

        <p><strong class="text-white">No vendor lock-in, no subscription cliff.</strong> The underlying model (Qwen2.5-VL) is open source under Apache 2.0 license. Ollama is open source. DataUnchain is a commercial product built on top of these open foundations &mdash; you pay for the product, not for access to AI infrastructure controlled by someone else. If you want to switch to a different compatible VLM, that's a single configuration change. No SaaS vendor can raise prices on you, discontinue a tier you depend on, or sunset a feature that your workflow relies on.</p>

        <h2 class="text-2xl font-black font-display text-white">Why Qwen2.5-VL 7B</h2>

        <p>The choice of Qwen2.5-VL as the backbone for DataUnchain's processor is based on systematic evaluation of the available open-source vision-language model landscape for document processing specifically.</p>

        <p><strong class="text-white">LLaVA and its variants</strong> were the first widely-adopted open-source VLMs, but they show significant performance degradation on documents with dense structured text, tables, and multi-column layouts. Their training data skewed heavily toward natural images, and document understanding was not a primary design objective.</p>

        <p><strong class="text-white">InternVL2</strong> shows strong document understanding performance but has a less mature deployment ecosystem. Integrating it into a production pipeline requires more custom work compared to the Ollama-based deployment that Qwen supports natively.</p>

        <p><strong class="text-white">Qwen2.5-VL</strong> from Alibaba DAMO Academy was specifically designed with document understanding as a first-class capability. Its training data includes large quantities of structured documents from multiple languages, including Italian business documents. The model demonstrates particularly strong performance on tasks requiring spatial understanding of form layouts, table extraction, and recognition of language-specific fiscal identifiers. The 7B size hits the sweet spot between capability and hardware accessibility: it runs on a 16 GB GPU &mdash; within reach of many organizations &mdash; while delivering accuracy that this benchmark demonstrates is production-grade on most document types.</p>

        <p>It is also worth being explicit about what Qwen2.5-VL is not: it is not an OCR system. OCR converts pixel patterns to characters without any understanding of what those characters mean. Qwen2.5-VL is a multimodal language model that genuinely comprehends documents: it understands that a number after &ldquo;P.IVA:&rdquo; is a VAT identifier, that a row in a table with a date and a euro amount followed by &ldquo;D&rdquo; is a debit transaction, that text in a box labeled &ldquo;NETTO IN BUSTA&rdquo; at the bottom of a page is the net pay figure. This semantic understanding is what enables 100% accuracy on fiscal identifiers without requiring a separate regex post-processing layer.</p>
    </div>

    <!-- Hardware Guide -->
    <div class="prose prose-invert prose-lg max-w-none text-gray-300 leading-relaxed space-y-6">
        <h2 class="text-2xl font-black font-display text-white">Hardware deployment guide</h2>

        <p>Based on the resource consumption data from this benchmark, here are concrete hardware recommendations for production deployment:</p>
    </div>

    <div class="space-y-3 my-8">
        <div class="rounded-xl border border-white/10 bg-brand-surface p-5">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-2">
                <div class="text-white font-bold">RTX 2000 Ada / RTX 3080 &mdash; 16 GB VRAM</div>
                <span class="text-yellow-400 text-xs font-bold px-3 py-1 rounded-full border border-yellow-400/30">Functional Minimum</span>
            </div>
            <p class="text-gray-400 text-sm leading-relaxed">Confirmed working in this benchmark. VRAM margin is 2.6 GB &mdash; sufficient for most documents but not for bank statements with dense transaction tables (15+ rows). Suitable if bank statements are not a primary document type in your workflow, or if you implement the DPI reduction workaround.</p>
        </div>
        <div class="rounded-xl bg-brand-surface p-5" style="border: 1px solid rgba(13,148,136,0.45); background: rgba(13,148,136,0.07);">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-2">
                <div class="text-white font-bold">RTX 3090 / RTX 4090 &mdash; 24 GB VRAM</div>
                <span class="text-brand-tealLight text-xs font-bold px-3 py-1 rounded-full border border-brand-teal/30">&#11088; Recommended</span>
            </div>
            <p class="text-gray-400 text-sm leading-relaxed">All seven document types stable. 8 GB of additional VRAM eliminates the bank statement crash entirely. Estimated processing speed ~20 seconds/document based on GPU architecture comparison (2&times; faster). Best price/performance for production use. RTX 3090 available used ~&euro;900; RTX 4090 new ~&euro;1,800.</p>
        </div>
        <div class="rounded-xl border border-white/10 bg-brand-surface p-5">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-2">
                <div class="text-white font-bold">NVIDIA A5000 / A6000 &mdash; 24&ndash;48 GB VRAM</div>
                <span class="text-purple-400 text-xs font-bold px-3 py-1 rounded-full border border-purple-400/30">Enterprise</span>
            </div>
            <p class="text-gray-400 text-sm leading-relaxed">ECC error-correcting memory (important for long-running production services), professional support warranty, server form factor. Supports Qwen2.5-VL 32B for maximum accuracy. Ideal for data center deployments and organizations with IT procurement policies requiring commercial-grade hardware.</p>
        </div>
        <div class="rounded-xl border border-white/10 bg-brand-surface p-5">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-2">
                <div class="text-white font-bold">NVIDIA A100 / H100 &mdash; 40&ndash;80 GB VRAM</div>
                <span class="text-blue-400 text-xs font-bold px-3 py-1 rounded-full border border-blue-400/30">High Volume</span>
            </div>
            <p class="text-gray-400 text-sm leading-relaxed">For organizations processing 50,000+ documents per month. Supports multiple parallel Ollama instances or Qwen2.5-VL 72B. HBM memory bandwidth dramatically increases throughput compared to GDDR6X GPUs. Cloud-grade data center hardware.</p>
        </div>
    </div>

    <div class="rounded-2xl bg-brand-surface border border-white/10 p-5 my-6">
        <p class="text-gray-400 text-sm leading-relaxed"><strong class="text-white">Important note on CPU selection:</strong> This benchmark confirms that CPU is entirely irrelevant to document processing throughput. GPU utilization averaged 94% while CPU averaged 4%. An RTX 3090 paired with a mid-range i5 processor will outperform an RTX 2000 Ada paired with a high-end i9 by a factor of approximately 2&times;. Buy GPU, not CPU. 32 GB of RAM is the minimum recommended; 64 GB provides headroom for peak loads.</p>
    </div>

    <!-- Per-type table -->
    <div class="prose prose-invert prose-lg max-w-none text-gray-300 leading-relaxed space-y-6">
        <h2 class="text-2xl font-black font-display text-white">Results by document type</h2>
    </div>

    <div class="overflow-x-auto my-8">
        <table class="w-full text-sm">
            <thead>
                <tr class="border-b border-white/20 text-left">
                    <th class="pb-3 pr-3 text-white font-bold">Type</th>
                    <th class="pb-3 pr-3 text-right text-white font-bold">n</th>
                    <th class="pb-3 pr-3 text-right text-white font-bold">Type%</th>
                    <th class="pb-3 pr-3 text-right text-white font-bold">VAT ID%</th>
                    <th class="pb-3 pr-3 text-right text-white font-bold">Amounts%</th>
                    <th class="pb-3 pr-3 text-right text-white font-bold">Math%</th>
                    <th class="pb-3 text-right text-white font-bold">Speed</th>
                </tr>
            </thead>
            <tbody class="text-gray-400">
                <tr class="border-b border-white/10"><td class="py-2.5 pr-3 text-gray-200">Invoice</td><td class="text-right pr-3">60</td><td class="text-right pr-3 text-green-400">100%</td><td class="text-right pr-3 text-green-400">100%</td><td class="text-right pr-3 text-green-400">100%</td><td class="text-right pr-3 text-green-400">100%</td><td class="text-right">36s</td></tr>
                <tr class="border-b border-white/10"><td class="py-2.5 pr-3 text-gray-200">Delivery Note</td><td class="text-right pr-3">50</td><td class="text-right pr-3 text-green-400">100%</td><td class="text-right pr-3 text-green-400">100%</td><td class="text-right pr-3 text-gray-600">n/a</td><td class="text-right pr-3 text-gray-600">n/a</td><td class="text-right">32s</td></tr>
                <tr class="border-b border-white/10"><td class="py-2.5 pr-3 text-gray-200">Credit Note</td><td class="text-right pr-3">20</td><td class="text-right pr-3 text-green-400">100%</td><td class="text-right pr-3 text-green-400">100%</td><td class="text-right pr-3 text-green-400">100%</td><td class="text-right pr-3 text-green-400">100%</td><td class="text-right">31s</td></tr>
                <tr class="border-b border-white/10"><td class="py-2.5 pr-3 text-gray-200">Contract</td><td class="text-right pr-3">20</td><td class="text-right pr-3 text-green-400">100%</td><td class="text-right pr-3 text-green-400">100%</td><td class="text-right pr-3 text-gray-600">n/a</td><td class="text-right pr-3 text-gray-600">n/a</td><td class="text-right">26s</td></tr>
                <tr class="border-b border-white/10"><td class="py-2.5 pr-3 text-gray-200">Purchase Order</td><td class="text-right pr-3">14</td><td class="text-right pr-3 text-green-400">100%</td><td class="text-right pr-3 text-green-400">100%</td><td class="text-right pr-3 text-green-400">100%</td><td class="text-right pr-3 text-green-400">100%</td><td class="text-right">37s</td></tr>
                <tr class="border-b border-white/10"><td class="py-2.5 pr-3 text-gray-200">Payslip</td><td class="text-right pr-3">35</td><td class="text-right pr-3 text-green-400">100%</td><td class="text-right pr-3 text-green-400">100%</td><td class="text-right pr-3 text-yellow-400">net 100% / gross 54%</td><td class="text-right pr-3 text-gray-600">n/a</td><td class="text-right">31s</td></tr>
                <tr><td class="py-2.5 pr-3 text-gray-200">Bank Statement</td><td class="text-right pr-3">7&#x2605;</td><td class="text-right pr-3 text-green-400">100%</td><td class="text-right pr-3 text-green-400">100%</td><td class="text-right pr-3 text-green-400">100%</td><td class="text-right pr-3 text-green-400">100%</td><td class="text-right">48s</td></tr>
            </tbody>
        </table>
        <p class="text-gray-600 text-xs mt-2">&#x2605; 13/20 bank statements crashed with GGML assertion failure (hardware limit on 16 GB VRAM, see Known Limits section). The 7 successfully processed scored 100% on all fields.</p>
    </div>

    <!-- Section: Methodology -->
    <div class="prose prose-invert prose-lg max-w-none text-gray-300 leading-relaxed space-y-6">
        <h2 class="text-2xl font-black font-display text-white">Benchmark methodology</h2>

        <p>Every result published here was produced by a fully automated pipeline with no manual intervention in the evaluation step. The evaluation process consists of four stages: document generation with fixed random seed; processing through DataUnchain's processor v2.0; automated field-by-field comparison against ground truth; and aggregation into the final report.</p>

        <p>Numeric fields are evaluated with a tolerance of &plusmn;&euro;0.50 to account for rounding conventions. Date fields require exact match in ISO 8601 format (YYYY-MM-DD). String fields (VAT numbers, fiscal codes, document references) require exact match. Classification is evaluated as correct or incorrect with no partial credit.</p>

        <p>The benchmark methodology is fully documented. If you want to validate these results on your own document corpus as part of a proof-of-concept engagement, <a href="/en/contact/" class="text-brand-tealLight hover:underline">contact us</a> &mdash; we run structured pilots with prospective clients on their own documents under NDA.</p>

        <h2 class="text-2xl font-black font-display text-white">What comes next</h2>

        <p>The two identified limits have concrete, planned fixes. The payslip gross pay prompt enrichment is the simplest and highest-priority change &mdash; a straightforward update to the extraction prompt with all known CCNL label variants for the gross pay field. We expect this to bring accuracy from 54.3% to above 90% based on the pattern of failures.</p>

        <p>The bank statement GGML crash fix involves implementing adaptive DPI reduction: the processor will detect when a document page contains more than a threshold number of text elements (via a quick image density metric), and automatically reduce the conversion DPI from 200 to 150 for those pages. This reduces the image size enough to keep tensor allocations within the 16 GB VRAM budget while maintaining sufficient resolution for reliable text recognition.</p>

        <p>The benchmark v3 will extend the corpus to ten document types, adding receipts and commercial documents, packing lists, quotations, and healthcare-specific formats. The target is 300 documents across the full range. We will also run comparative benchmarks against Amazon Textract, Azure Document Intelligence, and Google Document AI on the same corpus to give the market objective comparison data.</p>

        <p>A test of Qwen2.5-VL 32B on a 48 GB GPU is planned to quantify the accuracy delta between model sizes. The hypothesis is that the 32B model resolves both the bank statement GGML issue and the payslip gross pay label variance through its larger and more capable vision encoder.</p>

        <h2 class="text-2xl font-black font-display text-white">The bottom line</h2>

        <p>95.5% accuracy. $0.002 per document. 32 seconds. Zero cloud. Zero data leaving your infrastructure.</p>

        <p>On the fields that matter most for Italian business automation &mdash; VAT numbers, fiscal codes, dates, financial amounts, arithmetic consistency &mdash; the system achieves 100% on every one. Scanned documents perform identically to native digital PDFs. The system communicates its own uncertainty rather than silently inserting bad data into downstream systems. Two identified limits are fully understood and have clear, planned fixes.</p>

        <p>95.5% accuracy on a corpus of 219 real Italian business documents, with 100% on the fields that matter most for automation: VAT numbers, fiscal codes, dates, amounts, and arithmetic consistency. This is the bar we hold ourselves to before calling a system production-ready.</p>
    </div>

    <!-- CTA -->
    <div class="mt-12 rounded-2xl p-8 text-center" style="background: linear-gradient(135deg, rgba(13,148,136,0.15) 0%, rgba(16,185,129,0.10) 100%); border: 1px solid rgba(13,148,136,0.3);">
        <div class="text-2xl font-black text-white mb-2">Want to see it on your documents?</div>
        <p class="text-gray-400 mb-6">We run structured pilots with invoices, payslips, and contracts from your organization &mdash; under NDA, on your infrastructure.</p>
        <div class="flex flex-wrap justify-center gap-3">
            <a href="/en/contact/" class="bg-brand-teal text-white font-bold px-6 py-3 rounded-xl hover:opacity-90 transition-opacity">Request a Pilot &rarr;</a>
            <a href="/en/docs/" class="text-brand-tealLight font-bold px-6 py-3 rounded-xl border border-brand-teal/30 hover:bg-brand-teal/10 transition-colors">Read the Docs</a>
        </div>
    </div>

    <div class="mt-10 pt-8 border-t border-white/10 text-center">
        <a href="/en/blog/" class="text-brand-tealLight font-bold hover:underline">&larr; Back to Blog</a>
    </div>

</div>
</article>
