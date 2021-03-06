import unittest


import tests.data as data


loader = unittest.TestLoader()
suite = unittest.TestSuite()

suite.addTests(loader.loadTestsFromModule(data))

runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)
