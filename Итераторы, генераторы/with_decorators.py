import requests
from datetime import datetime

File_Path = 'dec_logs.txt'


def log_dec(path):
    def decorators(old):
        def o_time(*args, **kvargs):
            res = old(*args, *kvargs)
            with open(path, 'w', encoding='utf-8') as f:
                f.write(f'Дата и время выполнения запроса, {datetime.now()}\n'
                           f'Вызвана функция: {old.__name__}\n'
                           f'С аргументами {args} и {kvargs}\n'
                           f'Возвращаемое значение {res}')
            print(f'Дата и время выполнения запроса, {datetime.now()}')
            print(f'Вызвана функция: {old.__name__}')
            print(f'С аргументами {args} и {kvargs}')
            res = old(*args, *kvargs)
            print(f'Возвращаемое значение {res}')
            return res
        return o_time
    return decorators


print('*' * 20)

@log_dec(File_Path)
def _function(*args, **kwargs):
    url = ', '.join(args)
    response =  requests.get(url=url)
    return response.status_code
_function('https://netology.ru')

print('|*|' * 20)


def decorators(old):
    def o_time(*args, **kvargs):
        print(f'Дата и время выполнения запроса, {datetime.now()}')
        print(f'Вызвана функция: {old.__name__}')
        print(f'С аргументами {args} и {kvargs}')
        res = old(*args, *kvargs)
        print(f'Возвращаемое значение {res}')
        return res

    return o_time



@decorators
def off():
    return 'всем! привет!'

print(off())




