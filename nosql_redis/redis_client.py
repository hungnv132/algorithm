import redis
from config import ConnectionInfo
# r = redis.StrictRedis(host='localhost', port=6379, db=0)
# r.set('name', 'hungnv132')
# print (r.get('age'))

pool = redis.ConnectionPool(connection_class=ConnectionInfo)
conn = redis.Redis(connection_pool=pool)

print (conn.get('age'))
