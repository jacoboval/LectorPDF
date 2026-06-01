from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput

from lector import extraer_texto


class RootWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)
        
        self.label = Label(text="Lector PDF",font_size=25, size_hint=(1, 0.3))
       
        self.add_widget(self.label)
        
        self.text = TextInput(
                multiline=True,
                size_hint=(1, 4),
                readonly=True,
                font_size=20,
                padding=(25, 25)
       )

        self.add_widget(self.text)
    
        self.btn = Button(text="Abrir PDF",font_size=25,size_hint=(1, 0.3))

        self.btn.bind(on_press=self.abrir_selector)

        self.add_widget(self.btn)

    def abrir_selector(self, instance):
        chooser = FileChooserListView(path="/mnt/c", filters=["*.pdf"])
        #chooser = FileChooserListView(filters=["*.pdf"])

        popup = Popup(
            title="Selecciona un PDF",
            content=chooser,
            size_hint=(0.9, 0.9)
        )

        def seleccionar(instance, selection,*args):
            if selection:
                ruta = selection[0]
                texto = extraer_texto(ruta)
                self.text.text = texto[:10000]
                self.text.cursor = (0, 0)
                self.text.scroll_y = 1
                self.text.focus = False
                self.label.text = "PDF cargado"
                popup.dismiss()

        chooser.bind(on_submit=seleccionar)
        popup.open()


class LectorApp(App):
    def build(self):
        return RootWidget()


LectorApp().run()