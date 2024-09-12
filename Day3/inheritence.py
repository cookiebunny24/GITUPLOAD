class A:
    def parent(self):
        print("This is parent")

class B(A):
    def child(self):
        print("child class")

bobj=B()
bobj.child()
bobj.parent()
