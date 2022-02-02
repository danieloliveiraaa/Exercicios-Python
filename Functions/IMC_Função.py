def Calc_imc(peso,altura):
    IMC = peso/(altura*altura)
    return IMC




op='N'
while op != 'S' and op !='s':
    
    peso = float(input("Entre com o peso: "))
    altura = float(input("Entre com a altura: "))

    Imc = Calc_imc(peso,altura)

    if Imc < 18.5:
        print("Magro")
    elif Imc >= 18.5 and Imc <= 24.9:
        print("Peso Normal")
    elif Imc > 24.9 and Imc <= 29.9:
        print("Sobrepeso")
    elif Imc > 29.9 and Imc <= 39.9:
        print("Obeso")
    else:
        print("Obesidade Grave")

    
       
    

    op = input("\n Digite 'S' para sair do sistema: ")





    
