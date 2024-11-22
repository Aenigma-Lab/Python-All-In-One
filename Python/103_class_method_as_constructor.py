# Define the 'Person' class
class Person:
    
    # Class attribute to count the number of instances created
    count_instance = 0  # This is a class variable, shared across all instances of the class

    # The __init__ method is the constructor that gets called when an instance is created
    def __init__(self, first_name, last_name, age):
        # Each time a new instance is created, increment the count_instance
        Person.count_instance += 1  # Access the class variable to keep track of how many instances are created
        
        # Assign instance variables to store the attributes for the instance
        self.first_name = first_name  # Instance variable for the first name
        self.last_name = last_name    # Instance variable for the last name
        self.age = age                # Instance variable for age
    
    # A class method to create an instance from a comma-separated string
    @classmethod
    def from_string(cls, string):
        # Split the string by commas, and assign the values to first, last, and age
        first, last, age = string.split(',')
        
        # Return a new instance of the class using the class method, passing the extracted data
        return cls(first, last, int(age))  # Convert the 'age' to an integer and pass it to the constructor
    
    # An instance method to return the full name of the person
    def full_name(self):
        # Access the instance variables to return a string combining the first and last name
        return f"{self.first_name} {self.last_name}"
    
    # Another instance method to check if the person is above 18 years of age
    def is_above_18(self):
        # Compare the 'age' instance variable with 18 and return True or False
        return self.age > 18
    
    # A class method to return the number of instances of the Person class created
    @classmethod
    def count_instances(cls):
        # Access the class variable 'count_instance' to get the number of instances
        return f"You have created {cls.count_instance} instance(s) of {cls.__name__}."  # Use __name__ to get the class name ('Person')

# Create an instance of the Person class using the constructor (__init__ method)
p1 = Person('Shubham', 'Mishra', 25)  # First name is 'Shubham', last name is 'Mishra', and age is 25
p2 = Person('Ashish', 'Kumar', 55)    # Another instance with first name 'Ashish', last name 'Kumar', and age 55

# Create an instance using the 'from_string' class method
p3 = Person.from_string('Amrendra,Bahubali,28')  # The string 'Amrendra,Bahubali,28' is split into first name, last name, and age

# Print the full name of the third instance using an instance method
print(p3.full_name())  # This will call p3.full_name(), which returns 'Amrendra Bahubali'

# Print the count of instances created using the class method
print(Person.count_instances())  # This will call the class method count_instances() to display the number of instances created
