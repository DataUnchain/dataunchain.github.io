---
layout: default
title: "Guida Completa all'Acquisizione Documenti con AI: Architettura, Strumenti e Workflow"
lang: it
categories: blog
date: 2026-03-15
description: "Tutto quello che devi sapere sull'acquisizione documenti con AI: architettura a 5 layer, strumenti, validazione, integrazione con ERP e CRM. Guida tecnica completa."
author: Antonio Trento
---

<article class="pt-36 pb-20 px-6">
  <div class="max-w-3xl mx-auto">
    <div class="mb-8">
      <span class="text-brand-tealLight text-xs font-bold uppercase tracking-widest">Blog · 15 Marzo 2026</span>
      <h1 class="text-4xl lg:text-5xl font-black font-display mt-4 mb-6">Guida Completa all'Acquisizione Documenti con AI: Architettura, Strumenti e Workflow</h1>
      <p class="text-gray-400 text-lg leading-relaxed">Ogni giorno le aziende italiane ricevono migliaia di fatture, DDT, ordini d'acquisto e contratti. La maggior parte di questi documenti viene ancora elaborata manualmente. Questa guida spiega come costruire un sistema di acquisizione documenti con AI che funziona davvero in produzione.</p>
    </div>

    <div class="prose prose-invert prose-lg max-w-none text-gray-300 leading-relaxed space-y-6">

      <h2 class="text-2xl font-black font-display text-white">Cos'è l'acquisizione documenti con AI?</h2>
      <p>L'acquisizione documenti con AI (<em>AI Document Ingestion</em>) è il processo automatizzato che legge un documento aziendale grezzo — PDF, scansione, immagine, email con allegato — e lo trasforma in dati strutturati pronti per essere inviati al gestionale, al CRM o al database aziendale.</p>
      <p>Il risultato finale non è una trascrizione del testo: è un oggetto JSON con tutti i campi estratti, validati e verificati. Per una fattura di acquisto, significa avere:</p>
      <ul class="space-y-2 text-gray-400">
        <li>🏢 <strong class="text-white">Fornitore:</strong> Ragione sociale, P.IVA, indirizzo, codice SDI</li>
        <li>📋 <strong class="text-white">Documento:</strong> Numero fattura, data, scadenza, condizioni di pagamento</li>
        <li>💰 <strong class="text-white">Importi:</strong> Imponibile, aliquote IVA (22%, 10%, 4%), totale lordo, ritenuta d'acconto</li>
        <li>📦 <strong class="text-white">Righe dettaglio:</strong> Descrizione, quantità, prezzo unitario, aliquota, totale riga</li>
      </ul>

      <div class="bg-brand-teal/10 border border-brand-teal/30 rounded-xl p-6 my-8">
        <p class="text-brand-tealLight font-bold text-sm uppercase tracking-wider mb-2">💡 Perché non basta l'OCR</p>
        <p class="text-gray-300 text-sm">Un sistema OCR tradizionale estrae il testo dal documento ma non lo <em>capisce</em>. Non sa che "150,00" è l'imponibile e non il totale. Non sa che "IV22" è l'aliquota IVA al 22%. I Vision Language Model invece leggono il documento come lo leggerebbe un contabile — comprendendo struttura, contesto e significato dei campi.</p>
      </div>

      <h2 class="text-2xl font-black font-display text-white">L'architettura a 5 layer</h2>
      <p>Un sistema di acquisizione documenti con AI ben progettato è composto da 5 layer distinti, ognuno con una responsabilità specifica:</p>

      <pre class="bg-gray-900 border border-white/10 rounded-xl p-6 text-sm text-gray-300 overflow-x-auto"><code>┌─────────────────────────────────────────────┐
│  LAYER 1 — ACQUISIZIONE                     │
│  Email / Telegram / API upload / Cartella   │
└────────────────────┬────────────────────────┘
                     │
┌────────────────────▼────────────────────────┐
│  LAYER 2 — PREPROCESSING                    │
│  Conversione PDF → immagini (DPI 200-300)   │
│  Rotazione, denoising, normalizzazione      │
└────────────────────┬────────────────────────┘
                     │
┌────────────────────▼────────────────────────┐
│  LAYER 3 — ESTRAZIONE AI (Vision LLM)       │
│  Qwen 2.5-VL / LLaMA 3.2-Vision / Mistral  │
│  Output: JSON strutturato con tutti i campi │
└────────────────────┬────────────────────────┘
                     │
┌────────────────────▼────────────────────────┐
│  LAYER 4 — VALIDAZIONE                      │
│  Math check (imponibile + IVA = totale)     │
│  Formato P.IVA, CF, IBAN, date             │
│  Confidence score, audit status             │
└────────────────────┬────────────────────────┘
                     │
┌────────────────────▼────────────────────────┐
│  LAYER 5 — INTEGRAZIONE                     │
│  Webhook / CSV / Email / FatturaPA          │
│  Salesforce / HubSpot / SAP B1 / Odoo      │
│  Zucchetti / TeamSystem / Mexal            │
└─────────────────────────────────────────────┘</code></pre>

      <h2 class="text-2xl font-black font-display text-white">Layer 1: Acquisizione documenti</h2>
      <p>Il primo layer gestisce come i documenti entrano nel sistema. Le modalità principali sono:</p>
      <ul class="space-y-3 text-gray-400">
        <li><strong class="text-white">Email monitor:</strong> Il sistema monitora una casella email dedicata (es. <code>fatture@azienda.it</code>). Quando arriva un'email con allegato PDF, lo estrae automaticamente e lo mette in coda per l'elaborazione. Supporta IMAP con autenticazione OAuth2 o App Password.</li>
        <li><strong class="text-white">Bot Telegram:</strong> L'operatore invia il documento via Telegram — foto, PDF o file. Il bot lo riceve e lo invia al processor. Utile per contesti mobili o chi lavora in magazzino.</li>
        <li><strong class="text-white">API REST:</strong> Un sistema esterno (ERP, portale fornitori) fa una POST a <code>/extract</code> con il file. Ideale per integrazioni enterprise.</li>
        <li><strong class="text-white">Cartella watchdog:</strong> Un processo monitora una cartella locale o di rete. Quando arriva un file nuovo, lo elabora automaticamente. Compatibile con scanner di rete aziendali.</li>
      </ul>

      <h2 class="text-2xl font-black font-display text-white">Layer 2: Preprocessing</h2>
      <p>Questa fase prepara il documento per l'AI. Il preprocessing è spesso sottovalutato, ma è critico per l'accuratezza del sistema:</p>
      <ul class="space-y-3 text-gray-400">
        <li><strong class="text-white">PDF nativo → immagini:</strong> I PDF vengono convertiti in immagini ad alta risoluzione (200-300 DPI) con <code>pdf2image</code> + Poppler. Ogni pagina diventa un'immagine PNG.</li>
        <li><strong class="text-white">Immagini già acquisite:</strong> Se il documento è già un'immagine (foto di fattura, scansione), viene processata direttamente.</li>
        <li><strong class="text-white">Normalizzazione:</strong> Correzione rotazione (deskewing), rimozione rumore di fondo, ottimizzazione contrasto per scansioni di bassa qualità.</li>
        <li><strong class="text-white">Multi-pagina:</strong> Ogni pagina viene elaborata separatamente, poi i risultati vengono consolidati. Fondamentale per fatture con allegati o DDT multi-pagina.</li>
      </ul>

      <h2 class="text-2xl font-black font-display text-white">Layer 3: Estrazione AI con Vision LLM</h2>
      <p>Il cuore del sistema. Un Vision Language Model riceve l'immagine del documento e un prompt strutturato, e restituisce un JSON con tutti i campi estratti.</p>
      <p>I modelli più usati per documenti italiani nel 2026:</p>

      <div class="overflow-x-auto">
        <table class="w-full text-sm border-collapse">
          <thead>
            <tr class="border-b border-white/20">
              <th class="text-left py-3 px-4 text-white font-bold">Modello</th>
              <th class="text-left py-3 px-4 text-white font-bold">Parametri</th>
              <th class="text-left py-3 px-4 text-white font-bold">Accuratezza fatture IT</th>
              <th class="text-left py-3 px-4 text-white font-bold">VRAM richiesta</th>
              <th class="text-left py-3 px-4 text-white font-bold">Velocità</th>
            </tr>
          </thead>
          <tbody class="text-gray-400">
            <tr class="border-b border-white/10">
              <td class="py-3 px-4 font-mono">Qwen 2.5-VL 7B</td>
              <td class="py-3 px-4">7B</td>
              <td class="py-3 px-4 text-green-400">94-96%</td>
              <td class="py-3 px-4">8 GB</td>
              <td class="py-3 px-4">~8s/doc</td>
            </tr>
            <tr class="border-b border-white/10">
              <td class="py-3 px-4 font-mono">Qwen 2.5-VL 72B</td>
              <td class="py-3 px-4">72B</td>
              <td class="py-3 px-4 text-green-400">97-98%</td>
              <td class="py-3 px-4">48 GB</td>
              <td class="py-3 px-4">~25s/doc</td>
            </tr>
            <tr class="border-b border-white/10">
              <td class="py-3 px-4 font-mono">LLaMA 3.2-Vision 11B</td>
              <td class="py-3 px-4">11B</td>
              <td class="py-3 px-4 text-yellow-400">91-93%</td>
              <td class="py-3 px-4">12 GB</td>
              <td class="py-3 px-4">~12s/doc</td>
            </tr>
            <tr class="border-b border-white/10">
              <td class="py-3 px-4 font-mono">Mistral Pixtral 12B</td>
              <td class="py-3 px-4">12B</td>
              <td class="py-3 px-4 text-yellow-400">90-92%</td>
              <td class="py-3 px-4">14 GB</td>
              <td class="py-3 px-4">~15s/doc</td>
            </tr>
          </tbody>
        </table>
      </div>

      <p>Per la maggior parte delle PMI italiane, <strong class="text-white">Qwen 2.5-VL 7B</strong> è il punto di equilibrio ottimale: alta accuratezza, gira su una GPU RTX 4080 da €800, produce risultati in ~8 secondi per documento.</p>

      <h2 class="text-2xl font-black font-display text-white">Layer 4: Validazione e confidence scoring</h2>
      <p>L'AI può sbagliare. Un sistema robusto non si fida ciecamente dell'output dell'AI, ma lo verifica con regole deterministiche:</p>

      <ul class="space-y-4 text-gray-400">
        <li>
          <strong class="text-white">Math check:</strong> Verifica che <code>imponibile + IVA = totale</code> con tolleranza configurabile (default ±0.10€). Se il controllo fallisce, il documento va in revisione manuale. Questo è il controllo più importante: un errore nel totale significa un pagamento sbagliato.
        </li>
        <li>
          <strong class="text-white">Validazione P.IVA:</strong> Controlla il formato (11 cifre, prefisso IT opzionale) e la checksum dell'ultimo carattere. Una P.IVA mal estratta blocca la registrazione in contabilità.
        </li>
        <li>
          <strong class="text-white">Validazione Codice Fiscale:</strong> 16 caratteri alfanumerici con algoritmo di checksum. Importante per note spese, compensi professionisti, CU.
        </li>
        <li>
          <strong class="text-white">Confidence score:</strong> Punteggio da 0 a 100 basato su: completezza dei campi estratti, risultato math check, validazione formati. Documenti con score &lt; 70 vengono automaticamente inviati in revisione manuale.
        </li>
      </ul>

      <div class="bg-yellow-900/20 border border-yellow-500/30 rounded-xl p-6 my-8">
        <p class="text-yellow-400 font-bold text-sm uppercase tracking-wider mb-2">⚠️ Attenzione: revisione umana non è opzionale</p>
        <p class="text-gray-300 text-sm">Un sistema di acquisizione documenti non dovrebbe essere "fully automatic" fin dall'inizio. La revisione umana per i casi dubbi è una feature, non una limitazione. In DataUnchain, ogni documento con confidence &lt; 70 o math check fallito entra in una coda di revisione con un'interfaccia dedicata per l'operatore.</p>
      </div>

      <h2 class="text-2xl font-black font-display text-white">Layer 5: Integrazione con sistemi aziendali</h2>
      <p>Il dato estratto deve arrivare nel sistema che lo utilizzerà. Le destinazioni tipiche per le aziende italiane:</p>

      <div class="overflow-x-auto">
        <table class="w-full text-sm border-collapse">
          <thead>
            <tr class="border-b border-white/20">
              <th class="text-left py-3 px-4 text-white font-bold">Sistema</th>
              <th class="text-left py-3 px-4 text-white font-bold">Tipo integrazione</th>
              <th class="text-left py-3 px-4 text-white font-bold">Caso d'uso principale</th>
            </tr>
          </thead>
          <tbody class="text-gray-400">
            <tr class="border-b border-white/10"><td class="py-3 px-4">Zucchetti</td><td class="py-3 px-4">REST API / CSV</td><td class="py-3 px-4">Contabilità, ciclo passivo</td></tr>
            <tr class="border-b border-white/10"><td class="py-3 px-4">TeamSystem</td><td class="py-3 px-4">Digital Hub API</td><td class="py-3 px-4">Contabilità PMI</td></tr>
            <tr class="border-b border-white/10"><td class="py-3 px-4">Mexal</td><td class="py-3 px-4">Tracciato ASCII</td><td class="py-3 px-4">Import fatture</td></tr>
            <tr class="border-b border-white/10"><td class="py-3 px-4">SAP Business One</td><td class="py-3 px-4">Service Layer REST</td><td class="py-3 px-4">ERP enterprise</td></tr>
            <tr class="border-b border-white/10"><td class="py-3 px-4">Salesforce</td><td class="py-3 px-4">REST API OAuth2</td><td class="py-3 px-4">CRM, record Account</td></tr>
            <tr class="border-b border-white/10"><td class="py-3 px-4">HubSpot</td><td class="py-3 px-4">Private App API</td><td class="py-3 px-4">CRM, Deal/Company</td></tr>
            <tr class="border-b border-white/10"><td class="py-3 px-4">Odoo</td><td class="py-3 px-4">XML-RPC</td><td class="py-3 px-4">ERP open source</td></tr>
            <tr class="border-b border-white/10"><td class="py-3 px-4">FatturaPA XML</td><td class="py-3 px-4">XML generazione</td><td class="py-3 px-4">Fatturazione elettronica SDI</td></tr>
          </tbody>
        </table>
      </div>

      <h2 class="text-2xl font-black font-display text-white">Tipi di documenti supportati</h2>
      <p>Un sistema di acquisizione documenti aziendale deve gestire molti più tipi di documenti rispetto alle sole fatture:</p>
      <ul class="space-y-2 text-gray-400">
        <li><strong class="text-white">Fattura di acquisto:</strong> Il caso più comune. Fornitore, importi, aliquote IVA, condizioni di pagamento.</li>
        <li><strong class="text-white">Documento di Trasporto (DDT):</strong> Mittente, destinatario, righe articoli, quantità, peso. Fondamentale per la logistica.</li>
        <li><strong class="text-white">Ordine di acquisto:</strong> Estratto e confrontato con la fattura ricevuta per il three-way matching.</li>
        <li><strong class="text-white">Nota di credito:</strong> Riconoscimento automatico (importi negativi, causale resa).</li>
        <li><strong class="text-white">Bolla doganale / CMR:</strong> Per import/export, dati dogana e trasportatore.</li>
        <li><strong class="text-white">Preventivo / Offerta:</strong> Estrazione condizioni commerciali, validità, righe prodotto.</li>
        <li><strong class="text-white">Contratto:</strong> Parti contraenti, durata, valore, clausole chiave, date di rinnovo.</li>
        <li><strong class="text-white">Nota spese:</strong> Dipendente, data, categoria spesa, importo, IVA, ricevuta allegata.</li>
      </ul>

      <h2 class="text-2xl font-black font-display text-white">Implementazione: guida in 7 fasi</h2>
      <p>Ecco come implementare un sistema di acquisizione documenti in produzione:</p>

      <div class="space-y-4">
        <div class="bg-gray-900/60 border border-white/10 rounded-lg p-5">
          <div class="flex items-center gap-3 mb-2">
            <span class="text-brand-tealLight font-black text-lg">01</span>
            <h3 class="text-white font-bold">Inventario documenti</h3>
          </div>
          <p class="text-gray-400 text-sm">Identifica i 3-5 tipi di documento con il volume più alto. Per la maggior parte delle PMI italiane: fatture passive, DDT in entrata, ordini fornitori. Misura il tempo medio di elaborazione manuale e calcola il potenziale di risparmio.</p>
        </div>
        <div class="bg-gray-900/60 border border-white/10 rounded-lg p-5">
          <div class="flex items-center gap-3 mb-2">
            <span class="text-brand-tealLight font-black text-lg">02</span>
            <h3 class="text-white font-bold">Dataset di test</h3>
          </div>
          <p class="text-gray-400 text-sm">Raccogli 50-100 documenti reali per tipo (anonimizzati). Questi serviranno per valutare l'accuratezza del sistema prima di andare in produzione. Includere almeno 10-15 casi "difficili": scansioni di bassa qualità, layout inusuali, più pagine.</p>
        </div>
        <div class="bg-gray-900/60 border border-white/10 rounded-lg p-5">
          <div class="flex items-center gap-3 mb-2">
            <span class="text-brand-tealLight font-black text-lg">03</span>
            <h3 class="text-white font-bold">Deploy infrastruttura</h3>
          </div>
          <p class="text-gray-400 text-sm">Server con GPU (RTX 4080 16GB per Qwen 7B), Docker + Ollama per il modello AI, Docker per il sistema DataUnchain. Per ambienti cloud-privato: VM AWS/Azure con GPU instance.</p>
        </div>
        <div class="bg-gray-900/60 border border-white/10 rounded-lg p-5">
          <div class="flex items-center gap-3 mb-2">
            <span class="text-brand-tealLight font-black text-lg">04</span>
            <h3 class="text-white font-bold">Configurazione canali di input</h3>
          </div>
          <p class="text-gray-400 text-sm">Scegli il canale principale: casella email dedicata (più semplice), bot Telegram (più immediato), API (più flessibile). Configura le credenziali e testa con 10-20 documenti reali.</p>
        </div>
        <div class="bg-gray-900/60 border border-white/10 rounded-lg p-5">
          <div class="flex items-center gap-3 mb-2">
            <span class="text-brand-tealLight font-black text-lg">05</span>
            <h3 class="text-white font-bold">Validazione accuratezza</h3>
          </div>
          <p class="text-gray-400 text-sm">Elabora il dataset di test e verifica l'accuratezza campo per campo. Obiettivo: &gt;95% sui campi critici (totale, P.IVA, numero fattura). Ottimizza il prompt se necessario per i tipi di documento più problematici.</p>
        </div>
        <div class="bg-gray-900/60 border border-white/10 rounded-lg p-5">
          <div class="flex items-center gap-3 mb-2">
            <span class="text-brand-tealLight font-black text-lg">06</span>
            <h3 class="text-white font-bold">Integrazione gestionale</h3>
          </div>
          <p class="text-gray-400 text-sm">Configura il connettore verso il tuo gestionale o CRM. Testa prima in ambiente di staging. Verifica che i dati arrivino nei campi corretti e che la contabilità riconosca i documenti importati.</p>
        </div>
        <div class="bg-gray-900/60 border border-white/10 rounded-lg p-5">
          <div class="flex items-center gap-3 mb-2">
            <span class="text-brand-tealLight font-black text-lg">07</span>
            <h3 class="text-white font-bold">Go-live graduale</h3>
          </div>
          <p class="text-gray-400 text-sm">Inizia con un volume ridotto (20-30% dei documenti). Monitora il tasso di revisione manuale. Aumenta gradualmente fino al 100%. Obiettivo: meno del 10% dei documenti in revisione manuale dopo il primo mese.</p>
        </div>
      </div>

      <h2 class="text-2xl font-black font-display text-white">Performance e ROI atteso</h2>
      <p>Benchmark reali su documenti italiani con Qwen 2.5-VL 7B (RTX 4080):</p>
      <ul class="space-y-2 text-gray-400">
        <li>⏱️ <strong class="text-white">Tempo medio elaborazione:</strong> 8-12 secondi per documento (PDF nativo), 15-20 secondi (scansione)</li>
        <li>🎯 <strong class="text-white">Accuratezza fatture digitali:</strong> 96-98% sui campi principali</li>
        <li>🎯 <strong class="text-white">Accuratezza scansioni:</strong> 91-94% (dipende dalla qualità della scansione)</li>
        <li>👤 <strong class="text-white">Tasso revisione manuale:</strong> 5-10% nel regime normale</li>
        <li>💰 <strong class="text-white">ROI tipico PMI (500 doc/mese):</strong> Break-even in 4-6 mesi, risparmio netto &gt;€15.000/anno</li>
      </ul>

      <div class="bg-brand-teal/10 border border-brand-teal/30 rounded-xl p-6 my-8">
        <p class="text-brand-tealLight font-bold text-sm uppercase tracking-wider mb-2">📊 Calcolo risparmio esempio</p>
        <p class="text-gray-300 text-sm mb-3">Azienda con 800 fatture/mese. Tempo elaborazione manuale: 8 minuti/fattura. Costo orario operatore: €25/h.</p>
        <p class="text-gray-300 text-sm"><strong class="text-white">Costo attuale:</strong> 800 × 8 min × €25/60 = €2.667/mese (€32.000/anno)</p>
        <p class="text-gray-300 text-sm"><strong class="text-white">Con AI (10% revisione manuale):</strong> 80 × 8 min × €25/60 = €267/mese (€3.200/anno)</p>
        <p class="text-green-400 text-sm font-bold mt-2">Risparmio netto: ~€28.800/anno</p>
      </div>

      <h2 class="text-2xl font-black font-display text-white">Privacy e conformità GDPR</h2>
      <p>Le fatture e i DDT contengono dati personali e aziendali sensibili. Un sistema di acquisizione documenti deve rispettare il GDPR:</p>
      <ul class="space-y-3 text-gray-400">
        <li><strong class="text-white">Elaborazione in locale:</strong> Se il modello AI gira on-premise, nessun dato esce dall'azienda. Zero trasferimento verso cloud di terzi.</li>
        <li><strong class="text-white">Retention policy:</strong> I documenti originali devono essere conservati per 10 anni (Codice Civile art. 2220). Il sistema deve supportare questa policy.</li>
        <li><strong class="text-white">Accesso ai dati:</strong> Solo il personale autorizzato deve accedere alla dashboard e ai documenti. Autenticazione obbligatoria.</li>
        <li><strong class="text-white">Data minimization:</strong> Estrarre solo i campi necessari. Non salvare il contenuto completo del documento se non richiesto dalla normativa.</li>
      </ul>

      <h2 class="text-2xl font-black font-display text-white">Domande frequenti</h2>

      <details class="border border-white/10 rounded-lg p-4">
        <summary class="text-white font-bold cursor-pointer">L'AI può gestire fatture di fornitori esteri (in lingua diversa dall'italiano)?</summary>
        <p class="text-gray-400 mt-3 text-sm">Sì. I Vision Language Model moderni gestiscono nativamente più lingue. Qwen 2.5-VL 7B è particolarmente forte su documenti in inglese, tedesco, francese e spagnolo oltre all'italiano. Per lingue più rare o formati molto diversi (caratteri cinesi, arabi), l'accuratezza può scendere al 85-90%.</p>
      </details>

      <details class="border border-white/10 rounded-lg p-4 mt-3">
        <summary class="text-white font-bold cursor-pointer">Come si gestisce il DDT con righe molto numerose (50+ righe)?</summary>
        <p class="text-gray-400 mt-3 text-sm">Per documenti multi-pagina con molte righe, il sistema elabora ogni pagina separatamente e consolida i risultati. L'AI estrae le righe come array JSON. Per DDT con 50+ righe su 3-4 pagine, l'elaborazione richiede 30-60 secondi ma produce un risultato completo e preciso.</p>
      </details>

      <details class="border border-white/10 rounded-lg p-4 mt-3">
        <summary class="text-white font-bold cursor-pointer">Il sistema funziona anche con scansioni di qualità bassa (vecchi scanner)?</summary>
        <p class="text-gray-400 mt-3 text-sm">Dipende dalla qualità. Documenti con risoluzione &gt;150 DPI e testo leggibile funzionano bene. Scansioni molto sbiadite, con rumore intenso o testo parzialmente illegibile hanno accuratezza più bassa (80-88%). In questi casi, il sistema assegna automaticamente un confidence score basso e invia il documento in revisione manuale.</p>
      </details>

      <details class="border border-white/10 rounded-lg p-4 mt-3">
        <summary class="text-white font-bold cursor-pointer">Quante GPU servono per elaborare 5.000 documenti al giorno?</summary>
        <p class="text-gray-400 mt-3 text-sm">Con Qwen 7B su RTX 4080: ~8s/documento. 5.000 doc/giorno = 5.000 × 8s = 40.000 secondi = ~11 ore. Una singola GPU riesce a gestire questo volume elaborando in sequenza durante le ore lavorative. Per picchi più alti, è possibile parallelizzare su 2-3 GPU o usare il modello in parallelo con batch processing.</p>
      </details>

    </div>

    <div class="mt-12 pt-8 border-t border-white/10 text-center">
      <p class="text-gray-400 mb-4">Vuoi implementare l'acquisizione documenti con AI nella tua azienda?</p>
      <a href="/it/" class="inline-block bg-brand-teal text-white font-bold px-8 py-3 rounded-xl hover:bg-brand-tealLight transition-colors">Scopri DataUnchain →</a>
    </div>
  </div>
</article>
