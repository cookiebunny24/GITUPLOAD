list_um=[-8,-2,34,5]
for i in list_um:
    if i<0:
        print("neagtive--->",i)


print("-----------------------------------------------------------------------")
# Python program to print all odd numbers in a range
start,  end = 4, 9
for i in range(start,end+1):
    if(i%2!=0):
        print(i)


print("-----------------------------------------------------------------------")
# Python program to print all even numbers in a range
start1,  end1 = 15, 55

for num in range(start1,end1+1):
    if(num%2==0):
        print("even  - ",num)
