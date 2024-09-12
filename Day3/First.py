# # create strings different ways
#
# st="welcome"
# sr1='welcome'
# str= str('welcome')
# s=str("welcome")
# # create empty strings
# name=""
# name=''
# s= str()

# Strings are immutable
# str1="welcome"
# print(id(str1)) #2422768472912
# str1=str1+"python" #contaenation
# print(id(str1))
# print(str1*2) #priniting number of times mentioned
#

# SLICING
# str="welcome"
# print(str[1:3])
# print(str[:6])
# print(str[2:])
# print(str[:-1])
# print(str[:-2])


# ord() and char() for ascii value
print(ord('A'))
print(chr(65))


# min max len
print(max('hghkm'))
print(min('hghkm'))
print(len('hghkm'))

# in not in operators
lk="welcome"
print("come" in lk)
print("lome" in lk)
print("come" not in lk)
print("lovee" not in lk)
print("==========================================================================================")

# String comparisoon
print("time"=="tie")
print("time">"tie")
print("time"<"tie")
print("Zie">="tie")
print("abc">"")
print("==========================================================================================")
t="34234"
print(t.isdigit())
print(t.isalnum())
print(t.isalpha())
print(t.isascii())
print(t.isidentifier())
print(t.isdecimal())
print("==========================================================================================")
d="ghsdhj"
print(d.isupper())
print(d.islower())
print(d.isspace())
print(" ".isspace())
print("==========================================================================================")
# Search for substrings
print("Heena".startswith("He"))
print("Heena".endswith("na"))
print("Heena".find("He"))
print("Heena".find("s"))
print("HEeena".count("e"))

print("==========================================================================================")

ds="jejwwej"
print(ds.capitalize())
print(ds.title())
print(ds.upper())
print(ds.swapcase())
print(ds.replace("je","na"))
print("==========================================================================================")

sf="NEHA"
rev=""
for i in sf:
    rev=i+rev

    print(rev)

print("==========================================================================================")
d="welcome"

revu= d[::-1]
print(revu)