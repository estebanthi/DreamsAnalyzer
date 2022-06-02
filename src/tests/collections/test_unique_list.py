import unittest


from models.collections.unique_list import UniqueList


class TestUniqueList(unittest.TestCase):

    def test_init(self):
        numbers = [1, 3, 6, 2, 3, 1, 5]

        unique_list = UniqueList(numbers)
        self.assertIsInstance(unique_list, UniqueList)

    def test_is_unique(self):
        numbers = [1, 3, 6, 2, 3, 1, 5]
        unique_numbers = [1, 2, 3, 5, 6]

        unique_list = UniqueList(numbers)
        self.assertEqual(list(unique_list), unique_numbers)


if __name__ == '__main__':
    unittest.main()
