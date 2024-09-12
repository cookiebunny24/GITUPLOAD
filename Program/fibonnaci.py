# # Write a program to print fibonacci series upto n terms in python
# num = 10
# n1, n2 = 0, 1
# print("Fibonacci Series:", n1, n2, end=" ")
# for i in range(2, num):
#     n3 = n1 + n2
#     n1 = n2
#     n2 = n3
#     print(n3, end=" ")
#
# print()
#
# Python program to print Fibonacci Series
def fibonacciSeries(i):
    if i <= 1:
        return i
    else:
        return (fibonacciSeries(i - 1) + fibonacciSeries(i - 2))


num = 7

if num <= 0:
    print("Please enter a Positive Number")
else:
    print("Fibonacci Series:", end=" ")

for i in range(num):
    print(fibonacciSeries(i), end=" ")
