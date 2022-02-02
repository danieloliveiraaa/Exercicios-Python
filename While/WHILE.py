#IMC WHILE 

op = 'N'
while op != "S" and op != "s":
    nome=input("Digite o nome da pessoa : ")
    altura=float(input("Digite a altura : "))
    peso=float(input("Digite o peso : "))

    IMC = peso/(altura*altura)

    print(nome,"seu IMC é :", "%.2f" %IMC)

    op = input("Digite 'S' para sair do sistema")
    #Opção para sair do sistema





#TABUADA

num = float(input("Digite o numero da tabuada desejada : "))

soma=0
mult=1
x=0

while x <= 10:
    print(num, "x",x,"=", num*x)
    soma = soma+(num*x)
    if x >= 1:
        mult = mult*(num*x)
    x=x+1
print("Soma total dos resultados : ",soma)
print("Multiplicação dos resultados : " "%.2f" %mult)
