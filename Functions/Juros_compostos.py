def M(cap,tax,meses):
    Montante = cap*(1+tax)**meses
    return Montante
    






op='N'
while op != 'S' and op !='s':
    
    cap = float(input("Entre com o Capital: "))
    tax = float(input("Entre com a Taxa: "))
    meses = int(input("Entre com o Tempo: "))

    res = M(cap,tax,meses)
       
    print("Montante após",meses,"de aplicação --->","%.2f" %res)

    op = input("\n Digite 'S' para sair do sistema: ")    
