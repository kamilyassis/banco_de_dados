import requests
from tkinter import *


def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto = f'''
    Dolar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}
'''
    
    texto_cot["text"] = texto


janela = Tk()
#janel2 = Tk()
janela.title('Cotação Atual das Moedas')
#janela.geometry("400x400")
texto_orientacao = Label(janela, text = 'Clique no botão para ver as cotações das moedas')
texto_orientacao.grid(column=0,row=0, padx=10, pady=10)

botao = Button (janela, text="Buscar cotações Dólar/Euro/BTC", command=pegar_cotacoes)#passando funcao como parâmetro
botao.grid(column=0,row=1,padx=10, pady=10)

texto_cot = Label(janela,text='')
texto_cot.grid(column=0,row=2,padx=10, pady=10)
'''
texto_orientacao2 = Label(janela, text='Clique aqui agora')
texto_orientacao2.grid(column=1,row=1)
'''

janela.mainloop()
