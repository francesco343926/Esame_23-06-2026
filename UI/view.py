import flet as ft
from UI.alert import AlertManager

class View:
    def __init__(self, page : ft.Page):
        self._page = page
        self._controller = None

        self._alert = AlertManager(page)

        self._page.title = "Esame Yelp 23/06/2026"
        self._page.horizontal_alignment = 'CENTER' #ft.CrossAxisAlignment.CENTER
        self._page.window.width = 900


    def set_controller(self, controller):
        self._controller = controller

    def update_page(self):
        self._page.update()

    def show_alert(self, message):
        self._alert.show_alert(message)

    def load_interface(self):

        # PUNTO 1

        self._txt_nBus = ft.TextField(
            label="Num. minimo business recensiti",
            width=300
        )

        self._btnCreaGrafo = ft.ElevatedButton(
            text="Crea Grafo",
            on_click=self._controller.handler_crea_grafo
        )

        self._btnUtentiConnessi = ft.ElevatedButton(
            text="Utenti più connessi",
            disabled=True,
            on_click=self._controller.handler_utenti_connessi
        )

        row1 = ft.Row(
            controls=[
                self._txt_nBus,
                self._btnCreaGrafo,
                self._btnUtentiConnessi
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )

        self._page.controls.append(row1)

        # PUNTO 2

        self._ddUtente = ft.Dropdown(
            label="Utente iniziale",
            width=400,
            disabled=True
        )

        self._txtL = ft.TextField(
            label="Lunghezza sequenza",
            width=200,
            disabled=True
        )

        self._btnSequenza = ft.ElevatedButton(
            text="Cerca Sequenza",
            disabled=True, on_click=self._controller.handle_sequenza
        )

        row2 = ft.Row(
            controls=[
                self._ddUtente,
                self._txtL,
                self._btnSequenza
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )

        self._page.controls.append(row2)

        # RISULTATI

        self._lst_result = ft.ListView(
            expand=True,
            spacing=10,
            padding=20
        )

        self._page.controls.append(self._lst_result)

        self._page.update()