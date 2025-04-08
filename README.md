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

### 10. 📉 Sharpe Ratio e Calcolo CVaR

![Formula2](https://github.com/FrankLucs84/Finance/blob/main/2.jpg "Formula1")

![Formula1](https://github.com/FrankLucs84/Finance/blob/main/1.jpg "Formula2")

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

### 🔍 Spiegazione dettagliata dei risultati

---

📅 **Periodo analizzato**: 2016-01-01 → 2024-12-30  
Hai analizzato i dati giornalieri di Borsa su un intervallo di 9 anni completi.  
Tutto ciò che viene calcolato (rendimenti, rischio, CVaR…) si basa esclusivamente su questi dati storici.

---

📦 **N. asset analizzati**: 25  
Sono i 25 titoli che hai indicato nella lista `tickers`.  
Lo script ha scaricato i prezzi, pulito i dati e calcolato i rendimenti per tutti questi asset.

---

🎯 **Asset selezionati nel portafoglio**: 13  
L’algoritmo ha deciso di assegnare un peso diverso da zero solo a 13 dei 25 asset disponibili.  
Gli altri 12 hanno ricevuto peso zero perché **non miglioravano il rapporto rischio/rendimento**.  
✅ Questo è normale: il portafoglio è sparso solo su titoli utili a massimizzare lo Sharpe ratio e ridurre il CVaR.

---

📈 **Expected Return**: 2.89%  
Rendimento atteso annuale del portafoglio, calcolato dalle medie giornaliere ×252.  
👉 Rendimento contenuto ma stabile, tipico dei portafogli market-neutral (budget = 0).

---

📉 **Volatility (Annuale)**: 2.06%  
Oscillazione annualizzata dei rendimenti.  
👉 Molto bassa, indica che il portafoglio è **estremamente stabile**.  
Per confronto: l’S&P500 ha una volatilità tra 15% e 20%.

---

📊 **Sharpe Ratio**: 1.408  
Misura quanta performance ottieni per ogni unità di rischio:

\[
\text{Sharpe} = \frac{\text{Expected Return} - \text{Risk Free Rate}}{\text{Volatility}}
\]

👉 Valore >1 è ottimo → significa portafoglio **molto efficiente**.  
Nonostante il rendimento non elevato, **il rischio è ancora più basso**, quindi lo Sharpe è elevato.

---

⚠️ **CVaR (5%)**: -0.24%  
Indica la **perdita media nei peggiori giorni** (i peggiori 5% della distribuzione).  
👉 In caso di scenari molto negativi, la perdita media attesa è solo dello 0.24%.  
✅ Questo conferma la **bassa esposizione al rischio estremo**.

---

## 📦 File generati

| File | Descrizione |
|------|-------------|
| `pesi_portafoglio.csv` | Allocazioni finali del portafoglio |
| `rendimenti_portafoglio.csv` | Rendimenti giornalieri degli asset |
| `pie_chart_portfolio.png` | Grafico a torta |
| `bar_chart_portfolio.png` | Grafico a barre |

Cartella di output:

```
C:\Users\f.lucignano\Desktop\CFO\grafici_portafoglio
```

---

## 🔁 Estensioni possibili

| Obiettivo | Estensione |
|----------|------------|
| Aumentare rendimento | Rimuovere `budget=0` e testare solo long |
| Aggiungere settori | Gruppi con vincoli aggregati |
| Generare PDF | Usare `matplotlib.backends.backend_pdf` |
| Dashboard web | Streamlit con interattività |
| Analisi rolling | Rolling Sharpe, volatilità mobile |

---

## 🛠️ Requisiti

```bash
pip install yfinance matplotlib pandas riskfolio-lib
```

---

## 📚 Licenza

Progetto personale e didattico. Può essere esteso e riutilizzato liberamente per scopi interni o professionali.
