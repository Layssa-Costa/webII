from string import Template

def Main():
    # Cria uma lista vazia para armazenar os itens do carrinho
    cart = []

    # Adiciona itens à lista do carrinho usando dicionários
    cart.append(dict(item="Books", price=90, qty=5))
    cart.append(dict(item="Mobile", price=100, qty=40))
    cart.append(dict(item="Laptop", price=900, qty=2))
    cart.append(dict(item="Tables", price=50, qty=10))

    # Cria um modelo de string usando a classe Template
    cart_template = Template("$qty x $item = $price")

    # Inicializa a variável total para calcular o preço total
    total = 0

    # Imprime o cabeçalho
    print("My Cart :")

    # Itera sobre os dados do carrinho e imprime os detalhes de cada item
    for cart_data in cart:
        # Substitui os marcadores de posição pelos valores correspondentes no dicionário
        print(cart_template.substitute(cart_data))
        
        # Atualiza o preço total com o preço do item atual
        total += cart_data["price"]

    # Imprime o preço total
    print("Total Price : " + str(total))

# Verifica se o script está sendo executado como o programa principal
if __name__ == '__main__':
    # Chama a função Main() para executar o código
    Main()
