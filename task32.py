#todo: Дан генетический код ДНК (строка, состоящая из букв G, C, T, A)
# Постройте РНК, используя принцип замены букв: G → C, C → G, T → A, A→T.
# Напишите функцию, которая на вход получает ДНК, и возвращает РНК. Например:
# Ввод: GGCTAA
# Вывод: CCGATT

rnk_dict = {
    'G': 'C',
    'C': 'G',
    'T': 'A',
    'A': 'T'
}

def dnk_to_rnk(dnk_str):
    global rnk_dict
    return rnk_dict[dnk_str]

str_in = "GGCTAA"

print(''.join(list(map(dnk_to_rnk, str_in))))