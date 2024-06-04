import unittest
from collections import deque

from project.railway_station import RailwayStation


class TestRailwayStation(unittest.TestCase):
    def setUp(self) -> None:
        self.station = RailwayStation("Station 1")
        self.station.arrival_trains.append("Train 1")
        self.station.arrival_trains.append("Train 2")
        self.station.arrival_trains.append("Train 3")
        self.station.departure_trains.append("Train 4")
        self.station.departure_trains.append("Train 5")

    def test_if_init_method_sets_up_correctly(self):
        expected_name = "Station 1"
        expected_arrivals = deque(["Train 1", "Train 2", "Train 3"])
        expected_departures = deque(["Train 4", "Train 5"])

        self.assertEqual(expected_name, self.station.name)
        self.assertEqual(expected_arrivals, self.station.arrival_trains)
        self.assertEqual(expected_departures, self.station.departure_trains)

    def test_if_passing_invalid_name_raises_correctly(self):
        with self.assertRaises(ValueError) as ve:
            self.station.name = "S1"
        expected = "Name should be more than 3 symbols!"
        result = str(ve.exception)
        self.assertEqual(expected, result)

    def test_if_new_arrival_on_board_method_returns_correctly(self):
        self.station.new_arrival_on_board("Train 6")
        expected = deque(["Train 1", "Train 2", "Train 3", "Train 6"])
        result = self.station.arrival_trains
        self.assertEqual(expected, result)

    def test_if_train_has_arrived_returns_correctly_when_not_the_first_train_in_the_queue_is_passed(self):
        train_info = "Train 2"
        expected = f"There are other trains to arrive before {train_info}."
        result = self.station. train_has_arrived(train_info)
        self.assertEqual(expected, result)

    def test_if_train_has_arrived_returns_correctly_when_the_first_train_in_the_queue_is_passed(self):
        train_info = "Train 1"
        expected = f"{train_info} is on the platform and will leave in 5 minutes."
        result = self.station.train_has_arrived(train_info)
        self.assertEqual(expected, result)

        expected = deque(["Train 2", "Train 3"])
        result = self.station.arrival_trains
        self.assertEqual(expected, result)

        expected = deque(["Train 4", "Train 5", "Train 1"])
        result = self.station.departure_trains
        self.assertEqual(expected, result)

    def test_if_train_has_left_method_returns_correctly_if_first_train_is_passed(self):
        expected = True
        result = self.station.train_has_left("Train 4")
        self.assertEqual(expected, result)

        expected = deque(["Train 5"])
        result = self.station.departure_trains
        self.assertEqual(expected, result)

    def test_if_train_has_left_method_returns_correctly_if_not_first_train_is_passed(self):
        expected = False
        result = self.station.train_has_left("Train 5")
        self.assertEqual(expected, result)

        expected = deque(["Train 4", "Train 5"])
        result = self.station.departure_trains
        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()

