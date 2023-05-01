# Назовем пароль хорошим, если
#
# его длина равна 9 или более символам
# в нем присутствуют большие и маленькие буквы любого алфавита
# в нем имеется хотя бы одна цифра
# Напишите программу, которая требует ввода нового пароля до тех пор, пока не будет введен хороший.
#
#
# На вход программе подается произвольное количество паролей, каждый на отдельной строке. Гарантируется, что среди них присутствует хороший.
#
#
# Для каждого введенного пароля программа должна вывести текст:
#
# LengthError, если длина введенного пароля меньше 9 символов
# LetterError, если в нем все буквы имеют одинаковый регистр
# DigitError, если в нем нет ни одной цифры
# Success!, если введенный пароль хороший
#
# После ввода хорошего пароля все последующие пароли должны игнорироваться.
# Примечание 1. Приоритет вывода сообщений об ошибке в случае невыполнения нескольких условий:
# LengthError, затем LetterError, а уже после DigitError.
#
#
# Sample Input 1:
#
# arr1
# Arrrrrrrrrrr
# arrrrrrrrrrrrrrr1
# Arrrrrrr1
# Sample Output 1:
#
# LengthError
# DigitError
# LetterError
# Success!
#
# Sample Input 2:
#
# beegeek
# Beegeek123
# Beegeek2022
# Beegeek2023
# Beegeek2024
# Sample Output 2:
# LengthError
# Success!

class LengthError(Exception):
    def __init__(self):
        self.txt = 'LengthError'


class LetterError(Exception):
    def __init__(self):
        self.txt = 'LetterError'


class DigitError(Exception):
    def __init__(self):
        self.txt = 'DigitError'


def iscorrect_length(string):
    if len(string) < 9:
        return False
    return True


def isletters_have_same_reg(string):
    if (string == string.upper()) or (string == string.lower()):
        return True
    return False


def isdigits(string):
    return any(char.isdigit() for char in string)


good_password = False
while True:
    password = input('Введите пароль: ')
    try:
        if not iscorrect_length(password):
            raise LetterError()
        if isletters_have_same_reg(password):
            raise LetterError
        if not isdigits(password):
            raise DigitError
        print('Success!')
        break
    except Exception as e:
        print(e.txt)