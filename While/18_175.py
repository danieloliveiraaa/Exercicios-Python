#Desenvolver um programa em python que leia 12 idades
# e alturas digitados pelo usuario e apresente
#quantas idades estão acima de 18 anos e quantos tem mais de 
#1,75m.


qtmaior=0
qtaltura=0

x=1


while x <= 12:
    idade = int(input("Digite a idade : "))
    altura = float(input("Digite a altura : "))

    if idade >= 18:
        qtmaior = qtmaior+1
    if altura >= 1.75:
        qtaltura = qtaltura+1
     x=x+1

     print("Total de maiores de 18 anos : ",qtmaior)
     print("Total de maiores de 1,75m : ",qtaltura)
