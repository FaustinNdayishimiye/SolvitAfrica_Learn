class Student:
    def __init__(self, name,age,grade):
       self.name=name
       self.age =age
       self.grade = grade
       
    def get_info (self): #METHODS
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"
        
    
#CREATING OBJ
Student1= Student("Fred", 7,"A" )
Student2= Student ("Frank", 18, "C")
Student3= Student("X", "Y", "Z")
        
        
    #printing info of all student 
print(Student1.get_info())
print(Student2.get_info())  
print(Student3.get_info())

   
   