
# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3
import os
import sys
import easy
import normal

print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print(" cp <file_name> - создает копию указанного файла")
    print("rm <file_name> - удаляет указанный файл ")
    print("cd <full_path or relative_path> - меняет текущую директорию на указанную")
    print("ls - отображение полного пути текущей директории")



def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))


def ping():
    print("pong")

def cp_file():

    if not file_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    easy.copy_file(file_name)


def remove_file():

    if not file_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    file_path = os.path.join(os.getcwd(), file_name)

    try:
        os.remove(file_path)
        print('Файл {} удален '.format(file_path))

    except FileNotFoundError:
        print('Файл {} не существует '.format(file_path))



def cd():
    if not paths:
        print("Необходимо указать путь директории вторым параметром")
        return

    normal.change_dir(os.path.abspath(paths))

def ls():
	print(os.path.abspath(os.getcwd()))




do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    'cp': cp_file,
    'rm': remove_file,
    'cd': cd,
    'ls': ls
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None

try:
    file_name = sys.argv[2]
except IndexError:
    file_name = None

try:
    paths = sys.argv[2]
except IndexError:
    paths = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")