import unittest

# check if course belongs to a minor
from minor import check_course_in_minor

class TestMinor(unittest.TestCase):
    # Jean
    def test_check_course_in_minor(self):
        course = "MIE439H1S"
        minor = "Biomedical Engineering Minor"
        result = check_course_in_minor(course)
        self.assertEqual(result,minor)

if __name__ == '__main__':
    unittest.main()
