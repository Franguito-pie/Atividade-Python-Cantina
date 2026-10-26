#SISTEMA DE CANTINA ESCOLAR

j = 1
supermercado = 0

print("Bem vindo à nossa loja online! Veja os produtos abaixo:")

while j == 1:
    print("=======================================================")
    print("OPÇÃO     |PRODUTO               |PREÇO                ")
    print("1         |Suco                  |R$5,00               ")
    print("2         |Salgado               |R$7,00               ")
    print("3         |sanduíche             |R$10,00              ")
    print("4         |Finalizar Compra ---                      \n")

    p = int(input("Qual produto você deseja comprar? "))

    if p == 1:
        supermercado += 5

    elif p == 2:
        supermercado += 7

    elif p == 3:
        supermercado += 10

    elif p == 4:
        print("\nCompra finalizada com sucesso!")
        print(f"Valor da compra --- R${supermercado}")
        break

    else:
        print("\033[31mPor favor, digite uma opção existente!\033[m")