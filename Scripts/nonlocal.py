def f1(start):
    state = start
    print("f1")

    def f2(x):
        nonlocal state
        print(x, state)
        state += 1
    
    return f2

foo = f1(0)
foo("1) start")
foo("2) start")
foo("3) start")


def f3(start):
    def nested(label):
        print(label, nested.state)
        nested.state += 1
    nested.state = start
    return nested

F = f3(0)

F('a')
F('b')
F('c')

