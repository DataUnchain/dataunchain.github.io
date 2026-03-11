---
layout: default
title: "Abbiamo testato 219 documenti aziendali italiani su un'AI offline. Ecco i numeri."
lang: it
categories: blog
date: 2026-03-11
author: Antonio Trento
description: "Benchmark scientifico di DataUnchain su 219 documenti aziendali italiani — fatture, buste paga, contratti, DDT — con ground truth verificata. 95.5% di accuratezza. $0.002 a documento. Zero cloud."
---

<article class="pt-36 pb-20 px-4 sm:px-6">
<div class="max-w-3xl mx-auto">

<!-- Header -->
<div class="mb-10 reveal">
  <span class="text-brand-tealLight text-xs font-bold uppercase tracking-widest">Benchmark · 11 Marzo 2026</span>
  <h1 class="text-3xl sm:text-5xl font-black font-display mt-4 mb-6 leading-tight">Abbiamo testato 219 documenti aziendali italiani su un'AI offline. Ecco i numeri.</h1>
  <p class="text-gray-400 text-lg leading-relaxed">Fatture, buste paga, contratti, DDT — 219 documenti con ground truth verificata, elaborati da Qwen2.5-VL 7B che gira in locale su una GPU da $0.24/ora. Nessun cloud. Nessun abbonamento. Nessun dato che lascia la macchina.</p>
</div>

<!-- Hero Score -->
<div class="relative rounded-2xl overflow-hidden mb-12 reveal delay-100" style="background: linear-gradient(135deg, #0D9488 0%, #10B981 50%, #F59E0B 100%);">
  <div class="absolute inset-0 opacity-10" style="background-image: url('data:image/svg+xml,<svg width=\"60\" height=\"60\" viewBox=\"0 0 60 60\" xmlns=\"http://www.w3.org/2000/svg\"><g fill=\"none\" fill-rule=\"evenodd\"><g fill=\"%23ffffff\" fill-opacity=\"1\"><path d=\"M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z\"/></g></g></svg>');"></div>
  <div class="relative px-6 py-10 text-center">
    <div class="text-7xl sm:text-8xl font-black text-white mb-2">95.5%</div>
    <div class="text-white/80 text-xl font-bold mb-1">Punteggio di Accuratezza Complessivo</div>
    <div class="text-white/60 text-sm">su 206 documenti elaborati con successo · Qwen2.5-VL 7B · RTX 2000 Ada 16 GB</div>
  </div>
</div>

<!-- Key Stats Grid -->
<div class="grid grid-cols-2 sm:grid-cols-4 gap-3 mb-12 reveal delay-200">
  <div class="bg-brand-surface rounded-xl p-4 text-center border border-white/10">
    <div class="text-2xl font-black text-brand-tealLight">$0.002</div>
    <div class="text-gray-400 text-xs mt-1">a documento</div>
  </div>
  <div class="bg-brand-surface rounded-xl p-4 text-center border border-white/10">
    <div class="text-2xl font-black text-brand-tealLight">32s</div>
    <div class="text-gray-400 text-xs mt-1">tempo medio</div>
  </div>
  <div class="bg-brand-surface rounded-xl p-4 text-center border border-white/10">
    <div class="text-2xl font-black text-green-400">100%</div>
    <div class="text-gray-400 text-xs mt-1">P.IVA estratte</div>
  </div>
  <div class="bg-brand-surface rounded-xl p-4 text-center border border-white/10">
    <div class="text-2xl font-black text-green-400">SCAN=CLEAN</div>
    <div class="text-gray-400 text-xs mt-1">zero degrado</div>
  </div>
</div>

<!-- Body -->
<div class="prose prose-invert prose-lg max-w-none text-gray-300 leading-relaxed">

## La domanda a cui volevamo rispondere

Un modello open-source da 7B parametri, che gira su una GPU da €900, riesce a estrarre dati strutturati da documenti aziendali italiani in modo accurato abbastanza per l'uso in produzione?

Non una demo. Non screenshot selezionati. Un benchmark vero: 219 documenti, risposta corretta nota per ogni campo, confronto automatizzato, risultati pubblicati.

La risposta è sì — con una sola eccezione su un campo e un limite hardware, entrambi completamente documentati qui sotto.

---

## Il corpus: 219 documenti, 7 tipologie

Il 70% del corpus è stato degradato con effetti di scansione simulati — rumore gaussiano, rotazione ±3°, compressione JPEG qualità 60-85, timbri e watermark sovrapposti. Perché è così che si presentano i documenti aziendali reali.

</div>

<!-- Corpus Table -->
<div class="overflow-x-auto my-8 reveal">
  <table class="w-full text-sm">
    <thead>
      <tr class="border-b border-white/20 text-left">
        <th class="pb-3 pr-4 text-white font-bold">Tipo documento</th>
        <th class="pb-3 pr-4 text-right text-white font-bold">Doc</th>
        <th class="pb-3 text-white font-bold">Campi principali</th>
      </tr>
    </thead>
    <tbody class="text-gray-400">
      <tr class="border-b border-white/10"><td class="py-2.5 pr-4 text-white">Fattura</td><td class="text-right pr-4">60</td><td class="py-2.5">P.IVA, imponibile, IVA 22%, totale, righe</td></tr>
      <tr class="border-b border-white/10"><td class="py-2.5 pr-4 text-white">DDT (bolla di trasporto)</td><td class="text-right pr-4">50</td><td class="py-2.5">mittente, destinatario, trasportatore, merci</td></tr>
      <tr class="border-b border-white/10"><td class="py-2.5 pr-4 text-white">Busta Paga</td><td class="text-right pr-4">35</td><td class="py-2.5">CF dipendente, P.IVA azienda, CCNL, lordo, netto</td></tr>
      <tr class="border-b border-white/10"><td class="py-2.5 pr-4 text-white">Nota di Credito</td><td class="text-right pr-4">20</td><td class="py-2.5">fattura di riferimento, importo credito, motivo</td></tr>
      <tr class="border-b border-white/10"><td class="py-2.5 pr-4 text-white">Contratto</td><td class="text-right pr-4">20</td><td class="py-2.5">tipo, parti, entrambe le P.IVA, data stipula</td></tr>
      <tr class="border-b border-white/10"><td class="py-2.5 pr-4 text-white">Ordine di Acquisto</td><td class="text-right pr-4">14</td><td class="py-2.5">numero ordine, data consegna, totale, P.IVA</td></tr>
      <tr class="border-b border-white/10"><td class="py-2.5 pr-4 text-white">Estratto Conto Bancario</td><td class="text-right pr-4">20</td><td class="py-2.5">IBAN, saldo iniziale, movimenti, saldo finale</td></tr>
      <tr class="text-white font-bold"><td class="py-2.5 pr-4">Totale</td><td class="text-right pr-4">219</td><td></td></tr>
    </tbody>
  </table>
</div>

<div class="prose prose-invert prose-lg max-w-none text-gray-300 leading-relaxed">

**La ground truth è verificata matematicamente.** Per ogni fattura: `imponibile + iva = totale` esattamente. Per ogni busta paga: `lordo - trattenute = netto` al centesimo. Questo ci permette di testare non solo l'estrazione dei singoli campi, ma la capacità del sistema di rilevare errori aritmetici interni — critico per l'uso in produzione.

---

## Come funziona la pipeline

Tre step deterministici, nessuna magia:

**1 → Classify** — Il modello vede l'immagine della pagina e produce il tipo di documento. Nessun hint. Decide da solo.

**2 → Extract** — Prompt specifico per tipo → JSON strutturato. Ogni tipo ha il suo prompt ottimizzato.

**3 → Audit** — Python puro, zero AI. Valida l'algoritmo di checksum P.IVA a 11 cifre, il Codice Fiscale (16 char, tabelle ODD/EVEN, omocodia), gli intervalli delle date, e fa il math check a ±€0.10 di tolleranza.

Output: un `confidence` score (HIGH / MEDIUM / LOW) e un `audit_status` (VALIDATED / PENDING_REVIEW / NEEDS_REVIEW).

---

## I risultati

</div>

<!-- Accuracy Table -->
<div class="overflow-x-auto my-8 reveal">
  <div class="text-xs text-gray-500 uppercase tracking-wider mb-3 font-bold">Accuratezza campo per campo — 206 documenti con status OK</div>
  <table class="w-full text-sm">
    <thead>
      <tr class="border-b border-white/20 text-left">
        <th class="pb-3 pr-4 text-white font-bold">Campo</th>
        <th class="pb-3 pr-4 text-right text-white font-bold">Score</th>
        <th class="pb-3 text-white font-bold">Su</th>
      </tr>
    </thead>
    <tbody>
      <tr class="border-b border-white/10">
        <td class="py-2.5 pr-4 text-gray-300">Classificazione tipo documento</td>
        <td class="text-right pr-4"><span class="text-green-400 font-bold">100.0%</span></td>
        <td class="text-gray-500 text-xs">206/206</td>
      </tr>
      <tr class="border-b border-white/10">
        <td class="py-2.5 pr-4 text-gray-300">P.IVA / Codice Fiscale</td>
        <td class="text-right pr-4"><span class="text-green-400 font-bold">100.0%</span></td>
        <td class="text-gray-500 text-xs">206/206</td>
      </tr>
      <tr class="border-b border-white/10">
        <td class="py-2.5 pr-4 text-gray-300">Data emissione (YYYY-MM-DD esatto)</td>
        <td class="text-right pr-4"><span class="text-green-400 font-bold">100.0%</span></td>
        <td class="text-gray-500 text-xs">144/144</td>
      </tr>
      <tr class="border-b border-white/10">
        <td class="py-2.5 pr-4 text-gray-300">Imponibile (±€0.50)</td>
        <td class="text-right pr-4"><span class="text-green-400 font-bold">100.0%</span></td>
        <td class="text-gray-500 text-xs">94/94</td>
      </tr>
      <tr class="border-b border-white/10">
        <td class="py-2.5 pr-4 text-gray-300">IVA (±€0.50)</td>
        <td class="text-right pr-4"><span class="text-green-400 font-bold">100.0%</span></td>
        <td class="text-gray-500 text-xs">94/94</td>
      </tr>
      <tr class="border-b border-white/10">
        <td class="py-2.5 pr-4 text-gray-300">Totale fattura (±€0.50)</td>
        <td class="text-right pr-4"><span class="text-green-400 font-bold">100.0%</span></td>
        <td class="text-gray-500 text-xs">94/94</td>
      </tr>
      <tr class="border-b border-white/10">
        <td class="py-2.5 pr-4 text-gray-300">Netto busta paga (±€0.50)</td>
        <td class="text-right pr-4"><span class="text-green-400 font-bold">100.0%</span></td>
        <td class="text-gray-500 text-xs">35/35</td>
      </tr>
      <tr class="border-b border-white/10">
        <td class="py-2.5 pr-4 text-gray-300">Saldo finale estratto conto (±€0.50)</td>
        <td class="text-right pr-4"><span class="text-green-400 font-bold">100.0%</span></td>
        <td class="text-gray-500 text-xs">7/7</td>
      </tr>
      <tr class="border-b border-white/10">
        <td class="py-2.5 pr-4 text-gray-300">Numero documento di riferimento</td>
        <td class="text-right pr-4"><span class="text-green-400 font-bold">96.6%</span></td>
        <td class="text-gray-500 text-xs">199/206</td>
      </tr>
      <tr class="border-b border-white/10">
        <td class="py-2.5 pr-4 text-gray-300">Math check interno (±€0.10)</td>
        <td class="text-right pr-4"><span class="text-green-400 font-bold">100.0%</span></td>
        <td class="text-gray-500 text-xs">120/120</td>
      </tr>
      <tr>
        <td class="py-2.5 pr-4 text-gray-300">Lordo busta paga (±€0.50)</td>
        <td class="text-right pr-4"><span class="text-yellow-400 font-bold">54.3%</span></td>
        <td class="text-gray-500 text-xs">19/35 — varianza etichette CCNL</td>
      </tr>
    </tbody>
  </table>
</div>

<!-- SCAN=CLEAN Callout -->
<div class="rounded-2xl border border-brand-teal/30 bg-brand-teal/5 p-6 my-8 reveal">
  <div class="flex items-start gap-4">
    <div class="text-3xl mt-1">🔬</div>
    <div>
      <div class="text-white font-bold text-lg mb-2">SCAN = CLEAN. Senza eccezioni.</div>
      <p class="text-gray-400 text-sm leading-relaxed mb-4">Su ogni metrica misurata — P.IVA, importi, date, math check — i documenti scannerizzati (146 doc con rumore, rotazione, timbri, artefatti JPEG) hanno performance identiche ai PDF nativi digitali (60 doc). Zero degrado. Il modello è stato addestrato su immagini di documenti reali del mondo reale.</p>
      <div class="grid grid-cols-2 sm:grid-cols-5 gap-3">
        <div class="text-center"><div class="text-green-400 font-bold">100%</div><div class="text-gray-500 text-xs">Tipo SCAN</div></div>
        <div class="text-center"><div class="text-green-400 font-bold">100%</div><div class="text-gray-500 text-xs">Tipo CLEAN</div></div>
        <div class="text-center"><div class="text-green-400 font-bold">100%</div><div class="text-gray-500 text-xs">P.IVA SCAN</div></div>
        <div class="text-center"><div class="text-green-400 font-bold">100%</div><div class="text-gray-500 text-xs">P.IVA CLEAN</div></div>
        <div class="text-center"><div class="text-green-400 font-bold">100%</div><div class="text-gray-500 text-xs">Math SCAN</div></div>
      </div>
    </div>
  </div>
</div>

<!-- Confidence Distribution -->
<div class="rounded-2xl bg-brand-surface border border-white/10 p-6 my-8 reveal">
  <div class="text-xs text-gray-500 uppercase tracking-wider mb-4 font-bold">Distribuzione confidence — 219 documenti</div>
  <div class="space-y-3">
    <div class="flex items-center gap-3">
      <div class="text-blue-400 text-sm font-bold w-20">HIGH</div>
      <div class="flex-1 bg-white/10 rounded-full h-2 overflow-hidden">
        <div class="bg-blue-400 h-full rounded-full" style="width: 92.2%"></div>
      </div>
      <div class="text-white font-bold text-sm w-12 text-right">92.2%</div>
      <div class="text-gray-500 text-xs w-16">202 doc</div>
    </div>
    <div class="flex items-center gap-3">
      <div class="text-yellow-400 text-sm font-bold w-20">MEDIUM</div>
      <div class="flex-1 bg-white/10 rounded-full h-2 overflow-hidden">
        <div class="bg-yellow-400 h-full rounded-full" style="width: 1.8%"></div>
      </div>
      <div class="text-white font-bold text-sm w-12 text-right">1.8%</div>
      <div class="text-gray-500 text-xs w-16">4 doc</div>
    </div>
    <div class="flex items-center gap-3">
      <div class="text-red-400 text-sm font-bold w-20">LOW</div>
      <div class="flex-1 bg-white/10 rounded-full h-2 overflow-hidden">
        <div class="bg-red-400 h-full rounded-full" style="width: 5.9%"></div>
      </div>
      <div class="text-white font-bold text-sm w-12 text-right">5.9%</div>
      <div class="text-gray-500 text-xs w-16">13 doc</div>
    </div>
  </div>
  <p class="text-gray-500 text-xs mt-4">I 13 documenti LOW vengono instradati automaticamente alla revisione umana — non inseriti silenziosamente nel flusso dati. Il sistema sa quando non è sicuro.</p>
</div>

<div class="prose prose-invert prose-lg max-w-none text-gray-300 leading-relaxed">

---

## Cosa succede dentro la GPU

</div>

<!-- Resource Stats -->
<div class="grid grid-cols-2 sm:grid-cols-3 gap-3 my-8 reveal">
  <div class="bg-brand-surface rounded-xl p-4 border border-white/10">
    <div class="text-brand-tealLight text-xs font-bold uppercase tracking-wider mb-2">GPU Utilization</div>
    <div class="text-2xl font-black text-white">87–100%</div>
    <div class="text-gray-500 text-xs mt-1">media ~94% durante inferenza</div>
  </div>
  <div class="bg-brand-surface rounded-xl p-4 border border-white/10">
    <div class="text-brand-tealLight text-xs font-bold uppercase tracking-wider mb-2">VRAM Usata</div>
    <div class="text-2xl font-black text-white">13.3 GB</div>
    <div class="text-gray-500 text-xs mt-1">su 16 GB — 2.6 GB margine</div>
  </div>
  <div class="bg-brand-surface rounded-xl p-4 border border-white/10">
    <div class="text-brand-tealLight text-xs font-bold uppercase tracking-wider mb-2">Power Draw</div>
    <div class="text-2xl font-black text-white">~68 W</div>
    <div class="text-gray-500 text-xs mt-1">vicino al TDP — 6W in idle</div>
  </div>
  <div class="bg-brand-surface rounded-xl p-4 border border-white/10">
    <div class="text-brand-tealLight text-xs font-bold uppercase tracking-wider mb-2">CPU Load</div>
    <div class="text-2xl font-black text-white">~4%</div>
    <div class="text-gray-500 text-xs mt-1">pipeline 100% GPU-bound</div>
  </div>
  <div class="bg-brand-surface rounded-xl p-4 border border-white/10">
    <div class="text-brand-tealLight text-xs font-bold uppercase tracking-wider mb-2">Temperatura GPU</div>
    <div class="text-2xl font-black text-white">65–70°C</div>
    <div class="text-gray-500 text-xs mt-1">26°C in idle</div>
  </div>
  <div class="bg-brand-surface rounded-xl p-4 border border-white/10">
    <div class="text-brand-tealLight text-xs font-bold uppercase tracking-wider mb-2">RAM Usata</div>
    <div class="text-2xl font-black text-white">~35 GB</div>
    <div class="text-gray-500 text-xs mt-1">OS + Ollama + buffer</div>
  </div>
</div>

<div class="prose prose-invert prose-lg max-w-none text-gray-300 leading-relaxed">

**La pipeline è 100% GPU-bound.** CPU al 4% significa che il processore sta solo aspettando la GPU. Aggiungere CPU più veloci o più core non cambia nulla. Solo la GPU conta. Questo semplifica molto la pianificazione hardware.

---

## Limiti identificati — trasparenza totale

</div>

<!-- Limit 1 -->
<div class="rounded-2xl border border-yellow-500/30 bg-yellow-500/5 p-6 my-6 reveal">
  <div class="flex items-start gap-3">
    <div class="text-2xl">⚠️</div>
    <div>
      <div class="text-yellow-400 font-bold mb-2">Limite 1 — Crash GGML sugli estratti conto (13/20 doc)</div>
      <p class="text-gray-400 text-sm leading-relaxed mb-3">Gli estratti conto con tabelle di movimenti dense (15+ righe) producono un crash interno nel backend GGML di Ollama: <code class="text-yellow-300 bg-black/30 px-1 rounded">GGML_ASSERT(a->ne[2] * 4 == b->ne[0]) failed</code></p>
      <p class="text-gray-400 text-sm leading-relaxed mb-3">La classificazione funziona sempre. Il crash avviene nello step di estrazione, quando l'immagine densa + prompt lungo supera un limite di dimensione dei tensori nel modello 7B su 16 GB VRAM. I 7 estratti conto elaborati correttamente (meno righe di movimenti) ottengono 100% su tutti i campi incluso il saldo finale.</p>
      <div class="flex flex-wrap gap-2 mt-3">
        <span class="bg-black/30 text-brand-tealLight text-xs px-3 py-1 rounded-full font-bold">Fix: ridurre DPI per tabelle dense (200→150)</span>
        <span class="bg-black/30 text-brand-tealLight text-xs px-3 py-1 rounded-full font-bold">Alt: Qwen2.5-VL 14B/32B su 24GB+</span>
      </div>
    </div>
  </div>
</div>

<!-- Limit 2 -->
<div class="rounded-2xl border border-yellow-500/30 bg-yellow-500/5 p-6 my-6 reveal">
  <div class="flex items-start gap-3">
    <div class="text-2xl">⚠️</div>
    <div>
      <div class="text-yellow-400 font-bold mb-2">Limite 2 — Lordo busta paga: 54.3%</div>
      <p class="text-gray-400 text-sm leading-relaxed mb-3">Il netto viene estratto al 100% (etichetta sempre "NETTO IN BUSTA"). Il lordo al 54.3% perché i format delle buste paga italiane variano molto per CCNL — lo stesso campo appare come "RETRIBUZIONE LORDA", "IMPONIBILE LORDO", "TOTALE COMPETENZE", "IMPONIBILE CONTRIBUTIVO" a seconda del software gestionale.</p>
      <p class="text-gray-400 text-sm leading-relaxed">Il numero viene sempre letto correttamente quando trovato — è un problema di riconoscimento dell'etichetta, non di lettura del valore.</p>
      <div class="flex flex-wrap gap-2 mt-3">
        <span class="bg-black/30 text-brand-tealLight text-xs px-3 py-1 rounded-full font-bold">Fix: lista esplicita etichette nel prompt</span>
        <span class="bg-black/30 text-brand-tealLight text-xs px-3 py-1 rounded-full font-bold">Target: >90% in v2.1</span>
      </div>
    </div>
  </div>
</div>

<div class="prose prose-invert prose-lg max-w-none text-gray-300 leading-relaxed">

---

## $0.002 a documento — cosa significa davvero

A $0.24/ora con 32 secondi/documento su cloud, la matematica è semplice. Rendiamola concreta:

</div>

<!-- Economic Scenarios -->
<div class="space-y-4 my-8 reveal">
  <div class="rounded-2xl bg-brand-surface border border-white/10 p-5">
    <div class="flex items-center justify-between mb-3">
      <div class="text-white font-bold">Piccola impresa — 100 fatture/mese</div>
      <div class="text-brand-tealLight font-black text-lg">$0.20/mese</div>
    </div>
    <div class="text-gray-400 text-sm">vs. 2-4 ore di inserimento manuale a €18-22/ora = €36–88/mese. ROI: <span class="text-green-400 font-bold">440× più economico</span></div>
  </div>
  <div class="rounded-2xl bg-brand-surface border border-white/10 p-5">
    <div class="flex items-center justify-between mb-3">
      <div class="text-white font-bold">Media impresa — 2.000 doc/mese</div>
      <div class="text-brand-tealLight font-black text-lg">$4/mese</div>
    </div>
    <div class="text-gray-400 text-sm">Sostituisce 1-2 FTE ore/giorno di data entry. Competitor SaaS: €200-2.000/mese. <span class="text-green-400 font-bold">ROI immediato.</span></div>
  </div>
  <div class="rounded-2xl bg-brand-surface border border-white/10 p-5">
    <div class="flex items-center justify-between mb-3">
      <div class="text-white font-bold">On-premise con RTX 3090</div>
      <div class="text-brand-tealLight font-black text-lg">&lt;$0.001/doc</div>
    </div>
    <div class="text-gray-400 text-sm">RTX 3090 24GB ~€900 usata. Ammortizzata in 3 anni a 4 ore/giorno: hardware + energia scende sotto $0.001/documento. <span class="text-green-400 font-bold">Payback in settimane a volumi medi.</span></div>
  </div>
</div>

<div class="prose prose-invert prose-lg max-w-none text-gray-300 leading-relaxed">

---

## Cosa significa "completamente offline" per la tua azienda

Non è una feature — è una scelta architetturale con conseguenze reali.

**Nessun dato lascia la tua infrastruttura.** PDF convertiti in locale. Modello che gira in locale. JSON scritto in locale. Non un singolo byte dei tuoi documenti arriva ad Anthropic, OpenAI, Microsoft, Google, o chiunque altro.

**GDPR semplificato.** Nessun trasferimento internazionale di dati. Nessun accordo di trattamento dati con provider AI terzi. Nessun obbligo di notifica violazione a processori esterni. I tuoi documenti restano nel tuo edificio.

**Air-gap ready.** Una volta scaricato il modello (5 GB, operazione one-time), il sistema gira senza connessione internet. Reti di fabbrica isolate, archivi legali sicuri, reti governative — tutto supportato.

**Zero abbonamenti mensili.** Nessun costo per token. Nessun livello di utilizzo. L'infrastruttura è l'unico costo ricorrente.

---

## Guida hardware: cosa ti serve davvero

</div>

<!-- Hardware Cards -->
<div class="space-y-3 my-8 reveal">
  <div class="rounded-xl border border-white/10 bg-brand-surface p-4">
    <div class="flex flex-wrap items-center justify-between gap-2 mb-2">
      <div class="text-white font-bold">RTX 2000 Ada / RTX 3080 — 16 GB</div>
      <span class="bg-yellow-500/20 text-yellow-400 text-xs font-bold px-3 py-1 rounded-full">Minimo funzionante</span>
    </div>
    <p class="text-gray-400 text-sm">Funziona. Ma il margine VRAM è di 2.6 GB — stretto. Gli estratti conto a tabelle dense crashano. Usa se non elabori estratti conto regolarmente, oppure riduci il DPI come workaround.</p>
  </div>
  <div class="rounded-xl border border-brand-teal/40 bg-brand-teal/5 p-4">
    <div class="flex flex-wrap items-center justify-between gap-2 mb-2">
      <div class="text-white font-bold">RTX 3090 / RTX 4090 — 24 GB</div>
      <span class="bg-brand-teal/20 text-brand-tealLight text-xs font-bold px-3 py-1 rounded-full">⭐ Consigliato</span>
    </div>
    <p class="text-gray-400 text-sm">Tutti i tipi documentali stabili. Stimato ~20s/doc (2× più veloce). Miglior rapporto qualità/prezzo per uso produzione. RTX 3090 usata ~€900, RTX 4090 nuova ~€1.800.</p>
  </div>
  <div class="rounded-xl border border-white/10 bg-brand-surface p-4">
    <div class="flex flex-wrap items-center justify-between gap-2 mb-2">
      <div class="text-white font-bold">A5000 / A6000 — 24–48 GB</div>
      <span class="bg-purple-500/20 text-purple-400 text-xs font-bold px-3 py-1 rounded-full">Enterprise</span>
    </div>
    <p class="text-gray-400 text-sm">Memoria ECC, garanzia professionale, form factor server. Supporta Qwen2.5-VL 32B per accuratezza ancora più alta. Per installazioni data center.</p>
  </div>
  <div class="rounded-xl border border-white/10 bg-brand-surface p-4">
    <div class="flex flex-wrap items-center justify-between gap-2 mb-2">
      <div class="text-white font-bold">A100 / H100 — 40–80 GB</div>
      <span class="bg-blue-500/20 text-blue-400 text-xs font-bold px-3 py-1 rounded-full">Alto Volume</span>
    </div>
    <p class="text-gray-400 text-sm">Per 50.000+ documenti/mese. Supporta elaborazione parallela multipla o Qwen2.5-VL 72B. Classe data center enterprise.</p>
  </div>
</div>

<div class="rounded-2xl bg-brand-surface border border-white/10 p-5 my-6 text-sm text-gray-400 reveal">
  <strong class="text-white">Importante:</strong> la CPU è irrilevante per le performance. La GPU era al 94% di utilizzo medio per tutto il benchmark — la CPU al 4%. Una RTX 3090 + Core i5 batte una RTX 2000 Ada + Core i9 ogni volta. Investi in GPU, non in CPU.
</div>

<div class="prose prose-invert prose-lg max-w-none text-gray-300 leading-relaxed">

---

## Riepilogo per tipo documento

</div>

<!-- Per-type table -->
<div class="overflow-x-auto my-8 reveal">
  <table class="w-full text-sm">
    <thead>
      <tr class="border-b border-white/20 text-left">
        <th class="pb-3 pr-3 text-white font-bold">Tipo</th>
        <th class="pb-3 pr-3 text-right text-white font-bold">n</th>
        <th class="pb-3 pr-3 text-right text-white font-bold">Tipo</th>
        <th class="pb-3 pr-3 text-right text-white font-bold">P.IVA</th>
        <th class="pb-3 pr-3 text-right text-white font-bold">Importo</th>
        <th class="pb-3 pr-3 text-right text-white font-bold">Math</th>
        <th class="pb-3 text-right text-white font-bold">Vel.</th>
      </tr>
    </thead>
    <tbody class="text-gray-400">
      <tr class="border-b border-white/10">
        <td class="py-2.5 pr-3 text-white">Fattura</td>
        <td class="text-right pr-3">60</td>
        <td class="text-right pr-3 text-green-400">100%</td>
        <td class="text-right pr-3 text-green-400">100%</td>
        <td class="text-right pr-3 text-green-400">100%</td>
        <td class="text-right pr-3 text-green-400">100%</td>
        <td class="text-right">36s</td>
      </tr>
      <tr class="border-b border-white/10">
        <td class="py-2.5 pr-3 text-white">DDT (bolla)</td>
        <td class="text-right pr-3">50</td>
        <td class="text-right pr-3 text-green-400">100%</td>
        <td class="text-right pr-3 text-green-400">100%</td>
        <td class="text-right pr-3 text-gray-600">n/a</td>
        <td class="text-right pr-3 text-gray-600">n/a</td>
        <td class="text-right">32s</td>
      </tr>
      <tr class="border-b border-white/10">
        <td class="py-2.5 pr-3 text-white">Nota di Credito</td>
        <td class="text-right pr-3">20</td>
        <td class="text-right pr-3 text-green-400">100%</td>
        <td class="text-right pr-3 text-green-400">100%</td>
        <td class="text-right pr-3 text-green-400">100%</td>
        <td class="text-right pr-3 text-green-400">100%</td>
        <td class="text-right">31s</td>
      </tr>
      <tr class="border-b border-white/10">
        <td class="py-2.5 pr-3 text-white">Contratto</td>
        <td class="text-right pr-3">20</td>
        <td class="text-right pr-3 text-green-400">100%</td>
        <td class="text-right pr-3 text-green-400">100%</td>
        <td class="text-right pr-3 text-gray-600">n/a</td>
        <td class="text-right pr-3 text-gray-600">n/a</td>
        <td class="text-right">26s</td>
      </tr>
      <tr class="border-b border-white/10">
        <td class="py-2.5 pr-3 text-white">Ordine Acquisto</td>
        <td class="text-right pr-3">14</td>
        <td class="text-right pr-3 text-green-400">100%</td>
        <td class="text-right pr-3 text-green-400">100%</td>
        <td class="text-right pr-3 text-green-400">100%</td>
        <td class="text-right pr-3 text-green-400">100%</td>
        <td class="text-right">37s</td>
      </tr>
      <tr class="border-b border-white/10">
        <td class="py-2.5 pr-3 text-white">Busta Paga</td>
        <td class="text-right pr-3">35</td>
        <td class="text-right pr-3 text-green-400">100%</td>
        <td class="text-right pr-3 text-green-400">100%</td>
        <td class="text-right pr-3 text-yellow-400">netto 100% / lordo 54%</td>
        <td class="text-right pr-3 text-gray-600">n/a</td>
        <td class="text-right">31s</td>
      </tr>
      <tr>
        <td class="py-2.5 pr-3 text-white">Estratto Conto</td>
        <td class="text-right pr-3">7★</td>
        <td class="text-right pr-3 text-green-400">100%</td>
        <td class="text-right pr-3 text-green-400">100%</td>
        <td class="text-right pr-3 text-green-400">100%</td>
        <td class="text-right pr-3 text-green-400">100%</td>
        <td class="text-right">48s</td>
      </tr>
    </tbody>
  </table>
  <p class="text-gray-600 text-xs mt-2">★ 13/20 estratti conto: crash GGML (limite hardware, vedi sopra). I 7 elaborati correttamente: 100% su tutti i campi.</p>
</div>

<div class="prose prose-invert prose-lg max-w-none text-gray-300 leading-relaxed">

---

## Questo benchmark è completamente riproducibile

Ogni script è open-source. Il generatore usa un seed fisso. Puoi replicare questo test esatto:

```bash
git clone https://github.com/DataUnchain/dataunchain
cd dataunchain/demo/runpod
bash benchmark_run.sh
```

Requisiti: GPU ≥16 GB VRAM · Ollama + Qwen2.5-VL 7B · Python 3.11+

Lo script genera tutti i documenti, avvia il processor (senza timeout arbitrari — gira fino a completamento), ed esegue il confronto con la ground truth producendo il report JSON completo.

---

## Cosa stiamo migliorando

- **Processor v2.1**: fix prompt busta paga lordo + DPI adattivo per estratti conto
- **Benchmark v3**: aggiunte ricevute, packing list, preventivi — target 300 doc su 10 tipi
- **Test modello 32B**: delta accuratezza su hardware da 48GB
- **Confronto competitor**: stesso corpus vs. Amazon Textract, Azure Document Intelligence, Google Document AI

---

## Il punto finale

95.5% di accuratezza. $0.002/documento. 32 secondi. Zero cloud.

Sui campi che contano di più per l'automazione documentale aziendale italiana — P.IVA, date, importi, coerenza aritmetica — il sistema raggiunge il **100%** su ognuno. I documenti scannerizzati performano identicamente ai PDF nativi. Il sistema segnala la propria incertezza invece di passare silenziosamente dati errati a valle.

Un campo sotto il 90% (busta paga lordo: 54%). Un pattern di crash specifico all'hardware (estratto conto su 16 GB). Entrambi compresi. Entrambi risolvibili.

I dati sono pubblici. Il codice è open source. Eseguilo tu stesso.

</div>

<!-- Bottom CTA -->
<div class="mt-12 rounded-2xl p-8 text-center reveal" style="background: linear-gradient(135deg, rgba(13,148,136,0.15) 0%, rgba(16,185,129,0.10) 100%); border: 1px solid rgba(13,148,136,0.3);">
  <div class="text-2xl font-black text-white mb-2">Pronto a testarlo sui tuoi documenti?</div>
  <p class="text-gray-400 mb-6">DataUnchain è open source. Docker Compose up, trascina un PDF, ottieni JSON in 32 secondi.</p>
  <div class="flex flex-wrap justify-center gap-3">
    <a href="https://github.com/DataUnchain/dataunchain" class="bg-brand-teal text-white font-bold px-6 py-3 rounded-xl hover:bg-brand-teal/80 transition-colors">Vedi su GitHub →</a>
    <a href="/it/docs/" class="bg-white/10 text-white font-bold px-6 py-3 rounded-xl hover:bg-white/20 transition-colors">Leggi la Documentazione</a>
  </div>
</div>

<div class="mt-10 pt-8 border-t border-white/10 text-center">
  <a href="/it/blog/" class="text-brand-tealLight font-bold hover:underline">← Torna al Blog</a>
</div>

</div>
</article>
