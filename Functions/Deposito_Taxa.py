deposito = float(input("Digite o valor do deposito inicial : "))
taxa = float(input("Digite a taxa de juros da aplicação em % : "))

for x in range (10):

    deposito = deposito + (deposito*taxa/100)

    print("Valor corrigido no mês",x+1, "=====> R$", "%.2f" %deposito)
