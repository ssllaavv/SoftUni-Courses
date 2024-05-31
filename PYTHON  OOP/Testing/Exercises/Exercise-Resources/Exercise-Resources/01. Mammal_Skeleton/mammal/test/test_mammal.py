from unittest import TestCase, main

from project.mammal import Mammal


class TestMammal(TestCase):

    def setUp(self) -> None:
        self.mammal = Mammal("Gosho", "zombie", "wraughhh")

    def test_init_mammal(self):
        self.assertEqual("Gosho", self.mammal.name)
        self.assertEqual("zombie", self.mammal.type)
        self.assertEqual("wraughhh", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_if_correct_sound_is_vocalized_with_make_sound_method(self):
        result = self.mammal.make_sound()
        self.assertEqual("Gosho makes wraughhh", result)

    def test_if_get_kingdom_method_returns_correctly(self):
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_if_info_method_returns_correctly(self):
        result = self.mammal.info()
        expected = "Gosho is of type zombie"
        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()
