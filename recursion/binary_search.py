"""
 + Describe:
    - Binary search algorith is used to efficently locate a target value within a sorted sequence of n elements.
    - When the sequence is unsorted, the stardard method is use a loop => sequential search algorithm (O(n))
    - When the sequence is sorted and indexable => should use binary search algorithm (O(log n)
 + Ideas:
    - The algorithm remains 2 parameters,'low' and 'high', such that all the candidate entries have index at least low
      and at most high. Initially, low = and high = n - 1
    - mid = (low + high)/2
    - data[mid] divides the list into 2 parts
        - target_value = data[mid] => OK,
        - target_value < data[mid] => continue recurring in 'below part'
        - target_value > data[mid] => to recur in the other part
 + Base Cases(recursion):stop recurring when can not divide the list or found the target value
"""

# the list is sorted


def binary_search_v1(list, finding_value):
    low = 0                 # first element's position in the list
    high = len(list) - 1    # ending element's position in the list

    if low > high:
        return False        # recuring until list only have one element, low = 0; high = -1
    else:
        mid = (low + high) // 2  # middle position of the list
        if finding_value == list[mid]:
            return True
        elif finding_value < list[mid]:
            list = list[low:mid]
            return binary_search_v1(list, finding_value)
        else:
            list = list[mid+1:high+1]
            return binary_search_v1(list, finding_value)


def find_element(list, finding_value, low, high):
    if low > high:
        return False        # recuring until list only have one element, low = 0; high = -1
    else:
        mid = (low + high) // 2
        if finding_value == list[mid]:
            return True
        elif finding_value < list[mid]:
            return find_element(list, finding_value, low, mid-1)
        else:
            return find_element(list, finding_value, mid + 1, high)


def binary_search_v2(list, finding_value):
    return  find_element(list, finding_value, 0, len(list) - 1)



if __name__ == '__main__':
    list = [12, 21, 35, 40, 56, 78, 88, 90, 99]
    print(binary_search_v1(list, 21))
    print(list)
