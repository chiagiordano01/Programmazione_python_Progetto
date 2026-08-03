# Sistema di Gestione Zoo (Programmazione Python OO & GUI)

Progetto universitario sviluppato per il corso di Programmazione e Analisi Dati (A.A. 2024/25) - Università di Pisa.

**Autrice:**
* Chiara Giordano

---

## Descrizione del Progetto

Il progetto implementa un sistema software Orientato agli Oggetti (OOP) per la gestione avanzata di un catalogo di animali all'interno di uno zoo. Rispetto alla prima versione procedural-style, questa versione introduce una gerarchia di classi ereditate e un'interfaccia grafica utente (GUI) realizzata con **Tkinter**.

### Caratteristiche Principali:
1. **Gerarchia di Oggetti (`animali.py`)**:
   * Classe base `Animale` con gestione degli attributi generali (nome, sangue caldo/freddo, zampe, ambiente, verso) e controllo sui tipi/eccezioni.
   * Sottoclassi per classe di appartenenza: `Mammifero`, `Uccello`, `Pesce`.
   * Classi specifiche per specie: `Leone`, `Giraffa`, `Ippopotamo`, `Pinguino`, `Gufo`, `PescePagliaccio`.
2. **Gestione del Catalogo (`zoo.py`)**:
   * Gestione del dizionario dello zoo, assegnazione delle zone (es. "A1", "B2"), filtri per specie, classe o ambiente.
   * Funzionalità di salvataggio e caricamento dello stato dello zoo su file di testo (`salva` e `carica`).
3. **Interfaccia Grafica GUI (`gui.py`)**:
   * Realizzata tramite `tkinter`.
   * Permette l'inserimento manuale di nuovi animali, modifica della zona, visualizzazione dettagli, ricerca avanzata e gestione del salvataggio/caricamento via file picker.
4. **Testing e Robustezza (`main.py`, `testMy.py`)**:
   * Suite di test automatici che verifica il sollevamento corretto delle eccezioni (`TypeError`, `ValueError`, `KeyError`) e il rispetto delle gerarchie.

---

## Struttura dei File

* `animali.py`: Contiene la definizione di tutte le classi e la gerarchia degli animali.
* `zoo.py`: Contiene la classe gestore `Zoo` per la gestione del dizionario e i metodi di I/O.
* `gui.py`: Applicazione desktop con interfaccia grafica Tkinter.
* `main.py`: Script di test automatico finale fornito per la verifica dei metodi e delle eccezioni.
* `testMy.py`: Utility per le asserzioni di test e controllo eccezioni.

---

## Come Eseguire il Progetto

### Avviare l'interfaccia Grafica (GUI)
```bash
python gui.py