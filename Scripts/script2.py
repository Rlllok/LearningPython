def foo(a, b):
    return [x for x in a if x in b]

print(foo([1, 2, 3], [2]))
print(foo([1, 2, 2, 3], [2, 3, 3]))