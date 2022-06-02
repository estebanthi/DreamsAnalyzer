import unittest


from models.collections.base_collection import BaseCollection


class TestBaseCollection(unittest.TestCase):

    def test_init(self):
        items = [1, 2, 3]
        collection = BaseCollection(items)

    def test_init_empty(self):
        collection = BaseCollection()

    def test_get_item(self):
        items = [1, 2, 3]
        collection = BaseCollection(items)
        self.assertEqual(collection[1], items[1])

    def test_get_item_overflow(self):
        items = [1, 2, 3]
        collection = BaseCollection(items)
        with self.assertRaises(IndexError):
            collection[10]

    def test_iter(self):
        items = [1, 2, 3]
        collection = BaseCollection(items)

        new_list = [item for item in collection]
        self.assertEqual(items, new_list)

    def test_repr(self):
        items = [1, 2, 3]
        collection = BaseCollection(items)

        self.assertEqual(str(collection), str(items))

    def test_len(self):
        items = [1, 2, 3]
        collection = BaseCollection(items)

        self.assertEqual(len(collection), len(items))

    def test_append(self):
        items = [1, 2, 3]
        collection = BaseCollection(items)

        collection.append(19)
        self.assertEqual(collection[-1], 19)


if __name__ == '__main__':
    unittest.main()
