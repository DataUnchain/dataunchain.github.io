# Roadmap inserimento animazione pipeline — DataUnchain

> File di riferimento: `assets/animations/pipeline-animation-v2.svg`
> Data analisi: 2026-04-04

L'animazione mostra il flusso core del prodotto: **documento grezzo → AI on-premise → dati strutturati nel gestionale**.
Di seguito tutte le pagine del sito analizzate con priorità di inserimento, posizione suggerita e note.

---

## Priorità ALTA — Inserire subito

### 1. `it/index.html` + `en/index.html` — Homepage
**Posizione:** Sezione hero o immediatamente dopo, sopra la fold  
**Perché:** È la prima cosa che vede un visitatore. L'animazione comunica il prodotto in 5 secondi senza bisogno di leggere. Sostituisce o affianca il testo descrittivo.  
**Come:** Colonna destra nel layout hero (testo a sinistra, animazione a destra), oppure sezione dedicata "Come funziona in 3 passi" subito sotto l'hero.  
**Note:** Verificare che non rallenti il LCP (Largest Contentful Paint) — caricare l'SVG inline o con `<object>` lazy.

---

### 2. `it/early-access.html` + `en/early-access.html` — Pagina Early Adopter
**Posizione:** Sezione "Come funziona" (dopo il video demo, prima de "Il Problema")  
**Perché:** Il video demo mostra il prodotto reale. L'animazione può fare da "sintesi visiva" del processo prima che l'utente guardi il video intero. Aumenta la comprensione del valore prima della CTA.  
**Come:** Sezione autonoma `<section>` con titolo "La pipeline in sintesi" + animazione centrata full-width.  
**Note:** Il video Plyr è già presente — l'animazione deve stare prima o dopo, non competere visivamente.

---

### 3. `it/how-it-works.html` + `en/how-it-works.html` — Come Funziona
**Posizione:** Hero della pagina, sopra i dettagli tecnici delle fasi  
**Perché:** Questa è la pagina dove l'utente vuole capire il processo. L'animazione è la risposta visiva perfetta prima di entrare nei dettagli.  
**Come:** Hero con animazione a piena larghezza + titolo "Il flusso end-to-end" + poi le sezioni di dettaglio delle fasi.  
**Priorità:** Alta — è la pagina più adatta concettualmente.

---

## Priorità MEDIA — Valutare

### 4. `it/features.html` + `en/features.html` — Features
**Posizione:** Intro della pagina, prima dell'elenco delle feature  
**Perché:** L'animazione funge da "overview" prima che l'utente entri nelle singole funzionalità. Contestualizza le feature nel flusso reale.  
**Come:** Sezione intro con animazione + breve paragrafo, poi le card delle feature.  
**Note:** Non indispensabile se la pagina ha già visual chiari per ogni feature.

---

### 5. `it/why-dataunchain.html` + `en/why-dataunchain.html` — Perché DataUnchain
**Posizione:** Dopo l'introduzione, prima dei punti di differenziazione  
**Perché:** Rinforza il messaggio "nessun dato esce dalla rete" visivamente. Il badge "Nessun dato ha lasciato la tua rete" in fondo all'animazione è perfettamente allineato con il pitch di questa pagina.  
**Come:** Sezione "La differenza in un colpo d'occhio" con animazione centrata.  
**Note:** Utile soprattutto per visitatori che arrivano da ricerche su privacy/GDPR/on-premise.

---

### 6. `it/vlm-vs-ocr.html` + `en/vlm-vs-ocr.html` — VLM vs OCR
**Posizione:** Metà pagina, dopo la spiegazione di cosa è un VLM  
**Perché:** Il nodo centrale dell'animazione (icona "occhio"/vision) visualizza bene il concetto di Vision Language Model vs OCR tradizionale.  
**Come:** Sezione "Come vede il documento la nostra AI" + animazione + didascalia esplicativa.  
**Note:** Potrebbe richiedere una variante dell'animazione più focalizzata sul nodo AI (zoom sul centro).

---

### 7. `it/integrazioni-erp.html` + `en/erp-integrations.html` — Integrazioni ERP
**Posizione:** Hero o sezione introduttiva  
**Perché:** La parte destra dell'animazione mostra già TeamSystem, Zucchetti, SAP, Odoo. È il visual giusto per questa pagina.  
**Come:** Animazione con focus sulla parte destra (output → ERP), poi elenco completo dei connettori.  
**Note:** Potrebbe valere la pena creare una variante con più connettori ERP visibili a destra.

---

### 8. `it/architettura-privacy.html` + `en/architecture-privacy.html` — Architettura & Privacy
**Posizione:** Dopo l'intro sulla privacy, come schema visivo dell'architettura  
**Perché:** Il flusso "dati che non escono mai dalla rete" è il cuore di questa pagina. L'animazione e il badge finale lo comunicano perfettamente.  
**Come:** Sezione "Lo schema dell'architettura" con animazione + nota sul badge "Nessun dato ha lasciato la tua rete".  
**Note:** In questa pagina l'animazione ha più valore didattico che commerciale.

---

## Priorità BASSA — Non urgente

### 9. `it/pricing.html` + `en/pricing.html` — Pricing
**Posizione:** Sopra le tabelle prezzi, come reminder del valore  
**Perché:** Prima di vedere i prezzi, l'utente dovrebbe ricordarsi cosa sta comprando.  
**Come:** Mini-sezione "Cosa ottieni" con animazione ridotta (max 600px di larghezza) + poi pricing.  
**Note:** Rischio di allungare troppo la pagina. Valutare solo se il conversion rate è basso.

---

### 10. `it/use-cases.html` + `en/use-cases.html` — Use Cases
**Posizione:** Intro della pagina  
**Perché:** Contestualizza i casi d'uso nel flusso generale prima di entrare nei dettagli settoriali.  
**Come:** Sezione intro con animazione.  
**Note:** Meno urgente — i casi d'uso hanno già visual dedicati per settore.

---

## Pagine dove NON inserire

| Pagina | Motivo |
|---|---|
| `it/blog/` + `en/blog/` | Articoli — l'animazione distrarrebbe dalla lettura |
| `it/chi-siamo.html` + `en/about-us.html` | Pagina istituzionale — focus su team e storia, non sul prodotto |
| `it/roadmap.html` + `en/roadmap.html` | Roadmap — contenuto testuale/tabellare, l'animazione non aggiunge valore |
| `privacy/`, `terms/`, `dpa/` | Pagine legali — fuori contesto |
| `it/docs.html` + `en/docs.html` | Documentazione tecnica — gli utenti cercano informazioni specifiche |
| `it/document-ai-glossary.html` + `en/document-ai-glossary.html` | Glossario — contenuto enciclopedico, non promozionale |
| `it/benchmark-*` | Benchmark — i dati numerici sono il contenuto, non serve visual aggiuntivo |

---

## Varianti da considerare in futuro

| Variante | Pagina target | Modifica necessaria |
|---|---|---|
| **Focus ERP** | `integrazioni-erp.html` | Enfatizzare parte destra con più connettori, ridurre parte sinistra |
| **Focus Privacy** | `architettura-privacy.html` | Badge "nessun dato esce" più prominente, aggiungere icona firewall |
| **Focus VLM** | `vlm-vs-ocr.html` | Zoom sul nodo centrale con dettaglio dell'icona vision |
| **Versione orizzontale compatta** | `pricing.html`, sidebar | 600px larghezza max, animazione più veloce |
| **Versione dark su sfondo chiaro** | — | Solo se in futuro si aggiunge una sezione light-mode |

---

## Note tecniche per l'integrazione

- **Tag consigliato:** `<object type="image/svg+xml" data="/assets/animations/pipeline-animation-v2.svg">` — supporta le animazioni CSS in tutti i browser moderni
- **Alternativa:** `<img>` tag — le animazioni CSS SVG funzionano anche così in Chrome, Firefox, Safari ma non in Edge legacy
- **Lazy loading:** Aggiungere `loading="lazy"` sull'`<img>` o caricare l'`<object>` solo quando entra nel viewport (IntersectionObserver)
- **Accessibilità:** L'SVG ha già `role="img"` e `aria-label` — non serve altro
- **Responsive:** L'SVG ha `viewBox` — scala automaticamente. Basta `width: 100%; height: auto`
- **Performance:** Il file SVG è ~14KB — leggero, nessun impatto sul LCP se caricato lazy
