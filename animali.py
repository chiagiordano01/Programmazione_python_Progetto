# animali.py
# ==============================================================================
# Chiara Giordano, 700070, c.giordano19@studenti.unipi.it - Miriam Natale, 599729, m.natale8@studenti.unipi.it
# ==============================================================================

class Animale:
    """
    Classe base per TUTTI gli animali.
    Controlla:
      - nome (stringa non vuota)
      - sangue_caldo (bool)
      - numero_zampe (int >= 0)
      - verso (stringa o vuota; None ammesso, ma poi convertito a "")
      - ambiente (lista di stringhe contenente 'Terra', 'Acqua', 'Aria')
    """

    def __init__(self, nome, sangue_caldo, numero_zampe, verso, ambiente):
        # Controlli di tipo e valore
        if not isinstance(nome, str):
            raise TypeError("Il nome deve essere una stringa.")
        if not nome.strip():
            raise ValueError("Il nome non può essere vuoto.")

        if not isinstance(sangue_caldo, bool):
            raise TypeError("sangue_caldo deve essere un valore booleano (True/False).")

        if not isinstance(numero_zampe, int):
            raise TypeError("numero_zampe deve essere un intero.")
        if numero_zampe < 0:
            raise ValueError("numero_zampe deve essere >= 0.")

        if verso is not None and not isinstance(verso, str):
            raise TypeError("verso deve essere una stringa o None.")
        # Se verso è None, lo converto in stringa vuota per semplificare
        if verso is None:
            verso = ""

        if not isinstance(ambiente, list):
            raise TypeError("ambiente deve essere una lista di stringhe.")
        if len(ambiente) == 0:
            raise ValueError("ambiente deve contenere almeno un elemento.")
        for elem in ambiente:
            if not isinstance(elem, str):
                raise TypeError("Ogni elemento di ambiente deve essere stringa.")
            if elem not in ["Terra", "Acqua", "Aria"]:
                raise ValueError("Ambiente deve essere fra 'Terra', 'Acqua', 'Aria'.")

        # Assegno attributi
        self.nome = nome
        self.sangue_caldo = sangue_caldo
        self.numero_zampe = numero_zampe
        self.verso = verso
        self.ambiente = ambiente

    # ---------------------- GETTER & SETTER ----------------------
    def get_nome(self):
        return self.nome

    def set_nome(self, nuovo_nome):
        if not isinstance(nuovo_nome, str):
            raise TypeError("Il nome deve essere una stringa.")
        if not nuovo_nome.strip():
            raise ValueError("Il nome non può essere vuoto.")
        self.nome = nuovo_nome

    def get_sangue_caldo(self):
        return self.sangue_caldo

    def set_sangue_caldo(self, is_caldo):
        if not isinstance(is_caldo, bool):
            raise TypeError("sangue_caldo deve essere booleano.")
        self.sangue_caldo = is_caldo

    def get_numero_zampe(self):
        return self.numero_zampe

    def set_numero_zampe(self, n):
        if not isinstance(n, int):
            raise TypeError("numero_zampe deve essere un intero.")
        if n < 0:
            raise ValueError("numero_zampe deve essere >= 0.")
        self.numero_zampe = n

    def get_verso(self):
        return self.verso

    def set_verso(self, nuovo_verso):
        if not isinstance(nuovo_verso, str):
            raise TypeError("verso deve essere una stringa.")
        self.verso = nuovo_verso

    def get_ambiente(self):
        return self.ambiente

    def set_ambiente(self, nuovo_ambiente):
        if not isinstance(nuovo_ambiente, list):
            raise TypeError("ambiente deve essere una lista di stringhe.")
        if len(nuovo_ambiente) == 0:
            raise ValueError("ambiente non può essere vuoto.")
        for elem in nuovo_ambiente:
            if not isinstance(elem, str):
                raise TypeError("Ogni elemento di ambiente deve essere stringa.")
            if elem not in ["Terra", "Acqua", "Aria"]:
                raise ValueError("Ambiente deve essere 'Terra', 'Acqua' o 'Aria'.")
        self.ambiente = nuovo_ambiente

    # ---------------------- STR & EQ ----------------------
    def __str__(self):
        """
        Esempio di generazione stringa generica.
        Verrà personalizzata nelle sottoclassi specie per rispettare i test.
        """
        # Gestione zampe
        if self.numero_zampe == 0:
            zampe_str = "è senza zampe"
        else:
            zampe_str = f"ha {self.numero_zampe} zampe"

        # Gestione sangue
        sangue_str = "sangue caldo" if self.sangue_caldo else "sangue freddo"

        # Gestione ambiente (Terra e Acqua, ecc.)
        if len(self.ambiente) == 1:
            ambiente_str = self.ambiente[0]
        else:
            ambiente_str = " e ".join(self.ambiente)

        # Gestione verso
        if self.verso:
            verso_str = f" facendo un {self.verso}"
        else:
            verso_str = ""

        return f"{self.nome} {zampe_str}, {sangue_str} e vive in {ambiente_str}{verso_str}"

    def __eq__(self, other):
        if not isinstance(other, Animale):
            return False
        return (
            self.nome == other.nome and
            self.sangue_caldo == other.sangue_caldo and
            self.numero_zampe == other.numero_zampe and
            self.verso == other.verso and
            self.ambiente == other.ambiente
        )


# ==================================================================
# CLASSE MAMMIFERO
# ==================================================================
class Mammifero(Animale):
    """
    Stato aggiuntivo:
    - settimane_gestazione: int > 0
    """
    def __init__(self, nome, sangue_caldo, numero_zampe, verso, ambiente, settimane_gestazione):
        super().__init__(nome, sangue_caldo, numero_zampe, verso, ambiente)
        if not isinstance(settimane_gestazione, int):
            raise TypeError("settimane_gestazione deve essere un intero.")
        if settimane_gestazione <= 0:
            raise ValueError("settimane_gestazione deve essere > 0.")
        self.settimane_gestazione = settimane_gestazione

    def get_settimane_gestazione(self):
        return self.settimane_gestione

    def set_settimane_gestazione(self, settimane):
        if not isinstance(settimane, int):
            raise TypeError("settimane_gestazione deve essere un intero.")
        if settimane <= 0:
            raise ValueError("settimane_gestazione deve essere > 0.")
        self.settimane_gestazione = settimane

    def __str__(self):
        base = super().__str__()
        # es. "Alex ha 4 zampe, sangue caldo e vive in Terra facendo un Ruggito"
        return f"(Mammifero) {base}, con {self.settimane_gestazione} settimane di gestazione"

    def __eq__(self, other):
        if not isinstance(other, Mammifero):
            return False
        return super().__eq__(other) and self.settimane_gestazione == other.settimane_gestazione


# ==================================================================
# CLASSE UCCELLO
# ==================================================================
class Uccello(Animale):
    """
    Stato aggiuntivo:
    - volatile: bool
    """
    def __init__(self, nome, sangue_caldo, numero_zampe, verso, ambiente, volatile):
        super().__init__(nome, sangue_caldo, numero_zampe, verso, ambiente)
        if not isinstance(volatile, bool):
            raise TypeError("volatile deve essere booleano.")
        self.volatile = volatile

    def get_volatile(self):
        return self.volatile

    def set_volatile(self, v):
        if not isinstance(v, bool):
            raise TypeError("volatile deve essere booleano.")
        self.volatile = v

    def __str__(self):
        base = super().__str__()
        # es. "Skipper ha 2 zampe, sangue caldo e vive in Terra e Acqua facendo un Garrito"
        volo_str = "sa volare" if self.volatile else "non sa volare"
        return f"(Uccello) {base}, {volo_str}"

    def __eq__(self, other):
        if not isinstance(other, Uccello):
            return False
        return super().__eq__(other) and self.volatile == other.volatile


# ==================================================================
# CLASSE PESCE
# ==================================================================
class Pesce(Animale):
    """
    Stato aggiuntivo:
    - acqua: stringa fra "Dolce" e "Salata"
    """

    def __init__(self, nome, sangue_caldo, numero_zampe, verso, ambiente, acqua):
        # Inizializza la parte comune (nome, sangue_caldo, etc.)
        super().__init__(nome, sangue_caldo, numero_zampe, verso, ambiente)

        # Primo controllo: 'acqua' deve essere una stringa
        if not isinstance(acqua, str):
            raise TypeError("acqua deve essere una stringa ('Dolce' o 'Salata').")

        # Secondo controllo: valore ammesso "Dolce" o "Salata"
        if acqua not in ["Dolce", "Salata"]:
            raise ValueError("acqua deve essere 'Dolce' o 'Salata'.")

        self.acqua = acqua

    def get_acqua(self):
        return self.acqua

    def set_acqua(self, a):
        # Stessi controlli di tipo/valore anche nel setter
        if not isinstance(a, str):
            raise TypeError("acqua deve essere una stringa ('Dolce' o 'Salata').")
        if a not in ["Dolce", "Salata"]:
            raise ValueError("acqua deve essere 'Dolce' o 'Salata'.")
        self.acqua = a

    def __str__(self):
        """
        Esempio: "(Pesce) Nemo è senza zampe, sangue freddo e vive in Acqua Salata"
        
        """
        if self.numero_zampe == 0:
            zampe_str = "è senza zampe"
        else:
            zampe_str = f"ha {self.numero_zampe} zampe"
        sangue_str = "sangue caldo" if self.sangue_caldo else "sangue freddo"
        # Qui forziamo l'output "vive in Acqua <Dolce/Salata>"
        return (f"(Pesce) {self.nome} {zampe_str}, {sangue_str} "
                f"e vive in Acqua {self.acqua}")

    def __eq__(self, other):
        if not isinstance(other, Pesce):
            return False
        return (super().__eq__(other) and self.acqua == other.acqua)


# ==================================================================
# CLASSE SPECIE: LEONE, GIRAFFA, IPPOPOTAMO, PINGUINO, GUFO, PESCESPAGLIACCIO
# ==================================================================

class Leone(Mammifero):
    def __init__(self, nome, sangue_caldo=True, numero_zampe=4, verso="Ruggito",
                 ambiente=None, settimane_gestazione=7):
        if ambiente is None:
            ambiente = ["Terra"]
        super().__init__(nome, sangue_caldo, numero_zampe, verso, ambiente, settimane_gestazione)

    def __str__(self):
        # "Il Leone (Mammifero) Alex ha 4 zampe, sangue caldo e vive in Terra facendo un Ruggito, con 7 settimane di gestazione"
        # Ricreiamo la logica:
        if self.numero_zampe == 0:
            zampe_str = "è senza zampe"
        else:
            zampe_str = f"ha {self.numero_zampe} zampe"
        sangue_str = "sangue caldo" if self.sangue_caldo else "sangue freddo"
        ambiente_str = " e ".join(self.ambiente)
        verso_str = f" facendo un {self.verso}" if self.verso else ""
        return (f"Il Leone (Mammifero) {self.nome} {zampe_str}, {sangue_str} "
                f"e vive in {ambiente_str}{verso_str}, con {self.settimane_gestazione} settimane di gestazione")

    def __eq__(self, other):
        if not isinstance(other, Leone):
            return False
        return super().__eq__(other)


class Giraffa(Mammifero):
    def __init__(self, nome, sangue_caldo=True, numero_zampe=4, verso="Mugugno",
                 ambiente=None, settimane_gestazione=65):
        if ambiente is None:
            ambiente = ["Terra"]
        super().__init__(nome, sangue_caldo, numero_zampe, verso, ambiente, settimane_gestazione)

    def __str__(self):
        return (f"La Giraffa (Mammifero) {self.nome} "
                f"{'ha '+str(self.numero_zampe)+' zampe' if self.numero_zampe>0 else 'è senza zampe'}, "
                f"{'sangue caldo' if self.sangue_caldo else 'sangue freddo'} e vive in {' e '.join(self.ambiente)}"
                f"{f' facendo un {self.verso}' if self.verso else ''}, "
                f"con {self.settimane_gestazione} settimane di gestazione")

    def __eq__(self, other):
        if not isinstance(other, Giraffa):
            return False
        return super().__eq__(other)


class Ippopotamo(Mammifero):
    def __init__(self, nome, sangue_caldo=True, numero_zampe=4, verso="Ruggito",
                 ambiente=None, settimane_gestazione=8):
        if ambiente is None:
            ambiente = ["Terra", "Acqua"]
        super().__init__(nome, sangue_caldo, numero_zampe, verso, ambiente, settimane_gestazione)

    def __str__(self):
        return (f"L'Ippopotamo (Mammifero) {self.nome} "
                f"{'ha '+str(self.numero_zampe)+' zampe' if self.numero_zampe>0 else 'è senza zampe'}, "
                f"{'sangue caldo' if self.sangue_caldo else 'sangue freddo'} e vive in {' e '.join(self.ambiente)}"
                f"{f' facendo un {self.verso}' if self.verso else ''}, "
                f"con {self.settimane_gestazione} settimane di gestazione")

    def __eq__(self, other):
        if not isinstance(other, Ippopotamo):
            return False
        return super().__eq__(other)


class Pinguino(Uccello):
    def __init__(self, nome, sangue_caldo=True, numero_zampe=2, verso="Garrito",
                 ambiente=None, volatile=False):
        if ambiente is None:
            ambiente = ["Terra", "Acqua"]
        super().__init__(nome, sangue_caldo, numero_zampe, verso, ambiente, volatile)

    def __str__(self):
        volo = "sa volare" if self.volatile else "non sa volare"
        return (f"Il Pinguino (Uccello) {self.nome} "
                f"{'ha '+str(self.numero_zampe)+' zampe' if self.numero_zampe>0 else 'è senza zampe'}, "
                f"{'sangue caldo' if self.sangue_caldo else 'sangue freddo'} e vive in {' e '.join(self.ambiente)}"
                f"{f' facendo un {self.verso}' if self.verso else ''}, {volo}")

    def __eq__(self, other):
        if not isinstance(other, Pinguino):
            return False
        return super().__eq__(other)


class Gufo(Uccello):
    def __init__(self, nome, sangue_caldo=True, numero_zampe=2, verso="Bubbolio",
                 ambiente=None, volatile=True):
        if ambiente is None:
            ambiente = ["Aria"]
        super().__init__(nome, sangue_caldo, numero_zampe, verso, ambiente, volatile)

    def __str__(self):
        volo = "sa volare" if self.volatile else "non sa volare"
        return (f"Il Gufo (Uccello) {self.nome} "
                f"{'ha '+str(self.numero_zampe)+' zampe' if self.numero_zampe>0 else 'è senza zampe'}, "
                f"{'sangue caldo' if self.sangue_caldo else 'sangue freddo'} e vive in {' e '.join(self.ambiente)}"
                f"{f' facendo un {self.verso}' if self.verso else ''}, {volo}")

    def __eq__(self, other):
        if not isinstance(other, Gufo):
            return False
        return super().__eq__(other)


class PescePagliaccio(Pesce):
    def __init__(self, nome, sangue_caldo=False, numero_zampe=0, verso="",
                 ambiente=None, acqua="Salata"):
        if ambiente is None:
            ambiente = ["Acqua"]
        super().__init__(nome, sangue_caldo, numero_zampe, verso, ambiente, acqua)

    def __str__(self):
        return (f"Il PescePagliaccio (Pesce) {self.nome} "
                f"{'è senza zampe' if self.numero_zampe==0 else 'ha '+str(self.numero_zampe)+' zampe'}, "
                f"{'sangue caldo' if self.sangue_caldo else 'sangue freddo'} e vive in Acqua {self.acqua}")

    def __eq__(self, other):
        if not isinstance(other, PescePagliaccio):
            return False
        return super().__eq__(other)
