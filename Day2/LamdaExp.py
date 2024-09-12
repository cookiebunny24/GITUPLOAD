sum= lambda a,b: a+b
print(sum(5,4))


def sample(*args):
    for i in args:
        print(i)

sample(9,3,1,9)