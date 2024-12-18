import logging
import unittest

from runner_tests import RunnerTest

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        filemode="w",
        filename="runner_tests.log",
        encoding="utf8",
        format=("%(levelname)s | %(message)s"),
    )
    suite = unittest.TestSuite()
    test_loader = unittest.TestLoader()
    suite.addTest(test_loader.loadTestsFromTestCase(RunnerTest))
    test_runner = unittest.TextTestRunner()
    test_runner.run(suite)
