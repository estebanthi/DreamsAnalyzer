import unittest


from models.dataclasses.meta import Meta, MetaType


class TestMeta(unittest.TestCase):

    numeric_meta = Meta('A', 'a', MetaType.NUMERIC)
    string_meta = Meta('B', 'b', MetaType.STRING)

    sample_dream = {'meta': {"a": "1", "b": "red"}}

    def test_get_from_json_dream_numeric(self):
        new_meta = self.numeric_meta.get_from_json_dream(self.sample_dream)
        self.assertIsInstance(new_meta, Meta)
        self.assertEqual(new_meta.value, 1)

    def test_get_from_json_dream_string(self):
        new_meta = self.string_meta.get_from_json_dream(self.sample_dream)
        self.assertIsInstance(new_meta, Meta)
        self.assertEqual(new_meta.value, 'red')

    def test_get_from_json_dream_error(self):
        new_meta = self.string_meta.get_from_json_dream({'c': 2})
        self.assertIsInstance(new_meta, Meta)
        self.assertEqual(new_meta.value, None)

    def test_two_metas_not_eq(self):
        self.assertNotEqual(self.numeric_meta, self.string_meta)

    def test_two_metas_eq(self):
        self.assertEqual(self.numeric_meta, self.numeric_meta)

    def test_two_metas_eq_str(self):
        self.assertEqual('A', self.numeric_meta)

    def test_repr(self):
        str(self.numeric_meta)


if __name__ == '__main__':
    unittest.main()
