# Jogo da Forca em Python!!!!!!!!!!!!!!!!!!!!!!
#versão: 2.0.0

import random
from os import system,name 

def limpa_tela():
	#windows
	if name == 'nt':
		_= system('cls')

	#Mac ou Linux
	else:
		_= system('clear') 

#Função que desenha a forca na tela
def mostrar_enforcado(chances):
	# Lista de estágios da forca
	stages = [
	# Estágio 6 (final)
	'''
	__________
	|	 |
	|	 0
	|  \\|/
	|	 |
	|	/ \\
	_
	''''',
	# Estágio 5
	'''
	__________
	|	 |
	|	 0
	|       \\|/	
	|	 |
	|	/
	_
	''''',
	''''''
	# Estágio 4
	'''
	__________
	|	 |
	|	 0
	|  	\\|/
	|	 |
	|
	_
	''''',
	# Estágio 3
	'''
	__________
	|	 |
	|	 0
	|       \\|
	|	 |
	|
	_
	''''',
	# Estágio 2
	'''
	__________
	|	 |
	|	 0
	|	 |
	|	 |
	|
	_
	''''',
	# Estágio 1
	'''
	__________
	|	 |
	|	 0
	|
	|
	|
	_
	''''',
	# Estágio 0
	'''
	__________
	|        |
	|
	|
	|
	|
	_
	''''',
]
	return stages[chances]

# Função do jogo
def game():

	limpa_tela()
	print("\nEste é o jogo da forca em Python!")
	print("Adivinhe a palavra abaixo:\n")

	print("TEMA: cores\n")
	print("\n---------------------------\n")


	palavras = ['azul','laranja','roxo','rosa','marrom','amarelo','branco','preto',
	'cinza']

	palavra = random.choice(palavras)

	# list comprehension
	letras_descobertas = ['_' for letra in palavra]
	tabuleiro = letras_descobertas

	chances = 6

	letras_erradas = []

	while chances > 0:

		print(mostrar_enforcado(chances))
		print("Palavra: ", tabuleiro)
		print("Letras erradas:"," ".join(letras_erradas))



		# Tentativa
		tentativa = input("Digite uma letra: ").lower()
		print("\n---------------------------\n")

		# Condicional (1°)

		if tentativa in palavra:
			index = 0
			for letra in palavra:
				if tentativa == letra:
					letras_descobertas[index] = letra
				index += 1
		else:
			chances -= 1
			letras_erradas.append(tentativa)

		# Condicional (2°)
		if "_" not in letras_descobertas:
			print("\nVocê venceu, a palavra era:", palavra)
			print("\n---------------------------\n")
			break

		

	# Condicional (3°)
	if "_" in letras_descobertas:
		print("\nVocê perdeu, a palavra era:", palavra)
		print("\n---------------------------\n")

# Bloco main
if __name__ == "__main__":
	game()
	print("\nParabéns, você está aprendendo programação em Python. :)\n")