globalmy= "heena"

def myfun():
    localme= "suraj"
    print(globalmy)
    print(localme)

myfun()

# print(localme) #invalid bcz local variable?
print(globalmy)


xy=100
def cool():
    xy=200
    print(xy)
cool()


# xy=100
# def cool():
#     global xy
#     xy=200
#     print(xy)
# cool()
#
# print(xy)

#
# x=100
# def cool():
#     global x
#     x=500
#     print(x)
#
# cool()
# print(x)



x=100
def cool():
    global x
    x=500
    print(x)

print(x)