

#mock
carrinho = [['123', '1', 800.0, 2], ['123', '2', 40.00, 4], ['123', '1', 800.00, 1]] 

id_user = '123'
id_produto = '1'
price_product = 800.00
quantity_product = 2

item = [id_user, id_produto, price_product, quantity_product]


def get_item_cart_by_id(id_product):
    for id_product in carrinho:
       print(id_product)


get_item_cart_by_id(carrinho)

    