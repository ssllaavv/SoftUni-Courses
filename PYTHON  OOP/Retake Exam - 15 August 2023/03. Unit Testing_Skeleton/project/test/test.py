import unittest
from project.trip import Trip


class TestTrip(unittest.TestCase):
    def setUp(self) -> None:
        self.trip = Trip(20000, 2, True)

    def test_if_init_setups_correctly(self):

        expected = {'New Zealand': 7500, 'Australia': 5700, 'Brazil': 6200, 'Bulgaria': 500}
        result = self.trip.DESTINATION_PRICES_PER_PERSON
        self.assertEqual(expected, result)

        expected = 20000
        result = self.trip.budget
        self.assertEqual(expected, result)

        expected = 2
        result = self.trip.travelers
        self.assertEqual(expected, result)

        expected = True
        result = self.trip.is_family
        self.assertEqual(expected, result)

    def test_if_passing_less_than_one_travelers_raises_correctly(self):
        with self.assertRaises(ValueError) as ve:
            self.trip.travelers = 0
        expected = 'At least one traveler is required!'
        result = str(ve.exception)

        self.assertEqual(expected, result)

    def test_if_is_family_sets_to_False_when_travelers_count_is_changed_to_one(self):
        self.trip.is_family = False
        self.trip.travelers = 1
        self.trip.is_family = True

        expected = False
        result = self.trip.is_family
        self.assertEqual(expected, result)

    def test_if_booK_a_trip_method_with_invalid_destination_passed_returns_correctly(self):
        expected = 'This destination is not in our offers, please choose a new one!'
        result = self.trip.book_a_trip("The Moon")
        self.assertEqual(expected, result)

    def test_if_booK_a_trip_method_with_insufficient_budget_returns_correctly(self):
        self.trip.travelers = 9
        expected = 'Your budget is not enough!'
        result = self.trip.book_a_trip('New Zealand')
        self.assertEqual(expected, result)

    def test_if_valid_booK_a_trip_method_with_is_family_returns_correctly(self):
        expected = 'Successfully booked destination New Zealand! Your budget left is 6500.00'
        result = self.trip.book_a_trip('New Zealand')
        self.assertEqual(expected, result)

        expected = {'New Zealand': 13500,}
        result = self.trip.booked_destinations_paid_amounts
        self.assertEqual(expected, result)

        expected = 6500
        result = self.trip.budget
        self.assertEqual(expected, result)

    def test_if_valid_booK_a_trip_method_without_is_family_returns_correctly(self):
        self.trip.is_family = False

        expected = 'Successfully booked destination New Zealand! Your budget left is 5000.00'
        result = self.trip.book_a_trip('New Zealand')
        self.assertEqual(expected, result)

        expected = {'New Zealand': 15000}
        result = self.trip.booked_destinations_paid_amounts
        self.assertEqual(expected, result)

        expected = 5000
        result = self.trip.budget
        self.assertEqual(expected, result)

    def test_if_booking_status_method_returns_correctly_when_no_trips_added(self):
        expected = 'No bookings yet. Budget: 20000.00'
        result = self.trip.booking_status()
        self.assertEqual(expected, result)

    def test_if_booking_status_method_returns_correctly_when_there_are_destinations_added(self):
        self.trip.travelers = 1
        self.trip.is_family = False
        self.trip.booked_destinations_paid_amounts = {
            'New Zealand': 7500,
            'Australia': 5700,
            'Brazil': 6200,
            'Bulgaria': 500
        }
        expected = f"Booked Destination: Australia\n" \
                   f"Paid Amount: 5700.00\n" \
                   f"Booked Destination: Brazil\n" \
                   f"Paid Amount: 6200.00\n" \
                   f"Booked Destination: Bulgaria\n" \
                   f"Paid Amount: 500.00\n" \
                   f"Booked Destination: New Zealand\n" \
                   f"Paid Amount: 7500.00\n" \
                   f"Number of Travelers: 1\n" \
                   f"Budget Left: 20000.00"

        result = self.trip.booking_status()
        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()



