
# 📊 Portfolio Optimization with CVaR Constraint

Questo progetto esegue un'ottimizzazione di portafoglio utilizzando dati storici reali da Yahoo Finance.  
L'obiettivo è costruire un portafoglio **dollar-neutral** con **massimizzazione dello Sharpe Ratio** e **limitazione del rischio tramite CVaR (Conditional Value at Risk)**.

---

## 🚀 Funzionalità

- Scaricamento dati di 25 titoli USA dal 2016 al 2024
- Calcolo rendimenti giornalieri e pulizia dei dati
- Costruzione di un portafoglio:
  - con short selling abilitato
  - a somma pesi pari a zero (neutralità di capitale)
- Ottimizzazione con:
  - Modello: `Classic`
  - Rischio: `CVaR`
  - Obiettivo: `Sharpe Ratio`
- Calcolo delle performance:
  - Rendimento atteso
  - Volatilità annuale
  - Sharpe Ratio
  - CVaR al 5%
- Generazione grafici:
  - Torta delle allocazioni
  - Barre verticali dei pesi
- Esportazione dei risultati in CSV e PNG

---

## 📁 Output

Tutti i risultati vengono salvati nella cartella:

```
C:\Users\f.lucignano\Desktop\CFO\grafici_portafoglio
```

Contiene:
- `pesi_portafoglio.csv` — pesi ottimizzati per ciascun asset
- `rendimenti_portafoglio.csv` — rendimenti giornalieri degli asset
- `pie_chart_portfolio.png` — grafico a torta delle allocazioni
- `bar_chart_portfolio.png` — grafico a barre verticali

---

## ⚙️ Requisiti

Installa i pacchetti Python necessari:

```bash
pip install yfinance matplotlib pandas numpy riskfolio-lib
```

---

## 📈 Esempio di Risultato

```
Periodo analizzato: 2016-01-01 → 2024-12-30
N. asset analizzati: 25
Asset selezionati nel portafoglio: 13

Expected Return:         2.89%
Volatility (Annuale):    2.06%
Sharpe Ratio:            1.408
CVaR (5%):              -0.24%
```

### 📌 Interpretazione

| Indicatore         | Significato                                                                 |
|--------------------|-----------------------------------------------------------------------------|
| Expected Return     | Rendimento atteso medio annuo, basato sui dati storici                     |
| Volatility          | Oscillazione dei rendimenti (rischio totale)                               |
| Sharpe Ratio        | Efficienza del portafoglio: rendimento per unità di rischio                |
| CVaR (5%)           | Perdita media nei peggiori giorni del 5% (tail risk)                       |
| Asset selezionati   | Solo gli asset con peso ≠ 0 (gli altri sono esclusi dall’allocazione)      |

---

## 🧩 Note Tecniche

- L'ottimizzazione è eseguita su base storica (`hist=True`)
- La matrice di covarianza è stimata con il metodo **Ledoit-Wolf**, più robusto di quello classico
- L’ottimizzazione può essere estesa per includere:
  - vincoli settoriali
  - soglie minime/massime
  - approccio long-only (rimuovendo la neutralità di budget)

---

## 🧪 Estensioni possibili

- Report PDF automatico
- Dashboard web con Streamlit
- Analisi rolling nel tempo
- Integrazione con Excel (output multi-sheet)
- Backtest con benchmark (es. S&P 500)

---

## 👨‍💻 Autore

Frank Lucignano — *Project Manager & Business Analyst*

---

## 📜 Licenza

MIT License
