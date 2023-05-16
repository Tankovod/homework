# ------------- LESSON 8, EXERCISE 2 -------------------
# Write classes car, taxi

class Car:
    is_busy = False

    def __init__(self, color: str, count_passenger_seats: int, is_baby_seat: bool):
        self.color = color
        self.count_passenger_seats = count_passenger_seats
        self.is_baby_seat = is_baby_seat

    def __str__(self) -> str:
        return f'Car is {self.color}, seats: {self.count_passenger_seats}, baby seat: {self.is_baby_seat}'

    def __iter__(self):
        return self


class Taxi:
    def __init__(self, cars: list[Car]):
        self.cars = cars

    def find_car(self, count_passengers: int, is_baby: bool) -> Car | None:
        for car in self.cars:
            if all([is_baby <= car.is_baby_seat, count_passengers <= car.count_passenger_seats, car.is_busy == False]):
                car.is_busy = True
                return car
        else:
            return None


car = [Car('green', 5, True), Car('orange', 6, False), Car('blue', 2, False)]
taxi = Taxi(car)
print(taxi.find_car(6, False))
print(str(car[0]))

