#docstings example 


def main():
    print(foo(2, 2))
    print(foo.__doc__) #prints docsting


def foo(a, b):
    """
    this is docstring
    this is docstring
    """
    return a + b

if __name__ == "__main__":
    main()