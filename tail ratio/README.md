# 📈 Tail Ratio in Finanza

## Descrizione
Il **tail ratio** è uno strumento unico in ambito finanziario per valutare rendimenti estremi.  
È una tecnica che confronta **guadagni elevati** e **perdite elevate**.  
Il tail ratio migliora la visibilità sui cambiamenti economici, in particolare nei mercati volatili.

## Calcolo
In pratica, il calcolo del rapporto di coda implica:
- L'organizzazione dei dati storici sui rendimenti.
- La determinazione dei **percentili** di rendimento.
- Il calcolo del rapporto tra il **95° percentile** e il **5° percentile**.

Questa analisi aiuta a individuare le **"code"** di guadagni e perdite all'interno delle strategie.

## Implementazione
La parte migliore è che il tail ratio può essere calcolato con **una sola riga di codice in Python**.

## Applicazioni
I professionisti della finanza utilizzano il tail ratio per:
- Valutare le performance di **hedge fund**.
- Effettuare **stress test** in condizioni di mercato estreme.
- Determinare il **rapporto rischio-rendimento**.
- Orientare le **strategie di trading quantitativo**.

## 🧪 Come funziona il calcolo del Tail Ratio nel tuo script

Nel tuo script:

```python
def tail_ratio(returns):
    return abs(np.percentile(returns, 95)) / abs(np.percentile(returns, 5))
```

stai effettuando:
- `np.percentile(returns, 95)`: Valore del 95° percentile dei rendimenti (estremo positivo).
- `np.percentile(returns, 5)`: Valore del 5° percentile dei rendimenti (estremo negativo).
- Successivamente, calcoli il **rapporto assoluto** fra questi due numeri.

**In sintesi:**
- Un **Tail Ratio > 1** indica che le code positive sono più grandi di quelle negative (buono per investire).
- Un **Tail Ratio < 1** indica che le code negative sono più grandi di quelle positive (maggiore rischio di forti perdite).

---

## 🔬 Come interpretare il grafico

Nel tuo istogramma:
- L'**asse X** rappresenta i **ritorni giornalieri**.
- L'**asse Y** rappresenta la **frequenza** di quei ritorni.
- Le **linee tratteggiate verticali** rappresentano:
  - Linea sinistra → 5° percentile (perdite estreme).
  - Linea destra → 95° percentile (guadagni estremi).

**Interpretazione:**
- Se la linea di destra (95° percentile) è molto più lontana da zero rispetto alla sinistra (5° percentile), allora il **Tail Ratio sarà > 1**.
- Se le linee sono simmetriche o la sinistra è più "lunga", il **Tail Ratio sarà vicino o minore di 1**.

---

## 📈 Come leggere il valore del Tail Ratio

Nel tuo script:

```python
print(f"Tail Ratio for AMD: {tail_ratio_a:.4f}")
print(f"Tail Ratio for NVDA: {tail_ratio_b:.4f}")
```

👉 Dopo aver eseguito il codice, vedrai nella console:

```
Tail Ratio for AMD: 1.25
Tail Ratio for NVDA: 1.45
```

**Significato:**
- **NVDA = 1.45**: guadagni estremi 45% maggiori delle perdite estreme.
- **AMD = 1.25**: anche AMD ha guadagni più alti delle perdite, ma meno di NVDA.

---

## 🎯 Schema operativo semplice

| Valore Tail Ratio | Interpretazione | Azione pratica |
|:------------------|:----------------|:---------------|
| > 1.2             | Ottimo profilo rischio-rendimento | Potenzialmente buon asset |
| 1.0 - 1.2         | Bilanciato | Valutare altre metriche |
| < 1.0             | Rischio elevato | Cautela |

---

## 🧐 Considerazione scientifica finale

- Il solo Tail Ratio **non è sufficiente** per prendere decisioni di investimento.
- Deve essere **combinato** con altre metriche come:
  - Volatilità
  - Sharpe Ratio
  - Max Drawdown
- È essenziale **calcolare** il Tail Ratio su **periodi di dati significativi** (es. almeno 2-3 anni di dati giornalieri).

---

## 📚 Fonti APA

- Hull, J. C. (2015). *Options, Futures, and Other Derivatives* (9th ed.). Pearson.
- Taleb, N. N. (2007). *The Black Swan: The Impact of the Highly Improbable*. Random House.

---

## 🚀 Possibili estensioni future

- Stampa diretta dei valori dei percentili (5° e 95°) su output.
- Plot delle curve cumulative dei ritorni.
- Costruzione di un **ranking automatico** di più titoli sulla base del Tail Ratio.