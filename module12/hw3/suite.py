import unittest
from tournament_tests import TournamentTest
from runner_tests import RunnerTest

suite = unittest.TestSuite()
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

test_runner = unittest.TextTestRunner(verbosity=2)

if __name__ == "__main__":
    test_runner.run(suite)
