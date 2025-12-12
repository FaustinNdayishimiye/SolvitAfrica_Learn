
class  Animal:
    def __init__(self):
        self.__name= "name"
        self.__age= 0
        self.id= 12
        self.__grade= "A"
        
    def set_age(self,age):
        self.__age=age
    def get_age(self):
        return self.__age
    
    def set_name(self, name):
        self.__name=name
    def get_name(self):
        return self.__name
    
    def set_id(self,id):
         self.id=id
    def get_id(self):
        return self.id

    def set_grade(self, grade):
        self.grade= grade
    def get_grade(self):
        return self.__grade   
    # def speak(self):
    #     return "make sound"
    
# class Dog(Animal):
#     def speak(self):
#         #return "Woof"
#         return super().speak()  # super allows you to access properties from parent class
#     dog= Dog()

an=Animal()
#print(an.__name)
an.set_age(24)
print(an.get_age())
an.set_name("John")
print(an.get_name())
an.set_id(12)
print(an.get_id())
an.set_grade("A")
print(an.get_grade())
