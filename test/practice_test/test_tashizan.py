import unittest

from practice_test.tashizan import tashizan


class TestTashizan(unittest.TestCase):
    """test class of tashizan.py
    """

    def test_tashizan(self):
        """tashizanメソッドで足し算が行われるか確認する
        """
        value1 = 3
        value2 = 5
        expected = 8
        actual = tashizan(value1, value2)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
