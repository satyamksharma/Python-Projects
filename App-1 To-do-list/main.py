todos = []
print("Welcome to the todo list app")
print("Menu - ")
print("1.Add a todo")
print("2.Show all todos")
print("3.Edit a todo")
print("4.Complete a todo")
print("5.Exit")

while True:
    user_action = input("Choose an Option : ")
    user_action = user_action.strip().lower()
    match user_action:
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo)
            with open("todo.txt", "w") as file:
                for todo in todos:
                    file.write(todo + "\n")
        case "show":
            for index, item in enumerate(todos):
                print(f"{index + 1}. {item}")
        case "edit":
            index = int(input("Enter the todo to edit(number): ")) - 1
            new_todo = input("Enter the new todo: ")
            todos[index] = new_todo
            with open("todo.txt", "w") as file:
                for todo in todos:
                    file.write(todo + "\n")
            print("Todo edited successfully")
        case "complete":
            index = int(input("Enter the todo to complete(number): ")) - 1
            todos.pop(index)
            with open("todo.txt", "w") as file:
                for todo in todos:
                    file.write(todo + "\n")
        case "exit":
            break
        case _:
            print("Invalid action")

print("Bye!")
