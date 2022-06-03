import unittest


from models.dataclasses.category import Category


class TestCategory(unittest.TestCase):

    test_category = Category(1, 'Sports')

    def test_repr(self):
        self.assertIsInstance(str(self.test_category), str)

    def test_hash(self):
        test = {self.test_category: 'ok'}


if __name__ == '__main__':
    unittest.main()
