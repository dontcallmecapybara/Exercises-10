import random


# task 1
class Circle:
    '''
    Class of Circle.

    Parameters:
    -----------
    radius : int
             Radius of circle.

    Attributes:
    -----------
    all_circles : list
                  List of all class instances.
    pi : int
         The pi number.
    '''


    all_circles: list = []
    pi: float = 3.1415

    def __init__(self, radius = 1):
        self.radius = radius
        Circle.all_circles.append(self)

    def area(self):
        '''
        Calculating a circle area.

        Returns:
        --------
        int
            Circle Area.
        '''


        return Circle.pi * self.radius**2
    
    def __repr__(self):
        return str(self.radius)
    
    @staticmethod
    def total_area():
        '''
        Calculating sum of all areas of circles.

        Returns:
        --------
        int
            Sum of all areas of circles.
        '''

        return sum(circle.area() for circle in Circle.all_circles)
    

# task 2
class NavalBattle_2:
    '''
    Class of Naval Battle for task 2.

    Parameters:
    -----------
    player : str
             Set the identity of the player. If the value does not match,
             it generates an error.

    Attributes:
    -----------
    playing_field : list
                    A playing field for Naval Battle as a grid of 10x10.
    
    Raises:
    -------
    ValueError
        If the value does not match, it raises an error.  
    '''


    playing_field = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    
    def __init__(self, player):
        if player not in ['o', '~']:
            self.player = player
        else:
            raise ValueError('Недопустимое значение попадания игрока в корабль')

    def shot(self, x, y):
        '''
        Making shot on the playing field at the specified coordinates.

        Parameters:
        -----------
        x : int
            The x-coordinate of the shot. Must be between 1 and 10 (inclusive).
        y : int
            The y-coordinate (row) of the shot. Must be between 1 and 10 (inclusive).

        Print:
        ------
        str
            A message indicating whether the shot was a hit ("попал") or a miss ("мимо").
        '''
        if NavalBattle_1.playing_field[y - 1][x - 1] == 1:
            NavalBattle_1.playing_field[y - 1][x - 1] = self.player
            print('попал')
        else:
            NavalBattle_1.playing_field[y - 1][x - 1] = 'o'
            print('мимо')
    
    @staticmethod
    def show():
        '''
        Displays the hidden field.

        Prints:
        -------
        str
            Hidden playing field.
        '''


        count = 0
        info = ''
        for lst in NavalBattle_1.playing_field:
            for elem in lst:
                if elem == 0 or elem == 1:
                    info += '~'
                else:
                    info += elem
            if count != 9:
                info += '\n'
                count += 1
            
        print(info)
            

# task 3
class NavalBattle_3:
    '''
    Class of Naval Battle for task 3.

    Parameters:
    -----------
    player : str
             Set the identity of the player. If the value does not match,
             it generates an error.
    
    Attributes:
    -----------
    playing_field : None or list
                            If playing field is specified – list; else – None.
                            A pLaying field for Naval Battle as a grid of 10x10.
    ships : dict
            Dictionary of ships (keys) and their numbers (values).
    
    Raises:
    -------
    ValueError
        If the value does not match, it raises an error.             
    '''


    playing_field = None
    ships = {4: 1, 3: 2, 2: 3, 1: 4}
    
    def __init__(self, player):
        if player not in ['o', '~']:
            self.player = player
        else:
            raise ValueError('недопустимое значение попадания игрока в корабль')

    def shot(self, x, y):
        '''
        Making shot on the playing field at the specified coordinates.

        Parameters:
        -----------
        x : int
            The x-coordinate of the shot. Must be between 1 and 10 (inclusive).
        y : int
            The y-coordinate (row) of the shot. Must be between 1 and 10 (inclusive).

        Prints:
        ------
        str
            If the field is not specified, prints "игровое поле не задано".
            If this cell has already been shot at, prints "ошибка".
            A message indicating whether the shot was a hit ("попал") or a miss ("мимо").
        '''


        if NavalBattle_2.playing_field == None:
            print('игровое поле не заполнено')
        elif NavalBattle_2.playing_field[y - 1][x - 1] in (self.player, 'o'):
            print('ошибка')
        else:
            if NavalBattle_2.playing_field[y - 1][x - 1] == 1:
                NavalBattle_2.playing_field[y - 1][x - 1] = self.player
                print('попал')
            else:
                NavalBattle_2.playing_field[y - 1][x - 1] = 'o'
                print('мимо')


    @staticmethod
    def show():
        '''
        Displays the hidden field.

        Prints:
        -------
        str
            Hidden playing field.
        '''


        count = 0
        info = ''
        for lst in NavalBattle_2.playing_field:
            for elem in lst:
                if elem == 0 or elem == 1:
                    info += '~'
                else:
                    info += elem
            if count != 9:
                info += '\n'
                count += 1     
        print(info)


    @classmethod
    def new_game(cls):
        '''
        Class Method to randomly locate all ships on the playing field.

        Parameters:
        -----------
        cls : class
              The class the method is bound to.
        
        Raises:
        -------
        IndexError
            If a ship placement would go out of bounds of the playing field.
        '''


        cls.playing_field = [[0 for _ in range(10)] for _ in range(10)]
        
        for ship_size in cls.ships:
            for _ in range(cls.ships[ship_size]):
                orient = random.choice(['hor', 'ver'])
                while True:
                    if orient == 'hor':
                        x, y = random.randint(0, 10 - ship_size), random.randint(0, 9)
                    else:
                        x, y = random.randint(0, 9), random.randint(0, 10 - ship_size)
                    
                    try:
                        if all(cls.playing_field[j][i] == 0
                            for j in range(max(0, y - 1), min(10, y + (ship_size if orient == 'ver' else 1)) + 1)
                            for i in range(max(0, x - 1), min(10, x + (ship_size if orient == 'hor' else 1)) + 1)):
                            
                            for i in range(x, x + (ship_size if orient == 'hor' else 1)):
                                for j in range(y, y + (ship_size if orient == 'ver' else 1)):
                                    cls.playing_field[j][i] = 1
                            break
                    except IndexError:
                        continue


# task 4
class RomanNumber_4:
    '''
    Class of Roman Number.

    Paratemeters:
    -------------
    rom_value : str
                Gets the string and checks for roman numerals. 
                If it is not a roman numeral prints 'ошибка'.

    Attributes:
    -----------
    roman_num : dict
                Main roman numbers (keys) and its decimal equivalents (values).
    
    Prints:
    -------
    str
        Value of self.roman_num or None.
    '''


    roman_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    def __init__(self, rom_value):
        if RomanNumber_4.is_roman(rom_value):
            self.rom_value = rom_value
        else:
            self.rom_value = None
            print('ошибка')
    
    @staticmethod
    def is_roman(value):
        '''
        Checks the source string for roman number.

        Parameters:
        -----------
        value : str
                A string which could be a roman number.

        Returns:
        --------
        bool
             True if value is the roman number or False if isn't.
        '''


        numbers = list(value)
        if all(number in RomanNumber_4.roman_num for number in numbers):
            pass
        else:
            return False
        
        for comb in ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']:
            if value.count(comb) > 1:
                return False

        for i in range(len(numbers) - 1):
            if RomanNumber_4.roman_num[numbers[i]] < RomanNumber_4.roman_num[numbers[i+1]]:
                if numbers[i] == 'I' and numbers[i+1] not in ['V', 'X']:
                    print(numbers[i], numbers[i+1])
                    return False
                elif numbers[i] == 'X' and numbers[i+1] not in ['L', 'C']:
                    print(numbers[i], numbers[i+1])
                    return False
                elif numbers[i] == 'C' and numbers[i+1] not in ['D', 'M']:
                    print(numbers[i], numbers[i+1])
                    return False
        
        for j in range(len(numbers) - 2):
            for symbol in ['V', 'L', 'D']:
                if numbers[j] == symbol and numbers[j+1] == symbol:
                    return False
        
        for l in range(len(numbers) - 3):
            for symbol in ['I', 'X', 'C', 'M']:
                if numbers[l] == symbol and numbers[l+1] == symbol and numbers[l+2] == symbol and numbers[l+3] == symbol:
                    return False
        
        return True
    
    def decimal_number(self):
        '''
        Transforms a Roman number into a decimal value.

        Returns:
        --------
        int
            Decimal number, which is the equivalent of the Roman number.
        '''


        if self.rom_value == None:
            return None
        else:
            decimal_value = 0
            prev_num = 0
            for num in self.rom_value[::-1]:
                cur_num = RomanNumber_4.roman_num[num]
                if cur_num >= prev_num:
                    decimal_value += cur_num
                else:
                    decimal_value -= cur_num
                prev_num = cur_num
            
            return decimal_value

    def __repr__(self):
        return self.rom_value if self.rom_value != None else 'None'   


# task 5
class RomanNumber_5:
    '''
    Class of Roman Number.

    Paratemeters:
    -------------
    rom_value : str
                Gets the string and checks for a roman numerals or for an arabic numerals. 
                If it is not a roman numeral or an arabic numeral prints 'ошибка'.

    Attributes:
    -----------
    roman_num : dict
                Main roman numbers (keys) and its decimal equivalents (values).
    
    Prints:
    -------
    str
        Value of self.roman_num or None.
    '''


    roman_num = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400,
                 'C': 100, 'XC': 90, 'L': 50, 'XL': 40,
                 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}

    def __init__(self, rom_value):
        if RomanNumber_5.is_int(rom_value):
            self.int_value = rom_value
            self.rom_value = self.roman_number()
        elif RomanNumber_5.is_roman(rom_value):
            self.rom_value = rom_value
            self.int_value = self.decimal_number()
        else:
            self.rom_value = None
            self.int_value = None
            print('ошибка')

    def decimal_number(self):
        '''
        Transforms a Roman number into a decimal value.

        Returns:
        --------
        int
            Decimal number, which is the equivalent of the Roman number.
        '''


        if self.rom_value == None:
            return None
        else:
            decimal_value = 0
            prev_num = 0
            for num in self.rom_value[::-1]:
                cur_num = RomanNumber_5.roman_num[num]
                if cur_num >= prev_num:
                    decimal_value += cur_num
                else:
                    decimal_value -= cur_num
                prev_num = cur_num
            
            return decimal_value

    def roman_number(self):
        '''
        Transforms an arabic number into a roman number.

        Returns:
        --------
        str
            A roman number, which is the equivalent of the arabic number.
        '''


        if self.int_value == None:
            return None
        else:
            number = self.int_value
            roman = ''
            for key, value in RomanNumber_5.roman_num.items():
                while number >= value:
                    roman += key
                    number -= value
            return roman

    @staticmethod
    def is_int(value):
        '''
        Checks the source string for an arabic number.

        Parameters:
        -----------
        value : int
                An integer which could be an arabic number.

        Returns:
        --------
        bool
             True if value is the an arabic number or False if isn't.
        '''


        if isinstance(value, int) and 0 < value < 4000:
            return True
        else:
            return False

    @staticmethod
    def is_roman(value):
        '''
        Checks the source string for a roman number.

        Parameters:
        -----------
        value : str
                A string which could be a roman number.

        Returns:
        --------
        bool
             True if value is a roman number or False if isn't.
        '''


        if isinstance(value, str):
            numbers = list(value)
            if all(number in RomanNumber_5.roman_num for number in numbers):
                for comb in ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']:
                    if value.count(comb) > 1:
                        return False

                for i in range(len(numbers) - 1):
                    if RomanNumber_5.roman_num[numbers[i]] < RomanNumber_5.roman_num[numbers[i+1]]:
                        if numbers[i] == 'I' and numbers[i+1] not in ['V', 'X']:
                            print(numbers[i], numbers[i+1])
                            return False
                        elif numbers[i] == 'X' and numbers[i+1] not in ['L', 'C']:
                            print(numbers[i], numbers[i+1])
                            return False
                        elif numbers[i] == 'C' and numbers[i+1] not in ['D', 'M']:
                            print(numbers[i], numbers[i+1])
                            return False
                
                for j in range(len(numbers) - 2):
                    for symbol in ['V', 'L', 'D']:
                        if numbers[j] == symbol and numbers[j+1] == symbol:
                            return False
                
                for l in range(len(numbers) - 3):
                    for symbol in ['I', 'X', 'C', 'M']:
                        if numbers[l] == symbol and numbers[l+1] == symbol and numbers[l+2] == symbol and numbers[l+3] == symbol:
                            return False       
            else:
                return False
            
            return True
        
        else:
            return False

    def __repr__(self):
        return self.rom_value if self.rom_value != None else 'None'


# task 6
class RomanNumber_6:
    '''
    Class of Roman Number.

    Paratemeters:
    -------------
    rom_value : str
                Gets the string and checks for a roman numerals or for an arabic numerals. 
                If it is not a roman numeral or an arabic numeral prints 'ошибка'.

    Attributes:
    -----------
    roman_num : dict
                Main roman numbers (keys) and its decimal equivalents (values).
    
    Prints:
    -------
    str
        Value of self.roman_num or None.
    '''


    roman_num = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400,
                 'C': 100, 'XC': 90, 'L': 50, 'XL': 40,
                 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}

    def __init__(self, rom_value):
        if RomanNumber_5.is_int(rom_value):
            self.int_value = rom_value
            self.rom_value = self.roman_number()
        elif RomanNumber_5.is_roman(rom_value):
            self.rom_value = rom_value
            self.int_value = self.decimal_number()
        else:
            self.rom_value = None
            self.int_value = None
            print('ошибка')

    def decimal_number(self):
        '''
        Transforms a Roman number into a decimal value.

        Returns:
        --------
        int
            Decimal number, which is the equivalent of the Roman number.
        '''


        if self.rom_value == None:
            return None
        else:
            decimal_value = 0
            prev_num = 0
            for num in self.rom_value[::-1]:
                cur_num = RomanNumber_5.roman_num[num]
                if cur_num >= prev_num:
                    decimal_value += cur_num
                else:
                    decimal_value -= cur_num
                prev_num = cur_num
            
            return decimal_value

    def roman_number(self):
        '''
        Transforms an arabic number into a roman number.

        Returns:
        --------
        str
            A roman number, which is the equivalent of the arabic number.
        '''


        if self.int_value == None:
            return None
        else:
            number = self.int_value
            roman = ''
            for key, value in RomanNumber_5.roman_num.items():
                while number >= value:
                    roman += key
                    number -= value
            return roman

    @staticmethod
    def is_int(value):
        '''
        Checks the source string for an arabic number.

        Parameters:
        -----------
        value : int
                An integer which could be an arabic number.

        Returns:
        --------
        bool
             True if value is the an arabic number or False if isn't.
        '''


        if isinstance(value, int) and 0 < value < 4000:
            return True
        else:
            return False

    @staticmethod
    def is_roman(value):
        '''
        Checks the source string for a roman number.

        Parameters:
        -----------
        value : str
                A string which could be a roman number.

        Returns:
        --------
        bool
             True if value is a roman number or False if isn't.
        '''


        if isinstance(value, str):
            numbers = list(value)
            if all(number in RomanNumber_5.roman_num for number in numbers):
                for comb in ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']:
                    if value.count(comb) > 1:
                        return False

                for i in range(len(numbers) - 1):
                    if RomanNumber_5.roman_num[numbers[i]] < RomanNumber_5.roman_num[numbers[i+1]]:
                        if numbers[i] == 'I' and numbers[i+1] not in ['V', 'X']:
                            print(numbers[i], numbers[i+1])
                            return False
                        elif numbers[i] == 'X' and numbers[i+1] not in ['L', 'C']:
                            print(numbers[i], numbers[i+1])
                            return False
                        elif numbers[i] == 'C' and numbers[i+1] not in ['D', 'M']:
                            print(numbers[i], numbers[i+1])
                            return False
                
                for j in range(len(numbers) - 2):
                    for symbol in ['V', 'L', 'D']:
                        if numbers[j] == symbol and numbers[j+1] == symbol:
                            return False
                
                for l in range(len(numbers) - 3):
                    for symbol in ['I', 'X', 'C', 'M']:
                        if numbers[l] == symbol and numbers[l+1] == symbol and numbers[l+2] == symbol and numbers[l+3] == symbol:
                            return False       
            else:
                return False
            
            return True
        
        else:
            return False

    def __add__(self, other):
        if isinstance(other, RomanNumber_5):
            return RomanNumber_5(self.int_value + other.int_value)
        else:
            return 'ошибка'
        
    def __iadd__(self, other):
        if isinstance(other, RomanNumber_5):
            self.int_value += other.int_value
            self.rom_value = self.roman_number()  # Обновите rom_value
            return self
        else:
            print('ошибка')
    
    def __sub__(self, other):
        if isinstance(other, RomanNumber_5):
            return RomanNumber_5(self.int_value - other.int_value)
        else:
            return 'ошибка'
    
    def __isub__(self, other):
        if isinstance(other, RomanNumber_5):
            self.int_value -= other.int_value
            self.rom_value = self.roman_number()  # Обновите rom_value
            return self
        else:
            print('ошибка')
        
    def __mul__(self, other):
        if isinstance(other, RomanNumber_5):
            return RomanNumber_5(self.int_value * other.int_value)
        else:
            return 'ошибка'
    
    def __imul__(self, other):
        if isinstance(other, RomanNumber_5):
            self.int_value *= other.int_value
            self.rom_value = self.roman_number()  # Обновите rom_value
            return self
        else:
            print('ошибка')
    
    def __truediv__(self, other):
        if isinstance(other, RomanNumber_5):
            return RomanNumber_5(self.int_value / other.int_value)
        else:
            print('ошибка')
            return None
        
    def __itruediv__(self, other):
        if isinstance(other, RomanNumber_5):
            self.int_value /= other.int_value
            self.rom_value = self.roman_number()  # Обновите rom_value
            return self
        else:
            print('ошибка')
    
    def __floordiv__(self, other):
        if isinstance(other, RomanNumber_5):
            return RomanNumber_5(self.int_value // other.int_value)
        else:
            return 'ошибка'
    
    def __ifloordiv__(self, other):
        if isinstance(other, RomanNumber_5):
            self.int_value //= other.int_value
            self.rom_value = self.roman_number()  # Обновите rom_value
            return self
        else:
            print('ошибка')
    
    def __mod__(self, other):
        if isinstance(other, RomanNumber_5):
            return RomanNumber_5(self.int_value % other.int_value)
        else:
            return 'ошибка'
        
    def __imod__(self, other):
        if isinstance(other, RomanNumber_5):
            self.int_value %= other.int_value
            self.rom_value = self.roman_number()  # Обновите rom_value
            return self
        else:
            print('ошибка')
    
    def __pow__(self, other):
        if isinstance(other, RomanNumber_5):
            return RomanNumber_5(self.int_value ** other.int_value)
        else:
            return 'ошибка'
    
    def __ipow__(self, other):
        if isinstance(other, RomanNumber_5):
            self.int_value **= other.int_value
            self.rom_value = self.roman_number()  # Обновите rom_value
            return self
        else:
            print('ошибка')

    def __repr__(self):
        return str(self.rom_value)
