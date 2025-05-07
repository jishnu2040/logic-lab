import itertools

nested = [[1, 2], [3, 4,6], [5, 6]]
result = list(itertools.chain.from_iterable(nested))
print(result)
