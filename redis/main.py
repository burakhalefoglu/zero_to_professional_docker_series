import os 
import redis as rd 


REDIS_HOST = os.environ["REDIS_HOST"]
REDIS_PORT = os.environ["REDIS_PORT"]
REDIS_PASSWORD = os.environ["REDIS_PASSWORD"]

redis_client = rd.Redis(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD, db=0)

# Veri Ekle
redis_client.set('key1', 'value1')
redis_client.set('key2', 'value2')

# Veri Getir
print(redis_client.get('key1'))
print(redis_client.get('key2'))

# veri güncelle
redis_client.set('key1', 'value11') 

# Veri sil
redis_client.delete('key1')

try:
    print(redis_client.get('key1'))
except rd.RedisError as e:
    print(e)



