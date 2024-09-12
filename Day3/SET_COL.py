# myset={"apple","banana", "orange"}
# print(myset)

# myset = {"orange", "banana", "apple"}
# for i in myset:
#     print(i)

# myset = {"orange", "banana", "apple"}
# if "orange" in myset:
#     print("ITS present")
# else:
#     print("not present")


# myset = {"orange", "banana", "apple"}
# myset.add("olives")
# print(myset)
# myset.update(["ola","uber","rapido"])
# print(myset)
# print(len(myset))

# myset={'uber', 'rapido', 'banana', 'orange', 'olives', 'apple', 'ola'}
# myset.remove("uber")
# print(myset)
# myset.discard("ola")
# print(myset)
# myset.clear()
# print(myset)
# del myset
# print(myset)

myset={'uber', 'rapido', 'banana'}
myset2={ 'orange', 'olives', 'apple', 'ola'}
set2= {1,2,3}
set3=myset.union(myset2)
print(set3)
set2.update(myset)
print(set2)