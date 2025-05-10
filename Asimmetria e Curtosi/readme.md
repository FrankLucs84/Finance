# 📊 Oltre la Volatilità: Asimmetria e Curtosi nei Rendimenti Finanziari

> ❝ Nessun parametro di rischio fornisce il quadro completo. ❞  
Questa è una citazione che ripeto almeno una volta alla settimana. In finanza quantitativa, **ridurre il rischio a una singola metrica come la volatilità è limitante**. Esistono molte altre misure — spesso trascurate — che offrono una visione più ricca del comportamento di una strategia.

---

## 🎯 Obiettivo della Guida

Imparerai a:

- Comprendere il significato di **asimmetria (skewness)** e **curtosi (kurtosis)**.
- Calcolare questi due indicatori sui **rendimenti di SPY** con Python.
- Visualizzare graficamente la distribuzione e confrontarla con una normale.
- Estendere il ragionamento alla tua strategia di trading.

---

## 🧠 Perché non basta la deviazione standard?

La **volatilità**, ovvero la **deviazione standard dei rendimenti**, misura la dispersione attorno alla media. Tuttavia:

- Non ci dice **se i rischi sono principalmente al ribasso o al rialzo**.
- Non ci dice **quanto frequentemente si verificano eventi estremi**.

È qui che entrano in gioco **asimmetria e curtosi**:

| Metrica                     | Significato                                                                 |
|----------------------------|----------------------------------------------------------------------------|
| **Asimmetria (Skewness)**  | Indica se la distribuzione è sbilanciata a sinistra (negativa) o destra (positiva). |
| **Curtosi (Kurtosis)**     | Indica quanto le code della distribuzione sono "spesse" rispetto alla normale.     |

---

## 🔍 Importanza in ambito finanziario

Gli **analisti quantitativi** e i **gestori di portafoglio** utilizzano skewness e curtosi per:

- **Identificare i rischi di coda** (tail risk)
- Valutare la **robustezza delle strategie in scenari estremi**
- Costruire **stress test realistici**
- Adattare le strategie in base a condizioni di mercato non simmetriche

---

## 🧪 Esempio Pratico: SPY con Python

### Passaggi della Newsletter

1. **Importare le librerie**
2. **Scaricare i dati di SPY**
3. **Calcolare i rendimenti giornalieri**
4. **Calcolare skewness e kurtosi**
5. **Visualizzare la distribuzione dei rendimenti**

> 👉 Anche se qui analizziamo SPY, **puoi usare lo stesso approccio sui rendimenti del tuo portafoglio**.

---

## 📈 Interpretazione dei risultati

| Statistica        | Interpretazione                                          |
|-------------------|-----------------------------------------------------------|
| **Skew > 0**       | Più probabilità di ritorni estremamente positivi         |
| **Skew < 0**       | Più rischio di perdite estreme (comune nei mercati)      |
| **Kurtosis ≫ 3**   | Presenza di **eventi rari ma gravi** (code spesse)       |

> Nel caso di SPY, si osserva skew positivo e curtosi intorno a 7.7. Questo implica una **frequenza elevata di eventi anomali** (più di quanto atteso in una distribuzione normale) ma **a favore del lato positivo**.

---

## 🛠 Prossimi Passi per l'utente

1. Sostituisci SPY con il tuo asset/strategia.
2. Analizza il comportamento di skew/kurtosis su **finestre mobili temporali**.
3. Applica filtri: quali asset portano maggiore skew negativo?
4. Integra questi dati nei tuoi **modelli di rischio**, ad esempio:

```text
Se skew < -0.5 e kurtosis > 5 → segnala rischio di coda elevato

**NOTA BENE** Molte strategie vincono "poco e spesso" ma perdono "molto e raramente".
Uno skew negativo combinato con curtosi alta è il segnale di un potenziale crollo, invisibile a chi guarda solo la volatilità.
