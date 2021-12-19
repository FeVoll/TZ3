import unittest
import tz3
import math


filename = open("numbers.txt", "r")
numbersstr = filename.read()
nums = numbersstr.split(" ")
try:
    nums = list(map(int, nums))
except ValueError:
    print('Файл либо пустой/имеет неправильную структуру/содержит текстовые символы')
    print('Запишите числа в одну строку через пробел')


class TestNumsMethod(unittest.TestCase):


    def test_min_and_max(self):
        testnum_min = int(tz3.Tz.min_num(""))
        testnum_max = int(tz3.Tz.max_num(""))
        self.assertEqual(testnum_min, min(nums))
        self.assertEqual(testnum_max, max(nums))

    def test_max_greaterequal_min(self):
        testnum_min = int(tz3.Tz.min_num(""))
        testnum_max = int(tz3.Tz.max_num(""))
        self.assertGreaterEqual(testnum_max, testnum_min)

    def test_sum_multi(self):
        testnum_sum = int(tz3.Tz.sum_nums(""))
        testnum_multi = int(tz3.Tz.multi(""))
        self.assertEqual(testnum_sum, sum(nums))
        self.assertEqual(testnum_multi, math.prod(nums))


