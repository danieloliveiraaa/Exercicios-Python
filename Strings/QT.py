frase1 = input("Digite uma frase: ")
frase2 = input("Digite uma frase: ")

tam1=len(frase1)   #tamanho da frase inteira
tam2=len(frase2)

minusc=frase1.lower()
maiusc=frase2.upper()


qta=frase1.count("a")  #QUANTIDADE DE LETRAS A
qtg=frase2.count("g")

posc=frase1.find("c")
posa=frase2.find("i")

palavra1nova=frase1.replace("m","")#Altera o que será mostrado na tela
palavra2nova=frase2.replace("n","alt")


print("Tamanho da primeira frase digitada", tam1)
print("Tamanho da segunda frase digitada", tam2)
print("Tamanho da frase digitada", tam)
print("Quantidade de letras A",qta)
print("Quantidade de letras G",qtg)
print("Posição da letra 'c' na frase", posc)
print("Posição da letra 'c' na frase", posa)
