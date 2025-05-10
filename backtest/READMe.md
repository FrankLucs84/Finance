# 🧠 Cosa fa lo script, passo dopo passo

## 1. 📥 Scarica dati storici
Prende i dati di prezzo **orari** (`Open`, `High`, `Low`, `Close`) di un asset (es. **BTC-USD**) relativi agli **ultimi 30 giorni**, utilizzando `yfinance`.

---

## 2. 🔍 Crea un "pattern attuale"
Estrae gli **ultimi 66 valori** calcolati come media `(High + Low + Close) / 3`, noto come `HLC3`.  
Questo diventa il **pattern di riferimento** da cercare nel passato.

> 📊 È come dire:  
> *"Voglio sapere se nel passato il prezzo si è mai mosso in modo simile a come si sta muovendo adesso."*

---

## 3. 🧬 Cerca pattern simili nel passato
Scorre tutti i dati precedenti (escludendo l'ultima parte) e confronta **ogni finestra di 66 barre** con il pattern attuale, usando la **distanza euclidea**.

> 🎯 Trova i **5 pattern più simili** già accaduti.

---

## 4. 🔮 Per ogni pattern simile, guarda cosa è successo dopo
Per ciascun pattern trovato:

- Prende anche le **12 barre successive** come "proiezione futura"
- Le visualizza insieme al pattern attuale per confronto

> 🔮 È come dire:  
> *"Ogni volta che il prezzo ha avuto questa forma... dopo 12 ore cosa ha fatto?"*

---

## 5. 📊 Visualizza tutto
- Plotta i **pattern simili**
- Mostra anche il **segmento di prezzo futuro** che li seguiva
- Confronta tutto con il **pattern attuale** (in nero)

---

## 6. 🎞️ Anima il tutto in una GIF
Crea una **GIF animata** che mostra questo processo **frame per frame**, aggiornando i dati in ogni istante (simulando l’avanzare del tempo).

> ✅ Alla fine ottieni una **GIF** che **simula la previsione dei pattern**, frame dopo frame.

---

## 📦 In sintesi

| Funzione           | Descrizione                                      |
|--------------------|--------------------------------------------------|
| `yfinance`         | Scarica i dati (es. `BTC-USD`, intervallo `1h`)  |
| `scipy.euclidean`  | Confronta la similarità tra pattern di prezzo    |
| `matplotlib`       | Crea i grafici dei pattern e delle proiezioni    |
| `Pillow`           | Assembla i grafici in una **GIF animata**        |

---

## 🧪 A cosa serve in pratica?

- 🔁 **Backtest visivo** dei pattern di prezzo
- 📐 **Analisi euristica** delle forme che si ripetono
- 🎓 **Educazione**: per capire se certi movimenti hanno una “memoria storica”
- 💡 **Ispirazione per strategie**: può suggerire regole operative più robuste

