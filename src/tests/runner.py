import unittest


import tests.collections as collections
import tests.Controllers as Controllers
import tests.data as data
import tests.dataclasses as dataclasses
import tests.Models as Models


loader = unittest.TestLoader()
suite = unittest.TestSuite()

suite.addTests(loader.loadTestsFromModule(collections))
suite.addTests(loader.loadTestsFromModule(Controllers))
suite.addTests(loader.loadTestsFromModule(data))
suite.addTests(loader.loadTestsFromModule(dataclasses))
suite.addTests(loader.loadTestsFromModule(Models))

runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)
