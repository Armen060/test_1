
print("HI")

def f(*args,**kwargs):
    return sum(args)+sum(kwargs.values())
print(f(1, 2, 3))
print(f(4, 5, 6, 7, 8))
