class A:
    x, y=300, 200

class B(A):
    a,b= 10,30
    def m1(self,x,y):
        print(x+y)
        print("child class")
        print(self.a*self.b)
        print("This is parent")
        print(self.x+self.y)

obj=B()
obj.m1(100,23)
