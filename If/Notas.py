n1 = float(input("Digite a primeira nota : "))
n2 = float(input("Digite a segunda nota : "))
n3 = float(input("Digite a terceira nota : "))

media = (n1+n2+n3)/3

if media >= 7:
    print("Aprovado ^_^ ")
elif media < 4:
    print("Reprovado ;-; ")
else:
    print("Recuperação!!")



num1 = int(input("Digite primeiro número : "))
num2 = int(input("Digite o segundo número : "))
num3 = int(input("Digite o terceiro número : "))

if num1 > num2 and num1 > num3:
    print("O maior número é ", num1)
elif num2 > num1 and num2 > num3:
    print("O maior número é ", num2)
else:
    print("O maior número é ", num3)
    
    
