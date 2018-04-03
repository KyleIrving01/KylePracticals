import csv
import operator

movie_list = open("movies.csv", "r", encoding="windows-1252")
reader = csv.reader(movie_list, delimiter=',')

def get_menu_choice():
    def print_menu():       # Your menu design here
        print(30 * "-", "WALKER MENU", 30 * "-")
        print("L - List movies")
        print("A - Add a movie")
        print("W - Watch a movie")
        print("Q - Quit")
        print(73 * "-")

    loop = True
    choice = input

    while loop:          # While loop which will keep going until loop = False
        print_menu()    # Displays menu
        choice = input("Enter your choice [L, A, W, Q]: ")

        if choice == 'L':
            sort = sorted(reader, key=operator.itemgetter(1))
            for eachline in sort:
                print(eachline)
            choice = 2
            loop = False
        elif choice == '2':
            choice = ''
            while len(choice) == 0:
                choice = input("Enter custom folder name(s). It may be a list of folder's names (example: c:,d:\docs): ")
            int_choice = 2
            loop = False
        elif choice == '3':
            choice = ''
            while len(choice) == 0:
                choice = input("Enter a single filename of a file with custom folders list: ")
            int_choice = 3
            loop = False
        elif choice == '4':
            choice = ''
            while len(choice) == 0:
                choice = input("Enter a single filename of a conf file: ")
            int_choice = 4
            loop = False
        elif choice == '5':
            int_choice = -1
            print("Exiting..")
            loop = False  # This will make the while loop to end
        else:
            # Any inputs other than values 1-4 we print an error message
            input("Wrong menu selection. Enter any key to try again..")
    return [int_choice, choice]


print(get_menu_choice())