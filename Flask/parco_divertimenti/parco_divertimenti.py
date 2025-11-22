from flask import Flask, url_for, jsonify
from abc import abstractmethod, ABC


class Ride(ABC):
    id: str
    name: str
    min_height_cm: int

    def __init__(self, id, name, min_height_cm):
        self.id = id
        self.name = name
        self.min_height_cm = min_height_cm

    @abstractmethod
    def category(self):
        pass

    @abstractmethod
    def base_wait(self):
        pass

    def info(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'min_height_cm': self.min_height_cm
        }

    def wait_time(self, crowd_factor: float = 1.0) -> int:
        return int(self.base_wait() * crowd_factor)


class RollerCoaster(Ride):
    inversions: int

    def __init__(self, id, name, min_height_cm, inversions):
        super().__init__(id, name, min_height_cm)
        self.inversions = inversions

    def category(self):
        return 'roller_coaster'

    def base_wait(self):
        return 40

    def info(self):
        data = super().info()
        data['inversions'] = self.inversions
        return data


class Carousel(Ride):
    animals: list[str]

    def __init__(self, id, name, min_height_cm, animals):
        super().__init__(id, name, min_height_cm)
        self.animals = animals

    def category(self):
        return 'family'

    def base_wait(self):
        return 10

    def info(self):
        data = super().info()
        data['animals'] = self.animals
        return data


class Park:
    rides: dict[str, Ride]

    def __init__(self):
        self.rides = {}

    def add(self, ride: Ride) -> None:
        self.rides[ride.id] = ride

    def get(self, ride_id: str) -> Ride:
        return self.rides[ride_id]

    def list_all(self) -> list[Ride]:
        return sorted(self.rides.values(), key=lambda x: x.name)


# ------------------------

app = Flask(__name__)

my_park = Park()

# ------------------------

rc = RollerCoaster("rc1", "Thunder Loop", 140, 3)
car = Carousel("car1", "Magic Carousel", 90, ["horse", "dragon", "unicorn"])

my_park.add(rc)
my_park.add(car)


@app.route('/')
def home():
    return jsonify({
        'description': "Welcome to Park API",
        'car_caracteristics': url_for('get_ride', ride_id=car.id),
        'rc_wait': url_for('get_wait', ride_id=rc.id, crowd=2.0),
        'rides': url_for('get_rides')
    })


@app.route('/rides', methods=['GET'])
def get_rides():
    return jsonify({r.id: r.info() for r in my_park.list_all()})


@app.route('/rides/<ride_id>', methods=['GET'])
def get_ride(ride_id: str):
    ride = my_park.get(ride_id)
    return jsonify({ride_id: ride.info()})


@app.route('/rides/<ride_id>/wait/<float:crowd>', methods=['GET'])
def get_wait(ride_id: str, crowd: float = 1.0):
    ride = my_park.get(ride_id)
    return jsonify({'wait_min': ride.wait_time(crowd)})


# ------------------------

if __name__ == "__main__":
    app.run(debug=True)
