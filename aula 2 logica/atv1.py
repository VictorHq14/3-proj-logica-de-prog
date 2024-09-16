valor = int(input("Dê um valor a um produto X"))
valordividido = valor * 5
descontar = valordividido / 100 
valor_descontado = valor - descontar

print(f"O valor está com 5% de desconto e ficou por R${valor_descontado}")