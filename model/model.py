import mysql

from database.DB_connect import get_connection
from model.strumento import Strumento
from model.prestito import Prestito

from UI.view import View

'''
    MODELLO:
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Interagisce con il database
'''

class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        self._nome = nome
        self._responsabile = responsabile

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def responsabile(self):
        return self._responsabile

    @responsabile.setter
    def responsabile(self, responsabile):
        self._responsabile = responsabile

    def get_strumenti(self) -> list[Strumento] | None:
        """
            Funzione che legge tutti gli strumenti nel database
            :return: una lista con tutti gli strumenti presenti oppure None
        """

        # AGGIUNGERE OPZIONE: return None
        my_cursor = get_connection().cnx.cursor()
        query = f'''
                    SELECT * 
                    FROM strumento
                 '''
        my_cursor.execute(query)
        lista_strumenti = []

        for row in my_cursor:
            lista_strumenti.append(row)

        return lista_strumenti

    def cerca_strumenti_per_tipo(self, tipo) -> list[Strumento] | None:
        """
            Funzione che recupera una lista con tutti gli strumenti presenti nel database di un certo tipo
            :param tipo: il tipo dello strumento (es. "Chitarra")
            :return: una lista con tutti gli strumenti del tipo indicato oppure None
        """

        # AGGIUNGERE OPZIONE: return None
        cursore_dizionario = get_connection().cnx.cursor(dictionary=True)

        tipo = self.view.input_tipo_strumento

        query = f'''
                    SELECT * 
                    FROM strumento
                    WHERE tipo = '%s'
                 '''
        cursore_dizionario.execute(query, (tipo, ))


