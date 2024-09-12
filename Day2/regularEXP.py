pattern= "H[EENA]"
import  re
print("enter input")

text=input()

if re.search(pattern,text):
    print("matched")
else:
    print("notmatched")