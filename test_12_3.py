
from main import *
import unittest

def skip_if_frozen(method):
    def wrapper(self, *args, **kwargs):
        if self.is_frozen:
            self.skipTest('Тесты в этом кейсе заморожены')
        else:
            return method(self, *args, **kwargs)

    return wrapper

class RunnerTest(unittest.TestCase):
    is_frozen = False

    def test_walk(self):
        runner = Runner("John")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    @skip_if_frozen
    def test_run(self):
        runner = Runner('Maria')
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @skip_if_frozen
    def test_challenge(self):
        runner_1 = Runner('Oleg')
        runner_2 = Runner('Roman')
        for i in range(10):
            if i % 2 == 0:
                runner_1.run()
            else:
                runner_2.walk()
            self.assertNotEqual(runner_1.distance, runner_2.distance)

if __name__ == '__main__':
    unittest.main()




class TournamentTest(unittest.TestCase):
    all_results = {}
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_result = {}

    @skip_if_frozen
    def setUp(self):
        self.runner = [Runner("Усэйн", 10), Runner("Андрей", 9), Runner("Ник", 3)]

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print("{}:".format(key))
            for k, v in value.items():
                print("{}: {}".format(k, v))

    @skip_if_frozen
    def test_usain_nick(self):
        turn = Tournament(90, self.runner[0], self.runner[2])
        result = turn.start()
        self.assertTrue(list(result.values())[-1].name == "Ник")
        self.all_results["Результат Усейна и Ника"] = result

    @skip_if_frozen
    def test_andrey_nick(self):
        turn2 = Tournament(90, self.runner[1], self.runner[2])
        result = turn2.start()
        self.assertTrue(list(result.values())[-1].name == "Ник")
        self.all_results["Результат Андрея и Ника"] = result

    @skip_if_frozen
    def test_usain_andrey_nick(self):
        turn3 = Tournament(90, *self.runner)
        result = turn3.start()
        self.assertTrue(list(result.values())[-1].name == "Ник")
        self.all_results["Общий результат забега"] = result


if __name__ == '__main__':
    unittest.main()
