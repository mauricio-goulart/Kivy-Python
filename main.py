from kivy.app import App
from kivy.lang import Builder
import requests

GUI = Builder.load_file('tela.kv')


class Meuaplicativo(App):
    def build(self):
        return GUI

    def on_start(self):

        self.root.ids['moeda1'].text = f'USD/BRL = R${self.pegar_cota("USD")}'
        self.root.ids['moeda2'].text = f'EUR/BRL = R${self.pegar_cota("EUR")}'
        self.root.ids['moeda3'].text = f'BTC/BRL = R${self.pegar_cota("BTC")}'
        self.root.ids['moeda4'].text = f'ETH/BRL = R${self.pegar_cota("ETH")}'

    def pegar_cota(self, moeda)
        link = f'https://economia.awesomeapi.com.br/last/{moeda}-BRL'
        requisicao = requests.get(link)
        print(requisicao.json())
        dic_requisicao = requisicao.json()
        cotacao = dic_requisicao[f'{moeda}BRL']['bid']
        return cotacao


Meuaplicativo().run()
