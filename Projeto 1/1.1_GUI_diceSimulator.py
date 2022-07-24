#Descrição/Description
    # PT-BR
        # Simulador de um dado com GUI.
    # EU
        # Dice simulator with GUI.
from random import randint

def diceSimulator(msg):
    """
    param msg: Mensagem de sim ou são para executar o dado.
    return: Retorna um valor inteiro entre 1 e 6 ou uma mensagem de agradecimento.
    """
    if msg[0] in 'sS':
        val = randint(1,6)
        return f'Valor sorteado: {val}'
    else:
        return 'Obrigado! Até logo.'


import PySimpleGUI as sg

# Layout
layout = [
    [sg.Text('Jogar o dado?', size=(16,1))],
    [sg.Button('Sim', size=(8,1)),sg.Button('Nao', size=(8,1)), sg.Button('Quit', size=(8,1))],
    [sg.Text("", size=(16,1), key='OUTPUT')]
]

# Criar Janela
janela = sg.Window('Simulador de Dado', layout=layout)
while True:
    # Pegar valores
    eventos, valores = janela.Read()
    # Usar dados
    if eventos == 'Quit':
        janela.close()
        break
    else:
        res = diceSimulator(eventos)
        print(res)
        janela['OUTPUT'].update(value=res)