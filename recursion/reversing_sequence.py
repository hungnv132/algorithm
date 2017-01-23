

def _reverse(S, start, stop):
    if start < stop:
        S[start], S[stop] = S[stop], S[start]
        _reverse(S, start+1, stop-1)


def reverse(S):
    _reverse(S, 0, len(S)-1)


def reverse_v2(S):
    start, stop = 0,len(S)-1
    while start < stop:
        S[start], S[stop] = S[stop], S[start]
        start, stop = start+1, stop-1

if __name__ == '__main__':
    S = [1, 2, 3, 4, 5, 6, 7, 8]
    #reverse(S)
    reverse_v2(S)
    print(S)
