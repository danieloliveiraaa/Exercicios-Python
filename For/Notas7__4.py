baixas=0
media=0

for i in range (30):      # 31 repetições começando em 0 até 30
    valor = float(input("Digite uma nota ou '99' para sair : "))
    if valor == 99:       # saída forçada
        break
    if nota > 7:
        media = media+1
    if nota < 4:
        baixas = baixas+1
print("Quantidade de notas acima de sete :", media)
print("Quantidade de notas abaixo de quatro :", baixas)
