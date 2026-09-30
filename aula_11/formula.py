import random

cardapio = {
    "chocolate": 5.00,
    "baunilha": 4.50,
    "morango": 3.00,
    "flocos": 9.00
}

brindes = ["Canudo", "Copo personalizado", "Gelo", "Badge"]

def mostrar_cardapio():
    print("--Cardápio--")
    for sabor, preco in cardapio.items():
        print(f"{sabor}, R${preco:.2f}")

def fazer_pedido():
    total = 0
    pedido = []
    while True:
        sabor = input("\nEscolha o sabor: (digite 'fechar'para sair)")
        if sabor == "fechar":
            break
        elif sabor in cardapio:
            total += cardapio[sabor]
            pedido.append(sabor)
            print(f"{sabor} adicionado ao pedido!")
        else:
            print("Sabor nao disponivel")
    return pedido, total

mostrar_cardapio()
pedido, total = fazer_pedido()

print(f"\nSeu pedido: {pedido}")
print(f"Total: R${total:.2f}")

if total > 8:
    print(f"Ganhou brinde: {random.choice(brindes)}")