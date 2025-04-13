
# Analisi Clustering K-Medoids dei titoli azionari

Questo script esegue un'analisi di clustering su titoli tech usando **K-Medoids**, un algoritmo più robusto rispetto al K-Means, applicato su dati ridotti dimensionalmente con **PCA**.

---

## ✅ Step principali

1. **Download dati da Yahoo Finance**
   - Titoli analizzati: `AAPL`, `AMZN`, `GOOGL`, `MSFT`, `TSLA`
   - Periodo: dal `2020-01-01` al `2020-12-31`

2. **Preprocessing**
   - Estrazione prezzi di chiusura
   - **StandardScaler** per normalizzazione

3. **PCA (Principal Component Analysis)**
   - Riduzione a 2 dimensioni per permettere la visualizzazione

4. **Clustering**
   - Algoritmo: `KMedoids` (`scikit-learn-extra`)
   - Numero di cluster: `2`
   - Metodo: `'alternate'`

5. **Visualizzazione**
   - Ogni punto rappresenta un titolo
   - Colori indicano il cluster
   - Ogni titolo è etichettato

---

## 📈 Output

Il grafico viene salvato automaticamente come:

```
clustering_kmedoids.png
```

---

## 🧰 Requisiti

Installa le librerie richieste con:

```bash
pip install yfinance pandas scikit-learn scikit-learn-extra matplotlib
```

---

## 💡 Note

- `KMedoids` è più robusto rispetto a `KMeans` perché usa medoid anziché centroidi (meno sensibile agli outlier).
- PCA è solo per visualizzare, non migliora il clustering in sé ma rende tutto leggibile a colpo d’occhio.
