soma=0
qt=0
for i in range (25):
    numero = float(input("Digite uma numero ou '0' para sair : "))
    if numero == 0:       # saída 
        break
    soma = (soma+numero)
    qt = qt+1
    
print("Soma é: ",soma)
print("Quantidade de numeros: ", qt)
