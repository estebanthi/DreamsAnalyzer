import unittest
from unittest.mock import create_autospec


from models.Controllers.datacontroller import DataController
from models.data.data_decoder import DataDecoder
from models.dataclasses.category import Category
from models.dataclasses.tag import Tag
from models.dataclasses.dream import Dream
from models.data.data_representation import DataRepresentation
import datetime as dt
from tests.samples.test_data import json_data


class TestDataDecoder(unittest.TestCase):

    DataController = create_autospec(DataController)
    mock_controller = DataController()
    decoder = DataDecoder(mock_controller)

    test_category = Category(1, 'Sports')
    test_tag = Tag(18, 'Padel', test_category)
    test_dream = Dream(dt.datetime.fromtimestamp(1650949200), "Dream content 1", "Dream1", False, [test_tag])

    def test_parse_category(self):
        json_category = json_data['category']['1']
        category = self.decoder.parse_category(json_category)
        self.assertEqual(category, self.test_category)

    def test_get_categories(self):
        categories = self.decoder.get_categories(json_data['category'])
        self.assertIsInstance(categories, list)
        self.assertEqual(categories[0], self.test_category)

    def test_parse_tag(self):
        tag = self.decoder.parse_tag(json_data['tags']['18'])
        self.assertEqual(tag, self.test_tag)

    def test_get_tags(self):
        tags = self.decoder.get_tags(json_data['tags'])
        self.assertEqual(tags[0], self.test_tag)

    def test_parse_dream(self):
        dream = self.decoder.parse_dream(json_data['dreams']['0'], json_data['tags'])
        self.assertEqual(dream, self.test_dream)

    def test_get_dreams(self):
        dreams = self.decoder.get_dreams(json_data['dreams'], json_data['tags'])
        self.assertEqual(dreams[0], self.test_dream)

    def test_decode_ok(self):
        decoded_data = self.decoder.decode(json_data)
        self.assertIsInstance(decoded_data, DataRepresentation)

    def test_decode_nok(self):
        decoded_data = self.decoder.decode({'dreams': {}})
        self.mock_controller.notify_data_decoding_error.assert_called()
        self.assertIs(decoded_data, None)

if __name__ == '__main__':
    unittest.main()
