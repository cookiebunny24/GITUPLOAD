# def func(i,j):
#     print(i,j)
#
# func(23,45)
#
# func(j=90,i=28)


# def func(i,j=10):
#     print(i,j)
#
# func(23)
# func(j=100,i=209)



# def greetings(name, greetmsg):
#     print(greetmsg+ " "+name)
#
# greetings("heena", "LOVE YOU")
# greetings(greetmsg= "HATE YOU", name="VIVEK")


# def myfunc(a,b,c):
#     print(a,b,c)
#
# myfunc(10,2,3)
# myfunc(a=3,b=7,c=12)



def largest(a,b):
    if a>b:
        return a,b
    else:
        return b,a

print(largest(10,20))
print(largest(2,1))
print(type(largest(1,2)))