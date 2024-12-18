import unittest

from runner_and_tournament import Runner


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, "Тесты в этой кейсе заморожены")
    def test_walk(self):
        runner = Runner("test")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    @unittest.skipIf(is_frozen, "Тесты в этой кейсе заморожены")
    def test_run(self):
        runner = Runner("test")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @unittest.skipIf(is_frozen, "Тесты в этой кейсе заморожены")
    def test_challenge(self):
        runner1 = Runner("test1")
        runner2 = Runner("test2")
        for _ in range(10):
            runner1.walk()
            runner2.run()
        self.assertNotEqual(runner1.distance, runner2.distance)


if __name__ == "__main__":
    unittest.main()
