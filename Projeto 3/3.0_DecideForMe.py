#Descrição/Description
    # PT-BR
        # Mostra uma resposta para a pergunta do usuário, baseada em uma lista pré inserida.
    # EU
        # Shows an answer to the user's question, based on a pre-entered list.


from random import choice
def decide():
    respostas = [
        'Com certeza, você deve fazer isso!',
        'Não!, Não faça isso!',
        'Não sei, você que sabe.',
        'Acho que ta na hora certa.'
    ]

    input('O que deseja perguntar? ')
    print(choice(respostas))

decide()