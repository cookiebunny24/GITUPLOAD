class Bank:
    def rateOfInterest(self):
        return 0

class XBank(Bank):
    def rateOfInterest(self):
        return 10
class YBank(Bank):
    def rateOfInterest(self):
        return 20

obj=XBank()
print(obj.rateOfInterest())

objy=YBank()
print(objy.rateOfInterest())
