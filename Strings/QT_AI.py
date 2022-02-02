frase = input("Digite uma frase: ")

tam=len(frase)   #tamanho da frase inteira

qta=frase.count("a")  #QUANTIDADE DE LETRAS A
qti=frase.count("i")

posc=frase.find("c")
posa=frase.find("i")

palavranova=palavra.replace("n","alt") #Altera o que será mostrado na tela


print("Tamanho da frase digitada", tam)
print("Quantidade de letras A",qta)
print("Quantidade de letras I",qti)
print("Posição da letra 'c' na frase", posc)
print("Posição da letra 'c' na frase", posa)

