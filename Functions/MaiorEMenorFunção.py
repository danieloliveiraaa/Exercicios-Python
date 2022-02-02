def Maior(num1, num2)
    if num1 > num2:
        maior = num1
    else
        maior = num2
        return maior


op='N'
while op != "S" and op!= "s":
    num1=float(input("Digite o primeiro: "))
    num2=float(input("Digite o segundo: "))

    num=Maior(num1,num2)
    print("O maior é : ", num)

    op = input("Digite 'S' para sair do sistema")
