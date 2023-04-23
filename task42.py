#todo:
# Создайте функцию-генератор, которая создает последовательность числовых
# палиндромов: 1 2 3 4 5 6 7 8 9 11 22 33 44 55 66 77 88 99 101 111 121 131 141 151 161 171 181 191 202 212 …

def generate_num_palindrome(limit):
    return [number for number in range(limit) for digits in [[int(num) for num in str(number)]] if digits == digits[::-1]]


limit = 102
print(generate_num_palindrome(limit))