# 🧠 Portfolio Optimization con Python & Riskfolio-Lib

Questo progetto Python costruisce un **portafoglio azionario ottimizzato** a partire da dati storici di mercato, utilizzando `riskfolio-lib`, con approccio neutrale (long/short bilanciato) e controllo del rischio tramite CVaR.

---

## ⚙️ Funzionalità principali

- Scaricamento dati storici da Yahoo Finance
- Calcolo dei rendimenti giornalieri
- Costruzione di un portafoglio con vincolo di neutralità monetaria (budget = 0)
- Ottimizzazione con:
  - Modello "Classic"
  - Rischio CVaR
  - Obiettivo: massimizzare lo Sharpe Ratio
- Calcolo delle metriche:
  - Rendimento atteso annuo
  - Volatilità annua
  - Sharpe Ratio
  - CVaR (Conditional Value at Risk) al 5%
- Esportazione dei risultati:
  - Grafici PNG (torta e barre)
  - File CSV (pesi del portafoglio, rendimenti storici)
- Riepilogo testuale in console

---

## 🧩 Architettura dello script

### 1. 📦 Importazione librerie

```python
import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf
import riskfolio as rp
import numpy as np
```

---

### 2. 🧠 Funzione `portfolio_performance()`

Calcola manualmente le metriche di performance del portafoglio:

\[
\mu = \sum (w_i \cdot r_i) \cdot 252
\]

\[
\sigma = \sqrt{w^T \cdot \Sigma \cdot w}
\]

\[
\text{Sharpe Ratio} = \frac{\mu - r_f}{\sigma}
\]

---

### 3. 📁 Setup output

```python
output_folder = r"C:\Users\f.lucignano\Desktop\CFO\grafici_portafoglio"
```

---

### 4. 📈 Parametri principali

- Periodo: `2016-01-01` → `2024-12-30`
- Tickers: 25 azioni USA

---

### 5. 🧹 Download & pulizia dati

- Scarica i dati dei prezzi con `yfinance`
- Elimina asset con >30% di dati mancanti
- Interpola e riempie i dati mancanti
- Calcola rendimenti giornalieri con:

```python
Y = data.pct_change().dropna()
```

---

### 6. 🧠 Costruzione del portafoglio

```python
port = rp.Portfolio(returns=Y)
port.assets_stats(method_mu="hist", method_cov="ledoit")
```

- Media attesa storica
- Covarianza stimata con Ledoit-Wolf

---

### 7. ⚖️ Vincoli

```python
port.budget = 0         # dollar-neutral
port.sht = True         # consente posizioni short
```

---

### 8. 🧮 Ottimizzazione

```python
w = port.optimization(model="Classic", rm="CVaR", obj="Sharpe")
```

---

### 9. 📊 Calcolo performance

Conversione pesi in array:

```python
weights_array = w.values.flatten()
```

Chiamata:

```python
ret_ann, vol_ann, sharpe = portfolio_performance(Y, weights_array)
```

---

### 10. 📉 Calcolo CVaR (5%)
⚠️ CVaR (5%): -0.24%
Cosa misura?
Il Conditional Value at Risk al 5% indica la perdita media che ci si aspetta nei peggiori giorni del 5% della distribuzione.
Come lo interpreto?
•	Il valore è -0.24%, quindi nei peggiori giorni (quelli molto negativi), il portafoglio perde in media solo lo 0.24% in un giorno.
•	È un rischio molto basso: estremamente contenuto, coerente con un portafoglio difensivo e dollar-neutral.

```python
returns_portafoglio = Y @ w
CVaR = returns_portafoglio[returns_portafoglio <= returns_portafoglio.quantile(0.05)].mean()
```

---

### 11. 🖼️ Grafici e salvataggi

- `pie_chart_portfolio.png`
- `bar_chart_portfolio.png`
- `pesi_portafoglio.csv`
- `rendimenti_portafoglio.csv`

---

## 📈 Esempio di risultati ottenuti

```
Periodo analizzato: 2016-01-01 → 2024-12-30
N. asset analizzati: 25
Asset selezionati nel portafoglio: 13
Expected Return: 2.89%
Volatility (Annuale): 2.06%
Sharpe Ratio: 1.408
CVaR (5%): -0.24%
```

---

### ✅ Interpretazione

| Indicatore       | Spiegazione |
|------------------|-------------|
| **Expected Return** | Guadagno atteso annuo |
| **Volatility**       | Oscillazione media dei rendimenti |
| **Sharpe Ratio**     | Efficienza del portafoglio (rendimento per unità di rischio) |
| **CVaR (5%)**        | Perdita media nei giorni peggiori (5% peggiori rendimenti) |

---

## 📦 File generati

| File | Descrizione |
|------|-------------|
| `pesi_portafoglio.csv` | Allocazioni finali del portafoglio |
| `rendimenti_portafoglio.csv` | Rendimenti giornalieri degli asset |
| `pie_chart_portfolio.png` | Grafico a torta |
| `bar_chart_portfolio.png` | Grafico a barre |

Tutti salvati in:

```
C:\Users\f.lucignano\Desktop\CFO\grafici_portafoglio
```

---

## 🔁 Miglioramenti possibili

| Obiettivo | Estensione |
|----------|------------|
| Aumentare rendimento | Consentire portafoglio solo long (senza short) |
| Aggiungere settori | Raggruppamento e vincoli per settore o industria |
| Report PDF | Usare `pdfkit`, `matplotlib.backends.backend_pdf`, `WeasyPrint` |
| Dashboard interattiva | Streamlit |
| Analisi rolling | Calcolo su finestre mobili (es. Sharpe rolling 12 mesi) |

---

## 🛠️ Requisiti

```bash
pip install yfinance matplotlib pandas riskfolio-lib
```

---

## 📚 Licenza

Progetto personale e a scopo didattico. Utilizzabile liberamente per uso interno o professionale.

