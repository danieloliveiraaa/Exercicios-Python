def par_impar(num)  #função par ou impar com um parametro e sem valor de retorno
    if num%2==0:
        print("O número é par")
    else:
        print("O número digitado é impar")


op='N'
while op != '5' and op != 's':
    num = float(input("Digite um número : "))
    if num !=0:
        par_impar(num)
    else:
        print("Digitado zero, verifique.")

        
    op = input("\n Digite 'S' para sair do sistema")
        
