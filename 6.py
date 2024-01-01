# Define a class attribute “color” with a default value white. i.e., Every Vehicle
# should be white.

class Vehicle:
    #Setting default value to "white"
    color = "White"

    def __init__(self, make):
        self.make = make

    def display_info(self):
        print(f"Vehicle: {self.color} {self.make}")

def main():
    car1 = Vehicle("BMW")
    car2 = Vehicle("Maruti Suzuki")
    car3 = Vehicle("Audi")

    car1.display_info()  
    car2.display_info()
    car3.display_info()


if __name__=="__main__":
    main()