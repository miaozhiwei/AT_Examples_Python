from redis import StrictRedis, ConnectionPool

# 直连方式
# redis = StrictRedis(host='localhost', port=6379, db=1)

# # 连接池方式连接
# pool = ConnectionPool(host='localhost', port=6379, db=1)
# redis = StrictRedis(connection_pool=pool)

# # String
# redis.set('myString','abc')
# s = redis.get('myString')
# print(s)

# # Hash
# redis.hset('myHash', 'field_1', 'hello_1')
# redis.hset('myHash', 'field_2', 'hello_2')
# h1 = redis.hget('myHash', 'field_1')
# h2 = redis.hget('myHash', 'field_2')
# print(h1, h2)

# # List
# redis.lpush('myList', 'list1', 'list2')
# l = redis.lrange('myList', 0, 1000)
# print(l)

# # Set
# redis.sadd('mySet', 'test1')
# st = redis.smembers('mySet')
# print(st)

# # Zset
# redis.zadd('myZset', 1, 'rabbitmq')
# redis.zadd('myZset', 2, 'oracle')
# redis.zadd('myZset', 3, 'mongoDB')
# z = redis.zrangebyscore('myZset', 0, 1000)
# print(z)
