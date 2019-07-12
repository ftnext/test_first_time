import unittest

from practice_test.keisan import hikizan


class TestKeisan(unittest.TestCase):
    """test class of keisan.py
    """

    def test_hikizan(self):
        """hikizanメソッドで引き算が行われるか確認する
        """
        value1 = 3
        value2 = 5
        expected = -2
        actual = hikizan(value1, value2)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
