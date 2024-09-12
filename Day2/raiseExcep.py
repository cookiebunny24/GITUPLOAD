# print("started")
# age=4
# if age < 5:
#     raise ValueError
# else:
#     print("child is above 5")
#
#


print("started")
age=4
try:
    if age<5:
         raise ValueError("Below 5 is not allowed exception")
    else:
        print("child is above 5")
except ValueError as v:
    print("exception",v)

