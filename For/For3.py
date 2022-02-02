soma = 0

for i in range (10):      # 10 repetições começando em 0 até 9
    valor = float(input("Digite um valor ou '99' para sair : "))
    if valor == 99:       # saída forçada
        break
    soma = soma + valor # acumulador

print("Quantidade digitada : ", i+1)
print("Soma = ",soma)   
