# 1 2 3 4 5
# n = 2
# 4 5 1 2 3
# 23451

list1=[1,2,3,4,5]
size=len(list1)
list2=list()
n=2
for i in range(size,-1,-1):
    if list1.index(i)==n:
    temp=list1.index(i)
    temp2 =list1.insert(i+n,n)
