class Client:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    
    def calculate_bmi(self):
        return (self.weight / self.height ** 2)
    
    def health_status(self):
        bmi = self.calculate_bmi()
        if bmi < 19 :
            return "underWight!"
        elif 19 <= bmi < 25:
            return "Normall."
        elif 25 <= bmi < 30:
            return "OverWight!!"
        else:
            return "Fat!!!"

def show_clients():
    clients = [
        Client("Bahar", 36, 1.73, 60),
        Client("Hadi", 38, 1.78, 81),
        Client("Taha", 8, 1.24, 25)
    ]        
    for client in clients:
        print(f"{client.name} | age: {client.age}| BMI: {client.calculate_bmi():.2f}| Status: {client.health_status()}")

show_clients()