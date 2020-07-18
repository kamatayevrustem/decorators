from datetime import datetime
import time
import inspect


def my_decorator(some_function):
    def wrapper(*args, **kwargs):
        path = kwargs.get('path')
        full_path = f'{path}test.txt'
        with open(full_path, 'a', encoding="utf8") as f:
            f.write(f'Log, время запуска функции: {datetime.now()}\n')
            start_time = time.time()
            frame = inspect.currentframe()
            f.write(f'Название функции: {inspect.getframeinfo(frame).function}\n')
            f.write(f'Неименованные аргументы args: {args}\n')
            f.write(f'Именованные аргументы kwargs: {kwargs}\n')
            f.write(f'Результат выполнения функции: {some_function(*args, **kwargs)}\n')
            spend_time = time.time() - start_time
            f.write(f'Было потрачено времени на выполнение фукнции: {spend_time} секунд\n')
            f.write(f'Время окончания работы фукнции: {datetime.now()}')
            f.write('\n_________________________________________\n\n')

    return wrapper


@my_decorator
def addition(boys, girls, path):
    boys.sort()
    girls.sort()
    finish_return = []
    dating_couples = zip(boys, girls)
    dating_couples = set(dating_couples)
    if len(boys) == len(girls):
        finish_return.append('Идеальные пары:')
        for i, j in zip(boys, girls):
            finish_return.append(f'{i} и {j}')
    else:
        finish_return.append('Количество девочек и мальчиков не равно, поэтому быстрые свидания отменяются сегодня, извините')
    return finish_return

addition(['Peter', 'Alex', 'John', 'Arthur', 'Richard'], ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha'], path='D:/')