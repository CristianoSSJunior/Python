from os import system,name

def limpa_tela(self):
     #windows
     if name == 'nt':
           _= system('cls')

     #Mac ou Linux
     else:
          _= system('clear')


def r(valor1):
    valorfinal =  valor1 * cotad
    return valorfinal
    
def d(valor2):
   valorfinal2 = valor2 / cotad
   return valorfinal2

limpa_tela('self')
cotad = float(5.56)

print("Se você quiser converter do Dólar para o Real, digite 1. \nCaso queira converter do Real para o Dólar, digite 2.\n")
opcao = int(input(':'))
print('\n')

if(opcao ==1):
     print("Converter Dólar($) -> Real(R$).\nDigite o valor em real:")
     valor1 = float(input())
     if(valor1 >= 2):
          print(f'{valor1:.1f} reais valem {d(valor1):.2f} dólares.')
     elif(valor1 <= 1):
         print(f'{valor1:.1f} real vale {d(valor1):.2f} dólares.')
          

elif(opcao ==2):
     print("Converter Real(R$) -> Dólar($).\nDigite o valor em dólar:")
     valor2 = float(input())
     if(valor2 <= 1):
          print(f'{valor2:.1f} dólar vale {r(valor2):.2f} reais.')
     elif(valor2 >= 2):
          print(f'{valor2:.1f} dólares valem {r(valor2):.2f} reais.')     

