from gui import SuperMarketGUI
from cli_ar import main_menu
from cli_en import main_menu_en

if __name__ == "__main__":
    choice = int(input("You need to run App:\n[1] - Arabic Terminal\n[2] - English Terminal\n[3] - GUI\n"))

    if choice == 1:
        main_menu()
    elif choice == 2:
        main_menu_en()
    elif choice == 3:
        program = SuperMarketGUI()
        program.mainloop()
    else:
        print("Invalid Choice")