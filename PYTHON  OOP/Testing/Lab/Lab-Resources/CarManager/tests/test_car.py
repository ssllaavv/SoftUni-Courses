from project.car_manager import Car
import unittest


class TestCar(unittest.TestCase):

    def setUp(self):
        self.car = Car("Toyota", "Corola", 5.0, 50)

    def test_if_initialized_correctly(self):
        expected_make = "Toyota"
        expected_model = "Corola"
        expected_consumption = 5.0
        expected_capacity = 50
        expected_fuel_amount = 0
        self.assertEqual(expected_make, self.car.make)
        self.assertEqual(expected_model, self.car.model)
        self.assertEqual(expected_consumption, self.car.fuel_consumption)
        self.assertEqual(expected_capacity, self.car.fuel_capacity)
        self.assertEqual(expected_fuel_amount, self.car.fuel_amount)

    def test_if_setting_make_to_empty_string_raises_correctly(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ""
        expected = "Make cannot be null or empty!"
        result = str(ex.exception)
        self.assertEqual(expected, result)

    def test_is_changing_make_vith_valid_value_returns_correctly(self):
        self.car.make = "BMW"
        expected = "BMW"
        result = self.car.make
        self.assertEqual(expected, result)

    def test_if_setting_model_to_empty_string_raises_correctly(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ""
        expected = "Model cannot be null or empty!"
        result = str(ex.exception)
        self.assertEqual(expected, result)

    def test_if_setting_fuel_consumption_to_negative_value_raises_correctly(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = -3
        expected = "Fuel consumption cannot be zero or negative!"
        result = str(ex.exception)
        self.assertEqual(expected, result)

    def test_if_setting_fuel_capacity_to_negative_value_raises_correctly(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = -70
        expected = "Fuel capacity cannot be zero or negative!"
        result = str(ex.exception)
        self.assertEqual(expected, result)

    def test_if_setting_fuel_amount_toNegative_raises_correctly(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -40
        expected = "Fuel amount cannot be negative!"
        result = str(ex.exception)
        self.assertEqual(expected, result)

    def test_if_refuel_method_raises_correctly_if_negative_value_is_passed(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(-33)
        expected = "Fuel amount cannot be zero or negative!"
        result = str(ex.exception)
        self.assertEqual(expected, result)

    def test_if_refuel_method_returns_correctly_when_valid_value_is_passed(self):
        self.car.refuel(70)
        expected = 50
        result = self.car.fuel_amount
        self.assertEqual(expected, result)
        self.car.fuel_amount = 10
        self.car.refuel(10)
        expected = 20
        result = self.car.fuel_amount
        self.assertEqual(expected, result)

    def test_if_drive_method_raises_correctly_if_not_enough_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(100)
        expected = "You don't have enough fuel to drive!"
        result = str(ex.exception)
        self.assertEqual(expected, result)

    def test_if_drive_method_returns_correctly_if_there_is_enough_fuel(self):
        self.car.fuel_amount = 50
        self.car.drive(200)
        expected = 40
        result = self.car.fuel_amount
        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()


