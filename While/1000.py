#Programa que leia numeros inteiros
#digitados pelo usuario e apresente quantos
#desses são ##maiores## de 1000 e quantos são ##pares##


qtpares=0
qtmaior=0

op = 'N'

while op != "sim" and op != "Sim":
    num=float(input("Digite um numero : "))
    if num > 1000:
        qtmaior=qtmaior+1
    if num%2 == 0:
        qtpares = qtpares+1
       
    op = input("Deseja sair do sistema?  ")
    #Opção para sair do sistema


    print("Quantidade de pares digitados : ", qtpares)
    print("Quantidade de numeros acima de 1000 : ", qtmaior)
