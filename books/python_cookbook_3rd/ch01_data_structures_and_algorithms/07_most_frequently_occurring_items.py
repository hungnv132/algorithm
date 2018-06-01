from collections import Counter


def most_frequently_occurring_items():
    """
    - Problem: You have a sequence of items and you'd like determine the most
    frequently occurring items in the sequence.
    - Solution: Use the collections.Counter
    """

    words = [
        'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
        'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
        'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
        'my', 'eyes', "you're", 'under'
    ]
    word_counts = Counter(words)
    print(word_counts)
    # Counter({'eyes': 8, 'the': 5, 'look': 4, 'my': 3, 'into': 3, 'around': 2,
    #  "don't": 1, 'not': 1, "you're": 1, 'under': 1})

    top_three = word_counts.most_common(3)
    print(top_three)  # [('eyes', 8), ('the', 5), ('look', 4)]

    print(word_counts['look'])  # 4
    print(word_counts['the'])   # 5
    print(word_counts['into'])  # 3
    print(word_counts['eyes'])  # 8

    # if you want to increment the count manually, simply use addition
    morewords = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']
    for word in morewords:
        word_counts[word] += 1

    print(word_counts['eyes'])  # 9

    # or use update() method
    word_counts.update(morewords)
    print(word_counts['eyes'])  # 10

    a = Counter(words)
    b = Counter(morewords)

    # Combine counts
    c = a + b

    # Subtract counts
    d = a - b


if __name__ == '__main__':
    most_frequently_occurring_items()