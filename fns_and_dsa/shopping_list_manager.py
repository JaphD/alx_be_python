def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = int(input("Enter your choice: "))

        if choice == 1:
            input_add = input("Enter the item to add: ")
            shopping_list.append(input_add)
            pass
        elif choice == 2:
            input_remove = input("Enter the item to remove: ")
            shopping_list.remove(input_remove)
            pass
        elif choice == 3:
            print("Current Shopping List:")
            for item in shopping_list:
                print(f"- {item}")
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()