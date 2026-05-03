import pandas as pd

df = pd.read_csv('data/raw/dirty_orders.csv')
print(df)

df['amount'] = df['amount'].fillna(0)     # cambia los valores NaN O None por cero (0).

print(df)

df['amount'] = df['amount'].astype(int)   # cambia de datos flotantes a enteros.

#df['country'] =df['country'].str.lower()   # cambia los codigo de paises a minusculas.
df['country'] =df['country'].str.upper()   # cambia los codigo de paises a mayusculas.

print(df)

country_sumary = (
    df.groupby('country')
    .agg(
        total_orders=('order_id', 'count'),
        total_amount = ('amount', 'sum')
    )
)

print(country_sumary)

df['running_total'] = df['amount'].cumsum() # hace la suma acumulada de los montos
print(df)