

# Performance is O(n)
def linear_sum(S, n):
    if n==0:
        return 0
    else:
        return S[n-1] + linear_sum(S, n-1)

def sum(S):
    return linear_sum(S, len(S))

if __name__ == '__main__':
    S = [1, 2, 3, 4, 5]
    print(sum(S))