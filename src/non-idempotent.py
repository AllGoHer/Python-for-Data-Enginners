transformed = []          

def transform_orders(raw_orders):
    
    for order in raw_orders:
        transformed.append({
            'order_id':order['order_id'],
            'amount': float(order['amount']),  #convierte los montos de string a float
            'country': order['country'].upper()  #convierte codigo de país en mayuscula
        })

    return transformed

sample_orders = [      #Diccionarios de pedidos de muestra a ingresar a la lista.
    {'order_id': 1, 'amount': '100', 'country': 'us'},
    {'order_id': 2, 'amount': '200', 'country': 'pe'}
]

print(transform_orders(sample_orders))