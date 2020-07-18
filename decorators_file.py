from datetime import datetime
import time
import inspect
import os

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
def addition(a, b, path):
    result = a + b
    finish_return = "{} + {} = {}".format(a, b, result)
    return finish_return


addition(5, 10, path='D:/')
