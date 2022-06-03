import unittest


from models.dataclasses.tag import Tag


class TestTag(unittest.TestCase):

    tag = Tag(1, 'Test')

    def test_repr(self):
        str(self.tag)

    def test_hash(self):
        dic = {self.tag: 'ok'}


if __name__ == '__main__':
    unittest.main()
