
from time import time
from common import time_log as log
"""
  There are three sequences of numbers, A, B and C (No individual sequence 
  contains duplicate values), but there may be some numbers that are in two or 
  three of the sequences. If there are at least an element exists on all 
  sequences, then return 'False', else True
"""
A = [12, 45, 55, 89, 1, 9, 2]
B = [12, 51, 28, 41, 70, 88]
C = [23, 60, 49, 65, 80, 62]


# The this first algorithm's performance is O(n^3)
def disjoin_first(*args):
    A, B, C  = args[0], args[1], args[2]
    for a in A:
        for b in B:
            for c in C:
               if a == b == c:
                   return False
    return True


# performance is O(n^2)
def disjoin_second(*args):
    A, B, C = args[0], args[1], args[2]
    for a in A:
        for b in B:
            if a == b:
                for c in C:
                    if a == c:
                        return False
    return True


if __name__ == '__main__':
    log.print_time(disjoin_first, A, B, C)