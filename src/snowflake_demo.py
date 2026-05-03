import snowflake.connector

#Configura la conexion
conn = snowflake.connector.connect(
    user='All',
    password='xxxxxxx',
    account='qm70598.sa-east-1.aws',
    warehouse='COMPUTE_WH',
    database='DEMO_DB',
    schema='pUBLIC'
)


#Abre  Cursor
cursor = conn.cursor()

#Ejecuta una consulta
cursor.execute(
    ''' 
    CREATE TABLE IF NOT EXISTS orders(
    order_id INTEGER,
    amount INTEGER,
    country STRING
    )
    '''
)

# Insertar un registro

try:
    cursor.execute(
        '''
        INSERT INTO orders(order_id, amount, country)
        VALUES (%s, %s, %s)
        ''',
        (3, 300, 'PE')
    )
    print('Insert successful')
except Exception as e:
    print('Insert failed:', e)

#Seleccionar data desde la tabla
cursor.execute(
    'SELECT order_id, amount, country FROM orders'
)

rows = cursor.fetchall()

for row in rows:
    print(row)

#Cierra cursor
cursor.close()
conn.close()