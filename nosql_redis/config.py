from redis.connection import Connection

HOST = 'localhost'
PORT = 6379
DB = 0


class ConnectionInfo(Connection):

    def __init__(self):
        super(ConnectionInfo, self).__init__()
        self.host = HOST
        self.port = PORT
        self.db = DB

