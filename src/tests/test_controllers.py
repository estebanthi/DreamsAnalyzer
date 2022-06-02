import unittest


import tests.Controllers as Controllers


loader = unittest.TestLoader()
suite = unittest.TestSuite()

suite.addTests(loader.loadTestsFromModule(Controllers))

runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)
