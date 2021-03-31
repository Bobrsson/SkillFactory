from User import User

user1 = User('Петр Васечки', 1000, 'г.Москва', 'Ментор')
user2 = User('Вася Петров', 5000, 'г.Кукуевск', 'Сановник')

print(User.get_info_wallet(user1))
print('Наши гости: ', User.get_info_user(user1), User.get_info_user(user2))
