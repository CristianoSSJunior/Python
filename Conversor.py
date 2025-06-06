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
cotad = float(5.58)

print("Se você quiser converter do Dólar para o Real, digite 1. \nCaso queira converter do Real para o Dólar, digite 2.\n")
opcao = int(input(':'))
print('\n')

if(opcao ==1):
     print("Converter Dólar($) -> Real(R$).\nDigite o valor em real:")
     valor1 = float(input())
     if(valor1 >= 2):
          print(valor1,' reais valem ',d(valor1), ' dólares.')
     elif(valor1 <= 1):
         print(valor1, ', real vale ',d(valor1),' dólares.')
          

elif(opcao ==2):
     print("Converter Real(R$) -> Dólar($).\nDigite o valor em dólar:")
     valor2 = float(input())
     if(valor2 <= 1):
          print('{:.2f} dólar vale {:.2f} reais.'.format(r(valor2)))
     elif(valor2 >= 2):
          print(valor2,' dólares valem ',r(valor2),' reais.')     

