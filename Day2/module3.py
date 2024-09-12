from Day2 import module1
from Day3 import multipleInhe
from Day3 import multilevel

print(dir(module1)) #gives all the methods associated
obj=multipleInhe.B()
r=multilevel.C()
r1=multilevel.B()
print(r.child2())
print(r1.child())