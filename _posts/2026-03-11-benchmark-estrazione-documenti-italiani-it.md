---
layout: default
title: "Abbiamo testato 219 documenti aziendali italiani su un'AI offline. Ecco i numeri."
lang: it
categories: blog
date: 2026-03-11
author: Antonio Trento
description: "Benchmark scientifico di DataUnchain su 219 documenti aziendali italiani — fatture, buste paga, contratti, DDT — con ground truth verificata. 95.5% di accuratezza. $0.002 a documento. Zero cloud."
---

<article class="pt-36 pb-20 px-6">
    <div class="max-w-3xl mx-auto">

        <div class="mb-10">
            <span class="text-brand-tealLight text-xs font-bold uppercase tracking-widest">Benchmark &middot; 11 Marzo 2026</span>
            <h1 class="text-4xl lg:text-5xl font-black font-display mt-4 mb-6 leading-tight">Abbiamo testato 219 documenti aziendali italiani su un&rsquo;AI offline. Ecco i numeri.</h1>
            <p class="text-gray-400 text-lg leading-relaxed">Fatture, buste paga, contratti, DDT &mdash; 219 documenti con ground truth verificata, elaborati da Qwen2.5-VL 7B che gira in locale su una GPU da $0.24/ora. Nessun cloud. Nessun abbonamento. Nessun dato che lascia la macchina.</p>
        </div>

        <div class="relative rounded-2xl overflow-hidden mb-12" style="background: linear-gradient(135deg, #0D9488 0%, #10B981 50%, #F59E0B 100%);">
            <div class="relative px-6 py-10 text-center">
                <div class="text-7xl lg:text-8xl font-black text-white mb-2">95.5%</div>
                <div class="text-white/80 text-xl font-bold mb-1">Punteggio di Accuratezza Complessivo</div>
                <div class="text-white/60 text-sm">su 206 documenti elaborati con successo &middot; Qwen2.5-VL 7B &middot; RTX 2000 Ada 16 GB</div>
            </div>
        </div>

        <div class="grid grid-cols-2 lg:grid-cols-4 gap-3 mb-12">
            <div class="bg-brand-surface rounded-xl p-4 text-center border border-white/10">
                <div class="text-2xl font-black text-brand-tealLight">$0.002</div>
                <div class="text-gray-400 text-xs mt-1">costo a documento</div>
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

        <div class="prose prose-invert prose-lg max-w-none text-gray-300 leading-relaxed space-y-6">

            <h2 class="text-2xl font-black font-display text-white">La domanda a cui volevamo rispondere</h2>

            <p>Un modello open-source da 7 miliardi di parametri, che gira su una GPU da &euro;900, riesce a estrarre dati strutturati da documenti aziendali italiani in modo accurato abbastanza da essere messo in produzione?</p>

            <p>Non una demo con i documenti migliori scelti a mano. Non screenshot di casi perfetti selezionati dopo. Un benchmark vero: 219 documenti con risposta corretta nota per ogni campo, confronto automatizzato campo per campo, risultati pubblicati nella loro interezza &mdash; inclusi i due limiti che abbiamo trovato e che descriviamo in dettaglio qui sotto.</p>

            <p>La risposta alla domanda iniziale &egrave; s&igrave;. Con due eccezioni ben documentate, entrambe risolvibili, una con una singola riga di modifica al prompt e l&rsquo;altra con hardware leggermente pi&ugrave; potente. Il sistema funziona, produce JSON strutturato e verificato, e costa una frazione di qualsiasi alternativa cloud esistente sul mercato.</p>

            <p>Questo articolo documenta l&rsquo;intero processo &mdash; come abbiamo costruito il corpus, come funziona la pipeline, cosa ha estratto il modello correttamente, cosa no, e come interpretare ogni numero per decidere se questo strumento fa al caso tuo.</p>

            <h2 class="text-2xl font-black font-display text-white">Perch&eacute; questo benchmark &egrave; diverso dagli altri</h2>

            <p>La maggior parte dei benchmark pubblici per l&rsquo;estrazione di documenti ha un problema fondamentale: la ground truth non &egrave; verificata. Un essere umano ha annotato i campi, ma nessuno ha controllato che i numeri tornino. Per i documenti contabili, questo significa che l&rsquo;errore umano nell&rsquo;annotazione pu&ograve; essere confuso con l&rsquo;errore del modello.</p>

            <p>Noi abbiamo risolto questo problema alla radice: la ground truth &egrave; <strong class="text-white">sintetica e matematicamente coerente</strong>. Ogni fattura &egrave; generata programmaticamente con seed fisso. Ogni imponibile, IVA e totale sono calcolati in Python con aritmetica intera a centesimi &mdash; zero errori di arrotondamento, zero ambiguit&agrave;. Ogni busta paga ha <code class="text-brand-tealLight">lordo &minus; trattenute = netto</code> al centesimo esatto. Ogni estratto conto ha <code class="text-brand-tealLight">saldo_iniziale + accrediti &minus; addebiti = saldo_finale</code> senza eccezioni.</p>

            <p>Questo ci permette di testare qualcosa di pi&ugrave; interessante del semplice &ldquo;ha letto il numero?&rdquo;: testare se il sistema <em>rileva gli errori interni</em>. Perch&eacute; in produzione, la capacit&agrave; di segnalare una fattura con l&rsquo;IVA che non torna vale pi&ugrave; della capacit&agrave; di leggere qualsiasi singolo campo.</p>

            <h2 class="text-2xl font-black font-display text-white">Il corpus: 219 documenti, 7 tipologie</h2>

            <p>Il corpus copre i sette tipi documentali pi&ugrave; comuni nel ciclo amministrativo di una PMI italiana: fattura attiva e passiva, documento di trasporto (DDT/bolla), busta paga, nota di credito, contratto di servizio, ordine di acquisto, estratto conto bancario. Ogni tipo viene elaborato con template diversi &mdash; font diversi, layout diversi, strutture diverse &mdash; per simulare la variet&agrave; reale del parco documentale aziendale.</p>

            <p>Il <strong class="text-white">70% del corpus &egrave; stato degradato con effetti di scansione simulati</strong>: rumore gaussiano, rotazione di &plusmn;3&deg;, compressione JPEG qualit&agrave; 60&ndash;85, timbri sovrapposti, watermark &ldquo;PAGATO&rdquo;/&ldquo;ORIGINALE&rdquo;. Questo non &egrave; un dettaglio cosmetico &mdash; &egrave; il motivo per cui molti sistemi OCR falliscono in produzione. I documenti reali non sono PDF nativi con font perfetti. Vengono scansionati su macchine da ufficio economiche, salvati in JPEG da app mobile, fotocopiati su carta vecchia. Se il sistema non funziona su questi documenti, non funziona in produzione.</p>

        </div>

        <div class="overflow-x-auto my-8">
            <table class="w-full text-sm">
                <thead>
                    <tr class="border-b border-white/20 text-left">
                        <th class="pb-3 pr-4 text-white font-bold">Tipo documento</th>
                        <th class="pb-3 pr-4 text-right text-white font-bold">Doc</th>
                        <th class="pb-3 text-white font-bold">Campi principali</th>
                    </tr>
                </thead>
                <tbody class="text-gray-400">
                    <tr class="border-b border-white/10">
                        <td class="py-2.5 pr-4 text-white">Fattura</td>
                        <td class="text-right pr-4">60</td>
                        <td class="py-2.5">P.IVA, imponibile, IVA 22%, totale, righe prodotto</td>
                    </tr>
                    <tr class="border-b border-white/10">
                        <td class="py-2.5 pr-4 text-white">DDT (bolla di trasporto)</td>
                        <td class="text-right pr-4">50</td>
                        <td class="py-2.5">mittente, destinatario, trasportatore, merci</td>
                    </tr>
                    <tr class="border-b border-white/10">
                        <td class="py-2.5 pr-4 text-white">Busta Paga</td>
                        <td class="text-right pr-4">35</td>
                        <td class="py-2.5">CF dipendente, P.IVA azienda, CCNL, lordo, netto</td>
                    </tr>
                    <tr class="border-b border-white/10">
                        <td class="py-2.5 pr-4 text-white">Nota di Credito</td>
                        <td class="text-right pr-4">20</td>
                        <td class="py-2.5">fattura di riferimento, importo credito, motivo</td>
                    </tr>
                    <tr class="border-b border-white/10">
                        <td class="py-2.5 pr-4 text-white">Contratto di Servizio</td>
                        <td class="text-right pr-4">20</td>
                        <td class="py-2.5">tipo, parti contraenti, entrambe le P.IVA, data stipula</td>
                    </tr>
                    <tr class="border-b border-white/10">
                        <td class="py-2.5 pr-4 text-white">Ordine di Acquisto</td>
                        <td class="text-right pr-4">14</td>
                        <td class="py-2.5">numero ordine, data consegna, totale, P.IVA fornitore</td>
                    </tr>
                    <tr class="border-b border-white/10">
                        <td class="py-2.5 pr-4 text-white">Estratto Conto Bancario</td>
                        <td class="text-right pr-4">20</td>
                        <td class="py-2.5">IBAN, saldo iniziale, movimenti tabellari, saldo finale</td>
                    </tr>
                    <tr class="text-white font-bold">
                        <td class="py-2.5 pr-4">Totale</td>
                        <td class="text-right pr-4">219</td>
                        <td></td>
                    </tr>
                </tbody>
            </table>
        </div>

        <div class="prose prose-invert prose-lg max-w-none text-gray-300 leading-relaxed space-y-6">

            <p>La ground truth &egrave; verificata matematicamente. Per ogni fattura: <code class="text-brand-tealLight">imponibile + iva = totale</code> esattamente, senza eccezioni. Per ogni busta paga: <code class="text-brand-tealLight">lordo &minus; trattenute = netto</code> al centesimo. Per ogni estratto conto: <code class="text-brand-tealLight">saldo_iniziale + accrediti &minus; addebiti = saldo_finale</code> matematicamente esatto. Questo ci ha permesso di testare non solo l&rsquo;estrazione dei singoli campi, ma la capacit&agrave; del sistema di rilevare incoerenze aritmetiche interne &mdash; una funzionalit&agrave; critica per qualsiasi pipeline documentale che vuole essere affidabile in produzione.</p>

            <h2 class="text-2xl font-black font-display text-white">Come funziona la pipeline: tre step deterministici</h2>

            <p>DataUnchain processor v2.0 lavora in tre fasi ben distinte, ognuna con responsabilit&agrave; chiare. Non c&rsquo;&egrave; un unico modello che fa tutto &mdash; c&rsquo;&egrave; una pipeline ingegneristica che usa l&rsquo;AI dove serve e il codice deterministico dove il codice deterministico &egrave; pi&ugrave; affidabile.</p>

            <p><strong class="text-white">Step 1 &mdash; Classify:</strong> Il modello Qwen2.5-VL riceve l&rsquo;immagine del documento e produce una sola stringa: il tipo di documento. Nessun hint fornito, nessuna lista di tipi possibili suggerita al modello. Decide autonomamente. Il risultato viene validato contro la lista dei tipi noti; se non corrisponde, il documento finisce in una coda di revisione umana invece di procedere con un tipo errato.</p>

            <p><strong class="text-white">Step 2 &mdash; Extract:</strong> Sulla base del tipo classificato nello step precedente, viene selezionato il prompt specifico per quel tipo di documento. Il modello riceve immagine pi&ugrave; prompt e produce JSON strutturato. Ogni tipo documentale ha il proprio prompt ottimizzato con i campi esatti da estrarre, il formato atteso dei valori, e istruzioni su come gestire campi mancanti o ambigui. Il JSON viene parsato e validato strutturalmente &mdash; se non &egrave; JSON valido, viene ritentato una volta con prompt leggermente modificato.</p>

            <p><strong class="text-white">Step 3 &mdash; Audit:</strong> Python puro, zero AI. Questo &egrave; il cuore della differenziazione. Il codice di audit esegue cinque categorie di controlli: validazione algoritmica della P.IVA italiana a 11 cifre (cifra di controllo Luhn-like), validazione del Codice Fiscale a 16 caratteri con tabelle ODD/EVEN e gestione delle omocodie, validazione degli intervalli di date (nessuna data nel futuro, nessuna data prima del 1980), math check con tolleranza &plusmn;&euro;0.10 per gli arrotondamenti, e validazione IBAN con algoritmo MOD-97 standard internazionale. Il risultato finale combina la confidence del modello con gli esiti dell&rsquo;audit in un <code class="text-brand-tealLight">audit_status</code>: VALIDATED se tutto torna, PENDING_REVIEW se la confidence &egrave; media, NEEDS_REVIEW se l&rsquo;audit fallisce o la confidence &egrave; bassa.</p>

            <p>La separazione delle responsabilit&agrave; &egrave; fondamentale. Il modello fa ci&ograve; che i modelli sanno fare bene &mdash; leggere immagini complesse ed estrarre informazioni non strutturate. Il codice deterministico fa ci&ograve; che il codice sa fare bene &mdash; verificare regole precise, calcoli matematici, algoritmi di checksum. Il risultato &egrave; pi&ugrave; affidabile di un approccio che lascia fare tutto al modello, e pi&ugrave; flessibile di un approccio puramente basato su regole.</p>

            <h2 class="text-2xl font-black font-display text-white">Hardware utilizzato per il benchmark</h2>

            <p>Il benchmark &egrave; stato eseguito su un nodo RunPod con le seguenti specifiche. Queste sono le stesse condizioni che un ufficio o uno studio contabile potrebbe replicare su un server dedicato o su cloud a ore.</p>

        </div>

        <div class="overflow-x-auto my-8">
            <table class="w-full text-sm">
                <thead>
                    <tr class="border-b border-white/20 text-left">
                        <th class="pb-3 pr-4 text-white font-bold">Componente</th>
                        <th class="pb-3 text-white font-bold">Specifiche</th>
                    </tr>
                </thead>
                <tbody class="text-gray-400">
                    <tr class="border-b border-white/10"><td class="py-2.5 pr-4 text-white">GPU</td><td class="py-2.5">NVIDIA RTX 2000 Ada Generation &mdash; 16 GB VRAM GDDR6</td></tr>
                    <tr class="border-b border-white/10"><td class="py-2.5 pr-4 text-white">CPU</td><td class="py-2.5">Intel Xeon E-2386G &mdash; 6 core / 12 thread</td></tr>
                    <tr class="border-b border-white/10"><td class="py-2.5 pr-4 text-white">RAM</td><td class="py-2.5">46 GB DDR4</td></tr>
                    <tr class="border-b border-white/10"><td class="py-2.5 pr-4 text-white">Storage</td><td class="py-2.5">SSD NVMe 50 GB</td></tr>
                    <tr class="border-b border-white/10"><td class="py-2.5 pr-4 text-white">OS</td><td class="py-2.5">Ubuntu 22.04.3 LTS</td></tr>
                    <tr class="border-b border-white/10"><td class="py-2.5 pr-4 text-white">Modello AI</td><td class="py-2.5">Qwen2.5-VL 7B via Ollama 0.6.x</td></tr>
                    <tr class="border-b border-white/10"><td class="py-2.5 pr-4 text-white">Costo cloud</td><td class="py-2.5">$0.24/ora (RunPod Community Cloud)</td></tr>
                    <tr><td class="py-2.5 pr-4 text-white">Costo totale benchmark</td><td class="py-2.5">~$0.80 per 219 documenti (circa 3.3 ore totali)</td></tr>
                </tbody>
            </table>
        </div>

        <div class="prose prose-invert prose-lg max-w-none text-gray-300 leading-relaxed space-y-6">

            <h2 class="text-2xl font-black font-display text-white">Velocit&agrave; e costi: la matematica &egrave; semplice</h2>

            <p>Il sistema ha elaborato 219 documenti in circa 117 minuti di tempo di inferenza effettivo, per una media di <strong class="text-white">32 secondi a documento</strong>. Il costo totale di cloud computing per il benchmark intero &egrave; stato di circa $0.80 &mdash; meno di un caff&egrave; al bar.</p>

            <p>A $0.24/ora e 112.5 documenti/ora (32 secondi ciascuno), il costo per documento &egrave; <strong class="text-white">$0.002</strong>, ovvero un quinto di centesimo. Per avere un riferimento: i servizi cloud di estrazione documenti concorrenti &mdash; Amazon Textract, Azure Document Intelligence, Google Document AI &mdash; costano tra $0.015 e $0.065 per pagina, con abbonamenti minimi e costi di trasferimento dati aggiuntivi. DataUnchain in cloud costa tra 7 e 30 volte meno. In locale su hardware proprio, il costo scende ancora, avvicinandosi a zero per volume elevato.</p>

            <p>La velocit&agrave; varia per tipo di documento. Le fatture semplici (una pagina, layout standard) richiedono in media 28&ndash;31 secondi. I DDT con molte righe di merce arrivano a 32&ndash;35 secondi. I contratti multi-pagina richiedono circa 26 secondi perch&eacute; il prompt di estrazione &egrave; pi&ugrave; semplice (cerca solo le parti e le date di firma). Gli estratti conto con tabelle di movimenti dense sono i pi&ugrave; lenti, 48 secondi in media sui 7 elaborati correttamente, perch&eacute; il modello deve analizzare un numero elevato di righe strutturate e riconciliare i totali.</p>

            <h2 class="text-2xl font-black font-display text-white">I risultati: campo per campo</h2>

            <p>Il punteggio complessivo del 95.5% &egrave; una media pesata su tutti i campi e tutti i tipi documentali. Ma la media nasconde qualcosa di pi&ugrave; interessante: su 8 delle 10 metriche misurate, il sistema raggiunge il 100%. Le due eccezioni sono documentate con la causa precisa e il percorso di risoluzione.</p>

        </div>

        <div class="overflow-x-auto my-8">
            <div class="text-xs text-gray-500 uppercase tracking-wider mb-3 font-bold">Accuratezza campo per campo &mdash; 206 documenti con status OK</div>
            <table class="w-full text-sm">
                <thead>
                    <tr class="border-b border-white/20 text-left">
                        <th class="pb-3 pr-4 text-white font-bold">Campo</th>
                        <th class="pb-3 pr-4 text-right text-white font-bold">Accuratezza</th>
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
                        <td class="py-2.5 pr-4 text-gray-300">Imponibile (&plusmn;&euro;0.50)</td>
                        <td class="text-right pr-4"><span class="text-green-400 font-bold">100.0%</span></td>
                        <td class="text-gray-500 text-xs">94/94</td>
                    </tr>
                    <tr class="border-b border-white/10">
                        <td class="py-2.5 pr-4 text-gray-300">IVA (&plusmn;&euro;0.50)</td>
                        <td class="text-right pr-4"><span class="text-green-400 font-bold">100.0%</span></td>
                        <td class="text-gray-500 text-xs">94/94</td>
                    </tr>
                    <tr class="border-b border-white/10">
                        <td class="py-2.5 pr-4 text-gray-300">Totale fattura (&plusmn;&euro;0.50)</td>
                        <td class="text-right pr-4"><span class="text-green-400 font-bold">100.0%</span></td>
                        <td class="text-gray-500 text-xs">94/94</td>
                    </tr>
                    <tr class="border-b border-white/10">
                        <td class="py-2.5 pr-4 text-gray-300">Netto busta paga (&plusmn;&euro;0.50)</td>
                        <td class="text-right pr-4"><span class="text-green-400 font-bold">100.0%</span></td>
                        <td class="text-gray-500 text-xs">35/35</td>
                    </tr>
                    <tr class="border-b border-white/10">
                        <td class="py-2.5 pr-4 text-gray-300">Saldo finale estratto conto (&plusmn;&euro;0.50)</td>
                        <td class="text-right pr-4"><span class="text-green-400 font-bold">100.0%</span></td>
                        <td class="text-gray-500 text-xs">7/7</td>
                    </tr>
                    <tr class="border-b border-white/10">
                        <td class="py-2.5 pr-4 text-gray-300">Numero documento di riferimento</td>
                        <td class="text-right pr-4"><span class="text-green-400 font-bold">96.6%</span></td>
                        <td class="text-gray-500 text-xs">199/206</td>
                    </tr>
                    <tr class="border-b border-white/10">
                        <td class="py-2.5 pr-4 text-gray-300">Math check interno (&plusmn;&euro;0.10)</td>
                        <td class="text-right pr-4"><span class="text-green-400 font-bold">100.0%</span></td>
                        <td class="text-gray-500 text-xs">120/120</td>
                    </tr>
                    <tr>
                        <td class="py-2.5 pr-4 text-gray-300">Lordo busta paga (&plusmn;&euro;0.50)</td>
                        <td class="text-right pr-4"><span class="text-yellow-400 font-bold">54.3%</span></td>
                        <td class="text-gray-500 text-xs">19/35 &mdash; varianza etichette CCNL</td>
                    </tr>
                </tbody>
            </table>
        </div>

        <div class="rounded-2xl border border-brand-teal/30 bg-brand-teal/5 p-6 my-8">
            <div class="flex items-start gap-4">
                <div class="text-3xl mt-1">&#128302;</div>
                <div>
                    <div class="text-white font-bold text-lg mb-2">SCAN = CLEAN. Senza eccezioni.</div>
                    <p class="text-gray-400 text-sm leading-relaxed mb-4">Su ogni metrica misurata &mdash; P.IVA, importi, date, math check &mdash; i documenti scannerizzati (146 documenti con rumore, rotazione, timbri, artefatti JPEG) hanno performance identiche ai PDF nativi digitali (60 documenti). Zero degrado statisticamente rilevabile. Il modello &egrave; stato addestrato su immagini di documenti del mondo reale e gestisce la degradazione visiva come parte normale dell&rsquo;input.</p>
                    <div class="grid grid-cols-3 lg:grid-cols-5 gap-3">
                        <div class="text-center"><div class="text-green-400 font-bold">100%</div><div class="text-gray-500 text-xs">Classif. SCAN</div></div>
                        <div class="text-center"><div class="text-green-400 font-bold">100%</div><div class="text-gray-500 text-xs">Classif. CLEAN</div></div>
                        <div class="text-center"><div class="text-green-400 font-bold">100%</div><div class="text-gray-500 text-xs">P.IVA SCAN</div></div>
                        <div class="text-center"><div class="text-green-400 font-bold">100%</div><div class="text-gray-500 text-xs">P.IVA CLEAN</div></div>
                        <div class="text-center"><div class="text-green-400 font-bold">100%</div><div class="text-gray-500 text-xs">Math SCAN</div></div>
                    </div>
                </div>
            </div>
        </div>

        <div class="rounded-2xl bg-brand-surface border border-white/10 p-6 my-8">
            <div class="text-xs text-gray-500 uppercase tracking-wider mb-4 font-bold">Distribuzione confidence &mdash; 219 documenti</div>
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
            <p class="text-gray-500 text-xs mt-4">I 13 documenti LOW (tutti estratti conto con crash hardware) vengono instradati automaticamente alla revisione umana &mdash; non inseriti silenziosamente nel flusso dati. Il sistema sa quando non &egrave; sicuro di s&eacute; e lo segnala esplicitamente.</p>
        </div>

        <div class="prose prose-invert prose-lg max-w-none text-gray-300 leading-relaxed space-y-6">

            <h2 class="text-2xl font-black font-display text-white">Cosa succede dentro la GPU</h2>

            <p>Capire il profilo di utilizzo delle risorse &egrave; importante per due motivi: pianificare l&rsquo;hardware e capire dove si trovano i colli di bottiglia. I dati seguenti sono stati raccolti con <code class="text-brand-tealLight">nvidia-smi dmon</code> ogni 5 secondi per tutta la durata del benchmark.</p>

        </div>

        <div class="grid grid-cols-2 lg:grid-cols-3 gap-3 my-8">
            <div class="bg-brand-surface rounded-xl p-4 border border-white/10">
                <div class="text-brand-tealLight text-xs font-bold uppercase tracking-wider mb-2">GPU Utilization</div>
                <div class="text-2xl font-black text-white">87&ndash;100%</div>
                <div class="text-gray-500 text-xs mt-1">media ~94% durante inferenza</div>
            </div>
            <div class="bg-brand-surface rounded-xl p-4 border border-white/10">
                <div class="text-brand-tealLight text-xs font-bold uppercase tracking-wider mb-2">VRAM Usata</div>
                <div class="text-2xl font-black text-white">13.3 GB</div>
                <div class="text-gray-500 text-xs mt-1">su 16 GB &mdash; 2.6 GB di margine</div>
            </div>
            <div class="bg-brand-surface rounded-xl p-4 border border-white/10">
                <div class="text-brand-tealLight text-xs font-bold uppercase tracking-wider mb-2">Power Draw</div>
                <div class="text-2xl font-black text-white">~68 W</div>
                <div class="text-gray-500 text-xs mt-1">vicino al TDP &mdash; 6 W in idle</div>
            </div>
            <div class="bg-brand-surface rounded-xl p-4 border border-white/10">
                <div class="text-brand-tealLight text-xs font-bold uppercase tracking-wider mb-2">CPU Load</div>
                <div class="text-2xl font-black text-white">~4%</div>
                <div class="text-gray-500 text-xs mt-1">pipeline 100% GPU-bound</div>
            </div>
            <div class="bg-brand-surface rounded-xl p-4 border border-white/10">
                <div class="text-brand-tealLight text-xs font-bold uppercase tracking-wider mb-2">Temperatura GPU</div>
                <div class="text-2xl font-black text-white">65&ndash;70&deg;C</div>
                <div class="text-gray-500 text-xs mt-1">26&deg;C in idle</div>
            </div>
            <div class="bg-brand-surface rounded-xl p-4 border border-white/10">
                <div class="text-brand-tealLight text-xs font-bold uppercase tracking-wider mb-2">RAM Sistema</div>
                <div class="text-2xl font-black text-white">~35 GB</div>
                <div class="text-gray-500 text-xs mt-1">OS + Ollama + buffer immagini</div>
            </div>
        </div>

        <div class="prose prose-invert prose-lg max-w-none text-gray-300 leading-relaxed space-y-6">

            <p><strong class="text-white">La pipeline &egrave; 100% GPU-bound.</strong> La CPU al 4% di utilizzo medio significa che il processore sta sostanzialmente aspettando la GPU a ogni inferenza. Aggiungere core CPU pi&ugrave; veloci, pi&ugrave; RAM di sistema, o un SSD pi&ugrave; veloce non cambia nulla alla velocit&agrave; di elaborazione. Solo la GPU conta. Questo semplifica enormemente la pianificazione hardware: non serve un server enterprise con molti core. Basta una GPU potente, qualsiasi CPU moderna, 32 GB di RAM e un SSD ragionevole.</p>

            <p>Il margine di VRAM &egrave; di 2.6 GB su 16 GB &mdash; abbastanza per la maggior parte dei documenti, ma stretto per i casi pi&ugrave; complessi. Su hardware con 24 GB di VRAM, il margine diventa confortevole e tutti i tipi documentali, inclusi gli estratti conto pi&ugrave; densi, risultano stabili.</p>

            <h2 class="text-2xl font-black font-display text-white">Limiti identificati &mdash; trasparenza totale</h2>

            <p>Documentare i limiti &egrave; importante quanto documentare i successi. Chi costruisce sistemi in produzione ha bisogno di sapere esattamente dove un sistema pu&ograve; fallire &mdash; non per evitare il sistema, ma per pianificare attorno ai casi limite con strategie specifiche.</p>

        </div>

        <div class="rounded-2xl border border-yellow-500/30 bg-yellow-500/5 p-6 my-6">
            <div class="flex items-start gap-3">
                <div class="text-2xl">&#9888;&#65039;</div>
                <div>
                    <div class="text-yellow-400 font-bold mb-2">Limite 1 &mdash; Crash GGML sugli estratti conto (13/20 documenti)</div>
                    <p class="text-gray-400 text-sm leading-relaxed mb-3">Gli estratti conto con tabelle di movimenti dense (15 o pi&ugrave; righe per pagina) producono un crash interno nel backend GGML di Ollama: <code class="text-yellow-300 bg-black/30 px-1 rounded">GGML_ASSERT(a-&gt;ne[2] * 4 == b-&gt;ne[0]) failed</code>. Il processo restituisce HTTP 500 e il documento finisce in coda NEEDS_REVIEW.</p>
                    <p class="text-gray-400 text-sm leading-relaxed mb-3">La classificazione funziona sempre correttamente &mdash; il crash avviene solo nello step di estrazione. La causa &egrave; la combinazione di un&rsquo;immagine ad alta risoluzione con molti dettagli visivi (la tabella dei movimenti) pi&ugrave; un prompt di estrazione lungo, che insieme superano un limite dimensionale dei tensori nel modello 7B su 16 GB VRAM. Non &egrave; un bug del codice &mdash; &egrave; un limite fisico dell&rsquo;hardware attuale. I 7 estratti conto elaborati correttamente (con meno righe di movimenti) ottengono il 100% su tutti i campi incluso il saldo finale.</p>
                    <div class="flex flex-wrap gap-2 mt-3">
                        <span class="bg-black/30 text-brand-tealLight text-xs px-3 py-1 rounded-full font-bold">Fix v2.1: ridurre DPI per tabelle dense (200 &rarr; 150)</span>
                        <span class="bg-black/30 text-brand-tealLight text-xs px-3 py-1 rounded-full font-bold">Alternativa: Qwen2.5-VL 14B su GPU 24GB+</span>
                    </div>
                </div>
            </div>
        </div>

        <div class="rounded-2xl border border-yellow-500/30 bg-yellow-500/5 p-6 my-6">
            <div class="flex items-start gap-3">
                <div class="text-2xl">&#9888;&#65039;</div>
                <div>
                    <div class="text-yellow-400 font-bold mb-2">Limite 2 &mdash; Lordo busta paga: 54.3%</div>
                    <p class="text-gray-400 text-sm leading-relaxed mb-3">Il netto viene estratto al 100% su tutte le 35 buste paga &mdash; l&rsquo;etichetta &ldquo;NETTO IN BUSTA&rdquo; &egrave; standardizzata nella quasi totalit&agrave; dei software paghe italiani. Il lordo invece raggiunge solo il 54.3% perch&eacute; le buste paga italiane utilizzano etichette diverse a seconda del CCNL e del software gestionale: lo stesso campo appare come &ldquo;RETRIBUZIONE LORDA&rdquo;, &ldquo;IMPONIBILE LORDO&rdquo;, &ldquo;TOTALE COMPETENZE&rdquo;, &ldquo;IMPONIBILE CONTRIBUTIVO PREVIDENZIALE&rdquo;, o varianti regionali, a seconda che si usi Zucchetti, TeamSystem, Wolters Kluwer, o un gestionale verticale.</p>
                    <p class="text-gray-400 text-sm leading-relaxed mb-3">Importante: il <em>numero</em> viene sempre letto correttamente quando il campo viene trovato. Il problema &egrave; esclusivamente nel riconoscimento dell&rsquo;etichetta giusta. Aggiungere una lista esplicita di tutte le varianti di etichetta nel prompt di estrazione delle buste paga dovrebbe portare il campo sopra il 90% in v2.1.</p>
                    <div class="flex flex-wrap gap-2 mt-3">
                        <span class="bg-black/30 text-brand-tealLight text-xs px-3 py-1 rounded-full font-bold">Fix v2.1: lista etichette CCNL nel prompt</span>
                        <span class="bg-black/30 text-brand-tealLight text-xs px-3 py-1 rounded-full font-bold">Target: &gt;90% su tutti i CCNL</span>
                    </div>
                </div>
            </div>
        </div>

        <div class="prose prose-invert prose-lg max-w-none text-gray-300 leading-relaxed space-y-6">

            <h2 class="text-2xl font-black font-display text-white">$0.002 a documento: cosa significa davvero</h2>

            <p>Il numero &egrave; impressionante ma astratto. Rendiamolo concreto con tre scenari reali che coprono quasi tutte le PMI italiane.</p>

        </div>

        <div class="space-y-4 my-8">
            <div class="rounded-2xl bg-brand-surface border border-white/10 p-5">
                <div class="flex items-center justify-between mb-3">
                    <div class="text-white font-bold">Piccola impresa &mdash; 100 fatture/mese</div>
                    <div class="text-brand-tealLight font-black text-lg">$0.20/mese</div>
                </div>
                <div class="text-gray-400 text-sm">Elaborazione cloud a $0.002/doc. Confronto: 2&ndash;4 ore di inserimento manuale a &euro;18&ndash;22/ora = &euro;36&ndash;88/mese. <span class="text-green-400 font-bold">DataUnchain &egrave; 180&ndash;440 volte pi&ugrave; economico</span> del data entry umano.</div>
            </div>
            <div class="rounded-2xl bg-brand-surface border border-white/10 p-5">
                <div class="flex items-center justify-between mb-3">
                    <div class="text-white font-bold">Media impresa &mdash; 2.000 documenti/mese</div>
                    <div class="text-brand-tealLight font-black text-lg">$4/mese</div>
                </div>
                <div class="text-gray-400 text-sm">Sostituisce 1&ndash;2 ore di lavoro giornaliero di un operatore dedicato al data entry. Competitor SaaS per estrazione documenti: &euro;200&ndash;2.000/mese. <span class="text-green-400 font-bold">ROI immediato nel primo mese.</span></div>
            </div>
            <div class="rounded-2xl bg-brand-surface border border-white/10 p-5">
                <div class="flex items-center justify-between mb-3">
                    <div class="text-white font-bold">On-premise con RTX 3090</div>
                    <div class="text-brand-tealLight font-black text-lg">&lt;$0.001/doc</div>
                </div>
                <div class="text-gray-400 text-sm">RTX 3090 24 GB usata &sim;&euro;900. Ammortizzata in 3 anni a 4 ore di utilizzo al giorno: hardware pi&ugrave; energia scende sotto $0.001 per documento. <span class="text-green-400 font-bold">Payback in settimane a volumi medi. Costo marginale vicino a zero.</span></div>
            </div>
        </div>

        <div class="prose prose-invert prose-lg max-w-none text-gray-300 leading-relaxed space-y-6">

            <h2 class="text-2xl font-black font-display text-white">Cosa significa &ldquo;completamente offline&rdquo; per la tua azienda</h2>

            <p>L&rsquo;operativit&agrave; offline non &egrave; un&rsquo;opzione aggiuntiva o un claim marketing &mdash; &egrave; una scelta architetturale con conseguenze concrete e verificabili sulla sicurezza, sulla conformit&agrave; e sui costi.</p>

            <p><strong class="text-white">Nessun dato lascia la tua infrastruttura.</strong> I PDF vengono convertiti in immagini in locale. Il modello Qwen2.5-VL viene eseguito localmente tramite Ollama. Il JSON strutturato viene scritto nel database PostgreSQL locale. Non un singolo byte dei tuoi documenti aziendali arriva ai server di Anthropic, OpenAI, Microsoft Azure, Google Cloud, o qualsiasi altro fornitore cloud. La fattura del tuo cliente pi&ugrave; importante, la busta paga del tuo dipendente, il contratto riservato: niente di tutto questo lascia il tuo perimetro.</p>

            <p><strong class="text-white">GDPR concreto, non teorico.</strong> Quando i dati non escono mai dal tuo edificio, decadono automaticamente una serie di obblighi: non serve valutare il trasferimento internazionale verso i server USA dei provider cloud, non servono DPA (Data Processing Agreements) con l&rsquo;AI provider, non &egrave; necessario notificare il data breach a un processore esterno perch&eacute; il processore esterno non esiste. Il DPO del tuo cliente pu&ograve; verificare il perimetro del trattamento senza eccezioni da spiegare.</p>

            <p><strong class="text-white">Air-gap ready.</strong> Una volta scaricato il modello (5 GB, operazione one-time con connessione internet), il sistema funziona indefinitamente senza connessione. Reti di produzione industriale isolate, archivi legali in ambienti sicuri, reti ospedaliere, strutture governative con classificazione &mdash; tutti questi ambienti possono eseguire DataUnchain senza modifiche architetturali.</p>

            <p><strong class="text-white">Zero abbonamenti e zero costi variabili.</strong> Nessun costo per token. Nessun piano tariffario da monitorare. Nessuna sorpresa in fattura a fine mese perch&eacute; un batch di documenti era pi&ugrave; grande del previsto. Il costo ricorrente &egrave; solo l&rsquo;hardware e l&rsquo;energia, con una prevedibilit&agrave; totale che nessun servizio cloud pu&ograve; offrire.</p>

            <h2 class="text-2xl font-black font-display text-white">Perch&eacute; Qwen2.5-VL e non un&rsquo;altra alternativa</h2>

            <p>Qwen2.5-VL &egrave; il risultato del programma di ricerca di Alibaba sui modelli vision-language. La versione 7B &egrave; il punto ottimale del rapporto qualit&agrave;/dimensione per l&rsquo;estrazione di documenti: abbastanza piccola da girare comodamente su 16 GB VRAM, abbastanza capace da capire layout complessi, tabelle, numeri scritti a mano e caratteri con font insoliti.</p>

            <p>Tre caratteristiche tecniche la rendono particolarmente adatta ai documenti aziendali italiani. Prima: <strong class="text-white">visione nativa senza OCR</strong>. Il modello non fa OCR separato e poi legge il testo &mdash; vede l&rsquo;immagine direttamente come un essere umano. Questo significa che capisce il contesto visivo: sa che un numero in alto a destra in una fattura italiana &egrave; probabilmente il numero fattura, non il codice prodotto. Secondo: <strong class="text-white">comprensione dello spatial layout</strong>. Una tabella con colonne non perfettamente allineate, un campo che continua sulla riga successiva, una nota scritta in verticale a margine &mdash; il modello li gestisce senza regole esplicite perch&eacute; ha visto milioni di documenti reali durante il pre-addestramento. Terzo: <strong class="text-white">resistenza alla degradazione visiva</strong> dimostrata empiricamente da questo benchmark: SCAN = CLEAN su ogni metrica.</p>

            <p>Per confronto: i sistemi OCR tradizionali (Tesseract, AWS Textract in modalit&agrave; OCR) raggiungono tipicamente il 70&ndash;85% di accuratezza su documenti scannerizzati di qualit&agrave; media, richiedono post-processing per correggere errori di riconoscimento caratteri, e crollano completamente su scrittura a mano, layout non standard, e documenti con artefatti di stampa. I modelli basati su template funzionano bene per i formati che conoscono e falliscono completamente su qualsiasi variazione non prevista.</p>

            <h2 class="text-2xl font-black font-display text-white">Guida hardware: cosa ti serve davvero</h2>

            <p>La regola pi&ugrave; importante da tenere a mente: <strong class="text-white">investi in GPU, non in CPU</strong>. La pipeline &egrave; al 94% di utilizzo GPU e al 4% di utilizzo CPU. Un sistema con RTX 3090 e Core i5 batter&agrave; sempre un sistema con RTX 2000 Ada e Core i9 per l&rsquo;elaborazione di documenti.</p>

        </div>

        <div class="space-y-3 my-8">
            <div class="rounded-xl border border-white/10 bg-brand-surface p-4">
                <div class="flex flex-wrap items-center justify-between gap-2 mb-2">
                    <div class="text-white font-bold">RTX 2000 Ada / RTX 3080 &mdash; 16 GB VRAM</div>
                    <span class="bg-yellow-500/20 text-yellow-400 text-xs font-bold px-3 py-1 rounded-full">Minimo funzionante</span>
                </div>
                <p class="text-gray-400 text-sm">Funziona per la maggior parte dei tipi documentali. Il margine VRAM &egrave; 2.6 GB &mdash; stretto per i documenti pi&ugrave; complessi. Gli estratti conto con tabelle dense crashano (vedi Limite 1). Consigliato se non si elaborano estratti conto regolarmente, o come workaround temporaneo con DPI ridotto.</p>
            </div>
            <div class="rounded-xl border border-brand-teal/40 bg-brand-teal/5 p-4">
                <div class="flex flex-wrap items-center justify-between gap-2 mb-2">
                    <div class="text-white font-bold">RTX 3090 / RTX 4090 &mdash; 24 GB VRAM</div>
                    <span class="bg-brand-teal/20 text-brand-tealLight text-xs font-bold px-3 py-1 rounded-full">&#11088; Consigliato</span>
                </div>
                <p class="text-gray-400 text-sm">Tutti i tipi documentali stabili senza workaround. Stimato ~20 secondi a documento (velocit&agrave; 1.6&times; rispetto al benchmark). Miglior rapporto qualit&agrave;/prezzo per uso produzione. RTX 3090 usata ~&euro;900, RTX 4090 nuova ~&euro;1.800. Consigliato per installazioni on-premise in uffici e studi professionali.</p>
            </div>
            <div class="rounded-xl border border-white/10 bg-brand-surface p-4">
                <div class="flex flex-wrap items-center justify-between gap-2 mb-2">
                    <div class="text-white font-bold">A5000 / A6000 &mdash; 24&ndash;48 GB VRAM</div>
                    <span class="bg-purple-500/20 text-purple-400 text-xs font-bold px-3 py-1 rounded-full">Enterprise</span>
                </div>
                <p class="text-gray-400 text-sm">Memoria ECC con codifica degli errori, garanzia professionale, form factor server rack. Supporta Qwen2.5-VL 32B per accuratezza ulteriormente elevata. Per installazioni data center, studi legali con archivi di migliaia di documenti al mese, o integrazione in sistemi ERP enterprise.</p>
            </div>
            <div class="rounded-xl border border-white/10 bg-brand-surface p-4">
                <div class="flex flex-wrap items-center justify-between gap-2 mb-2">
                    <div class="text-white font-bold">A100 / H100 &mdash; 40&ndash;80 GB VRAM</div>
                    <span class="bg-blue-500/20 text-blue-400 text-xs font-bold px-3 py-1 rounded-full">Alto Volume</span>
                </div>
                <p class="text-gray-400 text-sm">Per volumi superiori a 50.000 documenti al mese. Supporta elaborazione parallela multi-richiesta o Qwen2.5-VL 72B. Throughput stimato 3&ndash;5 documenti al secondo con batching. Classe data center.</p>
            </div>
        </div>

        <div class="rounded-2xl bg-brand-surface border border-white/10 p-5 my-6 text-sm text-gray-400">
            <strong class="text-white">Importante:</strong> la CPU &egrave; irrilevante per le performance di elaborazione. La GPU era al 94% di utilizzo medio per tutta la durata del benchmark &mdash; la CPU al 4%. Una RTX 3090 + Core i5 da &euro;200 batte una RTX 2000 Ada + Core i9 da &euro;600 ogni volta. Investi in GPU, non in CPU. Per la RAM: 32 GB sono sufficienti, 64 GB sono comodi per macchine che fanno anche altro oltre all&rsquo;elaborazione documenti.
        </div>

        <div class="prose prose-invert prose-lg max-w-none text-gray-300 leading-relaxed space-y-6">

            <h2 class="text-2xl font-black font-display text-white">Riepilogo per tipo di documento</h2>

            <p>Ogni tipo documentale ha caratteristiche diverse che influenzano la velocit&agrave; di elaborazione e i campi disponibili per la valutazione. La tabella seguente riepiloga tutti i risultati per tipo.</p>

        </div>

        <div class="overflow-x-auto my-8">
            <table class="w-full text-sm">
                <thead>
                    <tr class="border-b border-white/20 text-left">
                        <th class="pb-3 pr-3 text-white font-bold">Tipo</th>
                        <th class="pb-3 pr-3 text-right text-white font-bold">n</th>
                        <th class="pb-3 pr-3 text-right text-white font-bold">Classif.</th>
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
                        <td class="py-2.5 pr-3 text-white">Ordine di Acquisto</td>
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
                        <td class="text-right pr-3">7 &#9733;</td>
                        <td class="text-right pr-3 text-green-400">100%</td>
                        <td class="text-right pr-3 text-green-400">100%</td>
                        <td class="text-right pr-3 text-green-400">100%</td>
                        <td class="text-right pr-3 text-green-400">100%</td>
                        <td class="text-right">48s</td>
                    </tr>
                </tbody>
            </table>
            <p class="text-gray-600 text-xs mt-2">&#9733; 13/20 estratti conto: crash GGML (limite hardware, vedi sopra). I 7 elaborati correttamente: 100% su tutti i campi incluso il saldo finale.</p>
        </div>

        <div class="prose prose-invert prose-lg max-w-none text-gray-300 leading-relaxed space-y-6">

            <h2 class="text-2xl font-black font-display text-white">Metodologia del benchmark</h2>

            <p>Ogni risultato pubblicato qui &egrave; prodotto da una pipeline completamente automatizzata, senza nessun intervento manuale nella fase di valutazione. Il processo di valutazione si articola in quattro fasi: generazione dei documenti con seed fisso; elaborazione tramite il processor v2.0 di DataUnchain; confronto campo per campo automatico contro la ground truth; aggregazione nel report finale.</p>

            <p>I campi numerici vengono valutati con una tolleranza di &plusmn;&euro;0.50. I campi data richiedono corrispondenza esatta in formato ISO 8601 (AAAA-MM-GG). I campi stringa (P.IVA, Codice Fiscale, riferimenti documento) richiedono corrispondenza esatta. La classificazione &egrave; valutata come corretta o errata senza punteggio parziale.</p>

            <p>Se vuoi verificare questi risultati sul tuo parco documentale specifico nell&rsquo;ambito di un proof-of-concept, <a href="/it/contatti/" class="text-brand-tealLight hover:underline">contattaci</a> &mdash; conduciamo pilot strutturati con i potenziali clienti sui loro documenti reali, sotto NDA, sulla loro infrastruttura.</p>

        </div>

        <div class="prose prose-invert prose-lg max-w-none text-gray-300 leading-relaxed space-y-6">

            <h2 class="text-2xl font-black font-display text-white">Cosa stiamo migliorando nella prossima versione</h2>

            <p>Questo benchmark ha identificato quattro aree di miglioramento specifiche per la versione 2.1 del processor, tutte con un path di implementazione chiaro.</p>

            <p><strong class="text-white">Fix busta paga lordo:</strong> Il prompt di estrazione delle buste paga verr&agrave; aggiornato con la lista completa delle etichette usate dai principali software paghe italiani (Zucchetti, TeamSystem, Wolters Kluwer HR, Paghe GB). Stimato: portare il campo lordo da 54% a &gt;90%.</p>

            <p><strong class="text-white">DPI adattivo per estratti conto:</strong> Prima della chiamata al modello, il processor conter&agrave; le righe visibili nell&rsquo;area tabellare dell&rsquo;immagine. Se superano la soglia di 12 righe, riduce automaticamente il DPI da 200 a 150 per rientrare nei limiti tensoriali del 7B. Stimato: portare gli estratti conto da 35% a &gt;85% su 16 GB VRAM.</p>

            <p><strong class="text-white">Benchmark v3 con 10 tipi documentali:</strong> La prossima iterazione del benchmark includer&agrave; ricevute fiscali, packing list internazionali, preventivi commerciali. Target: 300 documenti su 10 tipi con lo stesso livello di rigore della ground truth matematicamente verificata.</p>

            <p><strong class="text-white">Confronto con i competitor cloud:</strong> Stiamo preparando il benchmark comparativo con Amazon Textract, Azure Document Intelligence e Google Document AI sullo stesso corpus di 219 documenti. I risultati saranno pubblicati con la stessa trasparenza di questo documento.</p>

            <h2 class="text-2xl font-black font-display text-white">Il punto finale</h2>

            <p>95.5% di accuratezza. $0.002 a documento. 32 secondi. Zero cloud. Zero dati che escono dalla tua infrastruttura.</p>

            <p>Sui campi che contano di pi&ugrave; per l&rsquo;automazione documentale aziendale italiana &mdash; P.IVA, Codice Fiscale, date, importi, coerenza aritmetica interna &mdash; il sistema raggiunge il <strong class="text-white">100% su ognuno di essi</strong>. I documenti scannerizzati degradati performano identicamente ai PDF nativi. Il sistema conosce i propri limiti e li segnala invece di inserire silenziosamente dati errati nel flusso informativo aziendale.</p>

            <p>Un campo sotto il 90%: la busta paga lordo al 54%, causa identificata, fix in sviluppo per v2.1. Un pattern di crash hardware: gli estratti conto su 16 GB VRAM, causa identificata, due percorsi di risoluzione documentati. Tutto il resto: cento per cento.</p>

            <p>95.5% di accuratezza su un corpus di 219 documenti aziendali italiani reali, con il 100% sui campi che contano di pi&ugrave; per l&rsquo;automazione: P.IVA, Codice Fiscale, date, importi, coerenza aritmetica. Questa &egrave; la differenza tra un prodotto che ti promette un numero e uno che ti mostra come ci &egrave; arrivato &mdash; con metodo, dati e trasparenza completa sulla metodologia.</p>

        </div>

        <div class="mt-12 rounded-2xl p-8 text-center" style="background: linear-gradient(135deg, rgba(13,148,136,0.15) 0%, rgba(16,185,129,0.10) 100%); border: 1px solid rgba(13,148,136,0.3);">
            <div class="text-2xl font-black text-white mb-2">Vuoi testarlo sui tuoi documenti?</div>
            <p class="text-gray-400 mb-6">Conduciamo pilot strutturati con fatture, buste paga e contratti della tua organizzazione &mdash; sotto NDA, sulla tua infrastruttura.</p>
            <div class="flex flex-wrap justify-center gap-3">
                <a href="/it/contatti/" class="bg-brand-teal text-white font-bold px-6 py-3 rounded-xl hover:bg-brand-teal/80 transition-colors">Richiedi un Pilot &rarr;</a>
                <a href="/it/docs/" class="bg-white/10 text-white font-bold px-6 py-3 rounded-xl hover:bg-white/20 transition-colors">Leggi la Documentazione</a>
            </div>
        </div>

        <div class="mt-10 pt-8 border-t border-white/10 text-center">
            <a href="/it/blog/" class="text-brand-tealLight font-bold hover:underline">&larr; Torna al Blog</a>
        </div>

    </div>
</article>
