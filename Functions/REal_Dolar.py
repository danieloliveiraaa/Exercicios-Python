def Convert(dolar):
    real = dolar * 5.50
    return real
    
op='N'
while op != "S" and op!= "s":

    dolar = float(input("Digite um valor em Dolar: "))
    
    conversao = Convert(dolar)
    
    print("O valor em dolares convertido para REAL é : ,", "%.2f" %conversao)

    op = input("Digite 'S' para sair do sistema")
    
