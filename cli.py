# from functions import get_todos, write_todos
import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

try:
    while True:
        user_action = input("Type add, show, edit, complete or exit: ")
        user_action = user_action.strip()  # For striping out the blank space

        if user_action.startswith('add'):
            todo = user_action[4:]
            if len(todo) > 0:
                todos = functions.get_todos()
                todos.append(todo + '\n')
                functions.write_todos(todos)
            else:
                print("Please enter a valid todo")

        elif user_action.startswith('show'):
            todos = functions.get_todos()

            for index, item in enumerate(todos):  # adds a counter to each item in a list or other iterable.
                item = item.strip('\n').title()
                row = f"{index + 1}. {item}"  # For defining f-string
                print(row)

        elif user_action.startswith('edit'):
            try:
                number = int(user_action[5:])
                number = number - 1
                todos = functions.get_todos()
                todos[number] = input("Enter the new todo: ") + '\n'
                functions.write_todos(todos)

            except ValueError:
                print("Your command is not valid.")
                continue

        elif user_action.startswith('complete'):
            try:
                number = int(user_action[9:])
                todos = functions.get_todos()
                index = number - 1
                todo_to_remove = todos[index].strip('\n')
                todos.pop(index)
                functions.write_todos(todos)
                message = f"Todo '{todo_to_remove}' was removed from the list."
                print(message)

            except IndexError:
                print("There is no item with that number.")
                continue

        elif user_action.startswith('exit'):
            break

        else:
            print("Command is not Valid")

except KeyboardInterrupt:
    print("\nProgram interrupted by user.")

print("Bye!")
