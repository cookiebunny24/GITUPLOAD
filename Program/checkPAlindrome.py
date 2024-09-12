input="abbcddda"
mydic=dict()
count_even=0
count_odd=0
for i in  input:
    # print(input[i])
    if(mydic.__contains__(i)):
        mydic[i]+=1
    else:
        mydic[i]=1

for x,y in mydic.items():
    print(y)
    if int(y)%2==0:
        count_even=count_even+1
    elif int(y)%2==1:
        count_odd=count_odd+1
        print(count_odd)


if count_odd > 1:
    print("cannot be not a palindrome ")
elif count_odd == 1:
    print("Its a palindrome string(")


