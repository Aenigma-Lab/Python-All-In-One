class Mobile:
    def __init__(self, name):
        self.name = name


class MobileStore:
    def __init__(self):
        self.mobiles = []

    def add_mobile(self, new_mobile):
        if isinstance(new_mobile, Mobile):
            self.mobiles.append(new_mobile)
        else:
            raise TypeError('new Mobile should be an object of the Mobile class.')

# Create instances and test
samsung = Mobile('One Plus 10')
mobile_store = MobileStore()
mobile_store.add_mobile(samsung)
mobo_phone = mobile_store.mobiles
print(mobo_phone[0].name)
