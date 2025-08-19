#Criado dia 18/06/2025
from os import system,name

list=[ 1,4,7,3,9,2,5,8,6,10,12,15,11,13,14,19,18,16,17]

def limpa_tela(self):
     #windows
     if name == 'nt':
           _= system('cls')

     #Mac ou Linux
     else:
          _= system('clear')

#Organizador de código
def organizar_lista(list):
    #Organiza a lista em ordem crescente
    list.sort()
    return list

def organizar_lista_decrescente(list):
    #Organiza a lista em ordem decrescente
    list.sort(reverse=True)
    #Retorna a lista organizada
    return list

def organizar_lista_aleatoria(list):
    import random
    #Organiza a lista de forma aleatória
    random.shuffle(list)
    return list

def organizar_lista_pares(list):
    #Organiza a lista com somente os números pares
    list[:] = [x for x in list if x % 2 == 0]
    #Organiza a lista em ordem decrescente
    list.sort(reverse=True,key=lambda x: x % 2)
    return list

def main():
    limpa_tela('self')
    print("Lista original:", list)
    organizar_lista(list)
    print("Lista organizada:", list)
    organizar_lista_decrescente(list)
    print("Lista organizada em ordem decrescente:", list)
    organizar_lista_pares(list)
    print("Lista organizada com os números pares:", list)
    organizar_lista_aleatoria(list)
    print("Lista organizada de forma aleatória:", list)

#Executa a função
if __name__ == "__main__":
    main()
