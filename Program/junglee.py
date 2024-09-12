# Find the second-highest number in an array
# Input -> { 100, 14, 46, 47, 95, 94, 97, 52 };


input1 = [100, 14, 46, 47, 95, 94, 97, 52]
highest, sec, temp = 1, 1, 1
le = len(input1) + 1
temp = 0

for i in range(0,len(input1)):
    for j in range(i+1,len(input1)):
        if input1[i]>input1[j]:
            temp=input1[i]
            input1[i]=input1[j]
            input1[j]=temp

print(input1)
print(input1[-2])