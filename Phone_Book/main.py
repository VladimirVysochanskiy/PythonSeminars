import ui
import functions as f

def main():
    while True:
        op = ui.get_op()
        if op == 1:
            new_entry = ui.get_data()
            f.add_data(new_entry)
        elif op == 2:
            find_entry = ui.find_name()
            f.find_person(find_entry)

        elif op == 3:
            break