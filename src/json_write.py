import json
data = {
    'orders':[
        {'id':1, 'items':[{'sku':'A1', 'qty':2}]},
        {'id':2, 'items':[{'sku':'B2', 'qty':1}]},
    ]
}

with open('orders.json', 'w')as f:
    json.dump(data, f, indent=2)