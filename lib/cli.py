# lib/cli.py

from helpers import (
    exit_program,
    create_trip,
    list_trips,
    find_trip_by_id,
    find_trip_by_name,
    update_trip,
    delete_trip,
    create_activity,
    list_activities,
    find_activity_by_name,
    find_activity_by_id,
    update_activity,
    delete_activity
)


def main():
    while True:
        main_menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            trip_menu()
        elif choice == "2":
            activity_menu()
        else:
            print("\033[31mInvalid choice\033[0m")


def main_menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Trip Menu")
    print("2. Activity Menu")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Create new trip")
    print("2. List trips")
    print("3. Delete a trip")
    print("4. Update a trip")
    print("5. Find trip by id")
    print("6. Find trip by name")
    print("7. Create new activity")
    print("8. List activities")
    print("9. Find activity by name")
    print("10. Find activity by id")
    print("11. Update an activity")
    print("12. Delete an activity")


if __name__ == "__main__":
    main()
