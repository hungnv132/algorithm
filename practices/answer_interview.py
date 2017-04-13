
city_list = [
    {'name': 'HP', 'population': 10000},
    {'name': 'HCM', 'population': 40000},
    {'name': 'HN', 'population': 80000},
    {'name': 'DN', 'population': 20000},
]

# --------------using sum() method-------------
print(sum(city['population'] for city in city_list))  # 150000


# ---------------using reduce() method, only python 2.7--------------
def tinh_tong(x, y):
    return x + y

population_list = (city['population'] for city in city_list)
print(reduce(tinh_tong, population_list))

# ---------------hoac su dung lambda--------------------
print(reduce(lambda x, y: x+y, (city['population'] for city in city_list)))


# -------------- sorting--------------
def compare1(item1, item2):
    return cmp(item1['population'], item2['population'])


def compare2(item1, item2):
    return cmp(item1, item2)


def key(item):
    return item['population']

# before
print(city_list)

# after
print(sorted(city_list, compare1))
# or
print(sorted(city_list, compare2, key))
# or shorter
print(sorted(city_list, lambda x, y: cmp(x, y), lambda x: x['population']))


#--------------- remove duplicate items in a list-----------------
num_list = [1, 2, 4, 6, 4, 2, 8, 8, 3, 2]
new_list = []
for item in num_list:
    if item not in new_list:
        new_list.append(item)

print(num_list)             # [1, 2, 4, 6, 4, 2, 8, 8, 3, 2]
print(new_list)             # [1, 2, 4, 6, 8, 3]

# or use set() method, cast back to list
print(list(set(num_list)))  # [1, 2, 4, 6, 8, 3]