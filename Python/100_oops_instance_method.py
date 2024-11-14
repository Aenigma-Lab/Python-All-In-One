# instance methods 
# instance and object both are same 

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

p1 = Person('Shubham','Mishra', 24)
p2 = Person('Raghav','Kumar',27)

print(p1.full_name())
# how the actually code is running
print(Person.full_name(p2))

print(Person.full_name(p1))

