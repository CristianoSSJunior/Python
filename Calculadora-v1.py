def soma(num1,num2): 
	resulSoma = num1 + num2
	return resulSoma
	
def sub(num1,num2):
	resulSub = num1 - num2
	return resulSub

def mult(num1,num2):
	resulMult = num1 * num2
	return resulMult

def div(num1,num2):
	resulDiv = num1 / num2
	return resulDiv

def poten(num1,num2):
	resulPoten = num1 ** num2
	return resulPoten


print("\n--------------- Calculadora em Python ---------------")

deNovo = 'y'
while deNovo == 'y':

	while True:
		try:
			print("\nSelecione a operação matemática desejada: ")
			print("\n1 - Soma \n2 - Subtração \n3 - Multiplicação \n4 - Divisão \n5 - Potenciação")			
		
			opcao = int(input("\nDigite a sua opção: "))
			if opcao in[1,2,3,4,5]:
				break
			else:
				print("\n----------------------------------------------------")
				print("\nOpção inválida, tente novamente.")
		except ValueError:
			print("\n----------------------------------------------------")
			print("\nEntrada inválida, digite um número entre 1 a 5!") 

	print("\n----------------------------------------------------")

	while True:
		try:

			num1 = float(input("\nDigite o primeiro número: "))
			num2 = float(input("\nDigite o segundo número: "))
			break
		except ValueError:
			print("Entrada inválida! Por favor, tente novamente.")

	if opcao == 1:		

		resulSoma = soma(num1,num2)
		print(num1, " + ", num2, " = ", soma(num1,num2))

	elif opcao == 2:

		resulSub = sub(num1,num2)
		print(num1, " - ", num2, " = ", sub(num1,num2))

	elif opcao == 3:

		resulMult = mult(num1,num2)
		print(num1, " x ", num2, " = ", mult(num1,num2))

	elif opcao == 4:
		if num2 != 0:

			resulDiv = div(num1,num2)
			print(num1," ÷ ", num2, " = ", div(num1,num2))
		else:
			print("Não é possível dividir por zero.")

	elif opcao == 5:

		resulPoten = poten(num1,num2)
		print(num1," ** ", num2, " = ", poten(num1,num2))

	deNovo = str(input("\nDeseja fazer outra conta? (y/n): ")).lower()
	if deNovo == 'n':
		break