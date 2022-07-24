
#Descrição/Description
    # PT-BR
        # Simulador de um dado.
    # EU
        # Dice simulator.

from random import randint

def diceSimulator(msg):
    """
    param msg: Mensagem de sim ou são para executar o dado.
    return: Retorna um valor inteiro entre 1 e 6.
    """
    if msg[0] in 'sS':
        val = randint(1,6)
        return(f'Valor sorteado: {val}')
    elif msg[0] in 'nN':
        return('Obrigado! Até logo.')
    else:
        return('Por favor digite SIM ou NAO')

while True:
    res = input('Deseja jogar dado? [S/N]: ')
    print(diceSimulator(res))
    if res[0] in 'Nn':
        break