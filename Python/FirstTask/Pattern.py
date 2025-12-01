from collections import Counter

def mineoperation(N, string):
    freq = Counter(string)
    result = []

    for char, count in freq.items():
        if count % 2 != 0:
            result.append(f"{char} {N}")
            N += 1  # inserting at the end increases string length

    print(len(result))
    for operation in result:
        print(operation)
        