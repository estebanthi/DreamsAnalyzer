import unittest
import unittest.mock as mock


from models.data.loaders.file_loader import FileLoader


class TestFileLoader(unittest.TestCase):

    file_loader = FileLoader()

    def test_load_ok(self):
        with mock.patch("builtins.open", mock.mock_open(read_data='{"test": "ok"}')):
            self.file_loader.load("test")

    def test_load_nok(self):
        with self.assertRaises(FileNotFoundError):
            self.file_loader.load("azertyuiop")

if __name__ == '__main__':
    unittest.main()
