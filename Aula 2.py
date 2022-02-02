#CALCULO IMC

nome = input("Digite seu nome : ")
peso = float(input("Digite o peso : "))
altura = float(input("Digite a altura : "))



IMC = peso/(altura**2)

# IMC = peso/(altura*altura)


print("Seu IMC é : ", "%.2f" %IMC)
