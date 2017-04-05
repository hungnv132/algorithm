

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


def _parition(A, p, r):
    pivot = A[r]
    i = p - 1
    j = p
    while j < r:
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
        j += 1
    A[i+1], A[r] = A[r], A[i+1]
    return i+1


def quick_sort(sequence, p, r):

    if p < r:
        split_index = _parition(sequence, p, r)
        quick_sort(sequence, p, split_index - 1)
        quick_sort(sequence, split_index + 1, r )


if __name__ == '__main__':
    S = [78, 1, 21,88, 12, 8, 50, 4]
    quick_sort(S, 0, len(S)-1)
    print(S)
