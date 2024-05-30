from project.cat import Cat
import unittest


class CatTest(unittest.TestCase):
    def setUp(self):
        self.cat = Cat("Tom")

    def test_if_cat_is_initialized_correctly_name_fed_sleepy_size(self):
        expected_name = 'Tom'
        expected_fed = False
        expected_sleepy = False
        expected_size = 0
        self.assertEqual(expected_name, "Tom")
        self.assertEqual(expected_sleepy, False)
        self.assertEqual(expected_fed, False)
        self.assertEqual(expected_size, 0)

    def test_cats_size_is_increased_after_eating(self):
        self.cat.eat()
        expected = 1
        result = self.cat.size
        self.assertEqual(expected, result)

    def test_Cat_is_fed_after_eating(self):
        self.cat.eat()
        expected = True
        result = self.cat.fed
        self.assertEqual(expected, result)

    def test_Cat_cannot_eat_if_already_fed_raises_an_error(self):
        self.cat.fed = True
        with self.assertRaises(Exception) as ex:
            self.cat.eat()
        expected = 'Already fed.'
        result = str(ex.exception)
        self.assertEqual(expected, result)

    def test_Cat_cannot_fall_asleep_if_not_fed_raises_an_error(self):
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()
        expected = 'Cannot sleep while hungry'
        result = str(ex.exception)
        self.assertEqual(expected, result)

    def test_Cat_is_not_sleepy_after_sleeping(self):
        self.cat.fed = True
        self.cat.sleepy = True
        self.cat.sleep()
        expected = False
        result = self.cat.sleepy
        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
