#Descrição/Description
    # PT-BR
        # Gera um número aleatório de acordo com os valores de "min" e "max" e o usuário tem que acertar.
        # Com GUI
    # EU
        # Generates a random number according to the values of "min" and "max" and the user has to get it right
        # With GUI


from random import randint
min = 0
max = 10
def kick(val, usu):
    if usu == val:
        return (f'Parabéns!! Você acertou o número {val}.')
    elif usu > val:
        return ('Tente um número menor!')
    else:
        return ('Tente um número maior!')

import PySimpleGUI as sg
#Layout
layout = [
    [sg.Text('Qual o seu chute?', size=(40,1))],
    [sg.Input(key='INPUT')],
    [sg.Button('Enviar'),sg.Button('Reset'), sg.Button('Quit')],
    [sg.Text("", size=(40,1), key='OUTPUT')]
]
# Criar Janela
janela = sg.Window('Chute um número', layout=layout)

rand = randint(min, max)
while True:
    # Pegar valores
    eventos, valores = janela.Read()
    # Usar dados
    if eventos[0] in 'Q':
        janela.close()
        break
    elif eventos[0] in 'R':
        rand = randint(min, max)
        janela['OUTPUT'].update(value='Valor atualizado!')
    else:
        res = kick(rand, int(valores['INPUT']))
        janela['OUTPUT'].update(value=res)

