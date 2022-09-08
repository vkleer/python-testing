import unittest
from student import Student


class TestStudent(unittest.TestCase):

    def test_full_name(self):
        student = Student('John', 'Doe')

        self.assertEqual(student.full_name, 'John Doe')

    def test_email(self):
        student = Student('John', 'Doe')

        self.assertEqual(student.email, 'john.doe@email.com')

    def test_alert_principal(self):
        student = Student('John', 'Doe')
        student.alert_principal()

        self.assertTrue(student.alert_principal)


if __name__ == '__main__':
    unittest.main()
