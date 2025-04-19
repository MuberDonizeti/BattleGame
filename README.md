# Jogo de Batalha

## Descrição
O projeto foi desenvolvido em Python , uma linguagem de programação de alto nível, interpretada e multiparadigma que é amplamente utilizada para diversos propósitos, desde scripts simples até aplicações complexas.

### Características da Linguagem no Projeto:
1. Orientação a Objetos (OOP): 
   - O código utiliza classes ( personagem , heroi , inimigo , jogo ) para estruturar a lógica do jogo.
   - Herança ( heroi e inimigo herdam de personagem ).
   - Encapsulamento (atributos privados como __vida , __energia , métodos como get_nome() ).
2. Módulos e Bibliotecas:  
   - random é usado para gerar números aleatórios (dano dos ataques, ações do inimigo).
3. Funcionalidades Principais:
   - Sistema de Batalha:
     - Turnos entre herói e inimigo.
     - Diferentes tipos de ataques (normal, especial, crítico).
     - Cura e regeneração de energia.
   - Progressão:
     - O herói sobe de nível após derrotar inimigos.
   - Interação com o Usuário:
     - Menu de ações via input() .
     - Exibição de status ( exibirDetalhes() ).
4. Tratamento de Dados: 
   - Uso de dicionários ( self.inimigos ) para armazenar informações dos inimigos.
5. Lógica de Jogo:
   - Loop principal ( while ) controla a batalha até a vitória ou derrota.

## Instalação
1. Clone o repositório para sua máquina local.
2. Certifique-se de ter o Python instalado.
3. Execute o arquivo `jogo.py` para iniciar o jogo.

## Regras do Jogo
- O herói começa com 100 de vida e pode escolher entre 5 ações em cada turno.
- Cada inimigo tem um nome, vida e tipo diferentes.
- O jogo termina quando o herói derrota todos os inimigos ou é derrotado.

## Como Jogar
1. Execute o jogo.
2. Escolha uma ação para o herói em cada turno:
   - Ataque Normal
   - Ataque Especial
   - Ataque Crítico
   - Curar
   - Regenerar Energia
3. Derrote todos os inimigos para vencer o jogo.

## Créditos
Desenvolvido por [DoniDev].