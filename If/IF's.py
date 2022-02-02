# IF ELSE

#Exemplo 1

num1 = int(input("Digite o primeiro número : "))
num2 = int(input("Digite o segundo número : "))

if num1 > num2:
    maior = num1
    #Poderia ser um print("o maior numero é : ", num1) ao invés de "maior = num1".
else:
    maior = num2

print("O maior numero é : ", maior)






#Exemplo 2

num1 = float(input("Digite um número entre 100 e 500 : "))

if num1 >= 100 and num1 < 200:
    print("O número digitado está entre 100 e 200")
elif num1 >= 200 and num1 < 300:
    print("O número digitado está entre 200 e 300")
elif num1 >= 300 and num1 < 400:
    print("O número digitado está entre 300 e 400")
elif num1 >= 400 and num1 < 500:
    print("O número digitado está entre 400 e 500")
else:
    print("O número digitado não esta entre 100 e 500")



#Exemplo 3

sal = float(input("Digite o valor do salario : "))

if sal >= 0 and sal <= 1200:
    sal=sal+(sal*0.15)
elif sal > 1200 and sal <= 2000:
    sal=sal+(sal*0.11)
elif sal > 2000 and sal <= 3400:
    sal=sal+(sal*0.08)
elif sal > 3400 and sal <= 5000:
    sal=sal+(sal*0.05)
else:
    sal=sal+(sal*0.02)

print("Salario reajustado : ", sal)


#Exemplo While

num = int(input("Digite o numero da tabuada desejada : ")) 

x = 0
while x <= num:
    print(x)
    x=x+1







    



    
