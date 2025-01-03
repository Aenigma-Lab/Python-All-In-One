# DRY --- DONT REPEAT YOURSELF

# Base class / Parent class
class Phone:
    def __init__(self, brand, model, price):
        # Initializing brand, model, and price for the phone
        self.brand = brand
        self.model = model
        self.price = max(price, 0)  # Ensuring that price is not negative

    def full_specification(self):
        # This method prints the full specification of the phone
        return f"Phone company is {self.brand}, model is {self.model}, and its price is {self.price}"

    def make_a_call(self, phone_number):
        # This method simulates making a call
        return f"Calling from {self.brand} and number is {phone_number} ..."

# Derived / Child class
class Smartphone(Phone):
    def __init__(self, brand, model, price, ram, rom, rear_camera):
        # Calling the parent class constructor using 'super()' to initialize brand, model, and price
    # two way to call parent first ways is uncommon and second way is very common to use

        # Phone.__init__(self, ram, rom,rear_camera) # this UNCOMMON way to write 
        super().__init__(brand, model, price)
        # Initializing additional attributes specific to Smartphone
        self.ram = ram
        self.rom = rom
        self.rear_camera = rear_camera

    # def full_specification(self):
    #     # Overriding the full_specification method to include additional smartphone details
    #     # Using super() to call the parent method and adding extra details for Smartphone
    #     phone_spec = super().full_specification()  # Get the full specification from the parent class
    #     return f"{phone_spec}, RAM: {self.ram}, ROM: {self.rom}, Rear Camera: {self.rear_camera}"

# Creating an instance of the base class (Phone)
phone = Phone('Nokia', 'Nokia 1100', -1599)

# Creating an instance of the derived class (Smartphone)
smartphone = Smartphone('Apple', 'iPhone 16 Pro Plus', 169999, '16 GB', '256 GB', '200 MP')

# Printing full specifications of both the phone and smartphone
print(phone.full_specification())  # Phone specification only
print(smartphone.full_specification())  # Smartphone specification with additional details

# Example of calling the make_a_call method
print(phone.make_a_call("123-456-7890"))
print(smartphone.make_a_call("987-654-3210"))

