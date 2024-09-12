# class Myclass:
#     name="jhon"
#
#     def __init__(self,name):
#         print("i am a constructor")
#         print(name)
#         print(self.name)
#
# mc=Myclass("naina")


class Myclass:
    def __init__(self,eid,name,salary): #constructor1
        self.empid=eid
        self.name=name
        self.salary=salary
        print(self.empid,self.name,self.salary)
    def display(self):
        print(self.empid,self.name,self.salary)
    def __str__(self):
        return self.name

e1=Myclass(1001,"NEHA",987654)
e1.display()
print(e1)
e2=Myclass(200,"KUSHI",986877)
e2.display()