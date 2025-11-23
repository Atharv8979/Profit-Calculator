from product import product_details
from calculator import calculate
from history import save_record, show_history, clear_history
from menu import show_menu

def wait():
    input("\nPress Enter to continue...")

def main():
    while True:
        show_menu()
        
        choice=int(input("Enter your choice: "))

        if choice == 1:
            cp, sp = product_details()
            message, Type, amount, percent = calculate(cp, sp)

            print("----------- RESULT -----------")
            print(message,end="\n------------------------------")

            save_record(cp, sp, Type, amount, percent)
            wait()

        elif choice == 2:
            show_history()
            wait()

        elif choice == 3:
            clear_history()
            wait()
            
        elif choice == 4:
            print("Thank you for using the program!")
            break

        else:
            print("Invalid choice!")
            wait()

main()
