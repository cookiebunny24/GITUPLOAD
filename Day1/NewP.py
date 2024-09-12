# Write a function to find duplicates in a list of numbers [1, 2, 3, 4, 5, 2, 3, 6]


list_x=[1, 2, 3, 4, 5, 2, 3, 6]
mydic= dict()

for i in list_x:
    if(mydic.__contains__(i)):
        mydic[i]+=1
        print(i, mydic[i])
    else:
        mydic[i]=1