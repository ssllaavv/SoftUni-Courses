from project.hero import Hero
import unittest


class TesHero(unittest.TestCase):
    def setUp(self) -> None:
        self.hero = Hero("Primary Hero", 5, 50, 3)
        self.enemy = Hero("Enemy Hero", 7, 70, 2)

    def test_if_initialization_works_correctly(self):
        expected_name = "Primary Hero"
        expected_level = 5
        expected_health = 50
        expected_damage = 3
        self.assertEqual(expected_name, self.hero.username)
        self.assertEqual(expected_level, self.hero.level)
        self.assertEqual(expected_health, self.hero.health)
        self.assertEqual(expected_damage, self.hero.damage)

    def test_if_battle_method_raises_correctly_when_the_same_hero_objet_passed(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)
        expected = "You cannot fight yourself"
        result = str(ex.exception)
        self.assertEqual(expected, result)

    def test_if_battle_method_raises_correctly_when_self_health_is_negative(self):
        self.hero.health = -12
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)
        expected = "Your health is lower than or equal to 0. You need to rest"
        result = str(ve.exception)
        self.assertEqual(expected, result)

    def test_if_battle_method_raises_correctly_if_enemy_hero_health_is_negative(self):
        self.enemy.health = -20
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)
        expected = "You cannot fight Enemy Hero. He needs to rest"
        result = str(ve.exception)
        self.assertEqual(expected, result)

    def test_if_battle_method_returns_correctly_when_there_is_draw(self):
        self.hero.health = 10
        self.enemy.health = 10

        result = self.hero.battle(self.enemy)
        self.assertEqual("Draw", result)
        self.assertEqual(-5, self.enemy.health)
        self.assertEqual(-4, self.hero.health)

    def test_if_battle_method_returns_correctly_when_hero_wins(self):
        self.enemy.health = 10

        result = self.hero.battle(self.enemy)
        self.assertEqual("You win", result)
        self.assertEqual(-5, self.enemy.health)
        self.assertEqual(41, self.hero.health)
        self.assertEqual(6, self.hero.level)
        self.assertEqual(8, self.hero.damage)

    def test_if_battle_method_returns_correctly_when_hero_lose(self):
        self.hero.health = 10

        result = self.hero.battle(self.enemy)
        self.assertEqual("You lose", result)
        self.assertEqual(60, self.enemy.health)
        self.assertEqual(-4, self.hero.health)
        self.assertEqual(8, self.enemy.level)
        self.assertEqual(7, self.enemy.damage)

    def test_if___str___method_returns_correctly(self):
        result = str(self.hero)
        expected = f"Hero Primary Hero: 5 lvl\n" \
                   f"Health: 50\n" \
                   f"Damage: 3\n"
        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()





