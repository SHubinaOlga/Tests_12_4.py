import unittest
import logging
from rt_with_exceptions import Runner

logging.basicConfig(level=logging.INFO, filemode='w',
                        filename='runner_tests.log', encoding='utf-8',
                        format='%(asctime)s | %(levelname)s | %(message)s')

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            slow = Runner('Mедленный', -1)
            for i in range(10):
                slow.walk()
            self.assertEqual(slow.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    def test_run(self):
       try:
            fast = Runner(555)
            for i in range(10):
                fast.run()
            self.assertEqual(fast.distance, 100)
            logging.info('"test_run" выполнен успешно')
       except TypeError:
            logging.warning('Неверный тип данных для объекта Runner',
                    exc_info=True)

if __name__ == '__main__':
   unittest.main()
