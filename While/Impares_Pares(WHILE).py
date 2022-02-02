somaImpares = 0
mult = 1
cont = 1

while cont <= 10:
    num = int(input("Digite um numero inteiro : "))
    if num > 0:
        if num % 2 == 0:
            multPares = multPares * num
        else:
            somaImpares = somaImpares + num
    cont = cont + 1

    print("Soma dos Impares = ", somaImpares)
    print("Multiplicação dos Pares = ", multPares)
