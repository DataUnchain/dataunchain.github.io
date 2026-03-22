---
layout: default
title: "Il Parsing di Documenti con AI Spiegato: Da PDF a Dati Strutturati"
lang: it
categories: blog
date: 2026-03-15
description: "Cos'è il document parsing con AI, come funziona, differenze con OCR tradizionale, sfide con documenti italiani (FatturaPA, DDT, scansioni) e benchmark di accuratezza."
author: Antonio Trento
---

<article class="pt-36 pb-20 px-6">
  <div class="max-w-3xl mx-auto">
    <div class="mb-8">
      <span class="text-brand-tealLight text-xs font-bold uppercase tracking-widest">Blog · 15 Marzo 2026</span>
      <h1 class="text-4xl lg:text-5xl font-black font-display mt-4 mb-6">Il Parsing di Documenti con AI Spiegato: Da PDF a Dati Strutturati</h1>
      <p class="text-gray-400 text-lg leading-relaxed">Ogni azienda riceve documenti in formati diversi: PDF nativi, scansioni, foto, XML. Il document parsing è il processo che trasforma questi documenti in dati strutturati utilizzabili dai sistemi informatici. Ecco come funziona con l'AI moderna.</p>
    </div>

    <div class="prose prose-invert prose-lg max-w-none text-gray-300 leading-relaxed space-y-6">

      <h2 class="text-2xl font-black font-display text-white">Cos'è il document parsing?</h2>
      <p>Il document parsing è il processo di estrazione di informazioni strutturate da documenti non strutturati o semi-strutturati. Un documento PDF di una fattura contiene le stesse informazioni di un record nel database — fornitore, importo, data — ma in un formato pensato per la lettura umana, non per i sistemi informatici.</p>
      <p>Il parser ha il compito di fare da ponte: riceve il documento in forma grezza e restituisce un oggetto dati strutturato (JSON, XML, CSV) che il sistema informatico può elaborare automaticamente.</p>

      <div class="bg-brand-teal/10 border border-brand-teal/30 rounded-xl p-6 my-6">
        <p class="text-brand-tealLight font-bold text-sm uppercase tracking-wider mb-2">Input vs Output</p>
        <div class="grid grid-cols-2 gap-4 text-sm">
          <div>
            <p class="text-white font-bold mb-1">Input (documento grezzo)</p>
            <p class="text-gray-400">Fattura PDF con testo, loghi, tabelle, timbri, firma digitale, 3 pagine</p>
          </div>
          <div>
            <p class="text-white font-bold mb-1">Output (dati strutturati)</p>
            <pre class="text-gray-400 text-xs"><code>{"fornitore": "Rossi S.r.l.",
 "piva": "IT01234567890",
 "numero": "FT-2026-0042",
 "data": "2026-03-10",
 "totale": 1830.00,
 "iva": 330.00}</code></pre>
          </div>
        </div>
      </div>

      <h2 class="text-2xl font-black font-display text-white">Approcci tradizionali al document parsing</h2>
      <p>Prima dell'AI moderna, il document parsing veniva fatto con approcci che funzionavano bene in condizioni controllate ma erano fragili nella realtà:</p>

      <div class="space-y-4">
        <div class="border border-white/10 rounded-lg p-4">
          <h3 class="text-white font-bold mb-1">Regex e regole di posizione</h3>
          <p class="text-gray-400 text-sm">Il parser cerca pattern come "Totale: [0-9]+,[0-9]{2}" nel testo estratto dall'OCR. Funziona solo se il layout è fisso. Non appena cambia un carattere nel template, la regex non matcha più.</p>
        </div>
        <div class="border border-white/10 rounded-lg p-4">
          <h3 class="text-white font-bold mb-1">Template matching</h3>
          <p class="text-gray-400 text-sm">Per ogni fornitore si definisce un template con le coordinate esatte dei campi. Estrae il testo in quelle coordinate. Richiede un template per ogni layout diverso. Con 100 fornitori → 100 template da mantenere.</p>
        </div>
        <div class="border border-white/10 rounded-lg p-4">
          <h3 class="text-white font-bold mb-1">Form recognizer ML</h3>
          <p class="text-gray-400 text-sm">Modelli ML addestrati su dataset di documenti specifici (es. solo fatture italiane). Migliore generalizzazione rispetto a regex, ma richiede training su molti esempi annotati. Difficile da adattare a nuovi tipi documento.</p>
        </div>
      </div>

      <h2 class="text-2xl font-black font-display text-white">Il parsing con Vision Language Model</h2>
      <p>I VLM moderni hanno rivoluzionato il document parsing eliminando il bisogno di template o training specifico per ogni tipo di documento.</p>

      <p>Il processo:</p>
      <ol class="space-y-2 text-gray-400 list-decimal list-inside">
        <li>Il documento viene convertito in immagine (o già è un'immagine)</li>
        <li>L'immagine viene codificata come sequenza di token visivi</li>
        <li>Il modello riceve: immagine + prompt che descrive cosa estrarre</li>
        <li>Il modello produce un JSON con i campi richiesti</li>
        <li>Il sistema valida il JSON e lo schema</li>
      </ol>

      <p>Il prompt esempio per una fattura:</p>
      <pre class="bg-gray-900 border border-white/10 rounded-xl p-4 text-xs text-gray-300 overflow-x-auto"><code>Sei un assistente specializzato nell'estrazione di dati da fatture italiane.
Analizza l'immagine e estrai i seguenti campi in formato JSON:
- fornitore: ragione sociale del fornitore
- piva_fornitore: partita IVA del fornitore (11 cifre)
- numero_fattura: numero del documento
- data_fattura: data di emissione (formato YYYY-MM-DD)
- imponibile: importo imponibile totale (numero decimale)
- iva: importo IVA totale (numero decimale)
- totale: importo totale della fattura (numero decimale)
- scadenza: data di scadenza del pagamento (formato YYYY-MM-DD)

Rispondi SOLO con il JSON, senza testo aggiuntivo.</code></pre>

      <h2 class="text-2xl font-black font-display text-white">Campi estraibili per tipo documento italiano</h2>

      <div class="overflow-x-auto">
        <table class="w-full text-sm border-collapse">
          <thead>
            <tr class="border-b border-white/20">
              <th class="text-left py-3 px-4 text-white font-bold">Documento</th>
              <th class="text-left py-3 px-4 text-white font-bold">Campi principali estraibili</th>
            </tr>
          </thead>
          <tbody class="text-gray-400">
            <tr class="border-b border-white/10"><td class="py-3 px-4 font-bold text-white">Fattura di acquisto</td><td class="py-3 px-4">Fornitore, P.IVA, numero, data, scadenza, imponibile, IVA (22%/10%/4%), totale, IBAN, righe dettaglio</td></tr>
            <tr class="border-b border-white/10"><td class="py-3 px-4 font-bold text-white">DDT</td><td class="py-3 px-4">Mittente, destinatario, numero DDT, data, vettore, righe articoli (codice, descrizione, q.tà, UM, peso), causale</td></tr>
            <tr class="border-b border-white/10"><td class="py-3 px-4 font-bold text-white">Ordine d'acquisto</td><td class="py-3 px-4">Acquirente, fornitore, numero ordine, data, condizioni, righe (articolo, q.tà, prezzo, IVA), totale</td></tr>
            <tr class="border-b border-white/10"><td class="py-3 px-4 font-bold text-white">Nota di credito</td><td class="py-3 px-4">Come fattura + riferimento fattura originale, causale della rettifica</td></tr>
            <tr class="border-b border-white/10"><td class="py-3 px-4 font-bold text-white">Contratto</td><td class="py-3 px-4">Parti (nome, CF/P.IVA), oggetto, valore, durata, data inizio/fine, rinnovo, penali, recesso</td></tr>
            <tr class="border-b border-white/10"><td class="py-3 px-4 font-bold text-white">Nota spese</td><td class="py-3 px-4">Dipendente, data, categoria (trasferta/vitto/alloggio/altro), importo, IVA, fornitore, riferimento progetto</td></tr>
          </tbody>
        </table>
      </div>

      <h2 class="text-2xl font-black font-display text-white">Le sfide specifiche dei documenti italiani</h2>

      <div class="space-y-4">
        <div class="bg-yellow-900/20 border border-yellow-500/30 rounded-lg p-4">
          <h3 class="text-yellow-400 font-bold mb-1">Layout altamente variabile</h3>
          <p class="text-gray-400 text-sm">Ogni software gestionale produce fatture con layout completamente diverso. Non esiste uno standard grafico. Zucchetti, TeamSystem, Fatture in Cloud, Excel, Word — ognuno produce un layout unico. Il VLM deve capire la struttura semantica indipendentemente dal layout.</p>
        </div>
        <div class="bg-yellow-900/20 border border-yellow-500/30 rounded-lg p-4">
          <h3 class="text-yellow-400 font-bold mb-1">Aliquote IVA multiple</h3>
          <p class="text-gray-400 text-sm">Una singola fattura può avere righe con aliquote IVA diverse (22%, 10%, 4%, 0% esente). Il parser deve estrarre l'imponibile e l'IVA per ogni aliquota, non solo il totale generale.</p>
        </div>
        <div class="bg-yellow-900/20 border border-yellow-500/30 rounded-lg p-4">
          <h3 class="text-yellow-400 font-bold mb-1">Formati di importo ambigui</h3>
          <p class="text-gray-400 text-sm">In Italia il separatore decimale è la virgola (es. "1.234,56"). Alcuni sistemi usano il punto (es. "1,234.56"). Il parser deve gestire entrambi i formati. Errori comuni: "1.234" interpretato come 1234 invece di 1.234.</p>
        </div>
        <div class="bg-yellow-900/20 border border-yellow-500/30 rounded-lg p-4">
          <h3 class="text-yellow-400 font-bold mb-1">Scansioni di documenti cartacei</h3>
          <p class="text-gray-400 text-sm">Molte PMI ancora ricevono fatture cartacee da alcuni fornitori. Le scansioni hanno qualità variabile, possono essere storte, con rumore di fondo, timbri sopra al testo. Il preprocessing è fondamentale.</p>
        </div>
      </div>

      <h2 class="text-2xl font-black font-display text-white">Benchmark accuratezza per tipo documento</h2>

      <div class="overflow-x-auto">
        <table class="w-full text-sm border-collapse">
          <thead>
            <tr class="border-b border-white/20">
              <th class="text-left py-3 px-4 text-white font-bold">Tipo documento</th>
              <th class="text-left py-3 px-4 text-white font-bold">Qualità</th>
              <th class="text-left py-3 px-4 text-white font-bold">DataUnchain VLM 7B</th>
              <th class="text-left py-3 px-4 text-white font-bold">DataUnchain VLM 72B</th>
            </tr>
          </thead>
          <tbody class="text-gray-400">
            <tr class="border-b border-white/10"><td class="py-3 px-4">Fattura PDF nativa</td><td class="py-3 px-4">Alta</td><td class="py-3 px-4 text-green-400">96%</td><td class="py-3 px-4 text-green-400">98%</td></tr>
            <tr class="border-b border-white/10"><td class="py-3 px-4">Fattura scansionata</td><td class="py-3 px-4">Alta</td><td class="py-3 px-4 text-green-400">93%</td><td class="py-3 px-4 text-green-400">96%</td></tr>
            <tr class="border-b border-white/10"><td class="py-3 px-4">Fattura scansionata</td><td class="py-3 px-4">Bassa</td><td class="py-3 px-4 text-yellow-400">82%</td><td class="py-3 px-4 text-yellow-400">87%</td></tr>
            <tr class="border-b border-white/10"><td class="py-3 px-4">DDT con tabelle</td><td class="py-3 px-4">Alta</td><td class="py-3 px-4 text-green-400">91%</td><td class="py-3 px-4 text-green-400">94%</td></tr>
            <tr class="border-b border-white/10"><td class="py-3 px-4">Contratto multi-pagina</td><td class="py-3 px-4">Alta</td><td class="py-3 px-4 text-yellow-400">88%</td><td class="py-3 px-4 text-green-400">92%</td></tr>
            <tr class="border-b border-white/10"><td class="py-3 px-4">Nota spese con scontrini</td><td class="py-3 px-4">Mista</td><td class="py-3 px-4 text-yellow-400">79%</td><td class="py-3 px-4 text-yellow-400">85%</td></tr>
          </tbody>
        </table>
      </div>

      <p class="text-sm text-gray-500">* Accuratezza misurata come % di campi estratti correttamente (exact match) su dataset di 500 documenti italiani reali. Hardware: RTX 4090, Ollama, temperatura 0.</p>

      <h2 class="text-2xl font-black font-display text-white">JSON Schema enforcement: garantire output strutturato</h2>
      <p>Un problema comune con i VLM è che a volte producono output non valido: JSON malformato, campi mancanti, o valori nel formato sbagliato. Per garantire un output strutturato e affidabile:</p>
      <ul class="space-y-2 text-gray-400">
        <li><strong class="text-white">Schema validation:</strong> Ogni output viene validato contro un JSON Schema. Campi obbligatori mancanti → il documento va in revisione.</li>
        <li><strong class="text-white">Retry con prompt raffinato:</strong> Se il JSON non è valido, il sistema fa una seconda chiamata all'AI con un prompt più specifico sul campo problematico.</li>
        <li><strong class="text-white">Valori null espliciti:</strong> Se un campo non è presente nel documento, l'AI deve restituire <code>null</code> (non una stringa vuota, non omettere il campo).</li>
        <li><strong class="text-white">Type coercion:</strong> Gli importi vengono sempre convertiti in <code>float</code>, le date in formato ISO 8601, i booleani in <code>true/false</code>.</li>
      </ul>

    </div>

    <div class="mt-12 pt-8 border-t border-white/10 text-center">
      <p class="text-gray-400 mb-4">DataUnchain usa il nostro VLM proprietario con schema enforcement automatico per ogni tipo di documento.</p>
      <a href="/it/" class="inline-block bg-brand-teal text-white font-bold px-8 py-3 rounded-xl hover:bg-brand-tealLight transition-colors">Prova DataUnchain →</a>
    </div>
  </div>
</article>
