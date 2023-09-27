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
    delete_activity,
    filter_activities_by_trip_id
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


def trip_menu():
    while True:
        trip_submenu()
        choice = input("> ")
        if choice == "0":
            break
        elif choice == "1":
            create_trip()
        elif choice == "2":
            list_trips()
        elif choice == "3":
            delete_trip()
        elif choice == "4":
            update_trip()
        elif choice == "5":
            find_trip_by_id()
        elif choice == "6":
            find_trip_by_name()
        else:
            print("\033[31mInvalid choice\033[0m")


def trip_submenu():
    print("Trip Menu:")
    print("0. Back to main menu")
    print("1. Create new trip")
    print("2. List trips")
    print("3. Delete a trip")
    print("4. Update a trip")
    print("5. Find trip by id")
    print("6. Find trip by name")


def activity_menu():
    while True:
        activity_submenu()
        choice = input("> ")
        if choice == "0":
            break
        elif choice == "1":
            create_activity()
        elif choice == "2":
            list_activities()
        elif choice == "3":
            find_activity_by_name()
        elif choice == "4":
            find_activity_by_id()
        elif choice == "5":
            update_activity()
        elif choice == "6":
            delete_activity()
        elif choice == "7":
            filter_activities_by_trip_id()
        else:
            print("\033[31mInvalid choice\033[0m")


def activity_submenu():
    print("Activity Menu:")
    print("0. Back to main menu")
    print("1. Create new activity")
    print("2. List activities")
    print("3. Find activity by name")
    print("4. Find activity by id")
    print("5. Update an activity")
    print("6. Delete activity")


if __name__ == "__main__":
    main()
