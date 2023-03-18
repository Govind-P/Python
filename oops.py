class computer:
    def init (self,specification,spec,speci):
        self.specification=specification
        self.spec=spec
        self.speci=speci
    def getspecs(self):
        self.specification=input("Enter specification of computer")
    def displayspecs(self):
        print("Specifications of computer are",self.specification)
class laptop(computer):
    def getspec(self):
        self.spec = input("Enter RAM size of laptop")
    def displayspec(self):
        print("RAM size is",self.spec,"GB")
class desktop(computer):
    def getspeci(self):
        self.speci = input("Enter processor feature of desktop")
    def getspeci(self):
        print("Processor features are",self.speci)
obj=laptop()
obj.getspecs()
obj.displayspecs()
obj.getspec()
obj.displayspec()
