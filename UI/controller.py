from model.model import Model
from UI.view import View
import flet as ft

class Controller:
    def __init__(self, view : View, model : Model):
        self._view = view
        self._model = model

    def handler_crea_grafo(self, e):
        try:
            self._model.nbus = int(self._view._txt_nBus.value)
            if self._model.nbus < 1 :
                raise ValueError
        except:
            self._view.show_alert("valore minore di 1")
            return

        self._model.creagrafo()  # aggiorna attr grafo delmodel

        self._view._lst_result.controls.clear()
        numnodi = self._model.grafo.number_of_nodes()
        numar = self._model.grafo.number_of_edges()
        self._view._lst_result.controls.append(
            ft.Text(f"Grafo creato , numero nodi : {numnodi}, numero archi {numar}"))

        self._view._btnUtentiConnessi.disabled = False
        self._view._ddUtente.disabled = False
        self._view._txtL.disabled = False
        self._view._btnSequenza.disabled = False

        self._view._page.update()

    def handler_utenti_connessi(self, e):
        lista = self._model.getlista()  # [(obj, stren-fl)]

        self._view._lst_result.controls.clear()

        for tup in lista:
            self._view._lst_result.controls.append(ft.Text(f"{tup[0].name} ({tup[0].id}) -> strength = {tup[1]}"))


        self._view._ddUtente.options.clear()
        utord= sorted(self._model.nodes, key=lambda x: x.name)

        for u in utord:
            self._view._ddUtente.options.append(ft.dropdown.Option(text= f"{u.name} ({u.id})", key= u.id))



        self._view._page.update()

    def handle_sequenza(self, e):
        try:
            self._model.L = int(self._view._txtL.value)
            if self._model.L < 2 or self._model.L > len(self._model.nodes):
                raise ValueError
            self._model.Ut = self._model.map[self._view._ddUtente.value]
            if not self._model.L:
                raise ValueError
            if not self._model.Ut:
                raise ValueError
        except:
            self._view._alert.show_alert('inserire un valore compreso tra 2 e il totale degli utenti')
            return



        self._model.cercapercorso()
        # self.bestpath= []       #[(obj1, obj2, peso)]
        self._view._lst_result.controls.clear()

        self._view._lst_result.controls.append(
            ft.Text(f"punteggio totale : {self._model.bestweight}"))
        self._view._lst_result.controls.append(
            ft.Text(f"sequenza trovata :"))

        self._view._lst_result.controls.append(
            ft.Text(f"{self._model.bestpath[0][0].name} ({self._model.bestpath[0][0].id})"))
        self._view._lst_result.controls.append(
            ft.Text(f"{self._model.bestpath[0][1].name} ({self._model.bestpath[0][1].id})"))
        for t in self._model.bestpath[1:]:
            self._view._lst_result.controls.append(
                ft.Text(f"{t[1].name} ({t[1].id}) "))


        self._view._page.update()


