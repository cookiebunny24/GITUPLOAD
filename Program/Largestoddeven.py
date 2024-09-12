

class Largest:
    def largestEven(self,list):
        curr=-1
        for num in list:
            num=int(num)
            if(num%2==0 and num>curr):
                curr=num

        print("largest even numer", curr)

    def largestOdd(self,list):
        curr0=-1
        for num in list:
            num=int(num)
            if(num%2==1 and num>curr0):
                curr0=num

        print("largest odd", curr0)

listnum = [1, 3, 5, 8, 6,11, 10,346]

obj = Largest()
obj.largestEven(listnum)
obj.largestOdd(listnum)