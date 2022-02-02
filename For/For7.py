qta=0
qtc=0

palavra = input("Digite uma palavra qualquer : ")

for x in palavra:
    if x == "a" or x == "A":
        qta = qta+1   #Contador de letras a
    if x == "c" or x == "C":
        qtc = qtc+1   #Contador de letras c

print("Quantidade de letras 'a' em ",palavra,"é:",qta)
print("Quantidade de letras 'c' em ",palavra,"é:",qtc)
        






     
