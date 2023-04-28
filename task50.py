# todo
# Создайте декоратор, которые переводит все текстовые аргументы функции в верхний регистр и возвращает их в виде списка текстовых аргументов.

def capitalize_string_args(func):
    def wrapper(*args):
        # arg_list = [arg for arg in args if type(arg) == str]
        arg_list = []
        for arg in args:
            if type(arg) == str:
                arg_list.append(arg)
        return [func(arg.upper()) for arg in arg_list]

    return wrapper


@capitalize_string_args
def return_text(text):
    return text


arglist = [1, 2, 'sadas', 'Hello', 'WORLd', 12.5]
print(return_text(arglist[0], arglist[1], arglist[2], arglist[3], arglist[4], arglist[5]))
