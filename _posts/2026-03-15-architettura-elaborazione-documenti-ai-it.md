---
layout: default
title: "Architettura di un Sistema di Elaborazione Documenti con AI: Guida Tecnica"
lang: it
categories: blog
date: 2026-03-15
description: "Architettura tecnica completa di un sistema AI per l'elaborazione documenti: diagrammi, schema database, layer di validazione, integrazione ERP. Con esempi di codice."
author: Antonio Trento
---

<article class="pt-36 pb-20 px-6">
  <div class="max-w-3xl mx-auto">
    <div class="mb-8">
      <span class="text-brand-tealLight text-xs font-bold uppercase tracking-widest">Blog · 15 Marzo 2026</span>
      <h1 class="text-4xl lg:text-5xl font-black font-display mt-4 mb-6">Architettura di un Sistema di Elaborazione Documenti con AI: Guida Tecnica</h1>
      <p class="text-gray-400 text-lg leading-relaxed">Come è fatto internamente un sistema di elaborazione documenti con AI? Questa guida tecnica spiega l'architettura layer per layer, con diagrammi, schema del database, e le decisioni di design che fanno la differenza in produzione.</p>
    </div>

    <div class="prose prose-invert prose-lg max-w-none text-gray-300 leading-relaxed space-y-6">

      <h2 class="text-2xl font-black font-display text-white">Vista d'insieme: i servizi del sistema</h2>

      <pre class="bg-gray-900 border border-white/10 rounded-xl p-6 text-sm text-gray-300 overflow-x-auto"><code>┌──────────────────────────────────────────────────────────────┐
│                    DOCKER COMPOSE STACK                      │
│                                                              │
│  ┌──────────────┐  ┌──────────────┐  ┌────────────────────┐ │
│  │  telegram-   │  │    email-    │  │   API REST         │ │
│  │  bot         │  │    monitor   │  │   FastAPI :8000    │ │
│  └──────┬───────┘  └──────┬───────┘  └─────────┬──────────┘ │
│         │                 │                     │            │
│         └────────────────┬┘                     │            │
│                          │                      │            │
│              ┌───────────▼──────────────────────▼──────────┐ │
│              │          PROCESSOR                          │ │
│              │   Classificazione + Estrazione AI           │ │
│              │   Validazione + Confidence Score            │ │
│              └───────────────────────┬──────────────────────┘ │
│                                      │                      │
│              ┌───────────────────────▼──────────────────────┐ │
│              │          OUTPUT ROUTER                      │ │
│              │   Dead-letter queue + Retry logic           │ │
│              │   18 adapter: Webhook/CRM/ERP/Gestionale    │ │
│              └──────────────────────────────────────────────┘ │
│                                                              │
│  ┌──────────────────┐  ┌──────────────────────────────────┐ │
│  │  Ollama          │  │  Dashboard Streamlit :8501        │ │
│  │  LLM server      │  │  Monitoring + Impostazioni       │ │
│  │  GPU accelerated │  │  Revisione documenti             │ │
│  └──────────────────┘  └──────────────────────────────────┘ │
│                                                              │
│  Volume persistente: /data/                                  │
│  SQLite DB + archivio PDF + results JSON + config           │
└──────────────────────────────────────────────────────────────┘</code></pre>

      <h2 class="text-2xl font-black font-display text-white">Schema del database</h2>
      <p>Il database SQLite contiene lo storico di ogni documento elaborato. Le tabelle principali:</p>

      <pre class="bg-gray-900 border border-white/10 rounded-xl p-6 text-sm text-gray-300 overflow-x-auto"><code>CREATE TABLE documents (
  id            INTEGER PRIMARY KEY AUTOINCREMENT,
  file_name     TEXT NOT NULL,
  file_hash     TEXT UNIQUE,           -- SHA256 per deduplicazione
  file_path     TEXT,                  -- Percorso nell'archivio
  source        TEXT,                  -- 'telegram' | 'email' | 'api'
  received_at   DATETIME DEFAULT CURRENT_TIMESTAMP,
  processed_at  DATETIME,
  status        TEXT DEFAULT 'pending', -- 'pending' | 'processing' | 'done' | 'error'

  -- Risultati estrazione
  tipo_documento TEXT,                 -- 'fattura' | 'ddt' | 'ordine' | ...
  result_path    TEXT,                 -- Percorso al JSON con tutti i campi estratti
  confidence     INTEGER,              -- 0-100
  audit_status   TEXT,                 -- 'VALIDATED' | 'NEEDS_REVIEW' | 'ERROR'

  -- Math check
  math_ok        BOOLEAN,
  math_delta     REAL,

  -- Revisione umana
  reviewed_by    TEXT,
  reviewed_at    DATETIME,
  review_notes   TEXT,

  -- Dispatch adapter
  dispatched_adapters  TEXT,           -- JSON array: ['webhook', 'zucchetti']
  dispatch_errors      TEXT            -- JSON: {'sap_b1': 'Connection timeout'}
);</code></pre>

      <h2 class="text-2xl font-black font-display text-white">Il Processor: cuore del sistema</h2>
      <p>Il processor è il servizio che trasforma il documento grezzo in dati strutturati. Le sue responsabilità:</p>

      <div class="space-y-4">
        <div class="bg-gray-900/60 border border-white/10 rounded-lg p-5">
          <h3 class="text-white font-bold mb-2">Step 1: Preprocessing del documento</h3>
          <p class="text-gray-400 text-sm">Il PDF viene convertito in immagini PNG con pdf2image (DPI configurabile, default 200). Per ogni pagina, il sistema applica: deskewing automatico, normalizzazione del contrasto, riduzione del rumore. Le immagini vengono codificate in base64 per l'invio al modello VLM.</p>
        </div>
        <div class="bg-gray-900/60 border border-white/10 rounded-lg p-5">
          <h3 class="text-white font-bold mb-2">Step 2: Classificazione tipo documento</h3>
          <p class="text-gray-400 text-sm">Il VLM riceve la prima pagina e un prompt di classificazione. Risponde con il tipo documento: 'fattura', 'ddt', 'ordine_acquisto', 'nota_credito', 'contratto', 'altro'. Questa classificazione determina lo schema di estrazione da usare nel passo successivo.</p>
        </div>
        <div class="bg-gray-900/60 border border-white/10 rounded-lg p-5">
          <h3 class="text-white font-bold mb-2">Step 3: Estrazione strutturata</h3>
          <p class="text-gray-400 text-sm">Il VLM riceve tutte le pagine del documento e un prompt specifico per il tipo documento. Il prompt descrive esattamente i campi da estrarre e il formato JSON richiesto. Il modello risponde con il JSON strutturato.</p>
        </div>
        <div class="bg-gray-900/60 border border-white/10 rounded-lg p-5">
          <h3 class="text-white font-bold mb-2">Step 4: Validazione</h3>
          <p class="text-gray-400 text-sm">Math check: verifica che imponibile + IVA = totale con tolleranza configurabile. Validazione formato P.IVA (11 cifre + checksum), CF, IBAN, date (ISO 8601). Calcolo confidence score (0-100) basato su completezza campi e risultato validazioni.</p>
        </div>
        <div class="bg-gray-900/60 border border-white/10 rounded-lg p-5">
          <h3 class="text-white font-bold mb-2">Step 5: Audit status</h3>
          <p class="text-gray-400 text-sm">VALIDATED: confidence ≥ 85 e math check OK → pronto per dispatch automatico. NEEDS_REVIEW: confidence 60-84 o math check fallito → entra in coda revisione umana. ERROR: confidence &lt; 60 o campi obbligatori mancanti → richiede intervento manuale.</p>
        </div>
      </div>

      <h2 class="text-2xl font-black font-display text-white">Il Router e la dead-letter queue</h2>
      <p>Il router riceve il risultato validato dal processor e lo invia agli adapter configurati. Il pattern architetturale fondamentale è la <strong class="text-white">dead-letter queue</strong>:</p>

      <pre class="bg-gray-900 border border-white/10 rounded-xl p-6 text-sm text-gray-300 overflow-x-auto"><code>┌─────────────────────────────────────────────────┐
│  ROUTER: _safe_dispatch()                        │
│                                                  │
│  Per ogni adapter configurato:                   │
│    try:                                          │
│      adapter.dispatch(result)  ───→ ✅ Successo  │
│    except Exception as e:                        │
│      → salva in failed_dispatches.jsonl          │
│      → continua con il prossimo adapter          │
│                                                  │
│  Failed dispatches:                              │
│    {                                             │
│      "doc_id": 1234,                             │
│      "adapter": "sap_b1",                        │
│      "error": "Connection timeout",              │
│      "timestamp": "2026-03-15T10:30:00Z",        │
│      "payload": {...}                            │
│    }                                             │
│                                                  │
│  Retry: manuale via dashboard o API              │
│  Auto-retry: configurabile ogni N minuti         │
└─────────────────────────────────────────────────┘</code></pre>

      <p>Questo pattern garantisce che un adapter fallito non blocchi gli altri. Se SAP B1 è irraggiungibile, il documento viene comunque inviato a Salesforce, all'email e al webhook. Solo il dispatch SAP B1 finisce nella dead-letter queue per il retry successivo.</p>

      <h2 class="text-2xl font-black font-display text-white">Decisioni di design critiche</h2>

      <div class="space-y-6">
        <div>
          <h3 class="text-xl font-bold text-white mb-2">Perché SQLite invece di PostgreSQL?</h3>
          <p class="text-gray-400">SQLite è sufficiente per volumi PMI (&lt;50.000 documenti/anno) e azzera la complessità operativa. Nessun servizio database separato da mantenere. Il file .db è copiabile direttamente per i backup. Per volumi enterprise (&gt;500.000 documenti/anno), la migrazione a PostgreSQL è prevista ma non necessaria per il 95% dei casi.</p>
        </div>
        <div>
          <h3 class="text-xl font-bold text-white mb-2">Perché Ollama come LLM server?</h3>
          <p class="text-gray-400">Ollama gestisce il lifecycle del modello (download, versioning, serving con GPU), espone un'API REST compatibile con OpenAI, gestisce la VRAM e il batching. Alternative valutate: llama.cpp diretto (meno funzionale), vLLM (ottimo ma più complesso per singolo modello), LocalAI (più versatile ma overhead maggiore).</p>
        </div>
        <div>
          <h3 class="text-xl font-bold text-white mb-2">Perché Docker Compose invece di Kubernetes?</h3>
          <p class="text-gray-400">Kubernetes è sovradimensionato per un'installazione single-node in una PMI. Docker Compose offre orchestrazione sufficiente, deploy in &lt;30 minuti, familiarità diffusa, update senza downtime con restart dei singoli container. Kubernetes ha senso solo per deployment multi-nodo o cloud managed (EKS, GKE).</p>
        </div>
        <div>
          <h3 class="text-xl font-bold text-white mb-2">Perché JSON per i risultati invece di colonne DB?</h3>
          <p class="text-gray-400">Lo schema di estrazione è diverso per ogni tipo documento (fattura vs DDT vs contratto). Salvare tutto in JSON permette di aggiungere nuovi tipi documento e nuovi campi senza migrazioni dello schema del database. Solo i metadati (confidence, status, tipo) sono in colonne DB per permettere query efficienti.</p>
        </div>
      </div>

      <h2 class="text-2xl font-black font-display text-white">Il layer di integrazione: 18 adapter</h2>
      <p>Ogni adapter implementa una sola interfaccia: riceve il payload JSON del documento e lo invia al sistema target. Gli adapter sono indipendenti: fallire in uno non blocca gli altri.</p>

      <div class="overflow-x-auto">
        <table class="w-full text-sm border-collapse">
          <thead>
            <tr class="border-b border-white/20">
              <th class="text-left py-3 px-4 text-white font-bold">Categoria</th>
              <th class="text-left py-3 px-4 text-white font-bold">Adapter</th>
              <th class="text-left py-3 px-4 text-white font-bold">Protocollo</th>
            </tr>
          </thead>
          <tbody class="text-gray-400">
            <tr class="border-b border-white/10"><td class="py-3 px-4" rowspan="4">Output generico</td><td class="py-3 px-4">Webhook</td><td class="py-3 px-4">HTTP POST JSON</td></tr>
            <tr class="border-b border-white/10"><td class="py-3 px-4">CSV/Excel</td><td class="py-3 px-4">File append</td></tr>
            <tr class="border-b border-white/10"><td class="py-3 px-4">Email</td><td class="py-3 px-4">SMTP</td></tr>
            <tr class="border-b border-white/10"><td class="py-3 px-4">Google Sheets</td><td class="py-3 px-4">Sheets API v4</td></tr>
            <tr class="border-b border-white/10"><td class="py-3 px-4" rowspan="2">Fatturazione IT</td><td class="py-3 px-4">FatturaPA XML</td><td class="py-3 px-4">Generazione XML SDI</td></tr>
            <tr class="border-b border-white/10"><td class="py-3 px-4">Fatture in Cloud</td><td class="py-3 px-4">REST API</td></tr>
            <tr class="border-b border-white/10"><td class="py-3 px-4" rowspan="3">CRM</td><td class="py-3 px-4">Salesforce</td><td class="py-3 px-4">REST API + OAuth2</td></tr>
            <tr class="border-b border-white/10"><td class="py-3 px-4">HubSpot</td><td class="py-3 px-4">REST API Private App</td></tr>
            <tr class="border-b border-white/10"><td class="py-3 px-4">Odoo</td><td class="py-3 px-4">XML-RPC</td></tr>
            <tr class="border-b border-white/10"><td class="py-3 px-4" rowspan="3">Gestionali IT</td><td class="py-3 px-4">Zucchetti</td><td class="py-3 px-4">REST / CSV</td></tr>
            <tr class="border-b border-white/10"><td class="py-3 px-4">TeamSystem</td><td class="py-3 px-4">Digital Hub API</td></tr>
            <tr class="border-b border-white/10"><td class="py-3 px-4">Mexal</td><td class="py-3 px-4">Tracciato ASCII</td></tr>
            <tr class="border-b border-white/10"><td class="py-3 px-4" rowspan="2">Enterprise</td><td class="py-3 px-4">Microsoft 365</td><td class="py-3 px-4">Graph API + OAuth2</td></tr>
            <tr class="border-b border-white/10"><td class="py-3 px-4">SAP Business One</td><td class="py-3 px-4">Service Layer REST</td></tr>
          </tbody>
        </table>
      </div>

      <h2 class="text-2xl font-black font-display text-white">Monitoring e metriche chiave</h2>
      <p>Le metriche da monitorare in produzione:</p>
      <ul class="space-y-2 text-gray-400">
        <li>📊 <strong class="text-white">Throughput:</strong> Documenti elaborati/ora. Alert se cala &gt;20% rispetto alla baseline.</li>
        <li>🎯 <strong class="text-white">Tasso revisione manuale:</strong> % documenti con audit_status = NEEDS_REVIEW. Obiettivo &lt;10%. Aumenti anomali segnalano problemi di qualità dei documenti in input.</li>
        <li>❌ <strong class="text-white">Dead-letter queue size:</strong> Numero di dispatch in errore in attesa di retry. Alert se supera 50.</li>
        <li>⏱️ <strong class="text-white">Latenza elaborazione:</strong> Tempo medio dal ricevimento al completamento. Aumenti indicano problemi GPU o Ollama.</li>
        <li>📈 <strong class="text-white">Confidence score medio:</strong> Tendenza nel tempo. Calo progressivo può indicare drift nei tipi di documento.</li>
      </ul>

    </div>

    <div class="mt-12 pt-8 border-t border-white/10 text-center">
      <p class="text-gray-400 mb-4">Questa è l'architettura che alimenta DataUnchain. Open source, deployabile in 30 minuti.</p>
      <a href="/it/" class="inline-block bg-brand-teal text-white font-bold px-8 py-3 rounded-xl hover:bg-brand-tealLight transition-colors">Esplora DataUnchain →</a>
    </div>
  </div>
</article>
