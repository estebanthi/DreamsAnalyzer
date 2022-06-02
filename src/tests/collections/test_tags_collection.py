import unittest


from models.dreams.tag import Tag
from models.collections.tags_collection import TagsCollection


class TestTagsCollection(unittest.TestCase):

    tag1 = Tag(1, 'HH')
    tag2 = Tag(2, 'WBTB')
    tag3 = Tag(3, 'DILD')

    tags_collection = TagsCollection([tag1, tag2])

    def test_contains_ok(self):
        self.assertIn(self.tag1, self.tags_collection)

    def test_contains_nok(self):
        self.assertNotIn(self.tag3, self.tags_collection)


if __name__ == '__main__':
    unittest.main()
