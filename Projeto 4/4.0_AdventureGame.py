#Descrição/Description
    # PT-BR
        # Um jogo que faz perguntas ao usuário, as escolhas do usuário o levarão em várias direções,
        # podendo chegar em vários finais distintos.
    # EU
        # A game that asks the user questions, the user's choices will take him in several directions,
        # and can reach several different endings.

from time import sleep
from utils import cor
from icecream import ic

class jogoDeAventura:
    def __init__(self):
        self.faccao1, self.faccao2 = '', ''
        self.totNorte, self.totSul = 0, 0

    def Iniciar(self):

        self.cap1()

        sleep(0.5)
        print('Teste finalizado!')
        sleep(1)
        print('CALCULANDO...')
        sleep(1)
        print(f'Parabéns. você entrou para a Facção {cor(self.minhaFaccao(), 0)}.')
        sleep(2)

        self.cap2(self.faccao1, self.faccao2)

    def minhaFaccao(self):
        return(self.faccao1)
    
    def cap1(self):
        """
        CAPITULO 1
            -> Decidindo a FACÇÃO
        """

        cap1 = '''
            O planeta onde vivemos foi dividido em dois, agora é um mundo de guerras,
            onde duas Facções disputão a liderança do mundo!
            A Facção Norte domina o lado de cima do planeta e a Facção Sul domina o lado de baixo.
            
            Bem na divisa entre os poderes, existem uma pequena ilha, onde quem nasce tem que passar
            por um teste para saber em qual facção irá entrar.

            Você nasceu nesta ilha e agora iremos descobrir para qual facção você irá.
            '''
        print(cap1)

        self.pergunta1 = 'Em qual mês você nasceu?\n[Jan/Fev/Mar/Abr/Mai/Jun/Jul/Ago/Set/Out/Nov/Dez]: ' # Jan - Jun -> Norte | Jul - Dez - > Sul
        self.pergunta2 = 'Você prefere espada ou escudos:\n[Espada/Escudo]: ' # Espada -> Norte | Escudo -> Sul
        self.pergunta3 = 'Qual a sua especialidade?\n[Linha de Frente/Tático]: ' # Linha de frente -> Sul | Tático -> Norte

        while True:
            r1 = input(self.pergunta1).capitalize().strip()
            if r1[0:3:] in 'JanFevMarAbrMaiJun':
                self.totNorte += 1
                break
            elif r1[0:3:] in 'JulAgoSetOutNovDez':
                self.totSul += 1
                break
            else:
                print('Por favor escolha uma das opções: [Jan, Fev, Mar, Abr, Mai, Jun, Jul, Ago, Set, Out, Nov ou Dez.')
        while True:
            r2 = input(self.pergunta2).capitalize().strip()
            if r2[0:3:] in 'Esp':
                self.totNorte += 1
                break
            if r2[0:3:] in 'Esc':
                self.totSul += 1
                break
            else:
                print('Por favor, escolha entre Espada ou Escudo.')
        while True:
            r3 = input(self.pergunta3).capitalize().strip()
            if r3[0:3:] in 'Lin':
                self.totSul += 1
                break
            if r3[0:3:] in 'TatTát':
                self.totNorte += 1
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
            Alguns meses depois de ter entrado para a Facção {cor(a, 0)}, depois de muito treinamento
            e estudo, você foi chamado para uma missão, onde teria que adentrar na facção {cor(b, 1)}
            e descobrir quais pontos fracos existiam em suas barreiras.
            ...
            Alguns meses depois você tem um relatório completo para entregar para os seus líderes.
            Ao entregar o relatório, a sua facção ({cor(a, 0)}) terá grandes chances de derrotar a faccão {cor(b, 1)}.
            ...
            Mas, você se apaixonou por uma garota que faz parte da facção {cor(b, 1)}, Lilian, você está relutante
            entre entregar o relatório e ter a certeza que sua amada iria morrer no ataque da facção {cor(a, 0)}
            ou destruir o relatório e fugir para a facção {cor(b, 1)} com sua amada.

            Faça uma sábia escolha:
            '''

        finais = [f'''
                        Parabéns! A Facção {cor(a, 0)} venceu a disputa e agora domina o mundo
                        com sabedoria e armonia todos vivem alegres e felizes...

                        Você vive pensando que fez o melhor para o seu povo e o mundo, mas infelizmente
                        lhe custou caro, sente muitas saudades de sua amada Lilian, o que o levou
                        a uma vida triste sem conseguir um novo amor.

                        GAME OVER!
                        ''',
                f'''
                        Que desastre!
                        
                        O relatório que você entregou para seus superiores tinha sido alterado,
                        agentes da facção {cor(b, 1)} descobriram que você era da facção {cor(a, 0)}
                        e para proteger a Facção {cor(b, 1)} eles alteraram todo o seu relatório.

                        Fazendo assim a Facção {cor(b, 1)} conseguir parar o ataque da Facção {cor(a, 0)} e vercer a guerra!
                        
                        Os líderes da facção {cor(b, 1)} prenderam você por ser um espião e nunca mais conseguiu ver a Lilian.

                        GAME OVER!
                        ''',
                f'''
                        Você decidiu destruir o relatório e viver com sua amada Lilian na Facção {cor(b, 1)}.

                        Porem, seus superiores ja tinham suspeitado de sua deslealdade e mandaram um segundo
                        agente para lhe investigar, e ao descobrir seus planos de destruir o relatório,
                        ele fez cópias e levou para seus superiores.

                        Em alguns mêses, a Facção {cor(a, 0)} fez um ataque brutal. Destruindo todos os postos
                        avançados da facção {cor(b, 1)}. Em poucas semanas a Facção {cor(a, 0)} conseguiu vencer a guerra.

                        Você tentou fugir com sua amanda, mas a sua traição não ficou impune. Seus líderes
                        prenderam você e sua amanda em prisões diferentes e nunca mais conseguiram se ver.

                        GAME OVER!
                        ''',
                f'''
                        Você decidiu destruir o relatório e viver com sua amada Lilian na Facção {cor(b, 1)}.

                        Porem durante suas investigações e comunicação com seus líderes da facção {cor(a, 0)},
                        alguns pontos de estratégias tinham sido conversado. 
                        Você tinha sido descoberto por agentes da facção {cor(b, 1)} e teve suas ligações grampeadas,
                        tornando possível um ataque suspresa da Facção {cor(b, 1)} na Facção {cor(a, 0)}.

                        Com isso a Facção {cor(b, 1)} consegue vencer a guerra.

                        Você é levado e preso pelos agentes da Facção {cor(b, 1)} por ser um espião da Facção {cor(a, 0)}
                        e não consegue viver com Lilian.
                        
                        GAME OVER!
                        '''
                ]
        
        print(cap2)

        while True:
            resCap2 = input('Entregar relatório ou Destruir relatório? ').capitalize().strip()
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


jogo = jogoDeAventura()
jogo.cap2()