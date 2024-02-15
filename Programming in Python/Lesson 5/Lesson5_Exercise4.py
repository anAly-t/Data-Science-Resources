# Exercise: Designing a Car Rental System:

# Define a class for a car with attributes like make, model, and rental price.
# Create a class for a car rental system that can manage a fleet of cars.
# Add methods for renting a car, returning a car, and displaying available cars.

class Car:
    def __init__(self, make, model, rental_price, is_rented=False):
        """
        Initialize a Car with make, model, rental price, and initial rental status.
        """
        self.make = make
        self.model = model
        self.rental_price = rental_price
        self.is_rented = is_rented

class CarRentalSystem:
    def __init__(self):
        """
        Initialize a CarRentalSystem with an empty fleet of cars.
        """
        self.fleet = []

    def add_car(self, car):
        """
        Add a new car to the fleet.
        """
        self.fleet.append(car)
        print(f"Added {car.make} {car.model} to the fleet.")

    def display_available_cars(self):
        """
        Display details of available cars in the fleet.
        """
        available_cars = [car for car in self.fleet if not car.is_rented]
        if not available_cars:
            print("No available cars in the fleet.")
        else:
            print("Available Cars:")
            for car in available_cars:
                print(f"{car.make} {car.model} - Rental Price: ${car.rental_price} per day")

    def rent_car(self, make, model):
        """
        Rent a car if it is available.
        """
        for car in self.fleet:
            if car.make == make and car.model == model and not car.is_rented:
                car.is_rented = True
                print(f"Rented {car.make} {car.model}. Rental Price: ${car.rental_price} per day.")
                return
        print(f"Car {make} {model} not available for rent or already rented.")

    def return_car(self, make, model):
        """
        Return a rented car.
        """
        for car in self.fleet:
            if car.make == make and car.model == model and car.is_rented:
                car.is_rented = False
                print(f"Returned {car.make} {car.model}. Thank you for using our service.")
                return
        print(f"Car {make} {model} not found or not currently rented.")

# Creating instances of the Car class
car1 = Car(make="Toyota", model="Camry", rental_price=50)
car2 = Car(make="Honda", model="Accord", rental_price=60)
car3 = Car(make="Ford", model="Mustang", rental_price=80)

# Creating an instance of the CarRentalSystem class
car_rental_system = CarRentalSystem()

# Adding cars to the fleet
car_rental_system.add_car(car1)
car_rental_system.add_car(car2)
car_rental_system.add_car(car3)

# Displaying available cars
car_rental_system.display_available_cars()

# Renting a car
car_rental_system.rent_car(make="Toyota", model="Camry")
car_rental_system.display_available_cars()

# Returning a rented car
car_rental_system.return_car(make="Toyota", model="Camry")
car_rental_system.display_available_cars()

# In this code:

# The Car class represents a car with attributes such as make, model, rental price, and rental status.
# The CarRentalSystem class has methods for adding cars to the fleet, displaying available cars, renting a car, and returning a car.
# Instances of the Car class are created for sample cars.
# An instance of the CarRentalSystem class is created.
# Cars are added to the fleet using the add_car method.
# The display_available_cars method is used to display details of available cars.
# The rent_car method is used to rent a car if it is available.
# The return_car method is used to return a rented car.
# The status of available cars is displayed after each operation.