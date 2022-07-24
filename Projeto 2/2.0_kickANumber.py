#Descrição/Description
    # PT-BR
        # Gera um número aleatório de acordo com os valores de "min" e "max" e o usuário tem que acertar.
    # EU
        # Generates a random number according to the values of "min" and "max" and the user has to get it right

from random import randint
min = 0
max = 10
def kick():
    num = randint(min, max)
    while True:
        try:
            usu = int(input('Qual o seu chute? '))
            if usu == num:
                print(f'Parabéns!! Você acertou o número {num}.')
                break
            elif usu > num:
                print('Tente um número menor!')
            else:
                print('Tente um número maior!')
        except:
            print('Digite um valor inteiro!')

kick()
    