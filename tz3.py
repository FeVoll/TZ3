
import time
start = time.time()
filename = open("numbers.txt", "r")
numbersstr = filename.read()
nums = numbersstr.split(" ")
try:
    nums = list(map(int, nums))
    list_len = len(nums)
    nums.sort()
except ValueError:
    print('Файл либо пустой/имеет неправильную структуру/содержит текстовые символы')
    print('Запишите числа в одну строку через пробел')

class Tz:


    def __init__(self):
        pass

    def min_num(self):
        min_num = nums[0]
        return min_num

    def max_num(self):
        max_num = nums[list_len-1]
        return max_num

    def sum_nums(self):
        total_sum = 0
        for x in nums:
            total_sum += x
        sum_nums = total_sum
        return sum_nums

    def multi(self):
        total_mult = 1
        for y in nums:
            total_mult *= y
        multiplication = total_mult
        return multiplication

    def show_stat(self):
        print(Tz.min_num(""))
        print(Tz.max_num(""))
        print(Tz.sum_nums(""))
        print(Tz.multi(""))






Tz.show_stat('')
end = time.time()

print(f"Скорость выполнения программы: {end - start} секунд(ы)")







