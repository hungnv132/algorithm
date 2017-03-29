from redis.connection import Connection
import redis

connection_info = dict(
    host='localhost',
    port=6379,
    db=0,
    password=None,
)


class ConnectionInfo(Connection):

    def __init__(self):
        super(ConnectionInfo, self).__init__(**connection_info)

    @classmethod
    def get_connection_pool(cls):
        return redis.ConnectionPool(connection_class=ConnectionInfo)

redis_object = redis.Redis(connection_pool=ConnectionInfo.get_connection_pool())


if __name__ == '__main__':
    try:
        redis_object.ping()
        print("OK!")
    except Exception as ex:
        print("ERROR")