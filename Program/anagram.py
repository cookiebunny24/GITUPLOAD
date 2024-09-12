str1="DAD"
str2="DDewdwea"
str1=str1.lower()
str2=str2.lower()
if len(str2)==len(str1):
    str2=sorted(str2)

    str1=sorted(str1)

    if str1.__eq__(str2):
        print("Strings are anagram")
    else:
        print("not an anagram")
else:
    print("size is different and not an anagram")