import unittest


from models.data.data_loader import DataLoader
from models.enums import DataLoadingMethod
from models.Controllers.datacontroller import DataController


class DataLoaderTest(unittest.TestCase):

    controller = DataController()
    data_loader = DataLoader(controller)

    def test_local_load(self):
        data = self.data_loader.load_data(DataLoadingMethod.LOCAL, path='data/test.json')
        self.assertIsInstance(data, dict)


if __name__ == "__main__":
    unittest.main()
