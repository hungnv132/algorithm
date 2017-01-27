from array import array
import sys
int_nums = array('i', [1, 2, 3, 4])
list = [1, 2, 3, 4]
print(sys.getsizeof(int_nums))
print(sys.getsizeof(list))
print(int_nums)  # array('i', [1, 2, 3, 4])
int_nums.append(5)
print(int_nums)  # array('i', [1, 2, 3, 4, 5])
