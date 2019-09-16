#keyword
def f1(a, b, c):
    print(a, b, c)

f1(1, 2, c=1)
# f1(c=1, 2, 3) --- ERROR

#default
def f2(a = []):
    a.append(1)
    print(a)

f2()
f2()
f2()

# **args
def f3(**args): print(args)

#f3(1, 2) --- ERROR (must use keywords)
f3(a = 1, b = 3)