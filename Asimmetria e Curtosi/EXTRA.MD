## 🔁 EXTRA: Possiamo utilizzare diversi database

Per ottenere i dati finanziari e calcolare i rendimenti, esistono **diverse fonti alternative**. Ogni fonte ha vantaggi e limitazioni. È importante conoscerle per scegliere quella più adatta al proprio flusso di lavoro.

### ✅ 1. Yahoo Finance (`yfinance`)

- **✔️ Pro**: Facile da usare, nessuna API key richiesta, dati aggiornati.
- **❌ Contro**: Rischio di *rate limiting* (blocco temporaneo), meno adatto per grandi volumi o uso in produzione.
- **Libreria Python**: `yfinance`
- **Perfetto per**: Prototipazione veloce, backtest su ETF e azioni.

### ✅ 2. Quandl (`quandl`)

- **✔️ Pro**: Offre dataset macroeconomici e finanziari certificati (FRED, Zacks, ecc.).
- **❌ Contro**: Alcuni dataset sono dismessi (es. `WIKI/SPY`), altri richiedono abbonamenti premium.
- **API Key**: Sì, necessaria anche per uso gratuito.
- **Perfetto per**: Dati storici validati, uso accademico o istituzionale.

### ✅ 3. Financial Modeling Prep (`FMP`)

- **✔️ Pro**: Dati completi e gratuiti con chiave API, incluse metriche fondamentali e storiche.
- **❌ Contro**: Richiede parsing manuale dei dati JSON (non esiste ancora una libreria Python ufficiale).
- **API Key**: Sì, registrazione gratuita.
- **Perfetto per**: Analisi fondamentale + tecnica, creazione di sistemi quantitativi personalizzati.

> 🔧 **Suggerimento pratico**: Per prototipazione e studio personale, *yfinance* è ancora una scelta eccellente. Per progetti strutturati o dataset fondamentali, **FMP** rappresenta una valida alternativa gratuita a provider come Bloomberg, mentre **Quandl** è ideale se si dispone di accesso a dataset specifici tramite il proprio ente/azienda.

## 🔎 Altri provider gratuiti di dati finanziari

Oltre a Yahoo Finance, Quandl e FMP, esistono altri servizi utili per ottenere dati di mercato, fondamentali, criptovalute e altro. Ecco i più affidabili **gratuiti**:

---

### ✅ 4. Alpha Vantage

- **✔️ Pro**: Ottimi dati storici su azioni, forex, criptovalute, indicatori tecnici.
- **❌ Contro**: Rate limit stringente (max 5 richieste al minuto), JSON annidato da parsare.
- **API Key**: Gratuita con registrazione.
- **Perfetto per**: Strategie tecniche, dati cripto, analisi multi-asset.
- **Libreria Python**: [`alpha_vantage`](https://github.com/RomelTorres/alpha_vantage)

---

### ✅ 5. Tiingo

- **✔️ Pro**: Dati storici precisi, fondamentali, notizie. API pulita e ben documentata.
- **❌ Contro**: Richiede registrazione e approvazione manuale per accesso completo.
- **API Key**: Gratuita per uso personale.
- **Perfetto per**: Backtest precisi, portafogli personalizzati.
- **Libreria Python**: [`tiingo`](https://github.com/hydrosquall/tiingo-python)

---

### ✅ 6. Polygon.io *(freemium)*

- **✔️ Pro**: Streaming real-time, dati tick-level, cripto, opzioni.
- **❌ Contro**: Piano gratuito limitato solo a pochi endpoint (es. daily close).
- **API Key**: Gratuita con account.
- **Perfetto per**: Analisi intraday, strumenti alternativi, opzioni.
- **Libreria Python**: [Polygon Python Client](https://github.com/polygon-io/client-python)

---

### ✅ 7. CoinGecko (per criptovalute)

- **✔️ Pro**: Dati di mercato cripto, capitalizzazione, storico, sentiment.
- **❌ Contro**: Alcune richieste hanno limiti giornalieri.
- **API Key**: Non necessaria (ma consigliata per uso intensivo).
- **Perfetto per**: Trading o analisi su Bitcoin, Ethereum, Altcoins.
- **Libreria Python**: [`pycoingecko`](https://github.com/man-c/pycoingecko)

---

### ✅ 8. EOD Historical Data *(freemium)*

- **✔️ Pro**: Accesso a dati EOD, fondamentali, macro e ETF globali.
- **❌ Contro**: Solo 20 richieste/giorno nel piano gratuito.
- **API Key**: Sì, con registrazione.
- **Perfetto per**: Analisi su mercati globali e portafogli internazionali.
- **Link**: [eodhistoricaldata.com](https://eodhistoricaldata.com/)

---

## 📌 Conclusione

| Provider          | Azioni | Fondamentali | Cripto | Intraday | API Key | Note                    |
|------------------|--------|--------------|--------|----------|---------|-------------------------|
| Yahoo Finance     | ✅     | ❌           | ✅     | ❌       | ❌      | Limiti e rate blocking |
| Quandl            | ✅     | ✅ (FRED, Zacks) | ❌ | ❌       | ✅      | Molti dataset a pagamento |
| FMP               | ✅     | ✅           | ✅     | ✅       | ✅      | JSON semplice, completo |
| Alpha Vantage     | ✅     | ❌           | ✅     | ✅       | ✅      | Buono per tecnici       |
| Tiingo            | ✅     | ✅           | ❌     | ✅       | ✅      | Dati precisi, lenti     |
| Polygon.io        | ✅     | ✅           | ✅     | ✅       | ✅      | Solo endpoint base free |
| CoinGecko         | ❌     | ❌           | ✅     | ❌       | ❌      | Migliore per crypto     |
| EOD Historical    | ✅     | ✅           | ✅     | ✅       | ✅      | Ideale per ETF globali  |

---

> 🎯 **Suggerimento**: per un setup robusto e gratuito, una combinazione di **FMP + Alpha Vantage + CoinGecko** copre quasi tutti gli asset class e use case quantitativi.
