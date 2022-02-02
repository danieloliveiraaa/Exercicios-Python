print("Imprime soma e multiplicação de números digitados")

soma = 0
mult = 1
x=1

while x <= 5:
    num = int(input("Digite um numero : "))
    soma = soma+num
    mult = mult*num
    x=x+1 #CONTADOR DO LAÇO DE REPETIÇÃO

    print("Soma dos números digitados : ",soma)
    print("Multiplicação dos números : ", mult)
