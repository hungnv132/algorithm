
###### =================
# print 'hungnv132'                     # 2.X
# print('hungnv132', end='abc')         # 3.X - print: hungnv132abc

###### =================
dic = dict(
    name='hungnv',
    age=21,
)

# print type(dic.keys())    # 2.X - return a list
print(type(dic.keys()))     # 3.X - <class 'dict_keys'>

keys = dic.keys()
print(keys)

# Integer

# print 1/2     # 2.X - print: 0
print(1/2)      # 3.X - print: 0.5
print(1//2)     # 3.X - print: 0