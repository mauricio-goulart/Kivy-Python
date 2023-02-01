from kivy.app import App
from kivy.lang import Builder

GUI = Builder.load_file('tela.kv')


class Meuaplicativo(App):
    def build(self):
        return GUI

    def on_start(self):
        self.root.ids


Meuaplicativo().run()
