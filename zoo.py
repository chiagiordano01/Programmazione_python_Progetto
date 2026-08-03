# zoo.py
# ==============================================================================
# Chiara Giordano, 700070, c.giordano19@studenti.unipi.it - Miriam Natale, 599729, m.natale8@studenti.unipi.it
# ==============================================================================

# Importa le classi da animali.py
from animali import (
    Animale, Mammifero, Uccello, Pesce,
    Leone, Giraffa, Ippopotamo, Pinguino, Gufo, PescePagliaccio
)


class Zoo:
    """
    Classe che gestisce un dizionario:
      nome_animale -> (oggetto_animale, zona)
    """

    def __init__(self):
        self.zoo = {}  # chiave = nome (str), valore = (oggetto Animale, zona)
    
    def __str__(self):
        """
        Stringa con una riga per animale:
        "Zona A1: Il Leone (Mammifero) Alex ha 4 zampe, ... \nZona A2: Il Pinguino (Uccello) Skipper ha 2 zampe, ..."
        """
        righe = []
        for nome, (animale, zona) in self.zoo.items():
            righe.append(f"Zona {zona}: {animale}")
        return "\n".join(righe)

    def __eq__(self, other):
        if not isinstance(other, Zoo):
            return False
        if len(self.zoo) != len(other.zoo):
            return False
        for nome, (animale, zona) in self.zoo.items():
            if nome not in other.zoo:
                return False
            a2, z2 = other.zoo[nome]
            if zona != z2 or animale != a2:
                return False
        return True

    def verifica_zona(self, zona):
        """
        Verifica se la zona è valida: deve iniziare con una lettera maiuscola seguita da un numero.
        Solleva un'eccezione se la zona non è valida.
        """
        if not isinstance(zona, str):
            raise TypeError("La zona deve essere una stringa.")
        if len(zona) < 2:
            raise ValueError("La zona deve contenere almeno due caratteri.")
        if not zona[0].isalpha() or not zona[0].isupper():
            raise ValueError("Il primo carattere della zona deve essere una lettera maiuscola.")
        if not zona[1:].isdigit():
            raise ValueError("I caratteri successivi al primo devono essere numeri.")

    def inserisci(self, animale, zona):
        """
        Inserisce un nuovo animale, controllando che:
         - animale è un'istanza di Animale o sottoclassi
         - zona è una stringa con lettera maiuscola + intero es 'A1'
         - se esiste già un animale con lo stesso nome => KeyError
        """
        if not isinstance(animale, Animale):
            raise TypeError("Il parametro 'animale' deve essere un oggetto Animale (o sottoclasse).")

        nome = animale.get_nome()
        if nome in self.zoo:
            raise KeyError(f"Esiste già un animale con nome '{nome}'. Impossibile inserirlo.")

        self.verifica_zona(zona)
        self.zoo[nome] = (animale, zona)

    def animale(self, nome):
        """
        Ritorna l'oggetto animale con nome 'nome'.
        Se non esiste, solleva KeyError.
        """
        if nome not in self.zoo:
            raise KeyError(f"Nessun animale con nome '{nome}' trovato.")
        return self.zoo[nome][0]

    def zona(self, nome):
        """
        Ritorna la zona in cui si trova l'animale 'nome'.
        Se non esiste, solleva KeyError.
        """
        if nome not in self.zoo:
            raise KeyError(f"Nessun animale con nome '{nome}' presente nello Zoo.")
        return self.zoo[nome][1]

    def elimina(self, nome):
        """
        Elimina l'animale con nome 'nome'.
        Se non esiste, KeyError.
        """
        if nome not in self.zoo:
            raise KeyError(f"Nessun animale con nome '{nome}' presente nello Zoo.")
        del self.zoo[nome]

    def cambia_zona(self, nome, zona):
        """
        Cambia la zona dell'animale 'nome'.
         - se 'nome' non esiste => KeyError
         - se zona non è stringa => TypeError
         - se non rispetta formato => ValueError
        """
        if nome not in self.zoo:
            raise KeyError(f"Nessun animale con nome '{nome}' presente nello Zoo.")
        if not isinstance(zona, str):
            raise TypeError("La nuova zona deve essere una stringa.")
        self.verifica_zona(zona)

        animale_esistente, _ = self.zoo[nome]
        self.zoo[nome] = (animale_esistente, zona)

    def zone(self):
        """
        Ritorna la lista delle zone presenti nello zoo (senza duplicati).
        """
        return list({info[1] for info in self.zoo.values()})

    def animali_zona(self, zona):
        """
        Ritorna la lista dei nomi degli animali presenti in una certa zona.
        Se nessuno, lista vuota.
        """
        return [nome for nome, (animale, z) in self.zoo.items() if z == zona]

    def zone_animali(self):
        """
        Ritorna un dizionario { zona: [nomi_animali], ... }.
        """
        risultato = {}
        for nome, (animale, z) in self.zoo.items():
            if z not in risultato:
                risultato[z] = []
            risultato[z].append(nome)
        return risultato

    def animali_classe(self, classe):
        """
        Ritorna i nomi degli animali la cui 'classe' (Mammifero, Uccello, Pesce).
        - solleva ValueError se la classe non è tra quelle
        - solleva TypeError se classe non è stringa
        """
        if not isinstance(classe, str):
            raise TypeError("classe deve essere una stringa.")
        classi_valide = ["Mammifero", "Uccello", "Pesce"]
        if classe not in classi_valide:
            raise ValueError(f"La classe {classe} non è fra quelle esistenti: {classi_valide}.")

        risultati = []
        for nome, (animale, z) in self.zoo.items():
            if classe == "Mammifero" and isinstance(animale, Mammifero):
                risultati.append(nome)
            elif classe == "Uccello" and isinstance(animale, Uccello):
                risultati.append(nome)
            elif classe == "Pesce" and isinstance(animale, Pesce):
                risultati.append(nome)
        return risultati

    def animali_specie(self, specie):
        """
        Ritorna i nomi degli animali di una data specie (es. "Pinguino").
        - se nessuno corrisponde, restituisce lista vuota (niente eccezioni)
        - solleva TypeError se specie non è stringa
        """
        if not isinstance(specie, str):
            raise TypeError("specie deve essere una stringa.")

        risultati = []
        for nome, (animale, z) in self.zoo.items():
            if animale.__class__.__name__ == specie:
                risultati.append(nome)
        return risultati

    def animali_ambiente(self, ambiente):
        """
        Ritorna i nomi degli animali che vivono in un certo ambiente
        (fra 'Terra', 'Acqua', 'Aria').
        - se ambiente non è stringa => TypeError
        - se non in ['Terra','Acqua','Aria'] => ValueError
        """
        if not isinstance(ambiente, str):
            raise TypeError("ambiente deve essere una stringa.")
        if ambiente not in ["Terra", "Acqua", "Aria"]:
            raise ValueError("ambiente deve essere 'Terra', 'Acqua' o 'Aria'.")

        return [nome for nome, (animale, z) in self.zoo.items() if ambiente in animale.get_ambiente()]

    def animali_con_zampe_almeno(self, numero_zampe=2):
        """
        Ritorna i nomi degli animali con almeno 'numero_zampe'.
        di default 2
        - se numero_zampe < 0 => ValueError
        - se non int => TypeError
        """
        if not isinstance(numero_zampe, int):
            raise TypeError("numero_zampe deve essere un intero.")
        if numero_zampe < 0:
            raise ValueError("numero_zampe deve essere >= 0.")

        return [
            nome
            for nome,(animale,z) in self.zoo.items()
            if animale.get_numero_zampe() >= numero_zampe
        ]

    def conta_sangue(self, sangue_caldo):
        """
        Ritorna il numero di animali con sangue_caldo (True) o sangue_freddo (False).
        - se sangue_caldo non è bool => TypeError
        """
        if not isinstance(sangue_caldo, bool):
            raise TypeError("sangue_caldo deve essere booleano.")

        c = 0
        for nome, (animale, z) in self.zoo.items():
            if animale.get_sangue_caldo() == sangue_caldo:
                c += 1
        return c

    def conta_classe(self, classe):
        """
        Ritorna il numero di animali di una certa classe fra Mammifero, Uccello, Pesce.
        - se classe non esiste => ValueError
        - se non str => TypeError
        """
        if not isinstance(classe, str):
            raise TypeError("La classe deve essere una stringa.")

        classi_valide = ["Mammifero", "Uccello", "Pesce"]
        if classe not in classi_valide:
            raise ValueError(f"La classe '{classe}' non è valida. Deve essere una tra {classi_valide}.")

        return len(self.animali_classe(classe))

    def conta_specie(self, specie):
        """
        Ritorna il numero di animali di specie 'specie'.
        - se non è str => TypeError
        """
        if not isinstance(specie, str):
            raise TypeError("La specie deve essere una stringa.")

        return len(self.animali_specie(specie))
    
    def salva(self, nome_file):
        """
        Salva lo stato dello zoo su file di testo.
        """
        with open(nome_file, "w", encoding="utf-8") as f:
            for nome, (animale, zona) in self.zoo.items():
                specie = animale.__class__.__name__
                sangue = str(animale.get_sangue_caldo())
                zampe = str(animale.get_numero_zampe())
                verso = animale.get_verso()
                amb = ",".join(animale.get_ambiente())

                extra = ""
                if isinstance(animale, Mammifero):
                    extra = str(animale.settimane_gestazione)
                elif isinstance(animale, Uccello):
                    extra = str(animale.volatile)
                elif isinstance(animale, Pesce):
                    extra = animale.get_acqua()

                riga = f"{zona};{specie};{nome};{sangue};{zampe};{verso};{amb};{extra}\n"
                f.write(riga)

    def carica(self, nome_file):
        """
        Carica lo stato dello zoo da file, sostituendo i dati correnti.
        - se formato non corretto => ValueError
        - se il file è illeggibile => solleva eventuali eccezioni di I/O
        """
        nuovo_zoo = {}
        with open(nome_file, "r", encoding="utf-8") as f:
            for riga in f:
                riga = riga.strip()
                if not riga:
                    continue
                campi = riga.split(";")
                if len(campi) != 8:
                    raise ValueError("Riga file non valida, servono 8 campi separati da ;")

                zona_file, specie, nome, sangue_str, zampe_str, verso, amb_str, extra = campi

                # Verifica manuale del formato della zona
                if len(zona_file) < 2 or not zona_file[0].isalpha() or not zona_file[0].isupper() or not zona_file[1:].isdigit():
                    raise ValueError("Formato zona non valido nel file.")

                if sangue_str not in ["True", "False"]:
                    raise ValueError("Valore sangue_caldo non corretto nel file.")
                sangue_caldo = (sangue_str == "True")

                try:
                    numero_zampe = int(zampe_str)
                except:
                    raise ValueError("numero_zampe non valido.")

                lista_amb = amb_str.split(",")
                if not lista_amb:
                    raise ValueError("Ambiente vuoto nel file.")

                # Ricostruisco l'animale in base alla specie
                if specie == "Leone":
                    settimane = int(extra)
                    animale = Leone(nome, sangue_caldo, numero_zampe, verso, lista_amb, settimane)
                elif specie == "Giraffa":
                    settimane = int(extra)
                    animale = Giraffa(nome, sangue_caldo, numero_zampe, verso, lista_amb, settimane)
                elif specie == "Ippopotamo":
                    settimane = int(extra)
                    animale = Ippopotamo(nome, sangue_caldo, numero_zampe, verso, lista_amb, settimane)
                elif specie == "Pinguino":
                    if extra not in ["True", "False"]:
                        raise ValueError("Valore volatile non corretto.")
                    volatile = (extra == "True")
                    animale = Pinguino(nome, sangue_caldo, numero_zampe, verso, lista_amb, volatile)
                elif specie == "Gufo":
                    if extra not in ["True", "False"]:
                        raise ValueError("Valore volatile non corretto per Gufo.")
                    volatile = (extra == "True")
                    animale = Gufo(nome, sangue_caldo, numero_zampe, verso, lista_amb, volatile)
                elif specie == "PescePagliaccio":
                    if extra not in ["Dolce", "Salata"]:
                        raise ValueError("Valore acqua non corretto per PescePagliaccio.")
                    animale = PescePagliaccio(nome, sangue_caldo, numero_zampe, verso, lista_amb, extra)
                else:
                    raise ValueError(f"Specie '{specie}' non gestita nel file.")

                if nome in nuovo_zoo:
                    raise ValueError(f"Nome animale duplicato nel file: {nome}")
                nuovo_zoo[nome] = (animale, zona_file)

        self.zoo = nuovo_zoo

    