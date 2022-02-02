def somanum():
    num1 = int(input("Digite o primeiro número ..."))
    num2 = int(input("Digite o segundo número ..."))

    soma = num1+num2
    print("O valor da soma dos dois números é >>>>>","%.2f" %soma)


op='N'
while op != 'S' and op != 's':
    somanum()
    op = input("\n Digite 'S' para sair do sistema")

    print("\n Programa finalizado")    
