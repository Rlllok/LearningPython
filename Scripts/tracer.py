def tracer(func, *pargs, **kargs):
    print('calling:', func.__name__)
    return func(*pargs, **kargs)            #Call func and return what func's retunr value[]

def func(a, b, c, d):
    return a + b + c +d

a = tracer(func, 1, 2, c=3, d=4)
print(tracer(func, 1, 2, c=3, d=4))
