import redis  # импортируем библиотеку

red = redis.Redis(
    host='redis-10852.c10.us-east-1-2.ec2.cloud.redislabs.com',
    # ваш хост, если вы поставили редис к себе на локальную машину, то у вас это будет localhost. Если же вы находитесь на windows, то воспользуйтесь полем host из вашей облачной БД которую мы создавали в скринкасте.
    port=10852,
    # порт подключения. На локальной машине это должно быть 6379. Для пользователей облачного сервиса порт всегд разный, по этому его надо копировать оттуда же, что и host.
    password='Cm2UQoTIEfe3t5pckFdqsKltdCt2gKeI'
# для локальной машины пароль не требуется (если вы устанавливали редис к себе на компьютер и не пользовались облачным сервисом из скринкаста выше) Для пользователей облачного сервиса пароль находится в вашей облачной базе данных в поле password
)
