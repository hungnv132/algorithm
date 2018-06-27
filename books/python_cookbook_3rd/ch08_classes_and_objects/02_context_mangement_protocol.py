
def making_objects_support_context_management_protocol():
    """
    - Problem: make your objects support the context-management protocol
    (the with statement).
    - Solution: need to implement __enter__() and __exit__() methods.
    """

    from socket import socket, AF_INET, SOCK_STREAM

    class LazyConnection(object):

        def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
            self.address = address
            self.family = family
            self.type = type
            self.sock = None

        def __enter__(self):
            if self.sock is not None:
                raise RuntimeError('Already connected')
            self.sock = socket(self.family, self.type)
            self.sock.connect(self.address)
            return self.sock

        def __exit__(self, exc_type, exc_val, exc_tb):
            self.sock.close()
            self.sock = None

    from functools import partial

    conn = LazyConnection(('www.python.org', 80))

    with conn as s:
        # conn.__enter__() executes: connection open
        s.send(b'GET /doc HTTP/1.0\r\n')
        s.send(b'Host: www.python.org\r\n')
        s.send(b'\r\n')
        resp = b''.join(iter(partial(s.recv, 8192), b''))
        print(resp)
        # conn.__exit__() executes: connection closed

    # with nested:
    class LazyConnection_v2(object):

        def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
            self.address = address
            self.family = family
            self.type = type
            self.connections = []

        def __enter__(self):
            sock = socket(self.family, self.type)
            sock.connect(self.address)
            self.connections.append(sock)
            return sock

        def __exit__(self, exc_type, exc_val, exc_tb):
            self.connections.pop().close()

    conn = LazyConnection_v2(('www.python.org', 80))
    with conn as s1:
        s1.send(b'GET /doc HTTP/1.0\r\n')
        s1.send(b'Host: www.python.org\r\n')
        s1.send(b'\r\n')
        resp = b''.join(iter(partial(s1.recv, 8192), b''))
        print(resp)
        with conn as s2:
            s2.send(b'GET /doc HTTP/1.0\r\n')
            s2.send(b'Host: www.python.org\r\n')
            s2.send(b'\r\n')
            resp = b''.join(iter(partial(s2.recv, 8192), b''))
            print(resp)


if __name__ == '__main__':
    making_objects_support_context_management_protocol()