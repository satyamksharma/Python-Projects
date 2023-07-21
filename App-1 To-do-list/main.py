#storing data in text files

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
            if todos.__contains__(todo):
                print("Todo already exists")
            todos.append(todo)
        case "show":
            for index, item in enumerate(todos):
                print(f"{index + 1}. {item}")

        case "edit":
            index = 1 + int(input("Enter the todo to edit(number): "))
            new_todo = input("Enter the new todo: ")
            todos[index] = new_todo
            print("Todo edited successfully")

        case "complete":
            index = 1 + int(input("Enter the todo to complete(number): "))
            todos.pop(index)
        case "exit":
            break
        case _:
            print("Invalid action")


print("Bye!")
