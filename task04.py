from solution import RomanNumber_4


num_1 = RomanNumber_4('VI')
print(num_1.rom_value)
print(num_1.decimal_number())
print(num_1)
num_2 = RomanNumber_4('IIII')
print(num_2.rom_value)
num_3 = RomanNumber_4('XXIV')
print(num_3.decimal_number())
num_4 = RomanNumber_4('QER2')
nums = []
nums.append(num_1)
nums.append(num_2)
nums.append(num_3)
nums.append(num_4)
print(nums)
print(RomanNumber_4.is_roman('MMMCMLXXXVI'))
print(RomanNumber_4.is_roman('MMМMMLXXXVI'))
