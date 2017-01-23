

def _reverse(S, start, stop):
    if start < stop:
        S[start], S[stop] = S[stop], S[start]
        _reverse(S, start+1, stop-1)


def reverse(S):
    _reverse(S, 0, len(S)-1)


if __name__ == '__main__':
    S = [1, 2, 3, 4, 5, 6, 7]
    reverse(S)
    print(S)
