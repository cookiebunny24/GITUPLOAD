print("started")
# num =input()
n= input()
try:
    a=10+n

except TypeError as l:
        print(("handled", l))
except NameError as m:
    print("nam e excep 2", m)
finally:
    print("I am in finallysdjhs")
print("EDEDN")


# try:
#     print(b)
# except NameError as m:
#     print("Excep 2", m)
#
# print("AFTER 2nd EXCEP")