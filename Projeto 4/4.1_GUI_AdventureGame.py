#Descrição/Description
    # PT-BR
        # Um jogo que faz perguntas ao usuário, as escolhas do usuário o levarão em várias direções,
        # podendo chegar em vários finais distintos.
        # Com GUI

        # OBS: Quando aparecer a primeira tela clique em 'Iniciar'
    # EU
        # A game that asks the user questions, the user's choices will take him in several directions,
        # and can reach several different endings.
        # With GUI

        # NOTE: When the first screen appears click on 'Start'

from optparse import Values
from time import sleep
import PySimpleGUI as sg
from utils import cor
from icecream import ic

class jogoDeAventura:
    def __init__(self):
        self.faccao1, self.faccao2 = '', ''
        self.totNorte, self.totSul = 0, 0

    def Iniciar(self):

        #Layout 
        layout = [
            [sg.Output(size=(80,15))],
            [sg.Input(size=(40, 2), key='INPUT')],
            [sg.Button('Iniciar'), sg.Button('Responder'), sg.Button('Quit')]
        ]
        #Criar Janela
        self.janela = sg.Window('Jogo de aventura', layout=layout)

        while True:
            self.lerJanela()
            if self.evento == 'Iniciar':
                self.cap1()
                break
            if self.evento == 'Quit':
                self.janela.Close()
                break

        print('Teste finalizado!')
        sleep(1)
        print('CALCULANDO...')
        sleep(1)
        print(f'Parabéns. Você entrou para a Facção {self.minhaFaccao()}.\n Aperte "Iniciar" para ir para o CAPITULO 2.')
        self.lerJanela()
        if self.evento == 'Quit':
                self.janela.close()

        self.cap2(self.faccao1, self.faccao2)

    def lerJanela(self):
        self.evento, self.valores = self.janela.Read()
    
    def minhaFaccao(self):
        return(self.faccao1)
    
    def cap1(self):
        """
        CAPITULO 1
            -> Decidindo a FACÇÃO
        """

        cap1 = '''
                                          CAPITULO 1

            O planeta onde vivemos foi dividido em dois, agora é um mundo de guerras,
            onde duas Facções disputão a liderança do mundo!
            A Facção Norte domina o lado de cima do planeta e a Facção Sul domina o lado de baixo.
            
            Bem na divisa entre os poderes, existem uma pequena ilha, onde quem nasce tem que passar
            por um teste para saber em qual facção irá entrar.

            Você nasceu nesta ilha e agora iremos descobrir para qual facção você irá.

            Aperte em 'Iniciar'
            '''
        print(cap1)
        self.lerJanela()
        if self.evento == 'Quit':
                self.janela.close()
        self.pergunta1 = 'Em qual mês você nasceu? (Responder)\n[Jan/Fev/Mar/Abr/Mai/Jun/Jul/Ago/Set/Out/Nov/Dez]: ' # Jan - Jun -> Norte | Jul - Dez - > Sul
        self.pergunta2 = 'Você prefere espada ou escudos? (Responder)\n[Espada/Escudo]: ' # Espada -> Norte | Escudo -> Sul
        self.pergunta3 = 'Qual a sua especialidade? (Responder)\n[Linha de Frente/Tático]: ' # Linha de frente -> Sul | Tático -> Norte

        print(self.pergunta1)
        while True: # Pergunta 1
            self.lerJanela()
            if self.evento == 'Quit':
                self.janela.close()
            if self.evento == 'Responder':
                r1 = self.valores['INPUT']
                if r1[0:3:] in 'JanFevMarAbrMaiJun':
                    self.totNorte += 1
                    ic(self.totNorte)
                    break
                elif r1[0:3:] in 'JulAgoSetOutNovDez':
                    self.totSul += 1
                    ic(self.totSul)
                    break
                else:
                    print('Por favor escolha uma das opções: [Jan, Fev, Mar, Abr, Mai, Jun, Jul, Ago, Set, Out, Nov ou Dez.')
        
        print(self.pergunta2)

        while True: # Pergunta 2
            self.lerJanela()
            if self.evento == 'Quit':
                self.janela.close()
            if self.evento == 'Responder':
                r2 = self.valores['INPUT']
                if r2[0:3:] in 'Esp':
                    self.totNorte += 1
                    ic(self.totNorte)
                    break
                if r2[0:3:] in 'Esc':
                    self.totSul += 1
                    ic(self.totSul)
                    break
                else:
                    print('Por favor, escolha entre Espada ou Escudo.')
        
        print(self.pergunta3)
        
    
        while True: # Pergunta 3
            self.lerJanela()
            if self.evento == 'Quit':
                self.janela.close()
            if self.evento == 'Responder':
                r3 = self.valores['INPUT']
                if r3[0:3:] in 'Lin':
                    self.totSul += 1
                    ic(self.totSul)
                    break
                if r3[0:3:] in 'TatTát':
                    self.totNorte += 1
                    ic(self.totNorte)
                    break
                else:
                    print('Por favor, escolha entre Espada ou Escudo.')

        if self.totNorte > self.totSul:
            self.faccao1 = 'Norte'
            self.faccao2 = 'Sul'
        else:
            self.faccao1 = 'Sul'
            self.faccao2 = 'Norte'

    def cap2(self, a='Norte', b='Sul'):
        """
        CAPITULO 2
            -> Continuação da história
        """
        cap2 = f'''
                                            CAPITULO 2

            Alguns meses depois de ter entrado para a Facção {a}, depois de muito treinamento
            e estudo, você foi chamado para uma missão, onde teria que adentrar na facção {b}
            e descobrir quais pontos fracos existiam em suas barreiras.
            ...
            Alguns meses depois você tem um relatório completo para entregar para os seus líderes.
            Ao entregar o relatório, a sua facção ({a}) terá grandes chances de derrotar a faccão {b}.
            ...
            Mas, você se apaixonou por uma garota que faz parte da facção {b}, Lilian, você está relutante
            entre entregar o relatório e ter a certeza que sua amada iria morrer no ataque da facção {a}
            ou destruir o relatório e fugir para a facção {b} com sua amada.

            Faça uma sábia escolha!

            Aperte em 'Iniciar'
            '''

        finais = [f'''
                        Parabéns! A Facção {a} venceu a disputa e agora domina o mundo
                        com sabedoria e armonia todos vivem alegres e felizes...

                        Você vive pensando que fez o melhor para o seu povo e o mundo, mas infelizmente
                        lhe custou caro, sente muitas saudades de sua amada Lilian, o que o levou
                        a uma vida triste sem conseguir um novo amor.

                        GAME OVER!
                        ''',
                f'''
                        Que desastre!
                        
                        O relatório que você entregou para seus superiores tinha sido alterado,
                        agentes da facção {b} descobriram que você era da facção {a}
                        e para proteger a Facção {b} eles alteraram todo o seu relatório.

                        Fazendo assim a Facção {b} conseguir parar o ataque da Facção {a} e vercer a guerra!
                        
                        Os líderes da facção {b} prenderam você por ser um espião e nunca mais conseguiu ver a Lilian.

                        GAME OVER!
                        ''',
                f'''
                        Você decidiu destruir o relatório e viver com sua amada Lilian na Facção {b}.

                        Porem, seus superiores ja tinham suspeitado de sua deslealdade e mandaram um segundo
                        agente para lhe investigar, e ao descobrir seus planos de destruir o relatório,
                        ele fez cópias e levou para seus superiores.

                        Em alguns mêses, a Facção {a} fez um ataque brutal. Destruindo todos os postos
                        avançados da facção {b}. Em poucas semanas a Facção {a} conseguiu vencer a guerra.

                        Você tentou fugir com sua amanda, mas a sua traição não ficou impune. Seus líderes
                        prenderam você e sua amanda em prisões diferentes e nunca mais conseguiram se ver.

                        GAME OVER!
                        ''',
                f'''
                        Você decidiu destruir o relatório e viver com sua amada Lilian na Facção {b}.

                        Porem durante suas investigações e comunicação com seus líderes da facção {a},
                        alguns pontos de estratégias tinham sido conversado. 
                        Você tinha sido descoberto por agentes da facção {b} e teve suas ligações grampeadas,
                        tornando possível um ataque suspresa da Facção {b} na Facção {a}.

                        Com isso a Facção {b} consegue vencer a guerra.

                        Você é levado e preso pelos agentes da Facção {b} por ser um espião da Facção {a}
                        e não consegue viver com Lilian.
                        
                        GAME OVER!
                        '''
                ]
        print()
        print(cap2)
        self.lerJanela()
        if self.evento == 'Quit':
                self.janela.close()

        while True:
            print('Entregar relatório ou Destruir relatório? (Responder)\n[Entregar/Destruir]: ')
            self.lerJanela()
            if self.evento == 'Quit':
                self.janela.close()
            if self.evento == 'Responder':
                resCap2 = self.valores['INPUT']
                if resCap2[0:3:] in 'Ent':
                    if a == 'Norte': # Sou do NORTE
                        print(finais[0])
                    else: # Sou do SUL
                        print(finais[1])
                    break
                elif resCap2[0:3:] in 'Des':
                    if a == 'Norte': # Sou do NORTE
                        print(finais[2])
                    else: # Sou do SUL | a = SUL
                        print(finais[3])

                    break
                else: 
                    print('Escolha entre entregar e destruir!')
        self.lerJanela()
        if self.evento == 'Quit':
                self.janela.close()

jogo = jogoDeAventura()
jogo.Iniciar()