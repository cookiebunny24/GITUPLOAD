# Online Python - IDE, Editor, Compiler, Interpreter
def reverse(s):
    list_s=s.split(" ")
    rev = ""
    print(list_s)
    for i in list_s:
        rev = i+" "+rev

    return rev


print (reverse ("Heena Chourasia"))
