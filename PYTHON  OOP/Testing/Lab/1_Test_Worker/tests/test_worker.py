from project.worker import Worker
import unittest


class WorkerTest(unittest.TestCase):
    def setUp(self):
        self.worker = Worker("Gosho", 1500, 10)

    def test_worker_is_initialized_with_correct_name_salary_and_energy(self):
        expected_name = 'Gosho'
        expected_salary = 1500
        expected_energy = 10
        expected_money = 0
        self.assertEqual(expected_name, self.worker.name)
        self.assertEqual(expected_salary, self.worker.salary)
        self.assertEqual(expected_energy, self.worker.energy)
        self.assertEqual(expected_money, self.worker.money)

    def test_if_the_workers_energy_is_incremented_after_the_rest_method_is_called(self):
        self.worker.rest()
        expected = 11
        result = self.worker.energy
        self.assertEqual(expected, result)

    def test_if_an_error_is_raised_if_the_worker_tries_to_work_with_negative_energy_or_equal_to_0(self):
        self.worker.energy = 0
        with self.assertRaises(Exception) as context:
            self.worker.work()
        expected = 'Not enough energy.'
        result = str(context.exception)
        self.assertEqual(expected, result)

    def test_if_the_workers_money_is_increased_by_his_salary_correctly_after_the_work_method_is_called(self):
        self.worker.work()
        expected = self.worker.salary
        result = self.worker.money
        self.assertEqual(expected, result)

    def test_if_the_workers_energy_is_decreased_after_the_work_method_is_called(self):
        self.worker.work()
        expected = 9
        result = self.worker.energy
        self.assertEqual(expected, result)

    def test_if_the_get_info_method_returns_the_proper_string_with_correct_values(self):
        self.worker.work()
        self.worker.work()
        result = self.worker.get_info()
        expected = 'Gosho has saved 3000 money.'
        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
