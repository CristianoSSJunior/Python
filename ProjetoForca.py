# Jogo da Forca em Python!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#versão: 3.0.0
# Programação Orientada a Objetos

# Import
import random
from os import system,name

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+ 
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']

def limpa_tela(self):
     #windows
     if name == 'nt':
           _= system('cls')

     #Mac ou Linux
     else:
          _= system('clear')
# Classe
class Hangman:

	# Método Construtor

	# Método para adivinhar a letra
	
	# Método para verificar se o jogo terminou
		
	# Método para verificar se o jogador venceu
		
	# Método para não mostrar a letra no board
		
	# Método para checar o status do game e imprimir o board na tela

     def __init__(self,palavra):
          self.palavra = palavra
          self.letras_erradas = []
          self.letras_descobertas = []

     def adivinhar(self,letra):

          if letra in self.palavra and letra not in self.letras_descobertas:
               self.letras_descobertas.append(letra)

          elif letra not in self.palavra and letra not in self.letras_erradas:
               self.letras_erradas.append(letra)

          else:
               return False

          return True 

     def jogo_terminou(self):

          return self.jogador_venceu() or (len(self.letras_erradas) == 6)

     def jogador_venceu(self):
          if "_" not in self.hide_words():
               return True
          return False

     def hide_words(self):
          rtn = ''

          for letra in self.palavra:
               if letra not in self.letras_descobertas:
                    rtn += '_'
               else:
                    rtn += letra
          return rtn

     # Método para
     def print_game_status(self):

          print(board[len(self.letras_erradas)])

          print('\nPalavra: ' + self.hide_words())

          print('\nLetras erradas: ',)           

          for letra in self.letras_erradas:
               print(letra,)

          print ()

          print('Letras corretas: ',)

          for letra in self.letras_descobertas:
               print(letra,)

          print('\n----------------------------------')     

          print()

def random_word():
     palavras = ['azul','laranja','roxo','rosa','marrom','amarelo','branco','preto',
     'cinza']

     palavra = random.choice(palavras)
     return palavra

def main():

     limpa_tela('self')

     game = Hangman(random_word())

     while not game.jogo_terminou():
          game.print_game_status()

          # Recebe input do terminal
          user_input = input('\nDigite uma letra: ')

          game.adivinhar(user_input)

     game.print_game_status()

     # De acordo com os status, imprime mensagem na tela para o usuário
     if game.jogador_venceu():
          print('\nParabéns! Você venceu!!')

     else:
          print('\nGame over! Você perdeu.')
          print('A palavra era ' + game.palavra)

     print('\nFoi bom jogar com você! Agora estude mais!\n')

#Executa o programa
if __name__ == "__main__":
     main()