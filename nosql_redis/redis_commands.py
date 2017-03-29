from nosql_redis.connection import redis_object


def p(data):
    return print(data)


def string_type_commands():

    # SET key value [EX seconds] [PX milliseconds] [NX|XX] => OK or nil
    redis_object.set('name', 'hungnv132')
    redis_object.set('age', 21)

    # SETEX key seconds value
    """Set `key` to hold the string `value` and set `key` to timeout after a given number of seconds."""
    p(redis_object.setex('address', 'hanoi', 10))           # True

    # GET key  =>   the value of key, or nil when key does not exist.
    p(redis_object.get('name'))

    #  DEL key [key ...]
    """Removes the specified keys. A key is ignored if it does not exist."""
    redis_object.set('score', 10)
    p(redis_object.delete('score'))         # 1
    p(redis_object.get('score'))            # None

    # APPEND key value  => the length of the string after the append operation.
    p(redis_object.append('name', 'Nguyen'))        # 15
    p(redis_object.get('name'))                     # b'hungnv132Nguyen'

    # INCR key              => the value of key after the increment
    # INCRBY key increment  => the value of key after the increment
    p(redis_object.incr('age'))             # 22
    p(redis_object.incr('age', 3))          # 25

    # DECR key             => the value of key after the decrement
    # DECRBY key decrement => the value of key after the decrement
    p(redis_object.decr('age'))         # 24
    p(redis_object.decr('age', 5))      # 19

    # STRLEN key  ==> the length of the string at key, or 0 when key does not exist.
    p(redis_object.strlen('name'))          # 15
    p(redis_object.strlen('age'))           # 2

    # SETRANGE key offset value
    """
    Overwrites part of the string stored at `key`, starting at the specified `offset`, for the entire length of value.
    ==>  the length of the string after it was modified by the command.
    """
    p(redis_object.setrange('name', 4, 'Viet'))         # 15
    p(redis_object.get('name'))                         # b'hungViet2Nguyen'

    # GETRANGE key start end
    p(redis_object.getrange('name', 2, 5))              # b'ngVi'


def list_type_commands():

    # RPUSH key value [value ...]    ==>
    """
        Insert all the specified values at the TAIL of the list stored at key
     => The length of the list after the push operation.
    """
    p(redis_object.rpush('lang', 'vi', 'en', 'jp'))         # 3

    # LPUSH key value [value ...]
    """
        Insert all the specified values at the HEAD of the list stored at `key`
        => the length of the list after the push operations.
    """
    p(redis_object.rpush('lang', 'fr', 'y',))         # 5

    # RPOP key  ==> Removes and returns the LAST element of the list stored at key.
    p(redis_object.rpop('lang'))            # b'jp'

    # LPOP key  ==> Removes and returns the FIRST element of the list stored at key
    p(redis_object.lpop('lang'))            # b'vi'

    #  LLEN key  ==> the length of the list at key.
    p(redis_object.llen('lang'))            # 2


def set_type_commands():

    #  SADD key member [member ...]
    """ Add the specified members to the set stored at key
    ==> the number of elements that were added to the set, not including all the elements already present into the set.
    """
    p(redis_object.sadd('country', 'VN', 'JP', 'US'))       # 3
    redis_object.sadd('country', 'VN')

    #  SMEMBERS key => Returns all the members of the set value stored at key.
    p(redis_object.smembers('country'))     # {b'VN', b'JP', b'US'}

    #  SISMEMBER key member => Returns if member is a member of the set stored at key
    p(redis_object.sismember('country', 'VN'))      # True

    # SREM key member [member ...]  => Remove the specified members from the set stored at key
    p(redis_object.srem('country', 'US'))       # 1

    # SPOP key [count]  => Removes and returns one or more random elements from the set value store at key.
    p(redis_object.spop('country'))     # b'JP'


def hash_type_commands():

    #  HSET key field value =>  Sets field in the hash stored at key to value.
    p(redis_object.hset('hash', 'name', 'hung'))        # 1

    # HGET key field => Returns the value associated with field in the hash stored at key
    p(redis_object.hget('hash','name'))     # b'hung'

    # HMSET key field value [field value ...] => Sets the specified fields to their respective values in the hash stored at key.
    p(redis_object.hmset('new_hash', {'name': 'hnv132', 'age': 21}))    # True

    # HMGET key field [field ...] => Returns the values associated with the specified fields in the hash stored at key.
    p(redis_object.hmget('new_hash', 'name', 'age'))    # [b'hnv132', b'21']
    p(redis_object.hget('new_hash', 'name'))            # b'hnv132'

    # HGETALL key  => Returns all fields and values of the hash stored at key
    p(redis_object.hgetall('new_hash'))         # {b'name': b'hnv132', b'age': b'21'}

    # HDEL key field [field ...] => Removes the specified fields from the hash stored at key
    p(redis_object.hdel('new_hash', 'name'))        # 1
    p(redis_object.hgetall('new_hash'))             # {b'age': b'21'}

if __name__ == '__main__':
    hash_type_commands()
