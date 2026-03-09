---
layout: default
title: "From PDF Chaos to Structured Data in Seconds"
lang: en
categories: blog
date: 2026-03-03
description: "A practical walkthrough: how DataUnchain transforms a stack of messy invoices into a clean Excel spreadsheet with zero manual data entry."
---

<article class="pt-36 pb-20 px-6">
    <div class="max-w-3xl mx-auto">
        <div class="mb-8">
            <span class="text-brand-tealLight text-xs font-bold uppercase tracking-widest">Blog · March 3, 2026</span>
            <h1 class="text-4xl lg:text-5xl font-black font-display mt-4 mb-6">From PDF Chaos to Structured Data in Seconds</h1>
            <p class="text-gray-400 text-lg leading-relaxed">You have 200 supplier invoices on your desk. Each one has a different format. Normally, this means a full day of manual data entry. With DataUnchain, it takes 3 minutes.</p>
        </div>

        <div class="prose prose-invert prose-lg max-w-none text-gray-300 leading-relaxed space-y-6">
            <h2 class="text-2xl font-black font-display text-white">Step 1: Scan and drop</h2>
            <p>Your scanner outputs PDFs to a network folder. DataUnchain's Watchdog service detects each new file instantly. Multi-page PDFs are automatically split into individual page images.</p>

            <h2 class="text-2xl font-black font-display text-white">Step 2: AI reads each page</h2>
            <p>Qwen 3.5 VL analyses each page image. Unlike OCR, it <em>understands</em> the document — it knows where the invoice number is, where the totals are, and can read handwritten notes next to the line items.</p>
            <p>You've configured the extraction prompt once:</p>
            <div class="code-block rounded-xl text-xs my-4">
                <span class="str">"Extract: invoice_number, date, supplier,</span><br>
                <span class="str"> vat_id, subtotal, vat, total, line_items.</span><br>
                <span class="str"> Reply in JSON."</span>
            </div>

            <h2 class="text-2xl font-black font-display text-white">Step 3: Math validation</h2>
            <p>For each invoice, Python checks: <code class="text-brand-tealLight">subtotal + vat == total</code>. If it doesn't match within a 2-cent tolerance, the record is flagged <code class="text-yellow-400">NEEDS_REVIEW</code> instead of <code class="text-green-400">VALIDATED</code>.</p>
            <p>Out of 200 invoices, typically 3–5 get flagged — either because the AI misread a digit, or because the original invoice actually has an error.</p>

            <h2 class="text-2xl font-black font-display text-white">Step 4: Clean export</h2>
            <p>All 200 invoices are now in PostgreSQL. Export to Excel with one click. Upload to your accounting software. Done.</p>
            <p><strong class="text-white">Total time: 3 minutes instead of 8 hours.</strong></p>
        </div>

        <div class="mt-12 pt-8 border-t border-white/10 text-center">
            <a href="/en/use-cases/" class="text-brand-tealLight font-bold hover:underline">See more use cases →</a>
        </div>
    </div>
</article>
