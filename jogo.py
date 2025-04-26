
import random
# personagem = classe mãe
class personagem:
    def __init__(self, nome, vida, nivel) -> None:
        self.__nome = nome
        self.__vida = vida
        self.__nivel = nivel

    #ja que os dados são privados é necessario criar os getters para acessar as informações em outra classe
    def get_nome(self):
        return self.__nome
    def get_vida(self):
        return self.__vida
    def get_nivel(self):
        return self.__nivel
    
    def exibirDetalhes(self):
        return f'Nome: {self.get_nome()}\nVida: {self.get_vida()}\nNivel: {self.get_nivel()}'
    
    def receberAtaque(self, dano):
        self.__vida -= dano
        if self.__vida < 0:
            self.__vida = 0
    def atacar(self, alvo):
        dano = random.randint(self.get_nivel() * 2, self.get_nivel() * 4)
        alvo.receberAtaque(dano)
        print(f'{self.get_nome()} atacou {alvo.get_nome()} e causou {dano} pontos de dano \n')
    

#heroi = controlado pelo usuario
class heroi(personagem):
    def __init__(self, nome, vida, nivel, habilidade) -> None:
        super().__init__(nome, vida, nivel)
        self.nome = nome
        self.__habilidade = habilidade
        self.__energia = 50
        self.__energia_max = 50

    def get_habilidade(self):
        return self.__habilidade
    
    def get_energia(self):
        return self.__energia
    
    def exibirDetalhes(self):
        return f'{super().exibirDetalhes()}\nHabilidade: {self.get_habilidade()}\nEnergia: {self.get_energia()}/{self.__energia_max}\n'
    
    def ataqueEspecial(self, alvo):
        custo_energia = 20
        if self.__energia >= custo_energia:
            dano = random.randint(self.get_nivel() * 4, self.get_nivel() * 6)
            alvo.receberAtaque(dano)
            self.__energia -= custo_energia
            print(f'{self.get_nome()} usou a habilidade especial {self.get_habilidade()} em {alvo.get_nome()} e causou {dano} de dano.')
        else:
            print(f'Energia insuficiente! Necessário {custo_energia} de energia.')
    
    def ataqueCritico(self, alvo):
        custo_energia = 30
        if self.__energia >= custo_energia:
            dano = random.randint(self.get_nivel() * 6, self.get_nivel() * 8)
            alvo.receberAtaque(dano)
            self.__energia -= custo_energia
            print(f'{self.get_nome()} usou Ataque Crítico em {alvo.get_nome()} e causou {dano} de dano.')
        else:
            print(f'Energia insuficiente! Necessário {custo_energia} de energia.')
    
    def curar(self):
        custo_energia = 40
        if self.__energia >= custo_energia:
            cura = random.randint(self.get_nivel() * 5, self.get_nivel() * 10)
            self._personagem__vida = min(100, self.get_vida() + cura)
            self.__energia -= custo_energia
            print(f'{self.get_nome()} se curou em {cura} pontos de vida.')
        else:
            print(f'Energia insuficiente! Necessário {custo_energia} de energia.')
    
    def regenerarEnergia(self):
        regeneracao = 20
        self.__energia = min(self.__energia_max, self.__energia + regeneracao)
        print(f'{self.get_nome()} recuperou {regeneracao} pontos de energia.')
    
#inimigo = adversario
class inimigo(personagem):
    def __init__(self, nome, vida, nivel, tipo) -> None:
        super().__init__(nome, vida, nivel)
        self.nome = nome
        self.__tipo = tipo
        self.__energia = 50
        self.__energia_max = 50

    def get_tipo(self):
        return self.__tipo
    
    def get_energia(self):
        return self.__energia
    
    def exibirDetalhes(self):
        return f'{super().exibirDetalhes()}\nTipo: {self.get_tipo()}\nEnergia: {self.get_energia()}/{self.__energia_max}\n'
    
    def ataqueFurtivo(self, alvo):
        custo_energia = 25
        if self.__energia >= custo_energia:
            dano = random.randint(self.get_nivel() * 4, self.get_nivel() * 6)
            alvo.receberAtaque(dano)
            self.__energia -= custo_energia
            print(f'{self.get_nome()} usou Ataque Furtivo em {alvo.get_nome()} e causou {dano} de dano.')
        else:
            self.atacar(alvo)
    
    def investidaPoderosa(self, alvo):
        custo_energia = 35
        if self.__energia >= custo_energia:
            dano = random.randint(self.get_nivel() * 6, self.get_nivel() * 8)
            alvo.receberAtaque(dano)
            self.__energia -= custo_energia
            print(f'{self.get_nome()} usou Investida Poderosa em {alvo.get_nome()} e causou {dano} de dano.')
        else:
            self.atacar(alvo)
    
    def regenerarEnergia(self):
        regeneracao = 20
        self.__energia = min(self.__energia_max, self.__energia + regeneracao)
        print(f'{self.get_nome()} recuperou {regeneracao} pontos de energia.')

    

class jogo:
    """classe orquestradora do jogo"""
    def __init__(self) -> None:
        self.heroi = heroi(nome='guerreiro', vida=100, nivel=1, habilidade='super Força')
        self.inimigos = [
            {'nome': 'Morcego', 'vida': 60, 'nivel': 1, 'tipo': 'Voador'},
            {'nome': 'Goblin', 'vida': 70, 'nivel': 2, 'tipo': 'Terrestre'},
            {'nome': 'Esqueleto', 'vida': 80, 'nivel': 3, 'tipo': 'Morto-vivo'},
            {'nome': 'Bruxa', 'vida': 100, 'nivel': 4, 'tipo': 'Mágico'},
            {'nome': 'Dragão', 'vida': 120, 'nivel': 5, 'tipo': 'Dragão'}
        ]
        self.inimigo_atual = 0
        self.inimigo = None

    def proximo_inimigo(self):
        if self.inimigo_atual < len(self.inimigos):
            dados_inimigo = self.inimigos[self.inimigo_atual]
            self.inimigo = inimigo(nome=dados_inimigo['nome'], 
                                 vida=dados_inimigo['vida'], 
                                 nivel=dados_inimigo['nivel'], 
                                 tipo=dados_inimigo['tipo'])
            return True
        return False

    def iniciarBatalha(self):
        print('''
        Bem-vindo à Arena de Batalha!\n
        Regras do jogo:
        - Cada inimigo aparecerá com um nome, vida e tipo.
        - O herói terá 100 de vida e poderá escolher entre 5 ações:
            1 - Ataque Normal: causará dano aleatório entre 2 e 4 vezes o nível do herói.
            2 - Ataque Especial: causará dano aleatório entre 4 e 6 vezes o nível do herói.
            3 - Ataque Crítico: causará dano aleatório entre 6 e 8 vezes o nível do herói.
            4 - Curar: restaurará 5 a 10 vezes o nível do herói de vida.
            5 - Regenerar Energia: restaurará 20 pontos de energia.\n''')
        
        while self.proximo_inimigo():
            print(f'\nInimigo {self.inimigo_atual + 1}: {self.inimigos[self.inimigo_atual]["nome"]} apareceu!')
            
            while self.heroi.get_vida() > 0 and self.inimigo.get_vida() > 0:
                print(f'\nDetalhes da batalha: ')
                print(self.heroi.exibirDetalhes())
                print(self.inimigo.exibirDetalhes())

                input('Pressione Enter para continuar...')
                print('\nEscolha sua ação:')
                print('1 - Ataque Normal')
                print('2 - Ataque Especial (20 energia)')
                print('3 - Ataque Crítico (30 energia)')
                print('4 - Curar (40 energia)')
                print('5 - Regenerar Energia')
                escolha = input('Sua escolha: ')
                print('\n')
                if escolha == '1':
                    self.heroi.atacar(self.inimigo)
                elif escolha == '2':
                    self.heroi.ataqueEspecial(self.inimigo)
                elif escolha == '3':
                    self.heroi.ataqueCritico(self.inimigo)
                elif escolha == '4':
                    self.heroi.curar()
                elif escolha == '5':
                    self.heroi.regenerarEnergia()
                else:
                    print('Escolha inválida, tente novamente')
                    continue

                if self.inimigo.get_vida() > 0:
                    # Lógica de ação do inimigo
                    acao_inimigo = random.randint(1, 4)
                    if acao_inimigo == 1:
                        self.inimigo.atacar(self.heroi)
                    elif acao_inimigo == 2:
                        self.inimigo.ataqueFurtivo(self.heroi)
                    elif acao_inimigo == 3:
                        self.inimigo.investidaPoderosa(self.heroi)
                    else:
                        self.inimigo.regenerarEnergia()
            
            if self.heroi.get_vida() <= 0:
                print('\nVocê foi derrotado! Fim de jogo!')
                break
            else:
                print(f'\nParabéns! Você derrotou o {self.inimigos[self.inimigo_atual]["nome"]}!')
                # Aumenta o nível do herói após cada vitória
                self.heroi._personagem__nivel += 1
                # Restaura vida e energia do herói
                self.heroi._personagem__vida = 100
                self.heroi._heroi__energia = 50
                print(f'Seu herói subiu para o nível {self.heroi.get_nivel()}!')
                print('Vida e energia do herói foram completamente restauradas!')
                self.inimigo_atual += 1
                
                if self.inimigo_atual < len(self.inimigos):
                    input('\nPressione Enter para enfrentar o próximo inimigo...')
                else:
                    print('\nParabéns! Você venceu todos os inimigos e completou o jogo!')

# criar instancia do jogo e iniciar a batalha
jogo = jogo()
jogo.iniciarBatalha()