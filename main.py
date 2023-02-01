from kivy.app import App
from kivy.lang import Builder
import requests

GUI = Builder.load_file('tela.kv')


class Meuaplicativo(App):
    def build(self):
        return GUI

    def on_start(self):
        self.pegar_cota('USD')
        self.root.ids['moeda1'].text = 'USD/BRL = R$7.07'
        self.root.ids['moeda2'].text = 'EUR/BRL = RS$5.50'

    def pegar_cota(self, moeda):
        link = f'https://economia.awesomeapi.com.br/last/{moeda}-BRL'
        requisicao = requests.get(link)
        print(requisicao.json())
        dic_requisicao = requisicao.json()
        cotacao = dic_requisicao[f'{moeda}BRL']['bid']


Meuaplicativo().run()
