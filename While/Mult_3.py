#Escreva um programa que mostre apenas os
#numeros multiplos de 3 ate
#um número digitado pelo usuario

num = int(input("Digite até que número deseja imprimir : "))

while num >=0:
    if num%3 == 0:
        print(num)
    num=num-1    

