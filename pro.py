import sys


def show_size_mem(function):
    def wrapper(*args, **kwargs):
        print('Функция:')
        f = function(*args, **kwargs)
        print('Занимаемая память:', sys.getsizeof(f))

    return wrapper


@show_size_mem
def list_num():
    number = [i for i in range(1, 1000000)]
    print('Создание списка с числами от 1 до 1000000')
    return number


@show_size_mem
def gen_num():
    number = (i for i in range(1, 1000000))
    print('Создание генератора чисел от 1 до 1000000')
    return number


show_size_mem(list_num())
show_size_mem(gen_num())
