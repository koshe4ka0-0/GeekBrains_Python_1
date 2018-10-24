# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
import os
import shutil
import sys

def make_new_dir(directory):

    dir_path = os.path.join(os.getcwd(), directory)

    try:

        os.mkdir(dir_path)
        print('Директория {} создана '.format(dir_path))

    except FileExistsError:
        print('Директория {} уже существует '.format(dir_path))

def delet_dir(directory):

    dir_path = os.path.join(os.getcwd(), directory)

    try:
        os.rmdir(dir_path)
        print('Директория {} удалена '.format(dir_path))

    except FileNotFoundError:
        print('Директория {} не существует '.format(dir_path))

def show_this_dir(path):

    for _ in os.listdir(path):
        print(_)

def copy_file(file):

    dupl_file = file + '.dupl'

    try:

        shutil.copy(file, dupl_file)
        print('Файл {} создан'.format(dupl_file))

    except FileNotFoundError:
        print('Файл {} не найден'.format(file))

    



if __name__ == '__main__':

    lst_of_dir = ['dir_' + str(i) for i in range(1,10)]

    # for directory in lst_of_dir:
    #     make_new_dir(directory)

    # for directory in lst_of_dir:
    #     delet_dir(directory)

    # path = os.getcwd()
    # show_this_dir(path)

    # file = sys.argv[0]
    # copy_file(file)


    # try:

    #     file = sys.argv[1]

    # except IndexError:
    #     file = None

    # copy_file(file)













