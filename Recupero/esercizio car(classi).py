
from abc import staticmethod

class Car:
    def __init__(self,number:float,hour:float) -> None:
        self.number = number
        self.hour = hour
        self.charge:float = 0

    def str(self):
        f"{self.number}   {self.hour}   {self.charge}$"


@staticmethod
def CalculateCharges(car_list:list[Car]) -> None:
    for car in car_list:
        if car.hour <= 3:
            car.charge = 2.00
        else:
            if car.hour >= 24:
                car.charge = 10.00
            else:
                car.charge += 2.00
                car.hour -= 3.00
                car.charge += car.hour * 0.25

    sum_hours:float = 0
    sum_charges:float= 0

    for car in car_list:
        sum_hours += car.hour
        sum_charges += car.charge


    print("Car   Hours   Charges") 
    for car in car_list:
        print(car) 
    print(f"TOTAL   {sum_hours}   {sum_charges:.2f}$")



if __name__ == '__main__':
    car1 = Car(1,1.5,2.00)
    car2 = Car(2,4.0,2.50)
    car3 = Car(3,24.0,14.50)

    my_list:list[Car] = (car1,car2,car3)

    CalculateCharges(my_list)


