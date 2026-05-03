import time
import requests 

retries = 3

for attemp in range(retries):
    try:
        response = requests.get('https://jsonplaceholder.typicode.com/posts')
        response.raise_for_status()
        print('Request successful')
        break
    except Exception as e:
        print(f'Attempt {attempt + 1} failed')
        time.sleep(2)
