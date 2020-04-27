import os


def get_available_num():
    list = os.listdir(os.getcwd())
    count = 0
    for x in list:
        if "test" in x:
            count += 1
    return count


def get_available():
    list = os.listdir(os.getcwd())
    answer = []
    for x in list:
        if "test" in x and "result" not in x:
            answer.append(x)
    print(answer)
    return answer


def is_file_available(name):
    list = os.listdir(os.getcwd())
    print(name)
    if name in list:
        return True
    return False


def pick_the_file():
    print("Доступно", get_available_num(), " файлов")
    file = input("Введите номер файла, начиная с 0: ")
    if is_file_available("test" + file + ".txt"):
        return file
    print("Ошибка")
    return ""


def setup(file, line_number):
    fh = open("test" + file + ".txt")
    counter = 0
    for line in fh:
        if counter >= int(line_number):
            break

        print(line)
        counter += 1


def check_input_string(str):
    """
        Принадлежит ли первый символ строки множеству английских букв, или является символом подчеркивания?
        Принадлежат ли все остальные символы слова множеству английских букв или множеству символов цифр или являются
        символами подчеркивания?
    """
    if 'a' <= str[0].lower() <= 'z' or str[0] == '_':
        for i in range(1, len(str)):
            if not ('a' <= str[i].lower() <= 'z'
                    or '0' <= str[i].lower() <= '9'
                    or str[i].lower() == '_'):
                return False

        return True
    return False


if __name__ == '__main__':
    print("Первая лабораторная: Распечатать в текстовом файле строки, предшествующие строке с заданным номером.")
    ans = pick_the_file()
    if ans != "":
        line_number = input("Введите номер строки до которой нужно распечатать текст: ")
        if int(line_number) > 0:
            setup(ans, line_number)
        else:
            print("Ошибка")

    print("Вторая лабораторная: Проверить, является ли вводимая строка правильным идентификатором.")
    input_string = input("Введите проверяемую строку: ")
    print(check_input_string(input_string))


