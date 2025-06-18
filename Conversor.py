#Data: 18/06/2025
import os
import requests

def limpa_tela():
     os.system('cls' if os.name == 'nt' else 'clear')
 
#Funções para a conversão
def converter_real(valor_real: float,cotacao: float) -> float: 
    return valor_real * cotacao
    
def converter_dolar(valor_dolar,cotacao):
     return valor_dolar / cotacao

def obter_opcao():
     while True:
          limpa_tela()
          print("1- Se você quiser converter do Dólar($) para o Real(R$)")
          print("2- Se você quiser converter do Real(R$) para o Dólar($)\n")
          opcao = input('Digite 1 ou 2: ').strip()
          if opcao in ('1','2'):
               return int(opcao)
          print("Opção inválida. Tente novamente.\n")

def converter(opcao):
     while True:
          try:
               print('\n------------------------|**|----------------------------')
               cotacao = obter_cotacao() #Valor da cota do dólar:
               print(f"\nA cotação atual do dólar é de R${cotacao:.2f}")

               #Variável para converter dólar para Real
               if(opcao == 1):
                    print("\nConverter Dólar($) -> Real(R$).\nDigite o valor em dólar:\n")
                    valor_dolar = float(input('$'))
                    if(valor_dolar >= 2):
                         print(f'\n${valor_dolar:.2f} dólares valem R${converter_real(valor_dolar,cotacao):.2f} reais.')
                    elif(valor_dolar <= 1):
                         print(f'\n${valor_dolar:.2f} dólar vale R${converter_real(valor_dolar,cotacao):.2f} reais.')      

                    #Variável para converter Real para dólar.
               elif (opcao == 2):
                         print("\nConverter Real(R$) -> Dólar($).\nDigite o valor em real:\n")
                         valor_real = float(input('R$'))
                         if(valor_real <= 1):
                              print(f'\nR${valor_real:.2f} real vale ${converter_dolar(valor_real,cotacao):.2f} dólares.')
                         elif(valor_real >= 2):
                              print(f'\nR${valor_real:.2f} reais valem ${converter_dolar(valor_real,cotacao):.2f} dólares.')  

               else:
                         print("\nOpção inválida.")
                         continue
               break
          
          except ValueError:
               print("\nEntrada inválida. Tente novamente.")

def obter_cotacao():
     try:
          resposta = requests.get("https://economia.awesomeapi.com.br/json/last/USD-BRL")
          resposta.raise_for_status()
          return float(resposta.json()['USDBRL']['bid'])
     except Exception as e:
          print(f'Erro ao obter cotação: {e}')
          return 5.5 # Valor padrão em caso de falha na requisição

#Função do conversor
def main():
     deNovo = 'y'
     while deNovo == 'y':

          limpa_tela() #Função para limpar a tela.

          opcao = obter_opcao() #Função para obter uma opção.

          converter(opcao) #Função para converter os valores.

          while True:
               deNovo = input("\nQuer converter novamente? (y/n): ").strip().lower()
               if deNovo in ('y', 'n'):
                    break
               print('\nOpção inválida. Tente novamente.')

#Executa o conversor:
if __name__ == '__main__':
     main()
#FINALIZADO dia 18/06/2025