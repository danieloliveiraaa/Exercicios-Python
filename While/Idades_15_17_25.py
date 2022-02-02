#Imprime quantidade de idades
#entre 15 e 17 anos e
#maiores de 25 anos


qtmenor15_17=0
qtmaior25=0

op = 'N'

while op != "Sim" and op != "sim":
    idade=int(input("Digite uma idade : "))
    if idade >= 15 and idade <= 17:
        qtmenor15_17 = qtmenor15_17 + 1
    if idade > 25: 
        qtmaior25 = qtmaior25 + 1
       
    op = input("Deseja sair do sistema?  ")
    #Opção para sair do sistema

    print("Entre 15 e 17 anos : ", qtmenor15_17)
    print("Acima de 25 anos : ", qtmaior25)
