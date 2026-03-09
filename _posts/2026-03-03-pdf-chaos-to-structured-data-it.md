---
layout: default
title: "Dal Caos dei PDF a Dati Strutturati in Secondi"
lang: it
categories: blog
date: 2026-03-03
description: "Una guida pratica: come DataUnchain trasforma un cumulo di fatture disordinate in un foglio Excel pulito senza nessun inserimento manuale."
---

<article class="pt-36 pb-20 px-6">
    <div class="max-w-3xl mx-auto">
        <div class="mb-8">
            <span class="text-brand-tealLight text-xs font-bold uppercase tracking-widest">Blog · 3 Marzo 2026</span>
            <h1 class="text-4xl lg:text-5xl font-black font-display mt-4 mb-6">Dal Caos dei PDF a Dati Strutturati in Secondi</h1>
            <p class="text-gray-400 text-lg leading-relaxed">Hai 200 fatture fornitori sulla scrivania. Ognuna con un formato diverso. Normalmente significa un giorno intero di data entry. Con DataUnchain, servono 3 minuti.</p>
        </div>

        <div class="prose prose-invert prose-lg max-w-none text-gray-300 leading-relaxed space-y-6">
            <h2 class="text-2xl font-black font-display text-white">Passo 1: Scansiona e rilascia</h2>
            <p>Il tuo scanner invia i PDF a una cartella di rete. Il servizio Watchdog di DataUnchain rileva ogni nuovo file istantaneamente. I PDF multipagina vengono automaticamente divisi in immagini singole.</p>

            <h2 class="text-2xl font-black font-display text-white">Passo 2: L'AI legge ogni pagina</h2>
            <p>Qwen 3.5 VL analizza ogni immagine. A differenza dell'OCR, <em>comprende</em> il documento — sa dove si trova il numero fattura, dove sono i totali, e riesce a leggere note scritte a mano accanto alle righe prodotto.</p>
            <p>Hai configurato il prompt di estrazione una volta sola:</p>
            <div class="code-block rounded-xl text-xs my-4">
                <span class="str">"Estrai: numero_fattura, data, fornitore,</span><br>
                <span class="str"> p_iva, imponibile, iva, totale,</span><br>
                <span class="str"> righe_prodotto. Rispondi in JSON."</span>
            </div>

            <h2 class="text-2xl font-black font-display text-white">Passo 3: Validazione matematica</h2>
            <p>Per ogni fattura, Python verifica: <code class="text-brand-tealLight">imponibile + iva == totale</code>. Se non corrisponde entro una tolleranza di 2 centesimi, il record viene segnalato come <code class="text-yellow-400">DA_VERIFICARE</code> invece di <code class="text-green-400">VALIDATO</code>.</p>
            <p>Su 200 fatture, tipicamente 3–5 vengono segnalate — o perché l'AI ha letto male una cifra, o perché la fattura originale ha effettivamente un errore.</p>

            <h2 class="text-2xl font-black font-display text-white">Passo 4: Export pulito</h2>
            <p>Tutte le 200 fatture sono ora in PostgreSQL. Esporta in Excel con un click. Carica nel gestionale. Fatto.</p>
            <p><strong class="text-white">Tempo totale: 3 minuti invece di 8 ore.</strong></p>
        </div>

        <div class="mt-12 pt-8 border-t border-white/10 text-center">
            <a href="/it/use-cases/" class="text-brand-tealLight font-bold hover:underline">Vedi altri casi d'uso →</a>
        </div>
    </div>
</article>
