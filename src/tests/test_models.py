import unittest


import tests.Models as Models


loader = unittest.TestLoader()
suite = unittest.TestSuite()

suite.addTests(loader.loadTestsFromModule(Models))

runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)
