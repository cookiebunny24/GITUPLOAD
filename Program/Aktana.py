def pal(s):
    rev = ""
    for i in s:
        rev = i + rev

    if rev.__eq__(s):
        return "yes"
    else:
        return "no"

stro="POP"
print(pal(stro))

# def pal(s: str)->bool:
#     return  s==s[::-1]
# print(pal("POP"))