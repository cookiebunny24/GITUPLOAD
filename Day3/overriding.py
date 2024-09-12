class A:
    x, y=300, 200
    def m1(self):
        print("This is parent")
        print(self.x+self.y)


class B(A):
    a,b= 10,30
    def m1(self):
        print("child class")
        print(self.a*self.b)
        super().m1() #to invoke parent class method through child class

obj=B()
obj.m1()
