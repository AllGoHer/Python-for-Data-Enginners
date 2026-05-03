import time
import pandas as pd
import numpy as np

#Crear DataFrame
df = pd.DataFrame({
    'amount':np.random.randint(1, 1000, size=1_000_000)
})

# Metodo lento: bucle
start = time.time()

total = 0
for val in df['amount']:
    total += val

print('Loop sum:', total)
print('Time Taken:', time.time()- start) 

#Metodo Rapido: Vectorizado
start = time.time()
total = df['amount'].sum()

print('Vectorized sum:', total)
print('Vectorized Time Taken:', time.time() - start)