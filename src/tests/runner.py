import unittest


import tests.collections as collections
import tests.Controllers as Controllers
import tests.data as data


loader = unittest.TestLoader()
suite = unittest.TestSuite()

suite.addTests(loader.loadTestsFromModule(collections))
suite.addTests(loader.loadTestsFromModule(Controllers))
suite.addTests(loader.loadTestsFromModule(data))

runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)
