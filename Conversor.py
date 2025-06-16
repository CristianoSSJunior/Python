from os import system,name

def limpa_tela():
     #windows
     if name == 'nt':
           _= system('cls')

     #Mac ou Linux
     else:
          _= system('clear')

#Funções para a conversão
def r(valor_real,cotacao):
    return valor_real * cotacao
    
def d(valor_dolar,cotacao):
     return valor_dolar / cotacao

#Função do conversor
def main():
     #Valor da cota do dólar:
     cotacao = float(5.56)

     deNovo = 'y'
     while deNovo == 'y':
          while True:
               try:

                    limpa_tela()
                    print("1- Se você quiser converter do Dólar($) para o Real. \n2- Caso queira converter do Real(R$) para o Dólar.\n")
                    opcao = int(input('Digite 1 ou 2: '))

                    #Variável para converter dólar para Real
                    if(opcao == 1):
                         print("\nConverter Dólar($) -> Real(R$).\nDigite o valor em dólar:\n")
                         valor_dolar = float(input('$'))
                         if(valor_dolar >= 2):
                              print(f'\n${valor_dolar:.2f} dólares valem R${r(valor_dolar,cotacao):.2f} reais.')
                         elif(valor_dolar <= 1):
                              print(f'\n${valor_dolar:.2f} dólar vale R${r(valor_dolar,cotacao):.2f} reais.')      

                    #Variável para converter Real para dólar.
                    elif (opcao == 2):
                         print("\nConverter Real(R$) -> Dólar($).\nDigite o valor em real:\n")
                         valor_real = float(input('R$'))
                         if(valor_real <= 1):
                              print(f'\nR${valor_real:.2f} real vale ${d(valor_real,cotacao):.2f} dólares.')
                         elif(valor_real >= 2):
                              print(f'\nR${valor_real:.2f} reais valem ${d(valor_real,cotacao):.2f} dólares.')  

                    else:
                         print("\nOpção inválida.")
                         continue

                    break
          
               except ValueError:
                    print("\nEntrada inválida. Tente novamente")
     
          deNovo = (input("\nQuer converter novamente?(y/n): ")).lower()
          if deNovo not in ('y', 'n'):
               print('Opção inválida. Tente novamente.')
               deNovo = 'y'
          elif deNovo == 'n':
               break

#Executa o conversor:
if __name__ == '__main__':
          main()