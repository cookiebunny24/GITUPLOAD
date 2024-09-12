# [2:19 PM] Sathish Srinivasan
# input - abcaba
# output- abcaabbaaa
str1 = "abcaba"
count = 0
mydic = {}
str2 = ""
for i in str1:
    if mydic.__contains__(i):
        mydic[i]+=1
        # print(mydic[i])
        for n in range(0,mydic[i]):
            str2=str2+i
    else:
        mydic[i] = 1
        str2 = str2 + i

# print(mydic)
print(str2)



