class Student:
    def __init__(self, name,age,grade):
       self.name=name
       self.age =age
       self.grade = grade
       
    def get_info (self):
        print(self.name, self.age , self.grade)
        
         
        X= Student("GAD", "12" , "40")
        X.get_info()