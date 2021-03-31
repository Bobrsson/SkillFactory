# Этот класс я реализовал для Задание 1.10.3 и Задание 1.10.4
class User:
    def __init__(self, name, wallet, sity, status):
        self.name = name
        self.wallet = wallet
        self.sity = sity
        self.status = status

    def get_name(self):
        return self.name

    def get_wallet(self):
        return self.wallet

    def get_name(self):
        return self.sity

    def get_wallet(self):
        return self.status

    def get_info_wallet(self):
        return str('Имя: {}. Деньги: {}.'.format(self.name, self.wallet))

    # метод для Задание 1.10.4
    def get_info_user(self):
        return str('Имя: {}. Город: {}. Статус: {}.'.format(self.name, self.sity, self.status))
