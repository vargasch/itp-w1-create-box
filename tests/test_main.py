import unittest

from create_box import create_box

first_box_expected = """
****
*  *
****
""".lstrip()

second_box_expected = """
@
""".lstrip()

third_box_expected = """
xxxxxxxxxxxxxxxxxxxxxxxx
x                      x
xxxxxxxxxxxxxxxxxxxxxxxx
""".lstrip()


class TestCreateBox(unittest.TestCase):
    def test_box(self):
        self.assertEqual(create_box(3, 4, '*', True), first_box_expected)

    def test_small_box(self):
        self.assertEqual(create_box(1, 1, '@', True), second_box_expected)

    def test_big_box(self):
        self.assertEqual(create_box(3, 24, 'x', True), third_box_expected)

    # Add your own test using third_box_expected
