def f1():
    acts = []
    
    for i in range(4):
        acts.append(lambda x: i ** x)
    
    return acts


acts = f1()
#They are different functions
print(acts[0])
print(acts[1])
#But they all have the same value of i (3 ** x), because they remember last value of i
print(acts[0](2))
print(acts[1](2))
print(acts[2](2))
print(acts[3](2))

def f2():
    acts = []
    
    for i in range(4):
        acts.append(lambda x, i=i: i ** x)  #Use default variable value
    
    return acts


acts = f2()
#Now it works like (i ** x)
print()
print(acts[0](2))
print(acts[1](2))
print(acts[2](2))
print(acts[3](2))