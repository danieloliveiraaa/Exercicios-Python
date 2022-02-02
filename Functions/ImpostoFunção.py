def calculaImposto(renda):
    if renda <= 1700.00:
        return 0
    elif renda <= 2500.00:
        return renda * 0.05
    elif renda <= 3700.00:
        return renda *0.15
    elif renda <= 5400.00:
        return renda * 0.20
    else:
        return renda * 0.25


op='N'
while op != 'S' and op != 's':
    print("\n Calculo de imposto com base no salário digitado: ")
    renda=float(input("Entre com o valor do salario mensal em R$: "))

    imposto=calcularImposto(renda) #chamada da função

    print("Para o salario de R$ ", renda,"O imposto será de R$ ","%.2f", %imposto)

    op = input("\n Digite 'S' para sair do sistema: ")

    print("\n Programa finalizado")
