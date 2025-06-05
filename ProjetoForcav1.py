# Jogo da Forca em Python!!!!!!!
#versão: 1.0.0

import random
from os import system,name 

def limpa_tela():
	#windows
	if name == 'nt':
		_= system('cls')

	#Mac ou Linux
	else:
		_= system('clear') 

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

	chances = 6

	letras_erradas = []

	while chances > 0:

		print(" ".join(letras_descobertas))
		print("\nChances restantes:", chances)
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
	print("\nParabéns, você está aprendendo programação em Python com a DSA. :)\n")
