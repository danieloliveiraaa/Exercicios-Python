idade = int(input("Digite a idade do seu carro : "))

if idade <= 3:
    print("Seu carro é novo")
else:
    print("Seu carro é velho")





idade = int(input("Digite sua idade : "))
altura = float(input("Digite sua altura : "))

if idade >= 18 and altura >= 1.50:
    print("Você é maior de idade e relativamente alto!!")
elif idade < 18 and altura < 1.50:
    print("Você ainda é menor de idade e baixo em estatura!!")
elif idade >= 18 and altura < 1.50:
    print ("Você é de maior de idade porém baixa estatura!!")
elif idade < 18 and altura >= 1.50:
    print ("Você é menor de idade porém alta estatura!!")



peso = float(input("Digite seu peso : "))
altura = float(input("Digite sua altura : "))

imc = peso/(altura*altura)

if imc < 18.5:
    print("Você está Magro!")
elif imc >= 18.5 and imc <= 24.9:
    print("Normal")
elif imc >= 25 and imc <= 29.9:
    print("Sobrepeso")
elif imc >= 30 and imc <= 39.9:
    print("Obeso")
else:
    print("Obesidade Grave")


    
    
