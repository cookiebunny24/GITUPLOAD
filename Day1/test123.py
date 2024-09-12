# Heena123Chourasia34Test111
str1="Heena123Chourasia34Test111"
sum=0
x=0
number=""
for i in str1:
    if i.isdigit():
        print(number)
        number=number + i
    elif i.isalpha():
        x = int (number)

sum = sum + x
number=""