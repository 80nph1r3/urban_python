import unittest
import runner_and_tournament as rat


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls) -> None:
        cls.all_results = {}

    @unittest.skipIf(is_frozen, "Тесты в этой кейсе заморожены")
    def setUp(self) -> None:
        self.runner1 = rat.Runner("Usain", 10)
        self.runner2 = rat.Runner("Andrew", 9)
        self.runner3 = rat.Runner("Nick", 3)

    @classmethod
    def tearDownClass(cls) -> None:
        print("\n")
        for result in cls.all_results.values():
            print({place: runner.name for place, runner in result.items()})

    @unittest.skipIf(is_frozen, "Тесты в этой кейсе заморожены")
    def test_tournament_1(self) -> None:
        tournament = rat.Tournament(90, self.runner1, self.runner3)
        results = tournament.start()
        self.all_results["test1"] = results
        self.assertTrue(results[2] == "Nick")

    @unittest.skipIf(is_frozen, "Тесты в этой кейсе заморожены")
    def test_tournament_2(self) -> None:
        tournament = rat.Tournament(90, self.runner2, self.runner3)
        results = tournament.start()
        self.assertTrue(results[2] == "Nick")
        self.all_results["test2"] = results

    @unittest.skipIf(is_frozen, "Тесты в этой кейсе заморожены")
    def test_tournament_3(self) -> None:
        tournament = rat.Tournament(90, self.runner1, self.runner2, self.runner3)
        results = tournament.start()
        self.assertTrue(results[1] == "Usain")
        self.assertTrue(results[3] == "Nick")
        self.all_results["test3"] = results


if __name__ == "__main__":
    unittest.main()
