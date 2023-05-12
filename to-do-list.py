from os import system
from time import sleep
import json

def json_file():
    with open('lista_de_tarefas.json', 'w', encoding='utf-8') as todo_json:
        json.dump(todo,
                  todo_json,
                  ensure_ascii=False,
                  indent=2)

todo = []
undo = []
count = 1
options = ('A', 'L', 'U', 'R')
commands = '''Choose an option:
[A] Add to the List
[L] List
[U] Undo
[R] Redo '''

print('-' * 40)
print(f'|{"To Do List":^38}|')

while True:
    print('-' * 40)

    if len(todo) != 0:
        print(f'*' * 20)
        print(f'|{"To Do List":^18}|')
        print(f'*' * 20)
        print(*todo, sep='\n')
        print(f'*' * 20)
    else:
        print('\033[33mNothing to list.\033[m')

    print(commands)
    option = input('-> ').upper().strip()
    print('-' * 40)

    if option not in options:
        while option not in options:
            system('cls')
            print("\033[31mThis isn't a valid choice. Try again:\033[m")
            print()
            print(commands)
            option = input('-> ').upper()
            print('-' * 40)
            
    if option == 'A':
        item = input('Add on your to do list: ').capitalize()
        todo.append(item)
        print(f'\033[32m{item} was added successfully!\033[m')
        json_file()
        print()

    elif option == 'L':
        if len(todo) == 0:
            print('\033[31mNothing to list.\033[m')
        else:
            continue

    elif option == 'U':
        if len(todo) == 0:
            print('\033[31mNothing to undo.\033[m')

        else:
            print('\033[32mThe last item was deleted successfully!\033[m')
            undo.append(todo.pop())
            count -= 1
            json_file()
            print()

    elif option == 'R':
        if len(undo) == 0:
            print('\033[31mNothing to redo.\033[m')
        else:
            redo_item = undo[-1]
            todo.append(redo_item)
            undo.pop()
            print('\033[32mThe redo was executed successfully!\033[m')
            json_file()
            print()

    sleep(1.5)
    system('cls')
