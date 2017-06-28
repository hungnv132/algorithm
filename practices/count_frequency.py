from functools import cmp_to_key

data = [
    {'id': 2, 'count': 1},
    {'id': 12, 'count': 1},
    {'id': 8, 'count': 1},
    {'id': 10, 'count': 2},
    {'id': 15, 'count': 2},
    {'id': 4, 'count': 2},
    {'id': 65, 'count': 4},
    {'id': 88, 'count': 8},
    {'id': 23, 'count': 8},
    {'id': 81, 'count': 8},
    {'id': 1, 'count': 12},
    {'id': 34, 'count': 12},
]


def check_seeding(id):
    return True if id in [2, 10, 15, 88, 81, 1, 34] else False


def compare(item1, item2):
    return cmp_to_key(item1['count'], item2['count'])


def count_frequency(data):
    print("Length of data: " + str(len(data)))
    for index, item in enumerate(data):
        if index == 0:
            last_count = item['count']
            times = 1
            if check_seeding(item['id']):
                count_seeding = 1
            else:
                count_seeding = 0

            continue
        if last_count == item['count']:
            times += 1

            if check_seeding(item['id']):
                count_seeding += 1
        else:
            print("{} count - {} - {} seeding ".format(last_count, times, count_seeding))
            last_count = item['count']
            times = 1

            if check_seeding(item['id']):
                count_seeding = 1
            else:
                count_seeding = 0

        if index == len(data) - 1:
            print("{} count - {} - {} seeding".format(last_count, times, count_seeding))

if __name__ == '__main__':
    count_frequency(data)
    print(sorted(data, key=compare))
