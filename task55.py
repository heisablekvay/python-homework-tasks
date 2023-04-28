# #todo: Написать авторизацию пользователя в систему.
# При реализации авторизации спроектировать абстрактный класс и реализовать методы в наследуемом классе
# login, check_password, check_login

# При запуске программы пользователю необходимо ввести
# логин и пароль, поэтапно.
# login: _________
# password: ________
#
# При неправильном вводе логина должно генерироваться пользовательское исключение LoginNotFound
# Введеный пароль должен проверятся на длину. Длина должна быть более 8 символов иначе генерируем пользовательское
# исключение LengthError
# При вводе некорректного пароля генерируем соответсвуещее исключение
# При успешном заходе генерируем исключение "Доступ разрешен!"

from abc import ABC, abstractmethod


class LoginNotFound(Exception):
    def __init__(self, login):
        super(Exception, self).__init__(f'Login {login} not found')


class LengthError(ValueError):
    def __init__(self, length):
        super(Exception, self).__init__(f'Length {length} should be more than 8')


class IncorrectPassword(Exception):
    def __init__(self):
        super(Exception, self).__init__('Inccorect password!')


class AccessAccepted(Exception):
    def __init__(self, login):
        super(Exception, self).__init__(f'Welcome back, {login}!')


class Auth(ABC):
    @abstractmethod
    def login(self, login, password):
        pass

    @abstractmethod
    def check_password(self, string):
        pass

    @abstractmethod
    def check_login(self, string):
        pass


class Authenticate(Auth):
    def check_login(self, string):
        if string != 'mylogin':
            raise LoginNotFound(string)

    def check_password(self, password):
        if len(password) < 9:
            raise LengthError(len(password))
        if password != 'helloworld':
            raise IncorrectPassword

    def login(self, login, password):
        self.check_login(login)
        self.check_password(password)
        raise AccessAccepted(login)


usr_auth = Authenticate()

try:
    usr_auth.login(input('login: '), input('password: '))
except* AccessAccepted as e:
    print(e.exceptions)
except* Exception as e:
    print(Exception, e)
