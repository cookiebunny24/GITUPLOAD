# mytupple=("apple","lime","orange")
# print(mytupple)


# mytupple=("apple","lime","orange")
# print(mytupple[1])
# print(mytupple[-1])

# mytupple=("apple","lime","orange","banana","juice","kiwi","melon","johkj")
# print(mytupple[3:5])
# print(mytupple[-4:-1])

# mytupple = ("apple", "lime", "orange", "banana", "juice", "kiwi", "melon", "johkj")
# # convert tuple to list and to list to tuple for CRUD
# mylist=list(mytupple)
# mylist[0]="papaya"
# mytupple=tuple(mylist)
# print(mytupple)


# mytupple = ("apple", "1", "orange")
# print(mytupple)



# mytupple = ("apple", "lime", "orange", "banana", "juice", "kiwi", "melon", "johkj")
# for i in mytupple:
#     print(i)

# mytupple= ("apple", "lime", "orange", "banana", "juice", "kiwi", "melon", "johkj")
# if "lime" in mytupple:
#     print("yes")
# else:
#     print("no")
#
# print(len(mytupple))
#
# mytupplemytupple = ("apple", "lime", "orange", "banana", "juice", "kiwi", "melon", "johkj")
# mytupple2=mytupple
# print(mytupple2)
#
#
# del mytupple2
# print(mytupple2)


tup1=(1,2,3)
tup2=("a","b","c")
tup3=tup1+tup2
print(tup3)
print(tup1.__eq__(tup2))
if tup1==tup2:
    print("tru")
else:
    print("false")