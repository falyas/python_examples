def fun(a):
    if a > 30:
        return 3
    else:
        print(a)
        return a + fun(a + 3)

print(fun(25))
