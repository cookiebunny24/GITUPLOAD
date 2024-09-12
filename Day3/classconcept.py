class Myclass:
    def m1(self):
        pass
    print("hiii")

    @staticmethod
    def m2(self,num):
        print(self,num)

mc=Myclass()
mc.m1()
mc.m2(34,343)
Myclass().m1()
Myclass().m2(3,2)