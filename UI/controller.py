import flet as ft
from UI.view import View
from model.model import DepositoStrumenti

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: DepositoStrumenti):
        self._model = model
        self._view = view

    def get_nome(self):
        return self._model.nome

    def get_responsabile(self):
        return self._model.responsabile

    def set_responsabile(self, responsabile):
        self._model.responsabile = responsabile

    def conferma_responsabile(self, e):
        self._model.responsabile = self._view.input_responsabile.value
        self._view.txt_responsabile.value = f"Responsabile: {self._model.responsabile}"
        self._view.update()

    # Altre Funzioni Event Handler
    def mostra_lista_strumenti(self, e):
        strumenti = self._model.get_strumenti()

        if strumenti is None:
            self._view.show_alert("Errore di connessione al database o query fallita!")
            return
        self._view.lista_strumenti.controls.clear()

        if len(strumenti) == 0:
            self._view.lista_strumenti.controls.append(ft.Text("Nessuno strumento presente nel deposito."))

        else:
            for s in strumenti:
                self._view.lista_strumenti.controls.append(ft.Text(str(s)))

        self._view.update()

    def cerca_strumenti_per_tipo(self, e):
        tipo = self._view.input_tipo_strumento.value

        if not tipo or tipo.strip() == "":
            self._view.show_alert("Inserire un tipo di strumento valido per la ricerca!")
            return

        strumenti = self._model.cerca_strumenti_per_tipo(tipo.strip())

        if strumenti is None:
            self._view.show_alert("Errore di connessione al database o query fallita!")
            return

        self._view.lista_strumenti_ricerca.controls.clear()

        if len(strumenti) == 0:
            self._view.lista_strumenti_ricerca.controls.append(ft.Text(f"Nessuno strumento trovato per il tipo '{tipo}'"))
        else:
            for s in strumenti:
                self._view.lista_strumenti_ricerca.controls.append(ft.Text(str(s)))

        self._view.update()
