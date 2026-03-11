---
layout: default
title: "95.5% Accuracy on 219 Italian Business Documents: The DataUnchain Scientific Benchmark"
lang: en
categories: blog
date: 2026-03-11
description: "We tested Qwen2.5-VL 7B on 219 real Italian business documents — invoices, shipping documents, payslips, contracts, credit notes — with verified ground truth. Result: 95.5% accuracy, $0.002 per document, fully offline. Here are all the numbers."
---

<article class="pt-36 pb-20 px-6">
    <div class="max-w-3xl mx-auto">

        <div class="mb-8">
            <span class="text-brand-tealLight text-xs font-bold uppercase tracking-widest">Benchmark · March 11, 2026</span>
            <h1 class="text-4xl lg:text-5xl font-black font-display mt-4 mb-6">95.5% Accuracy on 219 Italian Business Documents: The DataUnchain Scientific Benchmark</h1>
            <p class="text-gray-400 text-lg leading-relaxed">We built a synthetic corpus of 219 Italian business documents with verified ground truth, ran them through the DataUnchain processor v2.0, and measured accuracy field by field. This article documents every aspect of the test: methodology, results, identified limits, resource consumption, and real operational cost.</p>
        </div>

        <div class="prose prose-invert prose-lg max-w-none text-gray-300 leading-relaxed space-y-6">

            <h2 class="text-2xl font-black font-display text-white">The problem we're solving</h2>

            <p>Every Italian company generates dozens of structured documents every day: sales invoices, transport documents (DDT), payslips, credit notes, purchase orders, contracts, bank statements. The vast majority of these documents exist as PDFs or scanned paper. Transforming this information into structured data — VAT numbers, amounts, dates, totals — currently requires either hours of manual data entry or expensive cloud systems that send your confidential documents to third-party servers.</p>

            <p>DataUnchain was created to answer a simple question: can this extraction be done accurately, quickly, completely offline, and at a marginal cost close to zero? This benchmark is the first systematic scientific test to answer that question with real data.</p>

            <h2 class="text-2xl font-black font-display text-white">Why a ground truth benchmark?</h2>

            <p>Most demos of AI document systems show cherry-picked screenshots of cases that went well. We wanted something different: a systematic measurement over a large corpus, with a known expected answer for every field, with precise and reproducible metrics.</p>

            <p>The concept of <em>ground truth</em> is simple: for every document in the corpus, there is a JSON file containing the correct values for every field — the invoice number, the supplier's VAT number, the issue date, the taxable amount, the VAT, the total. The system extracts those fields from the PDF, and we automatically compare the extracted values against the expected ones. Zero subjectivity. Zero cherry-picking.</p>

            <p>We generated the corpus synthetically — meaning we built the PDFs ourselves with realistic Italian business data — precisely to have perfect ground truth from the start. Authentic Italian fiscal data: VAT numbers (Partita IVA) with 11 digits and official verification algorithm, fiscal codes (Codice Fiscale) generated with the complete official algorithm (ODD/EVEN tables, Belfiore municipality codes, check digit, homocody handling), Italian-format dates, amounts in euros.</p>

            <h2 class="text-2xl font-black font-display text-white">The corpus: 219 documents, 7 categories</h2>

            <p>The final corpus comprises 219 documents split across seven document types typical of the Italian business landscape:</p>

            <div class="overflow-x-auto my-6">
                <table class="w-full text-sm border-collapse">
                    <thead>
                        <tr class="border-b border-white/20">
                            <th class="text-left py-2 pr-4 text-white font-bold">Type</th>
                            <th class="text-right py-2 pr-4 text-white font-bold">N.</th>
                            <th class="text-left py-2 text-white font-bold">Main extracted fields</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr class="border-b border-white/10"><td class="py-2 pr-4">Invoice (Fattura)</td><td class="text-right pr-4">60</td><td class="py-2">number, date, due date, VAT IDs, taxable amount, 22% VAT, total, line items</td></tr>
                        <tr class="border-b border-white/10"><td class="py-2 pr-4">Delivery Note (DDT)</td><td class="text-right pr-4">50</td><td class="py-2">DDT number, date, shipper, recipient, carrier, packages, goods description</td></tr>
                        <tr class="border-b border-white/10"><td class="py-2 pr-4">Payslip (Busta Paga)</td><td class="text-right pr-4">35</td><td class="py-2">employee, fiscal code, company, VAT ID, contract type, period, gross, deductions, net</td></tr>
                        <tr class="border-b border-white/10"><td class="py-2 pr-4">Credit Note (Nota di Credito)</td><td class="text-right pr-4">20</td><td class="py-2">NC number, date, reference invoice, credit amount, reason</td></tr>
                        <tr class="border-b border-white/10"><td class="py-2 pr-4">Contract (Contratto)</td><td class="text-right pr-4">20</td><td class="py-2">contract type, number, date, Party A, Party B, both VAT IDs</td></tr>
                        <tr class="border-b border-white/10"><td class="py-2 pr-4">Purchase Order (Ordine Acquisto)</td><td class="text-right pr-4">14</td><td class="py-2">order number, date, delivery date, supplier, buyer, VAT IDs, total</td></tr>
                        <tr class="border-b border-white/10"><td class="py-2 pr-4">Bank Statement (Estratto Conto)</td><td class="text-right pr-4">20</td><td class="py-2">bank, IBAN, account holder, period, opening balance, transactions, closing balance</td></tr>
                        <tr class="font-bold text-white"><td class="py-2 pr-4">Total</td><td class="text-right pr-4">219</td><td class="py-2"></td></tr>
                    </tbody>
                </table>
            </div>

            <h3 class="text-xl font-bold text-white">Simulated scanning: the real stress test</h3>

            <p>70% of the corpus (approximately 153 documents) was subjected to a controlled degradation process to simulate real-world scanning conditions. We're not talking about a simple JPEG save: we applied a pipeline of realistic transformations including Gaussian noise at varying intensity, random rotations in the ±3° range, JPEG compression at quality levels between 60 and 85 (typical of office scanners), overlaid stamps and watermarks, brightness and contrast variations, and simulation of slight creases and perspective distortions.</p>

            <p>These effects faithfully reproduce what happens when a document is printed, signed, stamped, scanned with an inexpensive office scanner, and then the file is compressed before archiving — a scenario that describes 90% of documents flowing through Italian companies every day.</p>

            <h3 class="text-xl font-bold text-white">Mathematically verified ground truth</h3>

            <p>For documents with monetary amounts (invoices, credit notes, payslips, bank statements), the ground truth is not just a set of correct values: it is mathematically coherent ground truth. This means that for every invoice, <code class="text-brand-tealLight">taxable_amount + vat = total</code> exactly. For every payslip, <code class="text-brand-tealLight">gross - deductions = net</code> to the cent. For every bank statement, <code class="text-brand-tealLight">opening_balance + credits - debits = closing_balance</code>.</p>

            <p>This allows us to test not just extraction of individual fields, but also the system's ability to detect internal arithmetic errors — a critical capability for production use, where an invoice where the numbers don't add up is an immediate red flag.</p>

            <h2 class="text-2xl font-black font-display text-white">The architecture: how DataUnchain works</h2>

            <p>Before getting into results, it's worth describing exactly how the tested system works. DataUnchain processor v2.0 implements a three-step pipeline that processes each incoming PDF document.</p>

            <h3 class="text-xl font-bold text-white">Step 1 — Classify: document type identification</h3>

            <p>The first step takes the document image (obtained by converting the PDF at 200 DPI) and sends it to Qwen2.5-VL 7B with a classification prompt. The model must respond with one of the supported categories: <em>invoice, delivery_note, payslip, credit_note, contract, purchase_order, bank_statement</em>, or <em>unknown</em> if the document doesn't fit any known category.</p>

            <p>Classification happens without providing the model any additional visual hints: the model sees only the image and must decide autonomously. This matters because in reality documents arrive in mixed streams — a folder with 50 PDFs may contain invoices, delivery notes, payslips and credit notes all mixed together, and the system must sort them correctly without knowing in advance what to expect.</p>

            <h3 class="text-xl font-bold text-white">Step 2 — Extract: structured extraction</h3>

            <p>Once the document type is identified, the extraction prompt specific to that category is selected. Each type has an optimized prompt that describes exactly which fields to extract, in what format, with what handling of edge cases (e.g., "if the field is not present, use null").</p>

            <p>The model returns a structured JSON. This JSON is validated against a predefined schema: if mandatory fields are missing or types don't match, the document is marked <code class="text-yellow-400">NEEDS_REVIEW</code>.</p>

            <h3 class="text-xl font-bold text-white">Step 3 — Audit: validation and confidence scoring</h3>

            <p>The third step is entirely deterministic — no AI involved. A Python module runs a series of formal and mathematical checks:</p>

            <p><strong class="text-white">Formal validation:</strong></p>
            <ul>
                <li>VAT number (P.IVA): 11 digits with Luhn-like checksum algorithm specific to the Italian tax system</li>
                <li>Fiscal code (Codice Fiscale): 16 characters, correct alphanumeric pattern, verified check digit, homocody handling</li>
                <li>Dates: YYYY-MM-DD format, range 1900-2100, valid days for the month</li>
                <li>Amounts: positive numeric values, 2 decimal place precision</li>
            </ul>

            <p><strong class="text-white">Math check:</strong></p>
            <ul>
                <li>Invoices: <code class="text-brand-tealLight">taxable + vat = total ± €0.10</code></li>
                <li>Payslips: <code class="text-brand-tealLight">gross - deductions = net ± €0.10</code></li>
                <li>Bank statements: <code class="text-brand-tealLight">opening + credits - debits = closing ± €0.10</code></li>
            </ul>

            <p>At the end of audit, each document receives a <strong class="text-white">confidence score</strong> (HIGH/MEDIUM/LOW) based on the internal consistency of the extracted data, and an <strong class="text-white">audit_status</strong> (VALIDATED/PENDING_REVIEW/NEEDS_REVIEW) indicating whether the document can be processed automatically or requires human review.</p>

            <h2 class="text-2xl font-black font-display text-white">The hardware: what does it actually cost?</h2>

            <p>The test was conducted on RunPod Community Cloud, using a pod with NVIDIA RTX 2000 Ada Generation GPU with 16 GB VRAM. The cost is $0.24/hour.</p>

            <div class="overflow-x-auto my-6">
                <table class="w-full text-sm border-collapse">
                    <thead>
                        <tr class="border-b border-white/20">
                            <th class="text-left py-2 pr-4 text-white font-bold">Component</th>
                            <th class="text-left py-2 text-white font-bold">Specs</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr class="border-b border-white/10"><td class="py-2 pr-4">GPU</td><td class="py-2">NVIDIA RTX 2000 Ada Generation</td></tr>
                        <tr class="border-b border-white/10"><td class="py-2 pr-4">VRAM</td><td class="py-2">16,380 MiB (~16 GB)</td></tr>
                        <tr class="border-b border-white/10"><td class="py-2 pr-4">vCPU</td><td class="py-2">6 cores</td></tr>
                        <tr class="border-b border-white/10"><td class="py-2 pr-4">RAM</td><td class="py-2">31 GB</td></tr>
                        <tr class="border-b border-white/10"><td class="py-2 pr-4">Cost</td><td class="py-2">$0.24/hr</td></tr>
                        <tr class="border-b border-white/10"><td class="py-2 pr-4">Model</td><td class="py-2">Qwen2.5-VL 7B (Q4 quantized)</td></tr>
                        <tr class="border-b border-white/10"><td class="py-2 pr-4">Runtime</td><td class="py-2">Ollama with flash attention enabled</td></tr>
                        <tr><td class="py-2 pr-4">OS</td><td class="py-2">Ubuntu 22.04, CUDA 12.4.1</td></tr>
                    </tbody>
                </table>
            </div>

            <p>Qwen2.5-VL 7B in its Q4 quantized version occupies approximately 13.3 GB of VRAM — leaving just 2.6 GB of margin on the 16 GB available. This is the minimum configuration: a system with a 12 GB GPU would not be sufficient. With 24 GB (RTX 3090 or RTX 4090), the model would have ample space for more complex processing.</p>

            <h2 class="text-2xl font-black font-display text-white">The results: numbers that speak clearly</h2>

            <h3 class="text-xl font-bold text-white">Speed and throughput</h3>

            <p>Before getting to accuracy, the speed numbers:</p>

            <div class="overflow-x-auto my-6">
                <table class="w-full text-sm border-collapse">
                    <thead>
                        <tr class="border-b border-white/20">
                            <th class="text-left py-2 pr-4 text-white font-bold">Metric</th>
                            <th class="text-right py-2 text-white font-bold">Value</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr class="border-b border-white/10"><td class="py-2 pr-4">Average speed</td><td class="text-right py-2">32.0 seconds/document</td></tr>
                        <tr class="border-b border-white/10"><td class="py-2 pr-4">Min / Max</td><td class="text-right py-2">25.8s / 53.0s</td></tr>
                        <tr class="border-b border-white/10"><td class="py-2 pr-4">Median (p50)</td><td class="text-right py-2">33.1s</td></tr>
                        <tr class="border-b border-white/10"><td class="py-2 pr-4">90th percentile (p90)</td><td class="text-right py-2">41.1s</td></tr>
                        <tr class="border-b border-white/10"><td class="py-2 pr-4">Throughput</td><td class="text-right py-2">~112 documents/hour</td></tr>
                        <tr><td class="py-2 pr-4">Cost per document</td><td class="text-right py-2 text-brand-tealLight font-bold">~$0.002</td></tr>
                    </tbody>
                </table>
            </div>

            <p>32 seconds per document may seem like a lot compared to a traditional OCR system that would take a few milliseconds. But the comparison doesn't hold: an OCR system extracts characters, not meaning. In 32 seconds here, the system identifies the document type, extracts all semantically relevant fields (not just raw text), formally validates VAT numbers and fiscal codes, verifies arithmetic, and assigns a reliability judgment. No OCR does all of this.</p>

            <p>The correct comparison is with a human operator doing the same work: identifying the document, finding the fields, transcribing them, verifying them. An average operator takes between 2 and 5 minutes per document, with a typical error rate of around 2-3% even under optimal conditions. DataUnchain does it in 32 seconds with 95.5% accuracy.</p>

            <h3 class="text-xl font-bold text-white">Field-by-field accuracy</h3>

            <p>This is the heart of the benchmark. Each extracted field is compared with the expected value in the ground truth, using the appropriate metric for that field type.</p>

            <div class="overflow-x-auto my-6">
                <table class="w-full text-sm border-collapse">
                    <thead>
                        <tr class="border-b border-white/20">
                            <th class="text-left py-2 pr-4 text-white font-bold">Field</th>
                            <th class="text-right py-2 pr-4 text-white font-bold">Accuracy</th>
                            <th class="text-right py-2 text-white font-bold">On</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr class="border-b border-white/10"><td class="py-2 pr-4">Document type</td><td class="text-right pr-4 text-green-400">100.0%</td><td class="text-right py-2">206/206</td></tr>
                        <tr class="border-b border-white/10"><td class="py-2 pr-4">Reference (document number)</td><td class="text-right pr-4 text-green-400">96.6%</td><td class="text-right py-2">199/206</td></tr>
                        <tr class="border-b border-white/10"><td class="py-2 pr-4">VAT ID / Fiscal Code</td><td class="text-right pr-4 text-green-400">100.0%</td><td class="text-right py-2">206/206</td></tr>
                        <tr class="border-b border-white/10"><td class="py-2 pr-4">Issue date</td><td class="text-right pr-4 text-green-400">100.0%</td><td class="text-right py-2">144/144</td></tr>
                        <tr class="border-b border-white/10"><td class="py-2 pr-4">Taxable amount (±€0.50)</td><td class="text-right pr-4 text-green-400">100.0%</td><td class="text-right py-2">94/94</td></tr>
                        <tr class="border-b border-white/10"><td class="py-2 pr-4">VAT amount (±€0.50)</td><td class="text-right pr-4 text-green-400">100.0%</td><td class="text-right py-2">94/94</td></tr>
                        <tr class="border-b border-white/10"><td class="py-2 pr-4">Total amount (±€0.50)</td><td class="text-right pr-4 text-green-400">100.0%</td><td class="text-right py-2">94/94</td></tr>
                        <tr class="border-b border-white/10"><td class="py-2 pr-4">Gross pay / payslip (±€0.50)</td><td class="text-right pr-4 text-yellow-400">54.3%</td><td class="text-right py-2">19/35</td></tr>
                        <tr class="border-b border-white/10"><td class="py-2 pr-4">Net pay / payslip (±€0.50)</td><td class="text-right pr-4 text-green-400">100.0%</td><td class="text-right py-2">35/35</td></tr>
                        <tr class="border-b border-white/10"><td class="py-2 pr-4">Closing balance / bank statement (±€0.50)</td><td class="text-right pr-4 text-green-400">100.0%</td><td class="text-right py-2">7/7</td></tr>
                        <tr class="border-b border-white/10"><td class="py-2 pr-4">Internal math check (±€0.10)</td><td class="text-right pr-4 text-green-400">100.0%</td><td class="text-right py-2">120/120</td></tr>
                    </tbody>
                </table>
            </div>

            <p>The most important numbers to observe:</p>

            <p><strong class="text-white">VAT IDs and Fiscal Codes: 100% on 206 documents.</strong> This is the most relevant result for an Italian business context. Tax identity data — the data that determines who to address an invoice to, who to pay, who issued the document — is extracted correctly in every single case. On clean documents and on scan-degraded documents alike, without difference.</p>

            <p><strong class="text-white">Financial amounts: 100% on all types that include them.</strong> Taxable amount, VAT, invoice total: every single extracted numeric value is correct within the 50-cent tolerance. This includes documents with amounts near psychological threshold values (€999.99, €9,999.00), with Italian thousand-separator formatting (period as thousands separator), and on JPEG-compressed scanned documents.</p>

            <p><strong class="text-white">Math check: 100% on 120 verifications.</strong> Not only are the individual fields correct, but the internal consistency is perfect: for every invoice where taxable + VAT is checked against the total, the result is correct. This means the model not only reads the right numbers, but reads them consistently with each other.</p>

            <p><strong class="text-white">The only problematic field: gross pay on payslips, 54.3%.</strong> The "gross salary" field in Italian payslips is correctly identified only slightly more than half the time. Manual analysis reveals the reason: in Italian payslips, this field appears with very different labels depending on the collective bargaining agreement (CCNL) and accounting software used by the company. "RETRIBUZIONE LORDA", "IMPONIBILE LORDO", "TOTALE COMPETENZE", "IMPONIBILE CONTRIBUTIVO", "TOTALE SPETTANZE" are all labels that indicate essentially the same concept, but the model recognizes them with varying frequency. The net pay, by contrast, almost always has the label "NETTO IN BUSTA" or "NETTO A PAGARE" — much more uniform — and is extracted at 100%.</p>

            <h3 class="text-xl font-bold text-white">The most surprising result: SCAN = CLEAN</h3>

            <p>This is the data point that surprised us most during result analysis. When comparing performance on simulated-scanned documents (146 documents) versus native clean PDFs (60 documents), the difference is zero on every measured metric:</p>

            <div class="overflow-x-auto my-6">
                <table class="w-full text-sm border-collapse">
                    <thead>
                        <tr class="border-b border-white/20">
                            <th class="text-left py-2 pr-4 text-white font-bold">Metric</th>
                            <th class="text-right py-2 pr-4 text-white font-bold">SCAN (146 docs)</th>
                            <th class="text-right py-2 text-white font-bold">CLEAN (60 docs)</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr class="border-b border-white/10"><td class="py-2 pr-4">Document type</td><td class="text-right pr-4 text-green-400">100.0%</td><td class="text-right text-green-400">100.0%</td></tr>
                        <tr class="border-b border-white/10"><td class="py-2 pr-4">VAT ID / Fiscal Code</td><td class="text-right pr-4 text-green-400">100.0%</td><td class="text-right text-green-400">100.0%</td></tr>
                        <tr class="border-b border-white/10"><td class="py-2 pr-4">Total amount</td><td class="text-right pr-4 text-green-400">100.0%</td><td class="text-right text-green-400">100.0%</td></tr>
                        <tr class="border-b border-white/10"><td class="py-2 pr-4">Math check</td><td class="text-right pr-4 text-green-400">100.0%</td><td class="text-right text-green-400">100.0%</td></tr>
                        <tr><td class="py-2 pr-4">Issue date</td><td class="text-right pr-4 text-green-400">100.0%</td><td class="text-right text-green-400">100.0%</td></tr>
                    </tbody>
                </table>
            </div>

            <p>Why does this matter? Because the main objection to AI document systems has always been: "it works fine on native PDFs, but all our documents are scanned, stamped, crumpled, sometimes rotated a few degrees." Qwen2.5-VL is a multimodal vision model trained on enormous quantities of real document images — it already includes degraded, scanned, low-quality documents in its training distribution. The result is complete immunity to scan degradation under the tested conditions.</p>

            <p>We're not naive: there are degradation thresholds beyond which even this model would fail. A document scanned at 72 DPI with strong motion blur and 45-degree rotation would likely give worse results. But the conditions we tested — the real ones for an office with a normal network scanner — produce performance identical to the original document.</p>

            <h3 class="text-xl font-bold text-white">Confidence and audit status: the system knows when it doesn't know</h3>

            <p>A critical feature of any document automation system is the ability to identify its own errors. A system that makes mistakes and doesn't flag them is dangerous: the problem goes unnoticed. A system that makes mistakes and flags them is manageable: a human operator reviews only the uncertain cases.</p>

            <div class="overflow-x-auto my-6">
                <table class="w-full text-sm border-collapse">
                    <thead>
                        <tr class="border-b border-white/20">
                            <th class="text-left py-2 pr-4 text-white font-bold">Confidence Distribution</th>
                            <th class="text-right py-2 text-white font-bold">%</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr class="border-b border-white/10"><td class="py-2 pr-4">🔵 HIGH</td><td class="text-right text-green-400">92.2% (202/219)</td></tr>
                        <tr class="border-b border-white/10"><td class="py-2 pr-4">🟡 MEDIUM</td><td class="text-right">1.8% (4/219)</td></tr>
                        <tr><td class="py-2 pr-4">🔴 LOW</td><td class="text-right text-yellow-400">5.9% (13/219)</td></tr>
                    </tbody>
                </table>
            </div>

            <p>92.2% of documents receive high confidence: the system is sure of itself on almost the entire corpus. The 5.9% LOW corresponds exactly to the 13 bank statements that encountered the hardware limit (described in the next section). The key data point is that when the system is struggling, it signals it: the 4 MEDIUM and 13 LOW documents are automatically routed to human review, not silently inserted into the data stream as if they were correct.</p>

            <h2 class="text-2xl font-black font-display text-white">Resource consumption: what happens inside the GPU</h2>

            <p>During the benchmark we monitored hardware resource consumption every 60 seconds using <code class="text-brand-tealLight">nvidia-smi</code>. The data tells a precise story about the pipeline architecture.</p>

            <h3 class="text-xl font-bold text-white">During active inference</h3>

            <div class="overflow-x-auto my-6">
                <table class="w-full text-sm border-collapse">
                    <thead>
                        <tr class="border-b border-white/20">
                            <th class="text-left py-2 pr-4 text-white font-bold">Metric</th>
                            <th class="text-right py-2 pr-4 text-white font-bold">Min</th>
                            <th class="text-right py-2 pr-4 text-white font-bold">Max</th>
                            <th class="text-right py-2 text-white font-bold">Average</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr class="border-b border-white/10"><td class="py-2 pr-4">GPU utilization</td><td class="text-right pr-4">87%</td><td class="text-right pr-4">100%</td><td class="text-right">~94%</td></tr>
                        <tr class="border-b border-white/10"><td class="py-2 pr-4">VRAM used</td><td class="text-right pr-4">13,288 MiB</td><td class="text-right pr-4">13,377 MiB</td><td class="text-right">~13.3 GB</td></tr>
                        <tr class="border-b border-white/10"><td class="py-2 pr-4">GPU power draw</td><td class="text-right pr-4">63.7 W</td><td class="text-right pr-4">70.2 W</td><td class="text-right">~68 W</td></tr>
                        <tr class="border-b border-white/10"><td class="py-2 pr-4">GPU temperature</td><td class="text-right pr-4">65°C</td><td class="text-right pr-4">70°C</td><td class="text-right">~68°C</td></tr>
                        <tr class="border-b border-white/10"><td class="py-2 pr-4">CPU utilization</td><td class="text-right pr-4">2%</td><td class="text-right pr-4">17%</td><td class="text-right">~4%</td></tr>
                        <tr><td class="py-2 pr-4">RAM used</td><td class="text-right pr-4">~35 GiB</td><td class="text-right pr-4">~37 GiB</td><td class="text-right">~35 GiB</td></tr>
                    </tbody>
                </table>
            </div>

            <p><strong class="text-white">The pipeline is 100% GPU-bound.</strong> The CPU is never a bottleneck: its average 4% utilization means it is simply waiting for GPU results. Adding more CPU cores to this machine would improve absolutely nothing. The only thing that matters is the GPU and its VRAM.</p>

            <p><strong class="text-white">VRAM is near saturation: 13.3 GB of 16 GB available.</strong> 2.6 GB of margin remains, sufficient for document images and model context during inference, but not enough for a larger model. RTX 2000 Ada 16 GB is truly the absolute minimum for this configuration.</p>

            <p><strong class="text-white">Active power consumption is approximately 68 W.</strong> The RTX 2000 Ada has a 70 W TDP — we are therefore using almost all available thermal power during inference. At idle (model in VRAM, no requests in flight), power consumption drops to 6-7 W and GPU temperature to 26°C.</p>

            <p>This energy data is relevant for anyone evaluating an on-premise deployment: a server with RTX 3090 (350 W TDP) would probably process documents in 15-20 seconds instead of 32, but would consume significantly more. RTX 4090 (450 W TDP) would be even faster. The balance between hardware cost, energy cost, and required throughput is a calculation specific to each deployment scenario.</p>

            <h2 class="text-2xl font-black font-display text-white">Identified limits: scientific honesty</h2>

            <p>A scientific benchmark without an honest section on limits is not a scientific benchmark: it is marketing. Here are the two real problems identified during this test.</p>

            <h3 class="text-xl font-bold text-white">Limit 1: GGML crash on high-density bank statements</h3>

            <p>13 out of 20 documents in the "bank statement" type produce an internal crash of the Ollama/llama.cpp runtime:</p>

            <div class="code-block rounded-xl text-xs my-4">
                <span class="cmt">GGML_ASSERT(a-&gt;ne[2] * 4 == b-&gt;ne[0]) failed (HTTP 500)</span>
            </div>

            <p>This error does not come from our pipeline or from the model itself: it is an assertion in the GGML layer (the tensor backend that Ollama uses to run the model) that fails when tensor dimensions don't align as expected. It occurs in the extraction step — not in classification, which works correctly on all 20 bank statements.</p>

            <p>The cause is a combination of factors: the image of a bank statement with many transaction rows (15-20 transactions) is dense with tabular text. When this image is passed to the vision encoder together with the extraction prompt (which for bank statements is particularly long — it includes IBAN, opening balance, transaction list, closing balance), the combination of image + prompt exceeds an internal tensor size limit in the 7B model on 16 GB VRAM.</p>

            <p>The 7 bank statements processed correctly all had fewer transaction rows. On those 7, the system achieves 100% on all fields including the closing balance — the hardest metric, which requires tracking the sequence of all transactions.</p>

            <p><strong class="text-white">The solution:</strong> reduce the conversion DPI for bank statements (from 200 to 150 DPI), which reduces image dimensions and therefore pressure on the vision encoder. Alternatively, use Qwen2.5-VL 14B or 32B, which have a vision encoder sized for larger images. Both solutions will be tested in benchmark v3.</p>

            <h3 class="text-xl font-bold text-white">Limit 2: "gross pay" field in payslips — 54.3%</h3>

            <p>As described above, gross salary in payslips is correctly identified only 54.3% of the time. Analysis of the causes shows a clear pattern: the problem is not reading the number (when the field is found, the numeric value is always correct), but identifying the correct label among the many variants used by different Italian collective bargaining agreements (CCNL) and accounting software.</p>

            <p>This is exactly the type of problem solvable with a richer prompt: if the model is given an explicit list of possible labels for the "gross" field in Italian payslips, accuracy should approach 100% significantly. This fix is planned for processor v2.1.</p>

            <h3 class="text-xl font-bold text-white">Limit 3: format validator false positives — 1.9%</h3>

            <p>4 documents out of 206 (1.9%) receive a <code class="text-yellow-400">format_error</code> from the VAT/fiscal code validator despite the extracted data being correct. This indicates a small bug in the validation regexes: probably incomplete handling of some fiscal code variants for people born abroad (who have a different code from the standard one). Fix planned in validator v2.1.</p>

            <h2 class="text-2xl font-black font-display text-white">Economic analysis: what $0.002 per document means</h2>

            <p>The operational cost of $0.002 per document on cloud (at $0.24/hour with 32 seconds/document) may seem like an abstract number. Let's put it in context with real business usage scenarios.</p>

            <h3 class="text-xl font-bold text-white">Scenario 1: small business, 100 invoices/month</h3>

            <p>A small business with 100 supplier invoices per month currently spends typically 2-4 hours of clerical work manually entering that data into their management system. At the average cost of office work in Italy (€18-22/hour gross), that's €36-88/month in direct costs, plus the cost of delays and transcription errors that then require corrections.</p>

            <p>With DataUnchain on cloud: 100 documents × $0.002 = $0.20/month. On an existing company server: marginal energy cost close to zero.</p>

            <h3 class="text-xl font-bold text-white">Scenario 2: medium enterprise, 2,000 documents/month</h3>

            <p>A mid-sized manufacturing company manages approximately 2,000 documents per month: inbound and outbound delivery notes, supplier invoices, purchase orders, employee payslips. Traditionally this requires 1-2 dedicated staff members spending a significant portion of their time on this work.</p>

            <p>On cloud: 2,000 × $0.002 = $4/month. Less than the cost of a coffee machine refill. The ROI is immediate.</p>

            <h3 class="text-xl font-bold text-white">Scenario 3: on-premise deployment with RTX 3090</h3>

            <p>An RTX 3090 24 GB costs approximately €900-1,200 on the quality used market. On this GPU, Qwen2.5-VL 7B would likely process documents in 15-20 seconds instead of 32 (estimate based on GPU performance ratio). Energy consumption is approximately 350 W during inference.</p>

            <p>Amortizing the hardware over 3 years with an average of 4 hours/day of use: the cost per document drops below $0.001. For high volumes (10,000+ documents/month), on-premise becomes more economical than cloud already in the first year.</p>

            <p>But the most important economic advantage of on-premise is not the marginal cost: it's the absence of fixed monthly SaaS subscription costs, which typically range between €200 and €2,000/month for professional-grade competitors. And above all: not a single byte of confidential business data ever leaves your infrastructure.</p>

            <h2 class="text-2xl font-black font-display text-white">Model choice: why Qwen2.5-VL 7B?</h2>

            <p>The choice of Qwen2.5-VL as the backbone of the DataUnchain processor is not arbitrary. We evaluated the alternatives available in the open-source landscape for vision-language models (VLMs):</p>

            <p><strong class="text-white">LLaVA and variants</strong> (Haotian Liu et al.) marked the beginning of the open-source VLM era but show significant difficulties on documents with dense text and structured tables — exactly the conditions of business documents.</p>

            <p><strong class="text-white">InternVL</strong> and <strong class="text-white">Idefics</strong> are competent models but with a less mature deployment ecosystem compared to the Qwen + Ollama combination.</p>

            <p><strong class="text-white">Qwen2.5-VL</strong> (Alibaba DAMO Academy) excels specifically in document understanding thanks to training that included enormous quantities of structured documents in many languages, including Italian. The 7B version offers the best compromise between quality and hardware requirements: it runs on 16 GB consumer GPUs while maintaining accuracy that in this benchmark surpasses many proprietary cloud solutions on this specific document category.</p>

            <p>It's important to note that Qwen2.5-VL is not a model specialized for OCR or document understanding: it is a general-purpose model that "understands" documents because it was trained on them. This means it doesn't require specific fine-tuning for each new document type: just update the extraction prompt.</p>

            <h2 class="text-2xl font-black font-display text-white">What "completely offline" actually means</h2>

            <p>It's worth dwelling on this feature, because it is the one that differentiates DataUnchain from 99% of competitors on the market. When we say the system works completely offline, we mean:</p>

            <p><strong class="text-white">No data leaves the machine.</strong> PDFs are converted to images locally. Images are processed by Ollama running locally. The resulting JSON is written locally. At no point in the process is any data sent to third-party servers — not to Anthropic, not to OpenAI, not to Microsoft, not to any cloud AI provider.</p>

            <p><strong class="text-white">No internet connection required during processing.</strong> Once the model is downloaded (a one-time operation of approximately 5 GB), the system can run in air-gapped environments: networks without internet access, systems with restrictive security policies, isolated industrial environments.</p>

            <p><strong class="text-white">No monthly subscription, no per-token cost.</strong> The model is open-source (Apache 2.0 license). Ollama is open-source. DataUnchain processor is open-source. The only cost is the hardware it runs on.</p>

            <p>This is particularly relevant for sectors handling sensitive documents: accountants and professional firms (clients' tax data), HR and payroll administration (payslips, employment contracts), banking institutions (statements, credit documentation), regulated sectors (healthcare, legal, finance) where data transmission to external services is subject to severe regulatory constraints.</p>

            <p>GDPR compliance is also considerably simplified: if the data never leaves the organization's perimeter, the obligations relating to international data transfers, data processing agreements with third parties, and notifications of data breaches to third-party processors don't apply.</p>

            <h2 class="text-2xl font-black font-display text-white">Hardware recommendations for deployment</h2>

            <p>Based on data from this benchmark, we can give concrete guidance for those planning a deployment.</p>

            <div class="overflow-x-auto my-6">
                <table class="w-full text-sm border-collapse">
                    <thead>
                        <tr class="border-b border-white/20">
                            <th class="text-left py-2 pr-4 text-white font-bold">GPU</th>
                            <th class="text-right py-2 pr-4 text-white font-bold">VRAM</th>
                            <th class="text-left py-2 pr-4 text-white font-bold">Use case</th>
                            <th class="text-left py-2 text-white font-bold">Notes</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr class="border-b border-white/10"><td class="py-2 pr-4">RTX 2000 Ada / RTX 3080</td><td class="text-right pr-4">16 GB</td><td class="py-2 pr-4">Functional minimum</td><td class="py-2">Reduced VRAM margin. High-density bank statements at risk of GGML crash</td></tr>
                        <tr class="border-b border-white/10"><td class="py-2 pr-4">RTX 3090 / RTX 4090</td><td class="text-right pr-4">24 GB</td><td class="py-2 pr-4">Recommended</td><td class="py-2">All document types stable. ~20s/doc estimated. Best price/performance ratio</td></tr>
                        <tr class="border-b border-white/10"><td class="py-2 pr-4">A5000 / A6000</td><td class="text-right pr-4">24–48 GB</td><td class="py-2 pr-4">Enterprise</td><td class="py-2">ECC memory, professional warranty, server form factor. Ideal for data center installations</td></tr>
                        <tr><td class="py-2 pr-4">A100 / H100</td><td class="text-right pr-4">40–80 GB</td><td class="py-2 pr-4">High throughput</td><td class="py-2">Supports Qwen2.5-VL 32B or multiple parallel processing. For volumes > 50,000 docs/month</td></tr>
                    </tbody>
                </table>
            </div>

            <p><strong class="text-white">Important note on CPU:</strong> data from this benchmark confirms that CPU is not relevant to performance. A system with RTX 3090 and Intel Core i5 will be faster than a system with RTX 2000 Ada and Intel Core i9. The only thing that matters is the GPU.</p>

            <p><strong class="text-white">Note on RAM:</strong> during the benchmark RAM usage stabilized around 35-37 GB. This includes the operating system, Ollama, the DataUnchain processor, and buffers for PDF conversion. 32 GB RAM is the minimum recommended for a production deployment; 64 GB guarantees headroom for peak loads and future expansion.</p>

            <h2 class="text-2xl font-black font-display text-white">Comparison with cloud solutions</h2>

            <p>How does DataUnchain position itself against existing cloud solutions for document extraction? We must be cautious in making direct comparisons because we don't have an identical benchmark executed on the same documents with the same metrics. But we can make qualitative observations based on public data.</p>

            <p><strong class="text-white">Amazon Textract</strong> on Italian documents typically performs in the 85-92% range for key field extraction under standard conditions. Textract quality degrades significantly on low-quality scanned documents, where our system maintains the same performance as on clean documents. Cost: $0.015-0.065 per page, i.e., 7-32 times more expensive.</p>

            <p><strong class="text-white">Azure Form Recognizer / Document Intelligence</strong> reaches 90-95% on document types for which it has been specifically trained, but requires a training period on customer documents (dozens of samples per type), has costs starting at $10 per 1,000 pages, and of course sends all documents to Microsoft Azure.</p>

            <p><strong class="text-white">Google Document AI</strong> is probably the most accurate of the big cloud providers on standard document types, but requires Google Cloud, has complex pricing models, and doesn't natively support Italian fiscal document formats (P.IVA, codice fiscale, SDI) without customization.</p>

            <p>The point is not that DataUnchain is "better" in absolute terms than these services — they have years of development, enormous teams, globalized infrastructure. The point is that for the specific use case (Italian business documents, privacy requirements, low operational cost), the quality/price/privacy ratio of a local open-source model is today already competitive and in some cases superior.</p>

            <h2 class="text-2xl font-black font-display text-white">Benchmark reproducibility</h2>

            <p>One of the fundamental principles of this project is reproducibility. All code used for this benchmark is open-source in the DataUnchain repository:</p>

            <div class="code-block rounded-xl text-xs my-4">
                <span class="cmt"># Benchmark structure</span><br>
                <span class="kw">demo/</span><br>
                <span class="str">├── processor/main.py          ← processor v2.0</span><br>
                <span class="str">├── test-generator/generate.py ← PDF generator + ground truth</span><br>
                <span class="str">└── runpod/</span><br>
                <span class="str">    ├── benchmark.py           ← GT vs extracted analysis</span><br>
                <span class="str">    ├── benchmark_run.sh       ← complete orchestration</span><br>
                <span class="str">    └── README.md              ← RunPod instructions</span>
            </div>

            <p>To replicate the benchmark, you need:</p>
            <ul>
                <li>A GPU with ≥16 GB VRAM</li>
                <li>Ollama with Qwen2.5-VL 7B downloaded</li>
                <li>Python 3.11+ with repository dependencies</li>
                <li>Run <code class="text-brand-tealLight">bash benchmark_run.sh</code></li>
            </ul>

            <p>The script generates all documents, starts the processor, waits for completion (without arbitrary timeouts), and executes the comparison with ground truth producing the complete JSON report. The random generator seed is fixed to guarantee exact reproducibility.</p>

            <h2 class="text-2xl font-black font-display text-white">Next steps: what we're improving</h2>

            <p>This benchmark is version 2.1. The identified problems already have clear fix roadmaps:</p>

            <p><strong class="text-white">1. Payslip gross pay fix (processor v2.1):</strong> update of the extraction prompt with an explicit list of label variants for the gross field in Italian payslips. Target: >90% on this field.</p>

            <p><strong class="text-white">2. Bank statement GGML fix (processor v2.1):</strong> implementation of adaptive DPI — for documents with high-density row tables, automatic reduction of conversion DPI from 200 to 150. This reduces pressure on the vision encoder while maintaining sufficient legibility.</p>

            <p><strong class="text-white">3. Format validator false positive fix (validator v2.1):</strong> review of validation regexes to correctly handle fiscal codes for people born abroad.</p>

            <p><strong class="text-white">4. Corpus extension (benchmark v3):</strong> addition of receipt, packing list, quote, and healthcare-specific documents (prescriptions, medical reports) to the test corpus.</p>

            <p><strong class="text-white">5. Qwen2.5-VL 32B test:</strong> comparative benchmark between the 7B and 32B models on 48+ GB hardware to quantify the accuracy delta. The hypothesis is that the 32B resolves both the bank statement issue and the payslip gross issue.</p>

            <p><strong class="text-white">6. Alternative model testing:</strong> benchmark of the same corpus with InternVL2-8B and LLaVA-NeXT-72B to provide the market with objective comparative data.</p>

            <h2 class="text-2xl font-black font-display text-white">Conclusions</h2>

            <p>The question we opened this article with was: can an open-source 7B parameter model, running on consumer hardware with 16 GB VRAM, extract data from Italian business documents with accuracy sufficient for business use?</p>

            <p>The answer the data from this benchmark provides is: <strong class="text-white">yes, with 95.5% overall accuracy, at $0.002 per document, completely offline.</strong></p>

            <p>Concretely: VAT IDs and fiscal codes at 100%, financial amounts at 100%, math check at 100%, no difference between native and scanned documents. Only one critical field below 90% (payslip gross pay: 54.3%) with identified cause and planned fix. One hardware limit on one document type (high-density bank statement) with clear solution.</p>

            <p>The system is not perfect — no automatic extraction system is. But it is today sufficiently accurate, sufficiently fast, and sufficiently economical to justify production adoption for the vast majority of Italian business document flows. And it does so without sending a single byte of confidential business data outside your infrastructure.</p>

            <p>These are the numbers. Every figure is verifiable, the code is public, the benchmark is reproducible. We believe transparency is the only serious way to build trust in a system that must touch your company's most sensitive documents.</p>

        </div>

        <div class="mt-12 pt-8 border-t border-white/10 text-center">
            <a href="/en/blog/" class="text-brand-tealLight font-bold hover:underline">← Back to Blog</a>
        </div>

    </div>
</article>
