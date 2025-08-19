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

def main():
    limpa_tela()
    for numero in gerar_numeros():
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
