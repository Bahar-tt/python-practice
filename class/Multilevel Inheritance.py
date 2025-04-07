class Divice:
    def __init__(self, brand):
        self.brand = brand

    def show_brand(self):
        print("Brand: ", self.brand)

class Phone(Divice):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def show_model(self):
        print("Model: ", self.model)

class SmartPhone(Phone):
    def __init__(self, brand, model, os):
        super().__init__(brand, model)
        self.os = os

    def show_os(self):
        print("Operating System: ", self.os)


s = SmartPhone("Samsung", "Galexy A73", "Android")
s.show_brand()
s.show_model()
s.show_os()

        

