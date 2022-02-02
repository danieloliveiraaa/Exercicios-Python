def areaquadrado (lado)             #função area do quadrado
    area = lado * lado              #com um parâmetro
    return area

op='N'
while op != 'S' and op !='s':

    print("\n Cálculo do valor da área do quadrado \n")
    lado = float(input("Digite o valor do quadrado: "))

    if lado > 0:
        valorarea("Valor da área do quadrado é : ", "%.2f" %valorarea)
    else:
        print("Valor digitado incorreto. Verifique")

    op = input("\n Digite 'S' para sair do sistema")
