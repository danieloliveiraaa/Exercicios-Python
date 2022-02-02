def reajuste(capital,taxa,tempo):
    if renda <= 2000.00:
        return renda * 1.15
    else:
        return renda * 1.10
    


op='N'
while op != 'S' and op !='s':
    
    renda = float(input("Entre com o salario: "))

    reaj = reajuste(renda)
       
    print("Salario reajustado, será de R$", "%.2f" %reaj)

    op = input("\n Digite 'S' para sair do sistema :")
