def add_data(data_str):
    from os import path
    parent_dir = path.dirname(path.abspath(__file__))
    file = open(path.join(parent_dir, 'file.txt'), "a",encoding="UTF-8")
    # file = open("file.txt","a",encoding="UTF-8")
    file.write(data_str)
    file.close()

def find_person(data_str):
    from os import path
    parent_dir = path.dirname(path.abspath(__file__))
    file = open(path.join(parent_dir, 'file.txt'), "r",encoding="UTF-8")
    lst_str = file.readlines()
    for item in lst_str:
        if data_str.lower() in item.lower():
            print(item, end="")
    file.close()

    # for item in lst_str:                       # задел для замены/удаления
    #     if data_str.lower() in item.lower():
    #         print(lst_str.index(item), item, end="")
