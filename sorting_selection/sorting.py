

def _merge(S1, S2, S):
    """Merge two sorted Python list S1, S2 into properly sized list S"""
    i = j = 0
    while i+j < len(S):
        if j == len(S2)or (i < len(S1) and S1[i] < S2[j]):
            S[i+j] = S1[i]      # copy ith element of S1 as next item of S
            i += 1
        else:
            S[i+j] = S2[j]      # copy jth element of S2 as next item of S
            j += 1


def merge_sort(S):
    """Sort the elements of Python list S using the merge-sort algorithm"""
    n = len(S)
    if n < 2:
        return              # list is already sorted
    # divide
    mid = n // 2
    S1 = S[0:mid]
    S2 = S[mid:n]
    print('-----------')
    print('S1 = {0}'.format(S1))
    print('S2 = {0}'.format(S2))
    # conquer (with recursion)
    merge_sort(S1)
    merge_sort(S2)

    print('-----------')
    print('S = {0}'.format(S))

    _merge(S1, S2, S)
    print('S = {0}'.format(S))


if __name__ == '__main__':
    S = [78, 1, 21, 12, 8, 90, 38, 56, 5]
    merge_sort(S)
    print(S)
