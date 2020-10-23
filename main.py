import task1.Car as Car

def main():
    car1 = Car.Car("black", 123, "Lada 2107")
    print(car1)
    print(car1.increase_speed(1200))
    print(car1)
    print(car1.decrease_in_speed(1200))
    print(car1)
    print(car1.change_color("red"))
    print(car1.change_color(123))
    print(car1)

main()
