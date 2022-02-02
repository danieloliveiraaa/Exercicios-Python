def areaquadrado():     #Função area do quadrado sem parametro e sem valor de retorno
    print("\n Cálculo do valor da área do quadrado \n")
    lado = float(input("Digite o valor do lado do quadrado: "))
    if lado > 0:
        valorarea = lado*lado
        print("Valor da area do quadrado é :", "%.2f" %valorarea)
    else:
        print("Valor digitado incorreto. Verifique")


op='n'
while op != 'S' and op != 's':        #estrutura de repetição => usuario decide o fim
    areaquadrado()                    # chamada da função
    op = input("\n Digite 'S' para sair do sistema: ")
        
