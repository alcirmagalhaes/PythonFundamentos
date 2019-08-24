# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

def somar(x,y):
	result = x + y
	print("\n %d + %d = %d" %(x,y, result))

def subtrair(x,y):
	result = x - y
	print("\n %d - %d = %d" %(x,y, result))

def multiplicar(x,y):
	result = x * y
	print("\n %d * %d = %d" %(x,y, result))

def dividir(x,y):
	result = x / y
	print(" \n %d / %d = %f" %(x,y, result))

def executarOperacaoEscolhida(opcao):
	num1 = int (input ('Digite o primeiro número: '))
	num2 = int (input ('Digite o segundo número: '))
	#executar operação escolhida
	if opcao == 1:
		somar(num1,num2)
	elif opcao == 2:
		subtrair(num1,num2)
	elif opcao == 3:
		multiplicar(num1,num2)
	else:
		dividir(num1,num2)

def apresentarOperacoes():
	print("\n******************* Python Calculator *******************")
	print('1 - Soma')
	print('2 - Subtração')
	print('3 - Multiplicacao')
	print('4 - Divisão \n \n')



#apresentar tela de opções
while True:
	apresentarOperacoes()

	opcao = int (input ('Digite sua opção (1/2/3/4): '))
	if opcao not in range(1,5):
		print('Opção inválida!')	
	else:
		executarOperacaoEscolhida(opcao)
	
	continuar = input ("Deseja fazer outra operação (S)im ou (N)ão?")
	if (continuar == 'S' or continuar == 's'):
		continue
	else:
		break
	