import unittest


import tests.dataclasses as dataclasses


loader = unittest.TestLoader()
suite = unittest.TestSuite()

suite.addTests(loader.loadTestsFromModule(dataclasses))

runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)
