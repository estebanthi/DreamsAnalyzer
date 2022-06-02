import unittest


import tests.collections as collections


loader = unittest.TestLoader()
suite = unittest.TestSuite()

suite.addTests(loader.loadTestsFromModule(collections))

runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)
