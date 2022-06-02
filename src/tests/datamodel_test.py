import unittest
import datetime as dt


from models.Models.datamodel import DataModel
from models.Controllers.datacontroller import DataController
from models.data.data_representation import DataRepresentation
from models.enums import TypeFilterOptions


class DataModelTest(unittest.TestCase):

    controller = DataController()

    def test_init(self):
        datamodel = DataModel(self.controller)
        data = datamodel.data
        self.assertIs(type(data), DataRepresentation)

    def test_filter_by_date(self):
        datamodel = DataModel(self.controller)
        initial_length = len(datamodel.data.dreams)

        start = dt.datetime(2022, 5, 1)
        end = dt.datetime(2022, 5, 3)

        datamodel.filter_dreams(start, end)
        self.assertIs(initial_length > len(datamodel.data.dreams), True)

    def test_filter_by_type(self):
        datamodel = DataModel(self.controller)
        initial_length = len(datamodel.data.dreams)

        type_ = TypeFilterOptions.LUCID

        datamodel.filter_dreams(type_=type_)
        self.assertIs(initial_length > len(datamodel.data.dreams), True)



if __name__ == "__main__":
    unittest.main()
