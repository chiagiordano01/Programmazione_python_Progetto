# gui.py
# ==============================================================================
# Chiara Giordano, 700070, c.giordano19@studenti.unipi.it - Miriam Natale, 599729, m.natale8@studenti.unipi.it
# ==============================================================================

import tkinter as tk
from tkinter import messagebox, filedialog

# Import delle classi
from zoo import Zoo
from animali import (Leone, Giraffa, Ippopotamo, Pinguino, Gufo, PescePagliaccio,
                     Mammifero, Uccello, Pesce)

class ZooGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestione Zoo - Tutti i Metodi Richiamati")

        # Istanza dello Zoo
        self.zoo = Zoo()

        # ------------------------ FRAME: INSERIMENTO ANIMALE ------------------------
        frame_inserisci = tk.LabelFrame(root, text="Inserisci Nuovo Animale")
        frame_inserisci.pack(fill="x", padx=5, pady=5)

        tk.Label(frame_inserisci, text="Nome:").grid(row=0, column=0, padx=5, pady=2, sticky="e")
        self.entry_nome = tk.Entry(frame_inserisci)
        self.entry_nome.grid(row=0, column=1, padx=5, pady=2)

        tk.Label(frame_inserisci, text="Specie:").grid(row=1, column=0, padx=5, pady=2, sticky="e")
        self.entry_specie = tk.Entry(frame_inserisci)
        self.entry_specie.grid(row=1, column=1, padx=5, pady=2)

        tk.Label(frame_inserisci, text="Zona:").grid(row=2, column=0, padx=5, pady=2, sticky="e")
        self.entry_zona = tk.Entry(frame_inserisci)
        self.entry_zona.grid(row=2, column=1, padx=5, pady=2)

        btn_aggiungi = tk.Button(frame_inserisci, text="Aggiungi Animale", command=self.aggiungi_animale)
        btn_aggiungi.grid(row=3, column=0, columnspan=2, pady=5)


        # ------------------------ FRAME: MODIFICA ZONA ------------------------
        frame_modifica = tk.LabelFrame(root, text="Modifica Zona di un Animale")
        frame_modifica.pack(fill="x", padx=5, pady=5)

        tk.Label(frame_modifica, text="Nome animale:").grid(row=0, column=0, padx=5, pady=2, sticky="e")
        self.entry_nome_mod = tk.Entry(frame_modifica)
        self.entry_nome_mod.grid(row=0, column=1, padx=5, pady=2)

        tk.Label(frame_modifica, text="Nuova zona:").grid(row=1, column=0, padx=5, pady=2, sticky="e")
        self.entry_zona_mod = tk.Entry(frame_modifica)
        self.entry_zona_mod.grid(row=1, column=1, padx=5, pady=2)

        btn_modifica = tk.Button(frame_modifica, text="Modifica Zona", command=self.modifica_zona)
        btn_modifica.grid(row=2, column=0, columnspan=2, pady=5)

        # ------------------------ FRAME: MOSTRA ANIMALE ------------------------
        frame_mostra = tk.LabelFrame(root, text="Mostra Dettagli di un Animale")
        frame_mostra.pack(fill="x", padx=5, pady=5)

        tk.Label(frame_mostra, text="Nome animale:").grid(row=0, column=0, padx=5, pady=2, sticky="e")
        self.entry_mostra_nome = tk.Entry(frame_mostra)
        self.entry_mostra_nome.grid(row=0, column=1, padx=5, pady=2)

        btn_mostra = tk.Button(frame_mostra, text="Mostra Animale", command=self.mostra_animale)
        btn_mostra.grid(row=0, column=2, padx=5, pady=2)

        # ------------------------ FRAME: FILTRI E CONTEGGIO------------------------
        frame_filtri = tk.LabelFrame(root, text="Filtri & Conteggi")
        frame_filtri.pack(fill="x", padx=5, pady=5)

        # -- Ricerca per specie --
        tk.Label(frame_filtri, text="Specie:").grid(row=0, column=0, padx=5, pady=2, sticky="e")
        self.entry_specie_search = tk.Entry(frame_filtri)
        self.entry_specie_search.grid(row=0, column=1, padx=5, pady=2)
        btn_specie = tk.Button(frame_filtri, text="Trova per Specie", command=self.trova_per_specie)
        btn_specie.grid(row=0, column=2, padx=5, pady=2)

        # -- Ricerca per ambiente --
        tk.Label(frame_filtri, text="Ambiente:").grid(row=1, column=0, padx=5, pady=2, sticky="e")
        self.entry_ambiente_search = tk.Entry(frame_filtri)
        self.entry_ambiente_search.grid(row=1, column=1, padx=5, pady=2)
        btn_ambiente = tk.Button(frame_filtri, text="Trova per Ambiente", command=self.trova_per_ambiente)
        btn_ambiente.grid(row=1, column=2, padx=5, pady=2)

        # -- Conteggio per classe --
        tk.Label(frame_filtri, text="Classe:").grid(row=2, column=0, padx=5, pady=2, sticky="e")
        self.entry_classe_search = tk.Entry(frame_filtri)
        self.entry_classe_search.grid(row=2, column=1, padx=5, pady=2)
        btn_classe = tk.Button(frame_filtri, text="Conta per Classe", command=self.conta_classe)
        btn_classe.grid(row=2, column=2, padx=5, pady=2)

        # ------------------------ FRAME: SALVATAGGIO / CARICAMENTO ------------------------
        frame_file = tk.LabelFrame(root, text="Gestione File")
        frame_file.pack(fill="x", padx=5, pady=5)

        btn_salva = tk.Button(frame_file, text="Salva Zoo", command=self.salva_zoo)
        btn_salva.pack(side="left", padx=5, pady=5)

        btn_carica = tk.Button(frame_file, text="Carica Zoo", command=self.carica_zoo)
        btn_carica.pack(side="left", padx=5, pady=5)

        # ------------------------ AREA TESTO PER ELENCO ANIMALI ------------------------
        frame_elenco = tk.LabelFrame(root, text="Elenco Animali nello Zoo (aggiornato)")
        frame_elenco.pack(fill="both", expand=True, padx=5, pady=5)

        self.txt_elenco = tk.Text(frame_elenco, height=10, width=70)
        self.txt_elenco.pack(fill="both", expand=True)

        # ------------------------ PULSANTE USCITA ------------------------
        btn_esci = tk.Button(root, text="Esci dall'applicazione", command=self.root.quit)
        btn_esci.pack(padx=5, pady=10)

    # =========================================================================
    # INSERISCI / MODIFICA ZONA / MOSTRA ANIMALE
    # =========================================================================

    def aggiungi_animale(self):
        nome = self.entry_nome.get().strip()
        specie = self.entry_specie.get().strip()
        zona = self.entry_zona.get().strip()

        if not (nome and specie and zona):
            messagebox.showwarning("Attenzione", "Compila tutti i campi per inserire un animale!")
            return

        try:
            animale = self.crea_animale(specie, nome)
            self.zoo.inserisci(animale, zona)
            messagebox.showinfo("OK", f"Animale '{nome}' inserito con successo in zona {zona}.")
            self.aggiorna_elenco()
        except (KeyError, ValueError, TypeError) as e:
            messagebox.showerror("Errore", str(e))


    def modifica_zona(self):
        nome = self.entry_nome_mod.get().strip()
        nuova_zona = self.entry_zona_mod.get().strip()

        if not (nome and nuova_zona):
            messagebox.showwarning("Attenzione", "Compila sia il nome dell'animale che la nuova zona!")
            return

        try:
            self.zoo.cambia_zona(nome, nuova_zona)
            messagebox.showinfo("OK", f"Zona di '{nome}' aggiornata a {nuova_zona}.")
            self.aggiorna_elenco()
        except (KeyError, ValueError, TypeError) as e:
            messagebox.showerror("Errore", str(e))

    def mostra_animale(self):
        nome = self.entry_mostra_nome.get().strip()
        if not nome:
            messagebox.showwarning("Attenzione", "Inserisci il nome dell'animale da mostrare!")
            return
        try:
            animale = self.zoo.animale(nome) #restituisce l'oggetto animale
            zona = self.zoo.zona(nome)   #restituisce la zona
            # Creiamo un messaggio descrittivo
            msg = f"Nome: {nome}\nZona: {zona}\nDettagli:\n{animale}"
            messagebox.showinfo("Dettagli Animale", msg)
        except KeyError as e:
            messagebox.showerror("Errore", str(e))

    # =========================================================================
    # FILTRI & CONTEGGI
    # =========================================================================

    def trova_per_specie(self):
        specie = self.entry_specie_search.get().strip()
        if not specie:
            messagebox.showwarning("Attenzione", "Inserisci una specie!")
            return
        try:
            lista = self.zoo.animali_specie(specie) #restituisce lista di animale di quella specie
            if lista:
                msg = f"Animali di specie '{specie}':\n" + "\n".join(lista)
            else:
                msg = f"Nessun animale di specie '{specie}'."
            messagebox.showinfo("Risultato Ricerca per Specie", msg)
        except TypeError as e:
            messagebox.showerror("Errore", str(e))

    def trova_per_ambiente(self):
        ambiente = self.entry_ambiente_search.get().strip()
        if not ambiente:
            messagebox.showwarning("Attenzione", "Inserisci un ambiente (Terra, Acqua, Aria)!")
            return
        try:
            lista = self.zoo.animali_ambiente(ambiente) #lista animali che vivono nell'ambiente
            if lista:
                msg = f"Animali che vivono in '{ambiente}':\n" + "\n".join(lista)
            else:
                msg = f"Nessun animale vive in '{ambiente}'."
            messagebox.showinfo("Risultato Ricerca per Ambiente", msg)
        except (TypeError, ValueError) as e:
            messagebox.showerror("Errore", str(e))

    def conta_classe(self):
        classe = self.entry_classe_search.get().strip()
        if not classe:
            messagebox.showwarning("Attenzione", "Inserisci una classe (Mammifero, Uccello, Pesce)!")
            return
        try:
            numero = self.zoo.conta_classe(classe)
            messagebox.showinfo("Conteggio", f"Classe '{classe}': {numero} animale/i.") #numero di animali della classe
        except (TypeError, ValueError) as e:
            messagebox.showerror("Errore", str(e))

    # =========================================================================
    # CARICA / SALVA / USCITA
    # =========================================================================

    def salva_zoo(self):
        path = filedialog.asksaveasfilename(
            title="Salva Zoo su File",
            defaultextension=".txt",
            filetypes=[("File di testo", "*.txt"), ("Tutti i file", "*.*")]
        )
        if not path:
            return  # utente ha annullato
        try:
            self.zoo.salva(path)
            messagebox.showinfo("OK", f"Salvataggio completato su '{path}'.")
        except Exception as e:
            messagebox.showerror("Errore Salvataggio", str(e))

    def carica_zoo(self):
        path = filedialog.askopenfilename(
            title="Carica Zoo da File",
            filetypes=[("File di testo", "*.txt"), ("Tutti i file", "*.*")]
        )
        if not path:
            return
        try:
            self.zoo.carica(path)
            messagebox.showinfo("OK", f"Caricamento completato da '{path}'.")
            self.aggiorna_elenco()
        except Exception as e:
            messagebox.showerror("Errore Caricamento", str(e))

    # =========================================================================
    # METODI DI SUPPORTO
    # =========================================================================

    def crea_animale(self, specie, nome):
        """
        Crea un animale specifico in base alla stringa 'specie'.
        Se la specie non è riconosciuta, crea un Mammifero di default.
        """
        specie_lower = specie.lower()
        if specie_lower == "leone":
            return Leone(nome)
        elif specie_lower == "giraffa":
            return Giraffa(nome)
        elif specie_lower == "ippopotamo":
            return Ippopotamo(nome)
        elif specie_lower == "pinguino":
            return Pinguino(nome)
        elif specie_lower == "gufo":
            return Gufo(nome)
        elif specie_lower == "pescepagliaccio":
            return PescePagliaccio(nome)
        else:
            messagebox.showinfo("Specie non riconosciuta", f"Specie '{specie}' non gestita. Uso un Mammifero generico.")
            return Mammifero(nome, True, 4, "Verso", ["Terra"], 10)

    def aggiorna_elenco(self):
        """
        Aggiorna la text box con il contenuto di self.zoo (cioè __str__ di Zoo).
        """
        self.txt_elenco.delete("1.0", tk.END)
        if not self.zoo.zoo:
            self.txt_elenco.insert(tk.END, "Zoo vuoto.\n")
        else:
            self.txt_elenco.insert(tk.END, str(self.zoo))


if __name__ == "__main__":
    root = tk.Tk()
    app = ZooGUI(root)
    root.mainloop()
