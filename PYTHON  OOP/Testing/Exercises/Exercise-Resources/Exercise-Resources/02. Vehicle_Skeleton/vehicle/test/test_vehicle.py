import unittest
from project.vehicle import Vehicle


class TestVehicle(unittest.TestCase):
    def setUp(self) -> None:
        self.car = Vehicle(50, 150)

    def test_if__initialization_setup_correctly(self):
        expected_default_fuel_consumption = 1.25
        expected_fuel_consumption = 1.25
        expected_fuel = 50
        expected_horse_power = 150
        expected_capacity = 50
        self.assertEqual(expected_default_fuel_consumption, self.car.DEFAULT_FUEL_CONSUMPTION)
        self.assertEqual(expected_fuel_consumption, self.car.fuel_consumption)
        self.assertEqual(expected_fuel, self.car.fuel)
        self.assertEqual(expected_horse_power, self.car.horse_power)
        self.assertEqual(expected_capacity, self.car.capacity)

    def test_if_drive_method_raises_correctly_when_not_enough_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(20000)
        expected = "Not enough fuel"
        result = str(ex.exception)
        self.assertEqual(expected, result)

    def test_if_drive_method_returns_correctly_when_valid_distance_is_passed(self):
        self.car.drive(10)
        expected = 50 - 12.5
        result = self.car.fuel
        self.assertEqual(expected, result)

    def test_if_refuel_method_raises_correctly_when_too_much_fuel_passed(self):
        self.car.fuel = 40
        with self.assertRaises(Exception) as ex:
            self.car.refuel(20)
        expected = "Too much fuel"
        result = str(ex.exception)
        self.assertEqual(expected, result)

    def test_if_refuel_method_returns_correctly_when_valid_fuel_is_passed(self):
        self.car.fuel = 30
        self.car.refuel(15)
        expected = 45
        result = self.car.fuel
        self.assertEqual(expected, result)

    def test_is___str___method_returns_correctly(self):
        expected = f"The vehicle has 150 " \
                   f"horse power with 50 fuel left and " \
                   f"1.25 fuel consumption"
        result = str(self.car)
        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
