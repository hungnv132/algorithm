

print(lambda x, y: x + y)  # print: <function <lambda> at 0x0000000000807F28>
print('===================')
f = lambda x, y: x + y
a = f
print('===================')
print(f(2, 5))                      # print: 7
print(f('hung', 'nguyen'))          # print: hungnguyen
print((lambda x, y: x + y)(2, 4))   # print: 6
print('===================')
L = [lambda x:x*2, lambda x: x*3, lambda x: x*4]
for f in L:
    print(f(2))     # print: 4  6  8

print(L[1](8))      # print: 24

print('===================')

key = 'got'
dic = {
    'already': lambda: 2*3,
    'got': lambda: 2*4,
    'one': lambda: 2*5,
}
print( dic[key]())   # print: 8

print('===================')

lower = lambda x, y: x if x < y else y
print(lower('a', 'b'))  # print: a
print(lower('b', 'a'))  # print: a

print('===================')

def action(x):
    return lambda y: x +y

print(action(8))       # print: <function action.<locals>.<lambda> at 0x0000000000A818C8>
print(action(8)(6))     # print: 14

act = action(10)
print(act(8))           # prnt: 18
