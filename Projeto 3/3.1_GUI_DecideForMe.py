#Descrição/Description
    # PT-BR
        # Mostra uma resposta para a pergunta do usuário, baseada em uma lista pré inserida.
        # Com GUI
    # EU
        # Shows an answer to the user's question, based on a pre-entered list.
        # With GUI

from random import choice
import PySimpleGUI as sg

def decide():
    respostas = [
        'Com certeza, você deve fazer isso!',
        'Não! Não faça isso!',
        'Não sei, você que sabe.',
        'Acho que está na hora certa.'
    ]

    return(choice(respostas))

def gui():
    layout = [
        [sg.Text('Faça uma pergunta:')],
        [sg.Input(size=(40,1), key='INPUT')],
        [sg.Button('Perguntar'), sg.Button('Quit')],
        [sg.Output(size=(40,2))]
    ]

    janela = sg.Window('Decida por mim!', layout=layout)

    while True:
        evento, valores = janela.Read()
        if evento == 'Quit':
            janela.close()
            break
        elif evento == 'Perguntar':
            print(decide())

gui()

