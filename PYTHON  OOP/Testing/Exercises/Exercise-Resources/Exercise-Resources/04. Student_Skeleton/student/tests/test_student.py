from project.student import Student
import unittest


class TestStudent(unittest.TestCase):
    def setUp(self) -> None:
        self.student = Student("Gosho", {"Python": ["note one", "note two"]})

    def test_if_initialization_sets_up_correctly(self):
        expected_name = "Gosho"
        expected_courses = {"Python": ["note one", "note two"]}
        self.assertEqual(expected_name, self.student.name)
        self.assertEqual(expected_courses, self.student.courses)

    def test_if_enroll_method_returns_correctly_when_existing_course_is_updated(self):
        result = self.student.enroll("Python", ["note three", "note four"], "")
        expected = "Course already added. Notes have been updated."
        expected_notes = ["note one", "note two", "note three", "note four"]
        self.assertEqual(expected, result)
        self.assertEqual(expected_notes, self.student.courses['Python'])

    def test_if_enroll_method_returns_properly_if_new_course_is_added_and_notes_is_Y(self):
        result = self.student.enroll("Java", ["some Java notes", "second note"], "Y")
        expected = "Course and course notes have been added."
        expected_notes = ["some Java notes", "second note"]
        self.assertEqual(expected, result)
        self.assertEqual(expected_notes, self.student.courses["Java"])

    def test_if_enroll_method_returns_properly_if_new_course_is_added_and_notes_is_N(self):
        result = self.student.enroll("Java", ["some Java notes", "second note"], "N")
        expected = "Course has been added."
        expected_notes = []
        self.assertEqual(expected, result)
        self.assertEqual(expected_notes, self.student.courses["Java"])

    def test_if_add_notes_method_raises_correctly_if_unexisting_course_is_passed(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("Java", ["some note", "some other note"])
        expected = "Cannot add notes. Course not found."
        result = str(ex.exception)
        self.assertEqual(expected, result)

    def test_if_add_notes_returns_correctly_when_valid_course_name_isPassed(self):
        result = self.student.add_notes("Python", "note three")
        expected = "Notes have been updated"
        expected_notes = ["note one", "note two", "note three"]
        self.assertEqual(expected, result)
        self.assertEqual(expected_notes, self.student.courses["Python"])

    def test_if_leave_course_method_raises_correctly_if_invalid_course_is_passed(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("Java")
        expected = "Cannot remove course. Course not found."
        result = str(ex.exception)
        self.assertEqual(expected, result)

    def test_id_leave_course_method_returns_correctly_when_valid_course_is_passed(self):
        result = self.student.leave_course("Python")
        expected = "Course has been removed"
        self.assertEqual(expected, result)
        self.assertEqual({}, self.student.courses)


if __name__ == "__main__":
    unittest.main()


