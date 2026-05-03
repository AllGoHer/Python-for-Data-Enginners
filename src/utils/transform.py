def transform_orders(raw_orders):
    
    transformed = [] 
             
    for order in raw_orders:
        transformed.append({
            'order_id':order['order_id'],
            'amount': float(order['amount']),  
            'country': order['country'].upper()  
        })

    return transformed

