def get_op():
    op = int(input("1 - Импорт. \n2 - Экспорт. \n3 - Выход.\n"))
    return op

def get_data():
    surname = input("Фамилия: ")
    name = input("Имя: ")
    phone = input("Телефон: ")
    data_str = surname + " " + name + " " + phone + "\n"
    return data_str

def find_name():
    search = input("Введите Имя или Фамилию для поиска: ")
    return search

