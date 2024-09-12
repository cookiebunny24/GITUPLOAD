class A:
    x, y=300, 200
    def parent(self):
        print("This is parent")
        print(self.x+self.y)

class B:
    a,b= 10,30
    def child(self):
        print("child class")
        print(self.a*self.b)
class C(A,B):
    c,d=500,200
    def child2(self):
        print("another child")
        print(self.c-self.d)


obj=C()
obj.parent()
obj.child2()
obj.child()