from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

from tkinter import Tk
from tkinter import filedialog

from lector import extract_text_from_pdf

class RootWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)

        self.label = Label("Lector PDF listo", size_hint=(1, 0.1))
        self.add_widget(self.label)

        self.text = TextInput(text="", multiline=True)
        self.add_widget(self.text)

        self.btn = Button(text="Abrir PDF", size_hint=(1, 0.1))
        self.btn.bind(on_press=self.open_pdf)
        self.add_widget(self.btn)

    def abrir_pdf(self, instance):
        root = Tk()
        root.withdraw()  # Oculta la ventana principal de Tkinter

        file_path = filedialog.askopenfilename(filetypes=[("Archivos PDF", "*.pdf")])

        if file_path:
            texto = extract_text_from_pdf(file_path)

            # se mostrara una parte para no sarurar la UI
            self.text.text = texto[:8000]  # Muestra solo los primeros 8000 caracteres
            self.label.text = "PDF cargado correctamente"
            #self.label.text = f"Archivo abierto: {file_path}"


class LectorPDFApp(App):
    def build(self):
        return Label(
            text="Hola Jacobo\nLector PDF en construcción",
            font_size=28
        )


LectorPDFApp().run()
