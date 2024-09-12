class A:
    name="heena"

class B(A):
    name="JHON"
    def test(self):
        print(super().name)
obj=B()
obj.test()
print(obj.name)
