
cart = []
keep_buying = 'y'

def buy_item():
    id_user = input('Insira o id do usuário:   ')
    id_product = input('Insira o id do produto:   ')
    price_product = float(input('Insira o preço do produto:   '))
    quantity_product = int(input('Insira a quantidade de produto:   '))
    item = {
        'id_user': id_user, 
        'id_product': id_product, 
        'price_product': price_product, 
        'quantity_product': quantity_product
    }
    return item

def add_item_cart():
    cart.append(item)

while keep_buying == 'y':
    item = buy_item()
    add_item_cart(item)
    keep_buying = input('Continuar comprando? [y/n]:   ')
    if keep_buying == 'n': 
        break
 

 
def get_all_items_cart():
    for i in cart:
        return i


list_id_users = list(map(lambda x: x['id_user'], cart))
list_id_product = list(map(lambda x: x['id_product'], cart))
list_price_product = list(map(lambda x: x['price_product'], cart))
list_quantity_product = list(map(lambda x: x['quantity_product'], cart))


print(cart)
print(get_all_items_cart(cart))

def remove_item_id(cart):
    filter(lambda i: i.pop(), cart)




soma_total = 0
for list_price in item:
    soma_total += s[3] * s[2]


print(f'Valor: R$ {soma_total}')
    
 