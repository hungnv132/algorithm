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

def count_frequency(data):
    print("Length of data: " + str(len(data)))
    for index, item in enumerate(data):
        if index == 0:
            last_count = item['count']
            times = 1
            continue
        if last_count == item['count']:
            times += 1
        else:
            print("{} count - {} ".format(last_count, times))
            last_count = item['count']
            times = 1
        if index == len(data) - 1:
            print("{} count - {} ".format(last_count, times))

if __name__ == '__main__':
    count_frequency(data)
