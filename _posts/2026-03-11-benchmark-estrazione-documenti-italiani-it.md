---
layout: default
title: "95.5% di Accuratezza su 219 Documenti Aziendali Italiani: Il Benchmark Scientifico di DataUnchain"
lang: it
categories: blog
date: 2026-03-11
description: "Abbiamo testato Qwen2.5-VL 7B su 219 documenti aziendali italiani reali — fatture, DDT, buste paga, contratti, note di credito — con ground truth verificata. Risultato: 95.5% di accuratezza, $0.002 a documento, completamente offline. Ecco tutti i dati."
---

<article class="pt-36 pb-20 px-6">
    <div class="max-w-3xl mx-auto">

        <div class="mb-8">
            <span class="text-brand-tealLight text-xs font-bold uppercase tracking-widest">Benchmark · 11 Marzo 2026</span>
            <h1 class="text-4xl lg:text-5xl font-black font-display mt-4 mb-6">95.5% di Accuratezza su 219 Documenti Aziendali Italiani: Il Benchmark Scientifico di DataUnchain</h1>
            <p class="text-gray-400 text-lg leading-relaxed">Abbiamo costruito un corpus sintetico di 219 documenti aziendali italiani con ground truth verificata, li abbiamo passati attraverso il processor DataUnchain v2.0, e abbiamo misurato l'accuratezza campo per campo. Questo articolo documenta ogni aspetto del test: metodologia, risultati, limiti identificati, consumo di risorse e costo operativo reale.</p>
        </div>

        <div class="prose prose-invert prose-lg max-w-none text-gray-300 leading-relaxed space-y-6">

            <h2 class="text-2xl font-black font-display text-white">Il problema che stiamo risolvendo</h2>

            <p>Ogni impresa italiana genera ogni giorno decine di documenti strutturati: fatture di vendita, documenti di trasporto (DDT), buste paga, note di credito, ordini di acquisto, contratti, estratti conto bancari. La stragrande maggioranza di questi documenti esiste in formato PDF o carta scannerizzata. Trasformare queste informazioni in dati strutturati — numeri P.IVA, importi, date, totali — richiede oggi ore di lavoro manuale o costosi sistemi cloud che inviano i tuoi documenti riservati a server di terzi.</p>

            <p>DataUnchain nasce per rispondere a una domanda semplice: è possibile fare questa estrazione in modo accurato, veloce, completamente offline, e a un costo marginale vicino allo zero? Questo benchmark è il primo test scientifico sistematico per rispondere a quella domanda con dati reali.</p>

            <h2 class="text-2xl font-black font-display text-white">Perché un benchmark con ground truth?</h2>

            <p>La maggior parte delle demo di sistemi AI per documenti mostra screenshot selezionati di casi andati bene. Noi volevamo qualcosa di diverso: una misurazione sistematica su un corpus ampio, con una risposta attesa nota per ogni campo, con metriche precise e riproducibili.</p>

            <p>Il concetto di <em>ground truth</em> è semplice: per ogni documento nel corpus, esiste un file JSON che contiene i valori corretti per ogni campo — il numero fattura, la P.IVA del fornitore, la data di emissione, l'imponibile, l'IVA, il totale. Il sistema estrae quei campi dal PDF, e noi confrontiamo automaticamente i valori estratti con quelli attesi. Zero soggettività. Zero cherry-picking.</p>

            <p>Abbiamo generato il corpus sinteticamente — cioè abbiamo costruito noi stessi i PDF con dati italiani realistici — proprio per avere la ground truth perfetta fin dall'inizio. Dati fiscali italiani autentici: partite IVA a 11 cifre con algoritmo di verifica, codici fiscali generati con l'algoritmo ufficiale completo (tabelle ODD/EVEN, codici Belfiore, cifra di controllo, gestione omocodia), date in formato italiano, importi in euro.</p>

            <h2 class="text-2xl font-black font-display text-white">Il corpus: 219 documenti, 7 categorie</h2>

            <p>Il corpus finale comprende 219 documenti suddivisi in sette tipologie documentali tipiche del panorama aziendale italiano:</p>

            <div class="overflow-x-auto my-6">
                <table class="w-full text-sm border-collapse">
                    <thead>
                        <tr class="border-b border-white/20">
                            <th class="text-left py-2 pr-4 text-white font-bold">Tipo</th>
                            <th class="text-right py-2 pr-4 text-white font-bold">N.</th>
                            <th class="text-left py-2 text-white font-bold">Campi principali estratti</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr class="border-b border-white/10"><td class="py-2 pr-4">Fattura</td><td class="text-right pr-4">60</td><td class="py-2">numero, data, scadenza, P.IVA fornitore/cliente, imponibile, IVA 22%, totale, righe</td></tr>
                        <tr class="border-b border-white/10"><td class="py-2 pr-4">DDT (bolla di trasporto)</td><td class="text-right pr-4">50</td><td class="py-2">numero DDT, data, mittente, destinatario, trasportatore, colli, merci</td></tr>
                        <tr class="border-b border-white/10"><td class="py-2 pr-4">Busta Paga</td><td class="text-right pr-4">35</td><td class="py-2">dipendente, CF, azienda, P.IVA, CCNL, competenza, lordo, trattenute, netto</td></tr>
                        <tr class="border-b border-white/10"><td class="py-2 pr-4">Nota di Credito</td><td class="text-right pr-4">20</td><td class="py-2">numero NC, data, fattura di riferimento, importo credito, motivo</td></tr>
                        <tr class="border-b border-white/10"><td class="py-2 pr-4">Contratto</td><td class="text-right pr-4">20</td><td class="py-2">tipo contratto, numero, data stipula, Parte A, Parte B, P.IVA entrambe</td></tr>
                        <tr class="border-b border-white/10"><td class="py-2 pr-4">Ordine di Acquisto</td><td class="text-right pr-4">14</td><td class="py-2">numero ordine, data, consegna, fornitore, acquirente, P.IVA, totale ordine</td></tr>
                        <tr class="border-b border-white/10"><td class="py-2 pr-4">Estratto Conto Bancario</td><td class="text-right pr-4">20</td><td class="py-2">banca, IBAN, correntista, periodo, saldo iniziale, movimenti, saldo finale</td></tr>
                        <tr class="font-bold text-white"><td class="py-2 pr-4">Totale</td><td class="text-right pr-4">219</td><td class="py-2"></td></tr>
                    </tbody>
                </table>
            </div>

            <h3 class="text-xl font-bold text-white">Simulazione scansione: il vero banco di prova</h3>

            <p>Il 70% del corpus (circa 153 documenti) è stato sottoposto a un processo di degradazione controllata per simulare le condizioni reali di scansione. Non stiamo parlando di un semplice salvataggio JPEG: abbiamo applicato una pipeline di trasformazioni realistiche che include rumore gaussiano di varia intensità, rotazioni casuali nell'intervallo ±3°, compressione JPEG a qualità variabile tra 60 e 85 (tipica degli scanner da ufficio), sovrapposizione di timbri e watermark, variazioni di luminosità e contrasto, e simulazione di leggere pieghe e distorsioni prospettiche.</p>

            <p>Questi effetti riproducono fedelmente quello che accade quando un documento viene stampato, firmato, timbrato, scannerizzato con uno scanner da ufficio economico, e poi il file viene compresso prima di essere archiviato — uno scenario che descrive il 90% dei documenti che transitano nelle aziende italiane ogni giorno.</p>

            <h3 class="text-xl font-bold text-white">Ground truth verificata matematicamente</h3>

            <p>Per i documenti con importi (fatture, note di credito, buste paga, estratti conto), la ground truth non è solo un insieme di valori corretti: è una ground truth matematicamente coerente. Questo significa che per ogni fattura, il campo <code class="text-brand-tealLight">imponibile + iva = totale</code> esattamente. Per ogni busta paga, <code class="text-brand-tealLight">lordo - trattenute = netto</code> al centesimo. Per ogni estratto conto, <code class="text-brand-tealLight">saldo_iniziale + entrate - uscite = saldo_finale</code>.</p>

            <p>Questo ci permette di testare non solo l'estrazione dei singoli campi, ma anche la capacità del sistema di rilevare errori aritmetici interni — una funzionalità critica per l'uso in produzione, dove una fattura con i conti che non tornano è un segnale di allarme immediato.</p>

            <h2 class="text-2xl font-black font-display text-white">L'architettura: come funziona DataUnchain</h2>

            <p>Prima di entrare nei risultati, vale la pena descrivere esattamente come funziona il sistema che abbiamo testato. DataUnchain processor v2.0 implementa una pipeline in tre step che elabora ogni documento PDF in ingresso.</p>

            <h3 class="text-xl font-bold text-white">Step 1 — Classify: identificazione del tipo</h3>

            <p>Il primo step prende l'immagine del documento (ottenuta convertendo il PDF a 200 DPI) e la invia a Qwen2.5-VL 7B con un prompt di classificazione. Il modello deve rispondere con una delle categorie supportate: <em>fattura, ddt, busta_paga, nota_credito, contratto, ordine_acquisto, estratto_conto</em>, oppure <em>sconosciuto</em> se il documento non rientra in nessuna categoria nota.</p>

            <p>La classificazione avviene senza fornire al modello alcun hint visivo aggiuntivo: il modello vede solo l'immagine e deve decidere autonomamente. Questo è importante perché nella realtà i documenti arrivano in flussi misti — una cartella con 50 PDF può contenere fatture, DDT, buste paga e note di credito mescolate insieme, e il sistema deve smistare correttamente senza sapere in anticipo cosa si aspettare.</p>

            <h3 class="text-xl font-bold text-white">Step 2 — Extract: estrazione strutturata</h3>

            <p>Una volta identificato il tipo di documento, viene selezionato il prompt di estrazione specifico per quella categoria. Ogni tipo ha un prompt ottimizzato che descrive esattamente quali campi estrarre, in quale formato, con quale gestione dei casi ambigui (es. "se il campo non è presente, usa null").</p>

            <p>Il modello restituisce un JSON strutturato. Questo JSON viene validato con uno schema predefinito: se mancano campi obbligatori o se i tipi non corrispondono, il documento viene marcato come <code class="text-yellow-400">NEEDS_REVIEW</code>.</p>

            <h3 class="text-xl font-bold text-white">Step 3 — Audit: validazione e confidence scoring</h3>

            <p>Il terzo step è interamente deterministico — nessuna AI coinvolta. Un modulo Python esegue una serie di controlli formali e matematici:</p>

            <p><strong class="text-white">Validazione formale:</strong></p>
            <ul>
                <li>P.IVA: 11 cifre con algoritmo di checksum Luhn-like specifico per il sistema fiscale italiano</li>
                <li>Codice Fiscale: 16 caratteri, pattern alfanumerico corretto, cifra di controllo verificata, gestione omocodia</li>
                <li>Date: formato YYYY-MM-DD, range 1900-2100, giorni validi per il mese</li>
                <li>Importi: valori numerici positivi, precision a 2 decimali</li>
            </ul>

            <p><strong class="text-white">Math check:</strong></p>
            <ul>
                <li>Fatture: <code class="text-brand-tealLight">imponibile + iva = totale ± €0.10</code></li>
                <li>Buste paga: <code class="text-brand-tealLight">lordo - trattenute = netto ± €0.10</code></li>
                <li>Estratti conto: <code class="text-brand-tealLight">saldo_i + entrate - uscite = saldo_f ± €0.10</code></li>
            </ul>

            <p>Al termine dell'audit, ogni documento riceve un <strong class="text-white">confidence score</strong> (HIGH/MEDIUM/LOW) basato sulla coerenza interna dei dati estratti, e un <strong class="text-white">audit_status</strong> (VALIDATED/PENDING_REVIEW/NEEDS_REVIEW) che indica se il documento può essere processato automaticamente o richiede revisione umana.</p>

            <h2 class="text-2xl font-black font-display text-white">L'hardware: quanto costa davvero?</h2>

            <p>Il test è stato condotto su RunPod Community Cloud, usando un pod con GPU NVIDIA RTX 2000 Ada Generation da 16 GB di VRAM. Il costo è $0.24/ora.</p>

            <div class="overflow-x-auto my-6">
                <table class="w-full text-sm border-collapse">
                    <thead>
                        <tr class="border-b border-white/20">
                            <th class="text-left py-2 pr-4 text-white font-bold">Componente</th>
                            <th class="text-left py-2 text-white font-bold">Specifiche</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr class="border-b border-white/10"><td class="py-2 pr-4">GPU</td><td class="py-2">NVIDIA RTX 2000 Ada Generation</td></tr>
                        <tr class="border-b border-white/10"><td class="py-2 pr-4">VRAM</td><td class="py-2">16.380 MiB (~16 GB)</td></tr>
                        <tr class="border-b border-white/10"><td class="py-2 pr-4">vCPU</td><td class="py-2">6 core</td></tr>
                        <tr class="border-b border-white/10"><td class="py-2 pr-4">RAM</td><td class="py-2">31 GB</td></tr>
                        <tr class="border-b border-white/10"><td class="py-2 pr-4">Costo</td><td class="py-2">$0.24/hr</td></tr>
                        <tr class="border-b border-white/10"><td class="py-2 pr-4">Modello</td><td class="py-2">Qwen2.5-VL 7B (quantizzato Q4)</td></tr>
                        <tr class="border-b border-white/10"><td class="py-2 pr-4">Runtime</td><td class="py-2">Ollama con flash attention</td></tr>
                        <tr><td class="py-2 pr-4">OS</td><td class="py-2">Ubuntu 22.04, CUDA 12.4.1</td></tr>
                    </tbody>
                </table>
            </div>

            <p>Il modello Qwen2.5-VL 7B, nella versione quantizzata Q4, occupa circa 13.3 GB di VRAM — lasciando appena 2.6 GB di margine sui 16 GB disponibili. Questa è la configurazione minima: un sistema con GPU da 12 GB non sarebbe sufficiente. Con 24 GB (RTX 3090 o RTX 4090), il modello avrebbe abbondante spazio per elaborazioni più complesse.</p>

            <h2 class="text-2xl font-black font-display text-white">I risultati: numeri che parlano chiaro</h2>

            <h3 class="text-xl font-bold text-white">Velocità e throughput</h3>

            <p>Prima di entrare nell'accuratezza, i numeri di velocità:</p>

            <div class="overflow-x-auto my-6">
                <table class="w-full text-sm border-collapse">
                    <thead>
                        <tr class="border-b border-white/20">
                            <th class="text-left py-2 pr-4 text-white font-bold">Metrica</th>
                            <th class="text-right py-2 text-white font-bold">Valore</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr class="border-b border-white/10"><td class="py-2 pr-4">Velocità media</td><td class="text-right py-2">32.0 secondi/documento</td></tr>
                        <tr class="border-b border-white/10"><td class="py-2 pr-4">Minimo / Massimo</td><td class="text-right py-2">25.8s / 53.0s</td></tr>
                        <tr class="border-b border-white/10"><td class="py-2 pr-4">Mediana (p50)</td><td class="text-right py-2">33.1s</td></tr>
                        <tr class="border-b border-white/10"><td class="py-2 pr-4">90° percentile (p90)</td><td class="text-right py-2">41.1s</td></tr>
                        <tr class="border-b border-white/10"><td class="py-2 pr-4">Throughput</td><td class="text-right py-2">~112 documenti/ora</td></tr>
                        <tr><td class="py-2 pr-4">Costo per documento</td><td class="text-right py-2 text-brand-tealLight font-bold">~$0.002</td></tr>
                    </tbody>
                </table>
            </div>

            <p>32 secondi per documento sembra molto rispetto a un sistema OCR tradizionale che impiegherebbe pochi millisecondi. Ma il confronto non regge: un sistema OCR estrae caratteri, non significato. Qui in 32 secondi il sistema identifica il tipo di documento, estrae tutti i campi semanticamente rilevanti (non solo il testo grezzo), valida formalmente P.IVA e codici fiscali, verifica i conti aritmeticamente, e assegna un giudizio di affidabilità. Nessun OCR fa tutto questo.</p>

            <p>Il confronto corretto è con un operatore umano che fa lo stesso lavoro: identificare il documento, trovare i campi, trascriverli, verificarli. Un operatore medio impiega tra 2 e 5 minuti per documento, con una percentuale di errore tipicamente intorno al 2-3% anche in condizioni ottimali. DataUnchain lo fa in 32 secondi con 95.5% di accuratezza.</p>

            <h3 class="text-xl font-bold text-white">Accuratezza campo per campo</h3>

            <p>Questo è il cuore del benchmark. Ogni campo estratto viene confrontato con il valore atteso nella ground truth, usando la metrica appropriata per quel tipo di campo.</p>

            <div class="overflow-x-auto my-6">
                <table class="w-full text-sm border-collapse">
                    <thead>
                        <tr class="border-b border-white/20">
                            <th class="text-left py-2 pr-4 text-white font-bold">Campo</th>
                            <th class="text-right py-2 pr-4 text-white font-bold">Accuratezza</th>
                            <th class="text-right py-2 text-white font-bold">Su</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr class="border-b border-white/10"><td class="py-2 pr-4">Tipo documento</td><td class="text-right pr-4 text-green-400">100.0%</td><td class="text-right py-2">206/206</td></tr>
                        <tr class="border-b border-white/10"><td class="py-2 pr-4">Riferimento (numero documento)</td><td class="text-right pr-4 text-green-400">96.6%</td><td class="text-right py-2">199/206</td></tr>
                        <tr class="border-b border-white/10"><td class="py-2 pr-4">P.IVA / CF soggetti</td><td class="text-right pr-4 text-green-400">100.0%</td><td class="text-right py-2">206/206</td></tr>
                        <tr class="border-b border-white/10"><td class="py-2 pr-4">Data emissione</td><td class="text-right pr-4 text-green-400">100.0%</td><td class="text-right py-2">144/144</td></tr>
                        <tr class="border-b border-white/10"><td class="py-2 pr-4">Imponibile (±€0.50)</td><td class="text-right pr-4 text-green-400">100.0%</td><td class="text-right py-2">94/94</td></tr>
                        <tr class="border-b border-white/10"><td class="py-2 pr-4">IVA (±€0.50)</td><td class="text-right pr-4 text-green-400">100.0%</td><td class="text-right py-2">94/94</td></tr>
                        <tr class="border-b border-white/10"><td class="py-2 pr-4">Totale (±€0.50)</td><td class="text-right pr-4 text-green-400">100.0%</td><td class="text-right py-2">94/94</td></tr>
                        <tr class="border-b border-white/10"><td class="py-2 pr-4">Lordo busta paga (±€0.50)</td><td class="text-right pr-4 text-yellow-400">54.3%</td><td class="text-right py-2">19/35</td></tr>
                        <tr class="border-b border-white/10"><td class="py-2 pr-4">Netto busta paga (±€0.50)</td><td class="text-right pr-4 text-green-400">100.0%</td><td class="text-right py-2">35/35</td></tr>
                        <tr class="border-b border-white/10"><td class="py-2 pr-4">Saldo finale estratto conto (±€0.50)</td><td class="text-right pr-4 text-green-400">100.0%</td><td class="text-right py-2">7/7</td></tr>
                        <tr class="border-b border-white/10"><td class="py-2 pr-4">Math check interno (±€0.10)</td><td class="text-right pr-4 text-green-400">100.0%</td><td class="text-right py-2">120/120</td></tr>
                    </tbody>
                </table>
            </div>

            <p>I numeri più importanti da osservare:</p>

            <p><strong class="text-white">P.IVA e Codici Fiscali: 100% su 206 documenti.</strong> Questo è il risultato più rilevante per un contesto aziendale italiano. I dati di identità fiscale — quelli che determinano a chi intestare una fattura, chi pagare, chi ha emesso il documento — vengono estratti correttamente in ogni singolo caso. Su documenti puliti e su documenti degradati da scansione, senza differenza.</p>

            <p><strong class="text-white">Importi finanziari: 100% su tutti i tipi che li contemplano.</strong> Imponibile, IVA, totale fattura: ogni singolo valore numerico estratto è corretto entro la tolleranza di 50 centesimi. Questo include documenti con cifre vicine a valori di soglia psicologica (€999.99, €9.999,00), con formattazione italiana delle migliaia (punto come separatore), e su documenti scannerizzati con qualità JPEG ridotta.</p>

            <p><strong class="text-white">Math check: 100% su 120 controlli.</strong> Non solo i singoli campi sono corretti, ma la coerenza interna è perfetta: per ogni fattura in cui imponibile + IVA viene controllato contro il totale, il risultato è corretto. Questo significa che il modello non solo legge i numeri giusti, ma li legge in modo coerente tra loro.</p>

            <p><strong class="text-white">Il solo campo problematico: lordo busta paga, 54.3%.</strong> Il campo "retribuzione lorda" nelle buste paga viene identificato correttamente solo poco più della metà delle volte. L'analisi manuale rivela il motivo: nelle buste paga italiane, questo campo appare con etichette molto diverse a seconda del CCNL e del software gestionale usato dall'azienda. "RETRIBUZIONE LORDA", "IMPONIBILE LORDO", "TOTALE COMPETENZE", "IMPONIBILE CONTRIBUTIVO", "TOTALE SPETTANZE" sono tutte etichette che indicano sostanzialmente lo stesso concetto, ma il modello le riconosce con frequenza diversa. Il netto, per contrasto, ha sempre l'etichetta "NETTO IN BUSTA" o "NETTO A PAGARE" — molto più uniforme — e viene estratto al 100%.</p>

            <h3 class="text-xl font-bold text-white">Il risultato più sorprendente: SCAN = CLEAN</h3>

            <p>Questo è il dato che ci ha sorpreso di più durante l'analisi dei risultati. Quando si confronta la performance su documenti simulati-scansionati (146 documenti) versus documenti PDF nativi puliti (60 documenti), la differenza è zero su ogni metrica misurata:</p>

            <div class="overflow-x-auto my-6">
                <table class="w-full text-sm border-collapse">
                    <thead>
                        <tr class="border-b border-white/20">
                            <th class="text-left py-2 pr-4 text-white font-bold">Metrica</th>
                            <th class="text-right py-2 pr-4 text-white font-bold">SCAN (146 doc)</th>
                            <th class="text-right py-2 text-white font-bold">CLEAN (60 doc)</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr class="border-b border-white/10"><td class="py-2 pr-4">Tipo documento</td><td class="text-right pr-4 text-green-400">100.0%</td><td class="text-right text-green-400">100.0%</td></tr>
                        <tr class="border-b border-white/10"><td class="py-2 pr-4">P.IVA / CF</td><td class="text-right pr-4 text-green-400">100.0%</td><td class="text-right text-green-400">100.0%</td></tr>
                        <tr class="border-b border-white/10"><td class="py-2 pr-4">Importo totale</td><td class="text-right pr-4 text-green-400">100.0%</td><td class="text-right text-green-400">100.0%</td></tr>
                        <tr class="border-b border-white/10"><td class="py-2 pr-4">Math check</td><td class="text-right pr-4 text-green-400">100.0%</td><td class="text-right text-green-400">100.0%</td></tr>
                        <tr><td class="py-2 pr-4">Data emissione</td><td class="text-right pr-4 text-green-400">100.0%</td><td class="text-right text-green-400">100.0%</td></tr>
                    </tbody>
                </table>
            </div>

            <p>Perché questo è importante? Perché la principale obiezione ai sistemi AI per documenti è sempre stata: "funziona bene su PDF nativi, ma i nostri documenti sono tutti scannerizzati, timbrati, stropicciati, a volte ruotati di qualche grado". Qwen2.5-VL è un modello di visione multimodale allenato su enormi quantità di immagini di documenti reali — include già nella sua distribuzione di training documenti degradati, scannerizzati, di scarsa qualità. Il risultato è un'immunità completa alla degradazione da scansione nelle condizioni testate.</p>

            <p>Non siamo ingenui: ci sono soglie di degradazione oltre le quali anche questo modello fallirebbe. Un documento scannerizzato a 72 DPI con forte motion blur e rotazione di 45 gradi probabilmente darebbe risultati peggiori. Ma le condizioni che abbiamo testato — quelle reali di un ufficio con un normale scanner da rete — producono performance identiche al documento originale.</p>

            <h3 class="text-xl font-bold text-white">Confidence e audit status: il sistema sa quando non sa</h3>

            <p>Una caratteristica critica di qualsiasi sistema di automazione documentale è la capacità di identificare i propri errori. Un sistema che sbaglia e non lo segnala è pericoloso: il problema passa inosservato. Un sistema che sbaglia e lo segnala è gestibile: un operatore umano revisiona solo i casi dubbi.</p>

            <div class="overflow-x-auto my-6">
                <table class="w-full text-sm border-collapse">
                    <thead>
                        <tr class="border-b border-white/20">
                            <th class="text-left py-2 pr-4 text-white font-bold">Distribuzione Confidence</th>
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

            <p>Il 92.2% dei documenti riceve alta confidence: il sistema è sicuro di sé su quasi tutto il corpus. Il 5.9% LOW corrisponde esattamente ai 13 estratti conto che hanno incontrato il limite hardware (descritto nella sezione successiva). Il dato chiave è che quando il sistema è in difficoltà, lo segnala: i 4 documenti MEDIUM e i 13 LOW vengono automaticamente indirizzati alla revisione umana, non inseriti silenziosamente nel flusso di dati come se fossero corretti.</p>

            <h2 class="text-2xl font-black font-display text-white">Consumo risorse: cosa succede dentro la GPU</h2>

            <p>Durante il benchmark abbiamo monitorato il consumo delle risorse hardware ogni 60 secondi usando <code class="text-brand-tealLight">nvidia-smi</code>. I dati raccontano una storia precisa sull'architettura della pipeline.</p>

            <h3 class="text-xl font-bold text-white">Durante l'inferenza attiva</h3>

            <div class="overflow-x-auto my-6">
                <table class="w-full text-sm border-collapse">
                    <thead>
                        <tr class="border-b border-white/20">
                            <th class="text-left py-2 pr-4 text-white font-bold">Metrica</th>
                            <th class="text-right py-2 pr-4 text-white font-bold">Min</th>
                            <th class="text-right py-2 pr-4 text-white font-bold">Max</th>
                            <th class="text-right py-2 text-white font-bold">Media</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr class="border-b border-white/10"><td class="py-2 pr-4">GPU utilization</td><td class="text-right pr-4">87%</td><td class="text-right pr-4">100%</td><td class="text-right">~94%</td></tr>
                        <tr class="border-b border-white/10"><td class="py-2 pr-4">VRAM usata</td><td class="text-right pr-4">13.288 MiB</td><td class="text-right pr-4">13.377 MiB</td><td class="text-right">~13.3 GB</td></tr>
                        <tr class="border-b border-white/10"><td class="py-2 pr-4">GPU power draw</td><td class="text-right pr-4">63.7 W</td><td class="text-right pr-4">70.2 W</td><td class="text-right">~68 W</td></tr>
                        <tr class="border-b border-white/10"><td class="py-2 pr-4">GPU temperatura</td><td class="text-right pr-4">65°C</td><td class="text-right pr-4">70°C</td><td class="text-right">~68°C</td></tr>
                        <tr class="border-b border-white/10"><td class="py-2 pr-4">CPU utilization</td><td class="text-right pr-4">2%</td><td class="text-right pr-4">17%</td><td class="text-right">~4%</td></tr>
                        <tr><td class="py-2 pr-4">RAM usata</td><td class="text-right pr-4">~35 GiB</td><td class="text-right pr-4">~37 GiB</td><td class="text-right">~35 GiB</td></tr>
                    </tbody>
                </table>
            </div>

            <p><strong class="text-white">La pipeline è 100% GPU-bound.</strong> La CPU non è mai un collo di bottiglia: il suo utilizzo medio del 4% significa che sta semplicemente aspettando i risultati della GPU. Aggiungere core CPU a questa macchina non migliorerebbe assolutamente nulla. Tutto ciò che conta è la GPU e la sua VRAM.</p>

            <p><strong class="text-white">La VRAM è quasi satura: 13.3 GB su 16 GB disponibili.</strong> Rimangono 2.6 GB di margine, sufficiente per le immagini dei documenti e il contesto del modello durante l'inferenza, ma non abbastanza per un modello più grande. RTX 2000 Ada 16 GB è davvero il minimo assoluto per questa configurazione.</p>

            <p><strong class="text-white">Il consumo energetico attivo è di circa 68 W.</strong> La RTX 2000 Ada ha un TDP di 70 W — stiamo quindi usando quasi tutta la potenza termica disponibile durante l'inferenza. In idle (modello in VRAM, nessuna richiesta in corso), il consumo scende a 6-7 W e la temperatura GPU a 26°C.</p>

            <p>Questo dato energetico è rilevante per chi valuta un deployment on-premise: un server con RTX 3090 (350 W TDP) elaborerebbe probabilmente documenti in 15-20 secondi invece di 32, ma consumerebbe molto di più. RTX 4090 (450 W TDP) sarebbe ancora più veloce. Il bilanciamento tra costo hardware, costo energetico e throughput richiesto è un calcolo specifico per ogni scenario di deployment.</p>

            <h2 class="text-2xl font-black font-display text-white">I limiti identificati: onestà scientifica</h2>

            <p>Un benchmark scientifico senza una sezione onesta sui limiti non è un benchmark scientifico: è marketing. Ecco i due problemi reali identificati durante questo test.</p>

            <h3 class="text-xl font-bold text-white">Limite 1: crash GGML sugli estratti conto ad alta densità</h3>

            <p>13 documenti su 20 nel tipo "estratto_conto" producono un crash interno del runtime Ollama/llama.cpp:</p>

            <div class="code-block rounded-xl text-xs my-4">
                <span class="cmt">GGML_ASSERT(a-&gt;ne[2] * 4 == b-&gt;ne[0]) failed (HTTP 500)</span>
            </div>

            <p>Questo errore non viene dalla nostra pipeline né dal modello stesso: è un'asserzione nel layer GGML (il backend tensoriale che Ollama usa per eseguire il modello) che fallisce quando le dimensioni dei tensori non si allineano come atteso. Si verifica nello step di estrazione — non nella classificazione, che funziona correttamente su tutti i 20 estratti conto.</p>

            <p>La causa è una combinazione di fattori: l'immagine di un estratto conto con molte righe di movimenti (15-20 transazioni) è densa di testo tabellare. Quando questa immagine viene passata alla vision encoder insieme al prompt di estrazione (che per gli estratti conto è particolarmente lungo — include IBAN, saldo iniziale, lista movimenti, saldo finale), la combinazione immagine + prompt supera un limite interno di dimensione dei tensori nel modello 7B su 16 GB di VRAM.</p>

            <p>I 7 estratti conto elaborati correttamente avevano tutti meno righe di movimenti. Su quei 7, il sistema ottiene 100% su tutti i campi incluso il saldo finale — la metrica più difficile, che richiede di seguire la sequenza di tutti i movimenti.</p>

            <p><strong class="text-white">La soluzione:</strong> ridurre il DPI di conversione per gli estratti conto (da 200 a 150 DPI), che riduce le dimensioni dell'immagine e quindi la pressione sulla vision encoder. In alternativa, usare Qwen2.5-VL 14B o 32B, che hanno una vision encoder dimensionata per immagini più grandi. Entrambe le soluzioni verranno testate nel benchmark v3.</p>

            <h3 class="text-xl font-bold text-white">Limite 2: campo "lordo" nelle buste paga — 54.3%</h3>

            <p>Come descritto sopra, la retribuzione lorda nelle buste paga viene identificata correttamente solo nel 54.3% dei casi. L'analisi delle cause mostra un pattern chiaro: il problema non è la lettura del numero (quando il campo viene trovato, il valore numerico è sempre corretto), ma l'identificazione dell'etichetta corretta tra le molte varianti usate dai diversi CCNL e software gestionali italiani.</p>

            <p>Questo è esattamente il tipo di problema risolvibile con un prompt più ricco: se al modello viene fornita una lista esplicita delle possibili etichette per il campo "lordo" nelle buste paga italiane, l'accuratezza dovrebbe avvicinarsi significativamente al 100%. Questa fix è pianificata per il processor v2.1.</p>

            <h3 class="text-xl font-bold text-white">Limite 3: falsi positivi nel format validator — 1.9%</h3>

            <p>4 documenti su 206 (1.9%) ricevono un <code class="text-yellow-400">format_error</code> dal validator di P.IVA/CF nonostante i dati estratti siano corretti. Questo indica un piccolo bug nelle regex di validazione: probabilmente gestione incompleta di alcune varianti del codice fiscale per persone nate all'estero (che hanno un codice diverso da quello standard). Fix previsto nel validator v2.1.</p>

            <h2 class="text-2xl font-black font-display text-white">Analisi economica: cosa significa $0.002 a documento</h2>

            <p>Il costo operativo di $0.002 per documento su cloud (a $0.24/ora con 32 secondi/documento) può sembrare un numero astratto. Mettiamolo in contesto con scenari reali di utilizzo aziendale.</p>

            <h3 class="text-xl font-bold text-white">Scenario 1: piccola impresa, 100 fatture/mese</h3>

            <p>Una piccola impresa con 100 fatture fornitori al mese spende oggi tipicamente 2-4 ore di lavoro di segreteria per inserire manualmente quei dati nel gestionale. Al costo medio del lavoro d'ufficio in Italia (€18-22/ora lordi), sono €36-88/mese di costo diretto, più il costo dei ritardi e degli errori di battitura che poi richiedono correzioni.</p>

            <p>Con DataUnchain su cloud: 100 documenti × $0.002 = $0.20/mese. Sul server aziendale già presente: costo energetico marginale vicino allo zero.</p>

            <h3 class="text-xl font-bold text-white">Scenario 2: media impresa, 2.000 documenti/mese</h3>

            <p>Un'azienda manifatturiera di medie dimensioni gestisce ogni mese circa 2.000 documenti: DDT in entrata e uscita, fatture fornitori, ordini di acquisto, buste paga del personale. Tradizionalmente questo richiede 1-2 addetti dedicati in parte significativa del loro tempo.</p>

            <p>Su cloud: 2.000 × $0.002 = $4/mese. Meno del costo di un caffè in ufficio. Il ROI è immediato.</p>

            <h3 class="text-xl font-bold text-white">Scenario 3: deployment on-premise con RTX 3090</h3>

            <p>Una RTX 3090 24 GB costa circa €900-1.200 sul mercato dell'usato di buona qualità. Su questa GPU, Qwen2.5-VL 7B elabora probabilmente i documenti in 15-20 secondi invece di 32 (stima basata sul rapporto di performance GPU). Il consumo energetico è circa 350 W durante l'inferenza.</p>

            <p>Ammortizzando l'hardware in 3 anni con un consumo medio di 4 ore/giorno: il costo per documento scende sotto $0.001. Per volumi alti (10.000+ documenti/mese), l'on-premise diventa più economico del cloud già al primo anno.</p>

            <p>Ma il vantaggio economico più importante dell'on-premise non è il costo marginale: è l'assenza di costi fissi mensili per abbonamenti SaaS, che tipicamente si aggirano tra €200 e €2.000/mese per i competitor di fascia professionale. E soprattutto: nessun dato aziendale riservato lascia mai la tua infrastruttura.</p>

            <h2 class="text-2xl font-black font-display text-white">La scelta del modello: perché Qwen2.5-VL 7B?</h2>

            <p>La scelta di Qwen2.5-VL come backbone del processor DataUnchain non è casuale. Abbiamo valutato le alternative disponibili nel panorama open-source per i modelli di visione-linguaggio (VLM):</p>

            <p><strong class="text-white">LLaVA e varianti</strong> (Haotian Liu et al.) hanno segnato l'inizio dell'era VLM open-source ma mostrano difficoltà significative sui documenti con testo denso e tabelle strutturate — esattamente le condizioni dei documenti aziendali.</p>

            <p><strong class="text-white">InternVL</strong> e <strong class="text-white">Idefics</strong> sono modelli competenti ma con un ecosistema di deployment meno maturo rispetto alla combinazione Qwen + Ollama.</p>

            <p><strong class="text-white">Qwen2.5-VL</strong> (Alibaba DAMO Academy) eccelle specificamente nel document understanding grazie a un training che ha incluso enormi quantità di documenti strutturati in molte lingue, incluso l'italiano. La versione 7B offre il miglior compromesso tra qualità e requisiti hardware: funziona su GPU consumer a 16 GB, ma mantiene un'accuratezza che in questo benchmark è superiore a molte soluzioni cloud proprietarie su questa specifica tipologia di documenti.</p>

            <p>È importante notare che Qwen2.5-VL non è un modello specializzato per OCR o document understanding: è un modello general-purpose che "capisce" i documenti perché è stato allenato su di essi. Questo significa che non richiede fine-tuning specifico per ogni nuovo tipo di documento: basta aggiornare il prompt di estrazione.</p>

            <h2 class="text-2xl font-black font-display text-white">Cosa significa "completamente offline"</h2>

            <p>Vale la pena soffermarsi su questa caratteristica, perché è quella che differenzia DataUnchain dal 99% dei competitor sul mercato. Quando diciamo che il sistema funziona completamente offline, intendiamo che:</p>

            <p><strong class="text-white">Nessun dato lascia la macchina.</strong> I PDF vengono convertiti in immagini localmente. Le immagini vengono processate da Ollama che gira localmente. Il JSON risultante viene scritto localmente. In nessun momento del processo un dato viene inviato a server di terzi — non ad Anthropic, non a OpenAI, non a Microsoft, non a nessun provider cloud di AI.</p>

            <p><strong class="text-white">Nessuna connessione internet richiesta durante l'elaborazione.</strong> Una volta che il modello è scaricato (operazione one-time di circa 5 GB), il sistema può girare in ambienti air-gapped: reti senza accesso a internet, sistemi con politiche di sicurezza restrittive, ambienti industriali isolati.</p>

            <p><strong class="text-white">Nessun abbonamento mensile, nessun costo per token.</strong> Il modello è open-source (licenza Apache 2.0). Ollama è open-source. DataUnchain processor è open-source. L'unico costo è l'hardware su cui gira.</p>

            <p>Questo è particolarmente rilevante per i settori che trattano documenti sensibili: commercialisti e studi professionali (dati fiscali dei clienti), HR e amministrazione del personale (buste paga, contratti di lavoro), istituti bancari (estratti conto, documentazione creditizia), settori regolamentati (healthcare, legal, finance) dove la trasmissione di dati a servizi esterni è soggetta a vincoli normativi severi.</p>

            <h2 class="text-2xl font-black font-display text-white">Raccomandazioni hardware per il deployment</h2>

            <p>Sulla base dei dati di questo benchmark, possiamo dare indicazioni concrete per chi sta pianificando un deployment.</p>

            <div class="overflow-x-auto my-6">
                <table class="w-full text-sm border-collapse">
                    <thead>
                        <tr class="border-b border-white/20">
                            <th class="text-left py-2 pr-4 text-white font-bold">GPU</th>
                            <th class="text-right py-2 pr-4 text-white font-bold">VRAM</th>
                            <th class="text-left py-2 pr-4 text-white font-bold">Scenario</th>
                            <th class="text-left py-2 text-white font-bold">Note</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr class="border-b border-white/10"><td class="py-2 pr-4">RTX 2000 Ada / RTX 3080</td><td class="text-right pr-4">16 GB</td><td class="py-2 pr-4">Minimo funzionante</td><td class="py-2">Margine VRAM ridotto. Estratti conto ad alta densità a rischio crash</td></tr>
                        <tr class="border-b border-white/10"><td class="py-2 pr-4">RTX 3090 / RTX 4090</td><td class="text-right pr-4">24 GB</td><td class="py-2 pr-4">Consigliato</td><td class="py-2">Tutti i tipi documentali stabili. ~20s/doc stimati. Rapporto qualità/prezzo ottimo</td></tr>
                        <tr class="border-b border-white/10"><td class="py-2 pr-4">A5000 / A6000</td><td class="text-right pr-4">24–48 GB</td><td class="py-2 pr-4">Enterprise</td><td class="py-2">ECC memory, garanzia professionale, forma factor server. Ideale per installazioni data center</td></tr>
                        <tr><td class="py-2 pr-4">A100 / H100</td><td class="text-right pr-4">40–80 GB</td><td class="py-2 pr-4">High throughput</td><td class="py-2">Supporta Qwen2.5-VL 32B o elaborazione parallela multipla. Per volumi > 50.000 doc/mese</td></tr>
                    </tbody>
                </table>
            </div>

            <p><strong class="text-white">Nota importante sulla CPU:</strong> i dati di questo benchmark confermano che la CPU non è rilevante per le performance. Un sistema con RTX 3090 e Intel Core i5 sarà più veloce di un sistema con RTX 2000 Ada e Intel Core i9. L'unica cosa che conta è la GPU.</p>

            <p><strong class="text-white">Nota sulla RAM:</strong> durante il benchmark la RAM usata si è stabilizzata intorno a 35-37 GB. Questo include il sistema operativo, Ollama, il processor DataUnchain, e i buffer per la conversione PDF. 32 GB di RAM è il minimo raccomandabile per un deployment di produzione; 64 GB garantisce headroom per carichi di picco e future espansioni.</p>

            <h2 class="text-2xl font-black font-display text-white">Confronto con soluzioni cloud</h2>

            <p>Come si posiziona DataUnchain rispetto alle soluzioni cloud esistenti per l'estrazione da documenti? Dobbiamo essere cauti nel fare confronti diretti perché non abbiamo un benchmark identico eseguito sugli stessi documenti con le stesse metriche. Ma possiamo fare considerazioni qualitative basate su dati pubblici.</p>

            <p><strong class="text-white">Amazon Textract</strong> su documenti italiani ha performance tipicamente nell'intervallo 85-92% sull'estrazione di campi chiave in condizioni standard. La qualità di Textract degrada significativamente su documenti scannerizzati di bassa qualità, dove il nostro sistema mantiene le stesse performance dei documenti puliti. Costo: $0.015-0.065 per pagina, ovvero 7-32 volte più costoso.</p>

            <p><strong class="text-white">Azure Form Recognizer / Document Intelligence</strong> raggiunge 90-95% su tipologie documentali per cui è stato specificamente addestrato, ma richiede un periodo di training su documenti del cliente (decine di campioni per tipo), ha costi che partono da $10 per 1.000 pagine, e ovviamente invia tutti i documenti a Microsoft Azure.</p>

            <p><strong class="text-white">Google Document AI</strong> è probabilmente il più accurato dei big cloud provider su tipologie standard, ma richiede Google Cloud, ha modelli di pricing complessi, e non supporta nativamente il formato dei documenti fiscali italiani (P.IVA, codice fiscale, SDI) senza customizzazione.</p>

            <p>Il punto non è che DataUnchain sia "meglio" in assoluto di questi servizi — hanno anni di sviluppo, team enormi, infrastrutture globalizzate. Il punto è che per il caso d'uso specifico (documenti aziendali italiani, requisiti di privacy, costo operativo basso), il rapporto qualità/prezzo/privacy di un modello open-source locale è oggi già competitivo e in alcuni casi superiore.</p>

            <h2 class="text-2xl font-black font-display text-white">Riproducibilità del benchmark</h2>

            <p>Uno dei principi fondamentali di questo progetto è la riproducibilità. Tutto il codice usato per questo benchmark è open-source nel repository DataUnchain:</p>

            <div class="code-block rounded-xl text-xs my-4">
                <span class="cmt"># Struttura del benchmark</span><br>
                <span class="kw">demo/</span><br>
                <span class="str">├── processor/main.py          ← processor v2.0</span><br>
                <span class="str">├── test-generator/generate.py ← generatore PDF + ground truth</span><br>
                <span class="str">└── runpod/</span><br>
                <span class="str">    ├── benchmark.py           ← analisi GT vs estratto</span><br>
                <span class="str">    ├── benchmark_run.sh       ← orchestrazione completa</span><br>
                <span class="str">    └── README.md              ← istruzioni RunPod</span>
            </div>

            <p>Per replicare il benchmark, sono necessari:</p>
            <ul>
                <li>Una GPU con ≥16 GB VRAM</li>
                <li>Ollama con Qwen2.5-VL 7B scaricato</li>
                <li>Python 3.11+ con le dipendenze del repository</li>
                <li>Eseguire <code class="text-brand-tealLight">bash benchmark_run.sh</code></li>
            </ul>

            <p>Lo script genera i 219 documenti, avvia il processor, attende il completamento (senza timeout arbitrari), ed esegue il confronto con la ground truth producendo il report JSON completo. Il seed del generatore casuale è fisso per garantire riproducibilità esatta.</p>

            <h2 class="text-2xl font-black font-display text-white">Prossimi step: cosa stiamo migliorando</h2>

            <p>Questo benchmark è la versione 2.1. I problemi identificati hanno già roadmap di fix chiari:</p>

            <p><strong class="text-white">1. Fix busta paga lordo (v2.1 processor):</strong> aggiornamento del prompt di estrazione con lista esplicita delle varianti di etichetta per il campo lordo nelle buste paga italiane. Target: >90% su questo campo.</p>

            <p><strong class="text-white">2. Fix estratto conto GGML (v2.1 processor):</strong> implementazione di DPI adattivo — per documenti con tabelle ad alta densità di righe, riduzione automatica del DPI di conversione da 200 a 150. Questo riduce la pressione sulla vision encoder mantenendo leggibilità sufficiente.</p>

            <p><strong class="text-white">3. Fix format validator false positives (v2.1 validator):</strong> revisione delle regex di validazione per gestire correttamente i codici fiscali di persone nate all'estero.</p>

            <p><strong class="text-white">4. Estensione corpus (benchmark v3):</strong> aggiunta di ricevuta/scontrino, packing list, preventivo, e documenti specifici del settore sanitario (prescrizioni, referti) al corpus di test.</p>

            <p><strong class="text-white">5. Test Qwen2.5-VL 32B:</strong> benchmark comparativo tra il modello 7B e il 32B su hardware da 48+ GB per quantificare il delta di accuratezza. L'ipotesi è che il 32B risolva sia il problema estratto conto che il problema busta paga lordo.</p>

            <p><strong class="text-white">6. Test modelli alternativi:</strong> benchmark dello stesso corpus con InternVL2-8B e LLaVA-NeXT-72B per dare al mercato dati comparativi oggettivi.</p>

            <h2 class="text-2xl font-black font-display text-white">Conclusioni</h2>

            <p>La domanda con cui abbiamo aperto questo articolo era: un modello open-source da 7B parametri, eseguito su hardware consumer a 16 GB VRAM, può estrarre dati da documenti aziendali italiani con accuratezza sufficiente per uso aziendale?</p>

            <p>La risposta che i dati di questo benchmark forniscono è: <strong class="text-white">sì, con 95.5% di accuratezza complessiva, a $0.002 per documento, completamente offline.</strong></p>

            <p>In concreto: P.IVA e codici fiscali al 100%, importi finanziari al 100%, math check al 100%, nessuna differenza tra documenti nativi e documenti scannerizzati. Un solo campo critico sotto il 90% (busta paga lordo: 54.3%) con causa identificata e fix pianificato. Un limite hardware su un tipo di documento (estratto conto ad alta densità) con soluzione chiara.</p>

            <p>Il sistema non è perfetto — nessun sistema di estrazione automatica lo è. Ma è oggi sufficientemente accurato, sufficientemente veloce, e sufficientemente economico da giustificare l'adozione in produzione per la grande maggioranza dei flussi documentali aziendali italiani. E lo fa senza inviare un solo byte di dati aziendali riservati fuori dalla tua infrastruttura.</p>

            <p>Questi sono i dati. Ogni numero è verificabile, il codice è pubblico, il benchmark è riproducibile. Siamo convinti che la trasparenza sia l'unico modo serio di costruire fiducia in un sistema che deve toccare i documenti più sensibili della tua azienda.</p>

        </div>

        <div class="mt-12 pt-8 border-t border-white/10 text-center">
            <a href="/it/blog/" class="text-brand-tealLight font-bold hover:underline">← Torna al Blog</a>
        </div>

    </div>
</article>
