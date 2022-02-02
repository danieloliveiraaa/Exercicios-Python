


qtpositivos=0
qtnegativos=0
qtzeros=0

x=1

while x <=10:
    num = int(input("Digite o primeiro número "))
    if num > 0:
        qtpositivos = qtpositivos+1
    elif num < 0:
        qtnegativos = qtnegativos+1
    else:
        qtzeros = qtzeros+1
    x=x+1


    print("Total de positivos digitados : ", qtpositivos)
    print("Total de negativos digitados : ", qtnegativos)
    print("Total de zeros digitados : ", qtzeros)
