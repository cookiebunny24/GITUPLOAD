class A:
    x, y=300, 200
    c=100
    def parent(self):
        print("This is parent")
        print(self.x+self.y)

class B(A):
    a,b= 10,30
    def child(self):
        print("child class")
        print(self.a*self.b)
class C(B):
    c,d=500,200
    def child2(self):
        print("another child")
        print(self.c-self.d)
        print(super().c)
bobj=C()
bobj.child()
bobj.parent()
bobj.child2()