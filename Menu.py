from os import system #limpar "system("clear")"

def escreva(frase):
    msg = (len(frase) + 4) *  '-'
    print(frase)
    print(msg)

def menu():
    print('--------- MENU PRINCIPAL ----------')
    print(f'{escreva('  [1] - Listar candidatos ')}')
    print(f'{escreva('  [2] - Saber informações ')}')
    print(f'{escreva('  [3] - Gerar estatísticas')}')
    print(f'{escreva('  [4] - Sair')}')
menu() 
opcao =  input('Escolha um número =>  ')
while opcao != '1234':
   print('Número inválido =(\n Tente novamente!')
   opcao = input('Esolha um número =>  ' )
else:
  if opcao == '1':
    system("clear")
   #listar_candidatos() - Funções a serem implementadas
elif opcao == '2': 
   system("clear")
   #exibir_informações()      ''
elif opcao == '3':
   system("clear")
    #gerar_estatisticas()     ''
elif opcao == '4':
    system("clear")

    exit()
    #break
