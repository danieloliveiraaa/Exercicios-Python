maior=0
menor=0

for i in range (20):
    salario = float(input("Digite um salário ou '0' para sair : "))
    if salario == 0:       # saída 
        break
    if salario > maior:
        maior = salario
    if salario < menor or menor == 0:
        menor = salario

print("O menor salario é ",menor)
print("O maior salario é ", maior)
