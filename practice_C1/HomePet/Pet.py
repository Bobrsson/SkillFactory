class Pet:
    def __init__(self, name, age, gender, status):
        self.name = name
        self.age = age
        self.gender = gender
        self.status = status

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_gender(self):
        return self.gender

    def get_status(self):
        return self.status

    def get_info(self):
        print('Имя: {}. Взраст: {}. Пол: {}. Статус: {}.'.format(self.name, self.age, self.gender, self.status))
