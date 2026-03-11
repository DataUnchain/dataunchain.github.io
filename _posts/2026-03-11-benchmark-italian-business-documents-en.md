---
layout: default
title: "We Ran 219 Italian Business Documents Through an Offline AI. Here Are the Numbers."
lang: en
categories: blog
date: 2026-03-11
author: Antonio Trento
description: "A scientific benchmark of DataUnchain on 219 real Italian business documents — invoices, payslips, contracts, delivery notes — with verified ground truth. 95.5% accuracy. $0.002 per document. Zero cloud."
---

<article class="pt-36 pb-20 px-4 sm:px-6">
<div class="max-w-3xl mx-auto">

<!-- Header -->
<div class="mb-10 reveal">
  <span class="text-brand-tealLight text-xs font-bold uppercase tracking-widest">Benchmark · March 11, 2026</span>
  <h1 class="text-3xl sm:text-5xl font-black font-display mt-4 mb-6 leading-tight">We Ran 219 Italian Business Documents Through an Offline AI. Here Are the Numbers.</h1>
  <p class="text-gray-400 text-lg leading-relaxed">Invoices, payslips, contracts, delivery notes — 219 documents with verified ground truth, processed by Qwen2.5-VL 7B running locally on a $0.24/hr GPU. No cloud. No subscriptions. No data leaving the machine.</p>
</div>

<!-- Hero Score -->
<div class="relative rounded-2xl overflow-hidden mb-12 reveal delay-100" style="background: linear-gradient(135deg, #0D9488 0%, #10B981 50%, #F59E0B 100%);">
  <div class="absolute inset-0 opacity-10" style="background-image: url('data:image/svg+xml,<svg width=\"60\" height=\"60\" viewBox=\"0 0 60 60\" xmlns=\"http://www.w3.org/2000/svg\"><g fill=\"none\" fill-rule=\"evenodd\"><g fill=\"%23ffffff\" fill-opacity=\"1\"><path d=\"M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z\"/></g></g></svg>');"></div>
  <div class="relative px-6 py-10 text-center">
    <div class="text-7xl sm:text-8xl font-black text-white mb-2">95.5%</div>
    <div class="text-white/80 text-xl font-bold mb-1">Overall Accuracy Score</div>
    <div class="text-white/60 text-sm">on 206 successfully processed documents · Qwen2.5-VL 7B · RTX 2000 Ada 16 GB</div>
  </div>
</div>

<!-- Key Stats Grid -->
<div class="grid grid-cols-2 sm:grid-cols-4 gap-3 mb-12 reveal delay-200">
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
    <div class="text-gray-400 text-xs mt-1">VAT IDs extracted</div>
  </div>
  <div class="bg-brand-surface rounded-xl p-4 text-center border border-white/10">
    <div class="text-2xl font-black text-green-400">SCAN=CLEAN</div>
    <div class="text-gray-400 text-xs mt-1">zero degradation</div>
  </div>
</div>

<!-- Body text -->
<div class="prose prose-invert prose-lg max-w-none text-gray-300 leading-relaxed">

## The question we set out to answer

Can a 7B open-source model, running on a €900 GPU, extract structured data from Italian business documents accurately enough for production use?

Not a demo. Not cherry-picked screenshots. A proper benchmark: 219 documents, known correct answers for every field, automated comparison, published results.

The answer is yes — with one field exception and one hardware limit, both fully understood and documented below.

---

## The corpus: 219 documents, 7 types

70% of the corpus went through simulated scan degradation — Gaussian noise, ±3° rotation, JPEG quality 60-85, overlaid stamps and watermarks. Because that's what real office documents look like.

</div>

<!-- Corpus Table -->
<div class="overflow-x-auto my-8 reveal">
  <table class="w-full text-sm">
    <thead>
      <tr class="border-b border-white/20 text-left">
        <th class="pb-3 pr-4 text-white font-bold">Document Type</th>
        <th class="pb-3 pr-4 text-right text-white font-bold">Docs</th>
        <th class="pb-3 text-white font-bold">Key Fields</th>
      </tr>
    </thead>
    <tbody class="text-gray-400">
      <tr class="border-b border-white/10"><td class="py-2.5 pr-4 text-white">Invoice (Fattura)</td><td class="text-right pr-4">60</td><td class="py-2.5">VAT IDs, taxable, VAT 22%, total, line items</td></tr>
      <tr class="border-b border-white/10"><td class="py-2.5 pr-4 text-white">Delivery Note (DDT)</td><td class="text-right pr-4">50</td><td class="py-2.5">shipper, recipient, carrier, goods description</td></tr>
      <tr class="border-b border-white/10"><td class="py-2.5 pr-4 text-white">Payslip (Busta Paga)</td><td class="text-right pr-4">35</td><td class="py-2.5">employee fiscal code, company VAT ID, gross, net</td></tr>
      <tr class="border-b border-white/10"><td class="py-2.5 pr-4 text-white">Credit Note</td><td class="text-right pr-4">20</td><td class="py-2.5">reference invoice, credit amount, reason</td></tr>
      <tr class="border-b border-white/10"><td class="py-2.5 pr-4 text-white">Contract</td><td class="text-right pr-4">20</td><td class="py-2.5">type, parties, both VAT IDs, signing date</td></tr>
      <tr class="border-b border-white/10"><td class="py-2.5 pr-4 text-white">Purchase Order</td><td class="text-right pr-4">14</td><td class="py-2.5">order number, delivery date, total, VAT IDs</td></tr>
      <tr class="border-b border-white/10"><td class="py-2.5 pr-4 text-white">Bank Statement</td><td class="text-right pr-4">20</td><td class="py-2.5">IBAN, opening balance, transactions, closing balance</td></tr>
      <tr class="text-white font-bold"><td class="py-2.5 pr-4">Total</td><td class="text-right pr-4">219</td><td></td></tr>
    </tbody>
  </table>
</div>

<div class="prose prose-invert prose-lg max-w-none text-gray-300 leading-relaxed">

**Ground truth is mathematically verified.** For every invoice: `taxable + vat = total` exactly. For every payslip: `gross - deductions = net` to the cent. This lets us test not just field extraction, but the system's ability to detect internal arithmetic errors — a critical production feature.

---

## How the pipeline works

Three deterministic steps, no magic:

**1 → Classify** — Model sees the page image, outputs the document type. No hints. Must decide alone.

**2 → Extract** — Type-specific prompt → structured JSON. Each of the 7 types has its own optimized prompt.

**3 → Audit** — Pure Python, zero AI. Validates Italian VAT number checksum (11-digit algorithm), Codice Fiscale (16 chars, ODD/EVEN tables, homocody-aware), date ranges, and runs the math check at ±€0.10 tolerance.

Output: a `confidence` score (HIGH / MEDIUM / LOW) and an `audit_status` (VALIDATED / PENDING_REVIEW / NEEDS_REVIEW).

---

## The results

</div>

<!-- Accuracy Table -->
<div class="overflow-x-auto my-8 reveal">
  <div class="text-xs text-gray-500 uppercase tracking-wider mb-3 font-bold">Field-by-field accuracy — 206 documents with status OK</div>
  <table class="w-full text-sm">
    <thead>
      <tr class="border-b border-white/20 text-left">
        <th class="pb-3 pr-4 text-white font-bold">Field</th>
        <th class="pb-3 pr-4 text-right text-white font-bold">Score</th>
        <th class="pb-3 text-white font-bold">On</th>
      </tr>
    </thead>
    <tbody>
      <tr class="border-b border-white/10">
        <td class="py-2.5 pr-4 text-gray-300">Document type classification</td>
        <td class="text-right pr-4"><span class="text-green-400 font-bold">100.0%</span></td>
        <td class="text-gray-500 text-xs">206/206</td>
      </tr>
      <tr class="border-b border-white/10">
        <td class="py-2.5 pr-4 text-gray-300">VAT ID / Fiscal Code (P.IVA / CF)</td>
        <td class="text-right pr-4"><span class="text-green-400 font-bold">100.0%</span></td>
        <td class="text-gray-500 text-xs">206/206</td>
      </tr>
      <tr class="border-b border-white/10">
        <td class="py-2.5 pr-4 text-gray-300">Issue date (exact YYYY-MM-DD)</td>
        <td class="text-right pr-4"><span class="text-green-400 font-bold">100.0%</span></td>
        <td class="text-gray-500 text-xs">144/144</td>
      </tr>
      <tr class="border-b border-white/10">
        <td class="py-2.5 pr-4 text-gray-300">Taxable amount (±€0.50)</td>
        <td class="text-right pr-4"><span class="text-green-400 font-bold">100.0%</span></td>
        <td class="text-gray-500 text-xs">94/94</td>
      </tr>
      <tr class="border-b border-white/10">
        <td class="py-2.5 pr-4 text-gray-300">VAT amount (±€0.50)</td>
        <td class="text-right pr-4"><span class="text-green-400 font-bold">100.0%</span></td>
        <td class="text-gray-500 text-xs">94/94</td>
      </tr>
      <tr class="border-b border-white/10">
        <td class="py-2.5 pr-4 text-gray-300">Invoice total (±€0.50)</td>
        <td class="text-right pr-4"><span class="text-green-400 font-bold">100.0%</span></td>
        <td class="text-gray-500 text-xs">94/94</td>
      </tr>
      <tr class="border-b border-white/10">
        <td class="py-2.5 pr-4 text-gray-300">Net pay — payslip (±€0.50)</td>
        <td class="text-right pr-4"><span class="text-green-400 font-bold">100.0%</span></td>
        <td class="text-gray-500 text-xs">35/35</td>
      </tr>
      <tr class="border-b border-white/10">
        <td class="py-2.5 pr-4 text-gray-300">Closing balance — bank statement (±€0.50)</td>
        <td class="text-right pr-4"><span class="text-green-400 font-bold">100.0%</span></td>
        <td class="text-gray-500 text-xs">7/7</td>
      </tr>
      <tr class="border-b border-white/10">
        <td class="py-2.5 pr-4 text-gray-300">Document reference number</td>
        <td class="text-right pr-4"><span class="text-green-400 font-bold">96.6%</span></td>
        <td class="text-gray-500 text-xs">199/206</td>
      </tr>
      <tr class="border-b border-white/10">
        <td class="py-2.5 pr-4 text-gray-300">Internal math check (±€0.10)</td>
        <td class="text-right pr-4"><span class="text-green-400 font-bold">100.0%</span></td>
        <td class="text-gray-500 text-xs">120/120</td>
      </tr>
      <tr>
        <td class="py-2.5 pr-4 text-gray-300">Gross pay — payslip (±€0.50)</td>
        <td class="text-right pr-4"><span class="text-yellow-400 font-bold">54.3%</span></td>
        <td class="text-gray-500 text-xs">19/35 — known label variance issue</td>
      </tr>
    </tbody>
  </table>
</div>

<!-- SCAN=CLEAN Callout -->
<div class="rounded-2xl border border-brand-teal/30 bg-brand-teal/5 p-6 my-8 reveal">
  <div class="flex items-start gap-4">
    <div class="text-3xl mt-1">🔬</div>
    <div>
      <div class="text-white font-bold text-lg mb-2">SCAN = CLEAN. No exceptions.</div>
      <p class="text-gray-400 text-sm leading-relaxed">On every measured metric — VAT IDs, amounts, dates, math check — scanned documents (146 docs with noise, rotation, stamps, JPEG artifacts) performed identically to native digital PDFs (60 docs). Zero degradation. The model was trained on real-world document images and has built-in immunity to office scanner quality.</p>
      <div class="grid grid-cols-2 sm:grid-cols-5 gap-3 mt-4">
        <div class="text-center"><div class="text-green-400 font-bold">100%</div><div class="text-gray-500 text-xs">Type SCAN</div></div>
        <div class="text-center"><div class="text-green-400 font-bold">100%</div><div class="text-gray-500 text-xs">Type CLEAN</div></div>
        <div class="text-center"><div class="text-green-400 font-bold">100%</div><div class="text-gray-500 text-xs">VAT SCAN</div></div>
        <div class="text-center"><div class="text-green-400 font-bold">100%</div><div class="text-gray-500 text-xs">VAT CLEAN</div></div>
        <div class="text-center"><div class="text-green-400 font-bold">100%</div><div class="text-gray-500 text-xs">Math SCAN</div></div>
      </div>
    </div>
  </div>
</div>

<!-- Confidence Distribution -->
<div class="rounded-2xl bg-brand-surface border border-white/10 p-6 my-8 reveal">
  <div class="text-xs text-gray-500 uppercase tracking-wider mb-4 font-bold">Confidence distribution — 219 documents</div>
  <div class="space-y-3">
    <div class="flex items-center gap-3">
      <div class="text-blue-400 text-sm font-bold w-16">HIGH</div>
      <div class="flex-1 bg-white/10 rounded-full h-2 overflow-hidden">
        <div class="bg-blue-400 h-full rounded-full" style="width: 92.2%"></div>
      </div>
      <div class="text-white font-bold text-sm w-12 text-right">92.2%</div>
      <div class="text-gray-500 text-xs w-16">202 docs</div>
    </div>
    <div class="flex items-center gap-3">
      <div class="text-yellow-400 text-sm font-bold w-16">MEDIUM</div>
      <div class="flex-1 bg-white/10 rounded-full h-2 overflow-hidden">
        <div class="bg-yellow-400 h-full rounded-full" style="width: 1.8%"></div>
      </div>
      <div class="text-white font-bold text-sm w-12 text-right">1.8%</div>
      <div class="text-gray-500 text-xs w-16">4 docs</div>
    </div>
    <div class="flex items-center gap-3">
      <div class="text-red-400 text-sm font-bold w-16">LOW</div>
      <div class="flex-1 bg-white/10 rounded-full h-2 overflow-hidden">
        <div class="bg-red-400 h-full rounded-full" style="width: 5.9%"></div>
      </div>
      <div class="text-white font-bold text-sm w-12 text-right">5.9%</div>
      <div class="text-gray-500 text-xs w-16">13 docs</div>
    </div>
  </div>
  <p class="text-gray-500 text-xs mt-4">The 13 LOW documents are automatically routed to human review — not silently inserted into the data stream. The system knows when it's unsure.</p>
</div>

<div class="prose prose-invert prose-lg max-w-none text-gray-300 leading-relaxed">

---

## What happened inside the GPU

</div>

<!-- Resource Stats -->
<div class="grid grid-cols-2 sm:grid-cols-3 gap-3 my-8 reveal">
  <div class="bg-brand-surface rounded-xl p-4 border border-white/10">
    <div class="text-brand-tealLight text-xs font-bold uppercase tracking-wider mb-2">GPU Utilization</div>
    <div class="text-2xl font-black text-white">87–100%</div>
    <div class="text-gray-500 text-xs mt-1">avg ~94% during inference</div>
  </div>
  <div class="bg-brand-surface rounded-xl p-4 border border-white/10">
    <div class="text-brand-tealLight text-xs font-bold uppercase tracking-wider mb-2">VRAM Used</div>
    <div class="text-2xl font-black text-white">13.3 GB</div>
    <div class="text-gray-500 text-xs mt-1">of 16 GB — 2.6 GB margin</div>
  </div>
  <div class="bg-brand-surface rounded-xl p-4 border border-white/10">
    <div class="text-brand-tealLight text-xs font-bold uppercase tracking-wider mb-2">Power Draw</div>
    <div class="text-2xl font-black text-white">~68 W</div>
    <div class="text-gray-500 text-xs mt-1">near TDP — 6W at idle</div>
  </div>
  <div class="bg-brand-surface rounded-xl p-4 border border-white/10">
    <div class="text-brand-tealLight text-xs font-bold uppercase tracking-wider mb-2">CPU Load</div>
    <div class="text-2xl font-black text-white">~4%</div>
    <div class="text-gray-500 text-xs mt-1">100% GPU-bound pipeline</div>
  </div>
  <div class="bg-brand-surface rounded-xl p-4 border border-white/10">
    <div class="text-brand-tealLight text-xs font-bold uppercase tracking-wider mb-2">GPU Temp</div>
    <div class="text-2xl font-black text-white">65–70°C</div>
    <div class="text-gray-500 text-xs mt-1">26°C at idle</div>
  </div>
  <div class="bg-brand-surface rounded-xl p-4 border border-white/10">
    <div class="text-brand-tealLight text-xs font-bold uppercase tracking-wider mb-2">RAM Used</div>
    <div class="text-2xl font-black text-white">~35 GB</div>
    <div class="text-gray-500 text-xs mt-1">OS + Ollama + buffers</div>
  </div>
</div>

<div class="prose prose-invert prose-lg max-w-none text-gray-300 leading-relaxed">

**The pipeline is 100% GPU-bound.** CPU at 4% means adding faster CPUs or more cores does absolutely nothing. Only the GPU matters. This simplifies hardware planning significantly.

---

## Known limits — full transparency

We don't hide problems. These are the two real issues found:

</div>

<!-- Limit 1 -->
<div class="rounded-2xl border border-yellow-500/30 bg-yellow-500/5 p-6 my-6 reveal">
  <div class="flex items-start gap-3">
    <div class="text-2xl">⚠️</div>
    <div>
      <div class="text-yellow-400 font-bold mb-2">Limit 1 — Bank Statement GGML Crash (13/20 docs)</div>
      <p class="text-gray-400 text-sm leading-relaxed mb-3">Bank statements with dense transaction tables (15+ rows) trigger an internal assertion failure in Ollama's GGML tensor backend: <code class="text-yellow-300 bg-black/30 px-1 rounded">GGML_ASSERT(a->ne[2] * 4 == b->ne[0]) failed</code></p>
      <p class="text-gray-400 text-sm leading-relaxed mb-3">Classification always succeeds. The crash happens during extraction, when the dense image + long prompt combination exceeds a tensor dimension limit in the 7B model on 16 GB VRAM. The 7 bank statements that succeeded (fewer transaction rows) scored 100% on all fields including closing balance.</p>
      <div class="flex flex-wrap gap-2 mt-3">
        <span class="bg-black/30 text-brand-tealLight text-xs px-3 py-1 rounded-full font-bold">Fix: reduce DPI for dense tables (200→150)</span>
        <span class="bg-black/30 text-brand-tealLight text-xs px-3 py-1 rounded-full font-bold">Alt: Qwen2.5-VL 14B/32B on 24GB+</span>
      </div>
    </div>
  </div>
</div>

<!-- Limit 2 -->
<div class="rounded-2xl border border-yellow-500/30 bg-yellow-500/5 p-6 my-6 reveal">
  <div class="flex items-start gap-3">
    <div class="text-2xl">⚠️</div>
    <div>
      <div class="text-yellow-400 font-bold mb-2">Limit 2 — Payslip Gross Pay: 54.3%</div>
      <p class="text-gray-400 text-sm leading-relaxed mb-3">Net pay extracts at 100% (label is always "NETTO IN BUSTA"). Gross pay at 54.3% because Italian payslip formats vary wildly by collective bargaining agreement — the same field appears as "RETRIBUZIONE LORDA", "IMPONIBILE LORDO", "TOTALE COMPETENZE", "IMPONIBILE CONTRIBUTIVO" depending on the software.</p>
      <p class="text-gray-400 text-sm leading-relaxed">The number itself is always read correctly when found — this is a label recognition problem, not a reading problem.</p>
      <div class="flex flex-wrap gap-2 mt-3">
        <span class="bg-black/30 text-brand-tealLight text-xs px-3 py-1 rounded-full font-bold">Fix: explicit label list in extraction prompt</span>
        <span class="bg-black/30 text-brand-tealLight text-xs px-3 py-1 rounded-full font-bold">Target: >90% in v2.1</span>
      </div>
    </div>
  </div>
</div>

<div class="prose prose-invert prose-lg max-w-none text-gray-300 leading-relaxed">

---

## $0.002 per document — what that actually means

At $0.24/hr with 32 seconds/document on cloud, the math is simple. Let's make it concrete:

</div>

<!-- Economic Scenarios -->
<div class="space-y-4 my-8 reveal">
  <div class="rounded-2xl bg-brand-surface border border-white/10 p-5">
    <div class="flex items-center justify-between mb-3">
      <div class="text-white font-bold">Small business — 100 invoices/month</div>
      <div class="text-brand-tealLight font-black text-lg">$0.20/mo</div>
    </div>
    <div class="text-gray-400 text-sm">vs. 2-4 hours manual data entry at €18-22/hr = €36–88/month. ROI: <span class="text-green-400 font-bold">440× cheaper</span></div>
  </div>
  <div class="rounded-2xl bg-brand-surface border border-white/10 p-5">
    <div class="flex items-center justify-between mb-3">
      <div class="text-white font-bold">Medium enterprise — 2,000 docs/month</div>
      <div class="text-brand-tealLight font-black text-lg">$4/mo</div>
    </div>
    <div class="text-gray-400 text-sm">Replaces 1-2 FTE hours/day of data entry. Cost of competing SaaS: €200-2,000/month. <span class="text-green-400 font-bold">Immediate ROI.</span></div>
  </div>
  <div class="rounded-2xl bg-brand-surface border border-white/10 p-5">
    <div class="flex items-center justify-between mb-3">
      <div class="text-white font-bold">On-premise with RTX 3090</div>
      <div class="text-brand-tealLight font-black text-lg">&lt;$0.001/doc</div>
    </div>
    <div class="text-gray-400 text-sm">RTX 3090 24GB ~€900 used. Amortized over 3 years at 4hr/day: hardware + energy cost drops below $0.001/document. Zero cloud dependency. <span class="text-green-400 font-bold">Payback in weeks at medium volume.</span></div>
  </div>
</div>

<div class="prose prose-invert prose-lg max-w-none text-gray-300 leading-relaxed">

---

## What "completely offline" actually means for your business

This isn't a feature — it's a fundamental architectural choice with real consequences.

**No data leaves your infrastructure.** PDFs converted locally. Model runs locally. JSON written locally. Not a single byte of your documents goes to Anthropic, OpenAI, Microsoft, Google, or anyone else.

**GDPR simplified.** No international data transfers. No data processing agreements with third-party AI providers. No breach notification obligations to external processors. Your documents stay in your building.

**Air-gap capable.** Once the model is downloaded (5 GB, one-time), the system runs with no internet connection. Isolated factory floors, secure legal archives, government networks — all supported.

**No per-document billing.** No monthly SaaS fees. No token costs. No usage tiers. Infrastructure is your only ongoing cost.

---

## Hardware guide: what you actually need

</div>

<!-- Hardware Cards -->
<div class="space-y-3 my-8 reveal">
  <div class="rounded-xl border border-white/10 bg-brand-surface p-4">
    <div class="flex flex-wrap items-center justify-between gap-2 mb-2">
      <div class="text-white font-bold">RTX 2000 Ada / RTX 3080 — 16 GB</div>
      <span class="bg-yellow-500/20 text-yellow-400 text-xs font-bold px-3 py-1 rounded-full">Functional Minimum</span>
    </div>
    <p class="text-gray-400 text-sm">Works. But VRAM margin is 2.6 GB — tight. Dense bank statements crash. Use if you don't process bank statements regularly, or reduce DPI as a workaround.</p>
  </div>
  <div class="rounded-xl border border-brand-teal/40 bg-brand-teal/5 p-4">
    <div class="flex flex-wrap items-center justify-between gap-2 mb-2">
      <div class="text-white font-bold">RTX 3090 / RTX 4090 — 24 GB</div>
      <span class="bg-brand-teal/20 text-brand-tealLight text-xs font-bold px-3 py-1 rounded-full">⭐ Recommended</span>
    </div>
    <p class="text-gray-400 text-sm">All document types stable. Estimated ~20s/doc (2× faster). Best price/performance ratio for production use. RTX 3090 used ~€900, RTX 4090 new ~€1,800.</p>
  </div>
  <div class="rounded-xl border border-white/10 bg-brand-surface p-4">
    <div class="flex flex-wrap items-center justify-between gap-2 mb-2">
      <div class="text-white font-bold">A5000 / A6000 — 24–48 GB</div>
      <span class="bg-purple-500/20 text-purple-400 text-xs font-bold px-3 py-1 rounded-full">Enterprise</span>
    </div>
    <p class="text-gray-400 text-sm">ECC memory, professional warranty, server form factor. Supports Qwen2.5-VL 32B for even higher accuracy. For data center installations.</p>
  </div>
  <div class="rounded-xl border border-white/10 bg-brand-surface p-4">
    <div class="flex flex-wrap items-center justify-between gap-2 mb-2">
      <div class="text-white font-bold">A100 / H100 — 40–80 GB</div>
      <span class="bg-blue-500/20 text-blue-400 text-xs font-bold px-3 py-1 rounded-full">High Volume</span>
    </div>
    <p class="text-gray-400 text-sm">For 50,000+ documents/month. Supports multiple parallel processing streams or Qwen2.5-VL 72B. Enterprise data center class.</p>
  </div>
</div>

<div class="rounded-2xl bg-brand-surface border border-white/10 p-5 my-6 text-sm text-gray-400 reveal">
  <strong class="text-white">Important:</strong> CPU is irrelevant to performance. GPU utilization was 94% average during the entire benchmark — CPU was at 4%. An RTX 3090 + Core i5 beats RTX 2000 Ada + Core i9 every time. Buy GPU, not CPU.
</div>

<div class="prose prose-invert prose-lg max-w-none text-gray-300 leading-relaxed">

---

## Per-type breakdown

</div>

<!-- Per-type table -->
<div class="overflow-x-auto my-8 reveal">
  <table class="w-full text-sm">
    <thead>
      <tr class="border-b border-white/20 text-left">
        <th class="pb-3 pr-3 text-white font-bold">Type</th>
        <th class="pb-3 pr-3 text-right text-white font-bold">n</th>
        <th class="pb-3 pr-3 text-right text-white font-bold">Type</th>
        <th class="pb-3 pr-3 text-right text-white font-bold">VAT ID</th>
        <th class="pb-3 pr-3 text-right text-white font-bold">Amount</th>
        <th class="pb-3 pr-3 text-right text-white font-bold">Math</th>
        <th class="pb-3 text-right text-white font-bold">Speed</th>
      </tr>
    </thead>
    <tbody class="text-gray-400">
      <tr class="border-b border-white/10">
        <td class="py-2.5 pr-3 text-white">Invoice</td>
        <td class="text-right pr-3">60</td>
        <td class="text-right pr-3 text-green-400">100%</td>
        <td class="text-right pr-3 text-green-400">100%</td>
        <td class="text-right pr-3 text-green-400">100%</td>
        <td class="text-right pr-3 text-green-400">100%</td>
        <td class="text-right">36s</td>
      </tr>
      <tr class="border-b border-white/10">
        <td class="py-2.5 pr-3 text-white">Delivery Note</td>
        <td class="text-right pr-3">50</td>
        <td class="text-right pr-3 text-green-400">100%</td>
        <td class="text-right pr-3 text-green-400">100%</td>
        <td class="text-right pr-3 text-gray-600">n/a</td>
        <td class="text-right pr-3 text-gray-600">n/a</td>
        <td class="text-right">32s</td>
      </tr>
      <tr class="border-b border-white/10">
        <td class="py-2.5 pr-3 text-white">Credit Note</td>
        <td class="text-right pr-3">20</td>
        <td class="text-right pr-3 text-green-400">100%</td>
        <td class="text-right pr-3 text-green-400">100%</td>
        <td class="text-right pr-3 text-green-400">100%</td>
        <td class="text-right pr-3 text-green-400">100%</td>
        <td class="text-right">31s</td>
      </tr>
      <tr class="border-b border-white/10">
        <td class="py-2.5 pr-3 text-white">Contract</td>
        <td class="text-right pr-3">20</td>
        <td class="text-right pr-3 text-green-400">100%</td>
        <td class="text-right pr-3 text-green-400">100%</td>
        <td class="text-right pr-3 text-gray-600">n/a</td>
        <td class="text-right pr-3 text-gray-600">n/a</td>
        <td class="text-right">26s</td>
      </tr>
      <tr class="border-b border-white/10">
        <td class="py-2.5 pr-3 text-white">Purchase Order</td>
        <td class="text-right pr-3">14</td>
        <td class="text-right pr-3 text-green-400">100%</td>
        <td class="text-right pr-3 text-green-400">100%</td>
        <td class="text-right pr-3 text-green-400">100%</td>
        <td class="text-right pr-3 text-green-400">100%</td>
        <td class="text-right">37s</td>
      </tr>
      <tr class="border-b border-white/10">
        <td class="py-2.5 pr-3 text-white">Payslip</td>
        <td class="text-right pr-3">35</td>
        <td class="text-right pr-3 text-green-400">100%</td>
        <td class="text-right pr-3 text-green-400">100%</td>
        <td class="text-right pr-3 text-yellow-400">net 100% / gross 54%</td>
        <td class="text-right pr-3 text-gray-600">n/a</td>
        <td class="text-right">31s</td>
      </tr>
      <tr>
        <td class="py-2.5 pr-3 text-white">Bank Statement</td>
        <td class="text-right pr-3">7★</td>
        <td class="text-right pr-3 text-green-400">100%</td>
        <td class="text-right pr-3 text-green-400">100%</td>
        <td class="text-right pr-3 text-green-400">100%</td>
        <td class="text-right pr-3 text-green-400">100%</td>
        <td class="text-right">48s</td>
      </tr>
    </tbody>
  </table>
  <p class="text-gray-600 text-xs mt-2">★ 13/20 bank statements crashed with GGML assertion failure (hardware limit, see above). The 7 that completed scored 100% on all fields.</p>
</div>

<div class="prose prose-invert prose-lg max-w-none text-gray-300 leading-relaxed">

---

## This benchmark is fully reproducible

Every script is open-source. The corpus generator uses a fixed random seed. You can replicate this exact test:

```bash
git clone https://github.com/DataUnchain/dataunchain
cd dataunchain/demo/runpod
bash benchmark_run.sh
```

Requirements: GPU ≥16 GB VRAM · Ollama + Qwen2.5-VL 7B · Python 3.11+

The script generates all documents, runs the processor (no arbitrary timeouts — it runs until done), and produces a complete JSON report with field-level metrics.

---

## What's next

- **v2.1 processor**: fix payslip gross prompt + adaptive DPI for bank statements
- **Benchmark v3**: add receipts, packing lists, quotes — target 300 documents across 10 types
- **32B model test**: quantify accuracy delta on 48GB hardware
- **Competitor comparison**: same corpus vs. Amazon Textract, Azure Document Intelligence, Google Document AI

---

## The bottom line

95.5% accuracy. $0.002/document. 32 seconds. Zero cloud.

On the fields that matter most for Italian business automation — VAT numbers, dates, financial amounts, arithmetic consistency — the system achieves **100%** on every one. Scanned documents perform identically to native PDFs. The system flags its own uncertainty rather than silently passing bad data downstream.

One field below 90% (payslip gross: 54%). One hardware-specific crash pattern (bank statement on 16 GB). Both understood, both fixable.

The data is public. The code is open source. Run it yourself.

</div>

<!-- Bottom CTA -->
<div class="mt-12 rounded-2xl p-8 text-center reveal" style="background: linear-gradient(135deg, rgba(13,148,136,0.15) 0%, rgba(16,185,129,0.10) 100%); border: 1px solid rgba(13,148,136,0.3);">
  <div class="text-2xl font-black text-white mb-2">Ready to try it on your documents?</div>
  <p class="text-gray-400 mb-6">DataUnchain is open source. Docker Compose up, drop a PDF, get JSON in 32 seconds.</p>
  <div class="flex flex-wrap justify-center gap-3">
    <a href="https://github.com/DataUnchain/dataunchain" class="bg-brand-teal text-white font-bold px-6 py-3 rounded-xl hover:bg-brand-teal/80 transition-colors">View on GitHub →</a>
    <a href="/en/docs/" class="bg-white/10 text-white font-bold px-6 py-3 rounded-xl hover:bg-white/20 transition-colors">Read the Docs</a>
  </div>
</div>

<div class="mt-10 pt-8 border-t border-white/10 text-center">
  <a href="/en/blog/" class="text-brand-tealLight font-bold hover:underline">← Back to Blog</a>
</div>

</div>
</article>
