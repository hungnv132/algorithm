"""
+ Describe:
    - Place a tick with a numeric label
    - The length of the tick designating a whole inch as th 'major tick length'
    - Between the marks of whole inches, the ruler contains a series of 'minor sticks', placed at intervals of 1/2 inch,
      1/4 inch, and so on
    - As the size of the interval decrease by half, the tick length decreases by one
+ Base cases(recursion): tick_length = 0
+ Input: inch, major tick length
+ Output:
    --- 0
    -
    --
    -
    --- 1
    -
    --
    -
    --- 2
+ Ideas:
    - method draw_tick(...)  is only responsible for printing the line of ticks (eg: ---, -, ---, --)
    - method interver_v (...) : recursion of draw_tick(...) mehtod until tick_length = 0
    - draw_english_ruler(...) is main method
        - for loop: for displaying 'inch'
+ References: Data structures and Algorithms in Python by Goodrich, Michael T., Tamassia, Roberto, Goldwasser, Michael
"""


def draw_tick(length , tick_label=''):
    line = '-'*int(length)
    if tick_label:
        line += ' ' + tick_label
    print(line)


# interval_version 1
def interval_v1(tick_length):
    if tick_length > 1:
        interval_v1(tick_length - 1)

    draw_tick(tick_length)

    if tick_length > 1:
        interval_v1(tick_length - 1)


# interval_version 2
def interval_v2(tick_length):
    if tick_length > 0:
        interval_v2(tick_length - 1)
        draw_tick(tick_length)
        interval_v2(tick_length - 1)


def draw_english_ruler(inch, major_tick_length):
    draw_tick(major_tick_length, '0')
    for i in range(1,inch):
        interval_v2(major_tick_length - 1)
        draw_tick(major_tick_length, str(i))


if __name__ == '__main__':
    draw_english_ruler(4, 5)
