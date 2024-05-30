from project.extended_list import IntegerList
import unittest


class TestIntegerList(unittest.TestCase):
    def setUp(self):
        self.list = IntegerList(False, True, 1, 2, 3, 4, 5, 6, 7, "asd", 12.45)

    def test_if_initialize_correctly_only_integers(self):
        expected = [1, 2, 3, 4, 5, 6, 7]
        result = self.list._IntegerList__data
        self.assertEqual(expected, result)

    def test_if_get_data_method_returns_correctly(self):
        expected = self.list._IntegerList__data
        result = self.list.get_data()
        self.assertEqual(expected, result)

    def test_if_add_method_raises_correctly_if_non_int_type_is_passed(self):
        with self.assertRaises(ValueError) as ve:
            self.list.add("2.4")
        expected = "Element is not Integer"
        result = str(ve.exception)
        self.assertEqual(expected, result)

    def test_if_an_integer_is_added_correctly_with_add_method(self):
        self.list.add(8)
        result = self.list._IntegerList__data[7]
        expected = 8
        self.assertEqual(expected, result)

    def test_if_remove_index_method_raises_correctly_when_incorrect_index_is_passed(self):
        with self.assertRaises(IndexError) as err:
            self.list.remove_index(11)
        expected = "Index is out of range"
        result = str(err.exception)
        self.assertEqual(expected, result)

    def test_is_remove_index_method_removes_correctly_and_returns_correctly(self):
        result = self.list.remove_index(1)
        expected = 2
        self.assertEqual(expected, result)
        result = self.list._IntegerList__data
        expected = [1, 3, 4, 5, 6, 7]

    def test_if_get_method_raises_correctly_if_invalid_index_is_passed(self):
        with self.assertRaises(IndexError) as err:
            self.list.get(10)
        expected = "Index is out of range"
        result = str(err.exception)
        self.assertEqual(expected, result)

    def test_if_get_method_returns_correctly_when_valid_index_is_passed(self):
        result = self.list.get(4)
        expected = 5
        self.assertEqual(expected, result)

    def test_if_insert_method_raises_correctly_when_invalid_index_is_passed(self):
        with self.assertRaises(IndexError) as err:
            self.list.insert(11, 9)
        expected = "Index is out of range"
        result = str(err.exception)
        self.assertEqual(expected, result)

    def test_is_insert_method_raises_correctly_when_non_int_type_isPassed(self):
        with self.assertRaises(ValueError) as ve:
            self.list.insert(3, "alabala")
        expected = "Element is not Integer"
        result = str(ve.exception)
        self.assertEqual(expected, result)

    def test_if_insert_method_returns_correctly_when_valid_args_are_passed(self):
        self.list.insert(4, 10)
        expected = [1, 2, 3, 4, 10, 5, 6, 7]
        result = self.list._IntegerList__data
        self.assertEqual(expected, result)

    def test_is_get_biggest_method_returns_correctly(self):
        result = self.list.get_biggest()
        expected = 7
        self.assertEqual(expected, result)

    def test_is_get_index_method_returns_correctly(self):
        result = self.list.get_index(4)
        expected = 3
        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()









