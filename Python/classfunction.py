#creaete a code 
class Bird:
    def __init__(self,name,name1):
        self.name = name
        self.name1 = name1
class Bird1:
    def Bat(self):
        print("This is Flying")
class Bird2:
    def Owl(self):
        print("This is Byting ")
class derived(Bird1,Bird2):
    def __init__(self):
        Bird1.__init__(self,"Bat,","Owl")
        
        Bird2.__init__(self)     
d = derived()
d.Bat()
d.Owl()
print(derived.mro())
