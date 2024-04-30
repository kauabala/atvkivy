from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class RotuloApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.lab1 = Label(
            text='senai', color=[1, 0, 0, 1],
            font_size=40, bold=True
   )

        self.lab2 = Label(
            text='sesi', color=[0, 1, 0, 1],
            font_size=40, italic=True
    )

        self.lab3 = Label(
        text= 'ENEM',color=[0, 0, 1, 1],
        font_size