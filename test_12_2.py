from main import *
import unittest


class TournamentTest(unittest.TestCase):
    all_results = {}

    @classmethod
    def setUpClass(cls):
        cls.all_result = {}

    def setUp(self):
        self.runner = [Runner("Усэйн", 10), Runner("Андрей", 9), Runner("Ник", 3)]

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print("{}:".format(key))
            for k, v in value.items():
                print("{}: {}".format(k, v))

    def test_usain_nick(self):
        turn = Tournament(90, self.runner[0], self.runner[2])
        result = turn.start()
        self.assertTrue(list(result.values())[-1].name == "Ник")
        self.all_results["Результат Усейна и Ника"] = result

    def test_andrey_nick(self):
        turn2 = Tournament(90, self.runner[1], self.runner[2])
        result = turn2.start()
        self.assertTrue(list(result.values())[-1].name == "Ник")
        self.all_results["Результат Андрея и Ника"] = result

    def test_usain_andrey_nick(self):
        turn3 = Tournament(90, *self.runner)
        result = turn3.start()
        self.assertTrue(list(result.values())[-1].name == "Ник")
        self.all_results["Общий результат забега"] = result


if __name__ == '__main__':
    unittest.main()
