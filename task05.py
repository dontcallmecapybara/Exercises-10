from solution import RomanNumber_5


num_1 = RomanNumber_5(214)
print(num_1.int_value)
print(num_1.roman_number())
print(num_1.rom_value)
print(num_1)
num_2 = RomanNumber_5(5690)
print(num_2.int_value)
num_3 = RomanNumber_5('DXCVII')
print(num_3.int_value)
print(num_3.rom_value)
print(num_3)
print(RomanNumber_5.is_int(-614))
print(RomanNumber_5.is_int(3758))
