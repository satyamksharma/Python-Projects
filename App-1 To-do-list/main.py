while True:
    user_action = input("Type 'add', 'show', 'edit', 'delete', 'exit': ")
    user_action = user_action.strip().lower()
    match user_action:
        case "add":
            todo = input("Enter a new todo: ") + "\n"

            with open("todos.txt", "r") as file:
                todos = file.readlines()

            todos.append(todo)

            with open("todos.txt", "w") as file:
                file.writelines(todos)
            file.close()
        case "show":
            for index, item in enumerate(todos):
                print(f"{index + 1}. {item}")
        case "edit":
            number = int(input("Enter the number of the todo to edit: "))
            number = number - 1
            new_todo = input("Enter a new todo: ") + "\n"
            todos[number] = new_todo
            with open("todo.txt", "w") as file:
                file.writelines(todos)
            file.close()
        case "delete":
            number = int(input("Enter the number of the todo to delete: "))
            number = number - 1
            del todos[number]
            with open("todo.txt", "w") as file:
                file.writelines(todos)

            file.close()
        case "exit":
            break
        case _:
            print("Invalid input")
