import unittest


from models.dataclasses.dream import Dream
import datetime as dt


class TestDream(unittest.TestCase):

    test_dream = Dream(dt.datetime(2022, 1, 1), 'Test', 'Test', False)

    def test_repr(self):
        str(self.test_dream)


if __name__ == '__main__':
    unittest.main()
