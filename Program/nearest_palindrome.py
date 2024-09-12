# clearoute
# Given an integer, find the nearest palindrome to that number. Eg1. I/P : 115 O/P : 111 Eg2. I/P : 117 O/P : 121

def nearestpal(num):
    x=str(num)[::-1]
    if num==int(x):
        print("nearestpalindrome: ", num)
        return  True
    else:
        return  False

def nearest(num):
    sum, sub=num,num
    count=10
    for i in range(1,count):
        sum=sum+i
        if nearestpal(sum) == True:
            break
        sub=sub-i
        if nearestpal(sub) == True:
            break


nearest(145)

