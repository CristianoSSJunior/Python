#Criar uma função que crie novos números infinitamente e imprima-os na tela, com a opção de parar a execução.
import os
import requests

def limpa_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def gerar_numeros():
    n = 0
    while True:
        yield n
        n += 1

#Função que gera números infinitamente, mas não é táo eficiente
def gerar_numeros_pesado():

    lista_numeros = [x for x in range(9999999)] # Gerador infinito de números
    print(lista_numeros)
    return lista_numeros

def option_menu():
    while True:
        print("1- Opção 1: Criação otimizada")
        print("2- Opção 2: Criação pesada")
        opcao = input("Escolha uma opção (1 ou 2):").strip()
        if opcao in ('1','2'):
            return int(opcao)
        print("Opção inválida. Tente novamente. \n")

def Gerar(opcao):
    while True:
        try:
            if(opcao ==1):
                return gerar_numeros()
            else:
                return gerar_numeros_pesado()
            break
        except ValueError:
            print("Entrada inválida. Tente novamente.")

        
def main():
    limpa_tela()
    print("Gerador de números infinitos.\n")
    opcao = option_menu()

    for numero in Gerar(opcao):
        print(numero)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExecução interrompida pelo usuário.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        print("Programa finalizado.")