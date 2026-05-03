try:
    amount = '100'
    total = amount + 50
except TypeError:
    amount = int('100')
    total = amount + 50
    print(total)