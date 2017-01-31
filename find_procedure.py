import glob
import os.path

#migrations = 'Migrations'
migrations = 'Advanced Migrations'

#  бесконечный цикл
exit_while = False

files = ''
files = glob.glob(os.path.join(migrations, "*.sql"))

while exit_while is False:
    files_new = list()
    find_file = 0
    print('Введите строку ( или q - выход.): ')
    text_find = input()

    if text_find == 'q':
        exit_while = True
    else:
        for file in files:
            with open(file) as fopen:
                text = fopen.read()
                if text_find in text:
                    print(file)
                    find_file += 1
                    files_new.append(file)

    print('Кол-во :', find_file)
    files = files_new


