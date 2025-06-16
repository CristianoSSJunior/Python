from os import system,name

def limpa_tela():
     #windows
     if name == 'nt':
           _= system('cls')

     #Mac ou Linux
     else:
          _= system('clear')

def r(valor_real,cotad):
    return valor_real * cotad
    
def d(valor_dolar,cotad):
     return valor_dolar / cotad

deNovo = 'y'
while deNovo == 'y':
     while True:
          try:

               limpa_tela()
               cotad = float(5.56)
               print("Se você quiser converter do Dólar para o Real, digite 1. \nCaso queira converter do Real para o Dólar, digite 2.\n")
               opcao = int(input(':'))

               if(opcao == 1):
                    print("\nConverter Dólar($) -> Real(R$).\nDigite o valor em dólar:\n")
                    valor_dolar = float(input())
                    if(valor_dolar >= 2):
                         print(f'\n${valor_dolar:.1f} dólares valem R${r(valor_dolar,cotad):.2f} reais.')
                    elif(valor_dolar <= 1):
                         print(f'\n${valor_dolar:.1f} dólar vale R${r(valor_dolar,cotad):.2f} reais.')      

               elif (opcao == 2):
                    print("\nConverter Real(R$) -> Dólar($).\nDigite o valor em real:\n")
                    valor_real = float(input())
                    if(valor_real <= 1):
                         print(f'\nR${valor_real:.1f} real vale ${d(valor_real,cotad):.2f} dólares.')
                    elif(valor_real >= 2):
                         print(f'\nR${valor_real:.1f} reais valem ${d(valor_real,cotad):.2f} dólares.')  

               else:
                    print("\nOpção inválida.")
                    continue

               break
          
          except ValueError:
               print("\nEntrada inválida. Tente novamente")
     
     deNovo = (input("\nQuer converter novamente?(y/n):")).lower()
     if deNovo not in ('y', 'n'):
          print('Opção inválida. Tente novamente.')
          deNovo = 'y'
     elif deNovo == 'n':
          break
               
                    
          
     
