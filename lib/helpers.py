# lib/helpers.py
from models.itinerary import Trip, Activity


def exit_program():
    print("\033[32mGoodbye! \033[0m")
    exit()


def create_trip():
    name = input("\033[34mEnter name for the trip: \033[0m")
    location = input("\033[34mEnter trip location: \033[0m")
    try:
        location = Trip.create(name, location)
        print("\033[32mAdded trip! \033[0m")
    except Exception as exc:
        print("\033[31mError creating trip:  \033[0m", exc)


def list_trips():
    trips = Trip.get_all()
    for trip in trips:
        print(trip)


def find_trip_by_name():
    name = input("\033[34mEnter the trip name: \033[0m")
    trip = Trip.find_by_name(name)
    if trip:
        print(trip)
        view_activities_option = input("\033[34mDo you want to view activities for this trip? (yes/no): \033[0m").strip().lower()
        if view_activities_option == "yes":
            view_activities_for_trip(trip.id) 
    else:
        print(f'\033[31mTrip {name} not found. Please verify the name matches a valid trip. \033[0m')


def view_activities_for_trip(trip_id):
    activities = Activity.filter_by_trip_id(trip_id)
    if activities:
        print("\033[32mActivities for Trip ID", trip_id, ":\033[0m")
        for activity in activities:
            print(activity)

def find_trip_by_id():
    id_ = input("\033[34mEnter the trip id:  \033[0m")
    trip = Trip.find_by_id(id_)
    if trip:
        print(trip) 
        view_activities_option = input("\033[34mDo you want to view activities for this trip? (yes/no): \033[0m").strip().lower()
        if view_activities_option == "yes":
            view_activities_for_trip(trip.id)
    else:
        print(f'\033[31mTrip id {id_} not found. Please verify the id is a number that matches a valid trip \033[0m')


def update_trip():
    id_ = input("\033[34mEnter the trip id:  \033[0m")
    if trip := Trip.find_by_id(id_):
        try:
            name = input("\033[34mEnter trip's new name:  \033[0m")
            trip.name = name
            location = input("\033[34mEnter trip's new location:  \033[0m")
            trip.location = location

            trip.update()
            print("\033[32mTrip changed successfully! \033[0m")
        except Exception as exc:
            print("\033[31mError updating trip. \033[0m", exc)
    else:
        print(f'\033[31mTrip {id_} not found. \033[0m')


def delete_trip():
    id_ = input("\033[34mEnter trip id:  \033[0m")
    if trip := Trip.find_by_id(id_):
        trip.delete()
        print(f'\033[32mTrip id {id_} deleted. \033[0m')
    else:
        print(f'\033[31mTrip id {id_} not found. \033[0m')


def create_activity():
    activity_name = None
    description = None
    trip_id = None
    price = None
    day = None

    while True:
        activity_name = input("\033[34mEnter activity:  \033[0m")

        if not activity_name:
            print(
                "\033[31mActivity name cannot be empty. Please enter a valid name. \033[0m")
        else:
            break

    while True:
        description = input("\033[34mEnter description:  \033[0m")

        if not description:
            print(
                "\033[31mDescription cannot be empty. Please enter a valid description. \033[0m")
        else:
            break

    while True:
        try:
            trip_id = int(input("\033[34mEnter trip id: \033[0m"))
            if not Trip.find_by_id(trip_id):
                print(
                    "\033[31mTrip with the specified ID does not exist. Please choose a valid trip ID. \033[0m")
            else:
                break
        except ValueError:
            print("\033[31mInvalid input. Please enter a valid trip ID. \033[0m")

    while True:
        try:
            price = float(input("\033[34mEnter price:  \033[0m"))
            break
        except ValueError:
            print("\033[31mInvalid price. Please enter a valid price. \033[0m")

    while True:
        day = input("\033[34mEnter day:  \033[0m")
        if day in Activity.VALID_DAYS:
            break
        else:
            print(
                "\033[31mInvalid day of the week. Please enter a valid day. \033[0m")

    try:
        trip_instance = Trip.find_by_id(trip_id)

        if trip_instance:
            activity = Activity.create(
                activity_name, description, price, day, trip_id)
            print("\033[32mActivity added successfully! \033[0m")
            return activity
        else:
            print(
                "\033[31mTrip with the specified ID does not exist. Please choose a valid trip ID. \033[0m")
            return None
    except ValueError as e:
        print(str(e))
        return None


def list_activities():
    activities = Activity.get_all()
    if not activities:
        print("\033[31mNo activities found.\033[0m")
    else:
        for activity in activities:
            print(activity)


def find_activity_by_id():
    id_ = input("\033[34mEnter activity id:  \033[0m")
    activity = Activity.find_by_id(id_)
    if activity:
        print(activity)

        trips_with_activity = Trip.get_trips_with_activity(activity.id)

        if trips_with_activity:
            print("\n\033[36mTrips containing this activity:\033[0m")
            for trip in trips_with_activity:
                print(trip)
        else:
            print("\n\033[31mNo trips found containing this activity.\033[0m")
    else:
        print(
            f"\033[31mActivity id {id_} not found. Please verify id is an integer and matches a valid activity. \033[0m")


def get_valid_activity_name():
    while True:
        activity_name = input("\033[34mEnter activity's new name:  \033[0m")
        if activity_name:
            return activity_name
        else:
            print(
                "\033[31mActivity name cannot be empty. Please enter a valid name. \033[0m")


def get_valid_description():
    while True:
        description = input(
            "\033[34mEnter activity's new description:  \033[0m")
        if description:
            return description
        else:
            print(
                "\033[31mDescription cannot be empty. Please enter a valid description. \033[0m")


def get_valid_price():
    while True:
        try:
            price = float(
                input("\033[34mEnter new price of activity:$  \033[0m"))
            return price
        except ValueError:
            print("\033[31mInvalid price. Please enter a valid price. \033[0m")


def get_valid_day():
    while True:
        day = input("\033[34mEnter new day:  \033[0m")
        if day in Activity.VALID_DAYS:
            return day
        else:
            print(
                "\033[31mInvalid day of the week. Please enter a valid day. \033[0m")


def get_valid_trip_id():
    while True:
        try:
            trip_id = int(input("\033[34mEnter new trip id: \033[0m"))
            return trip_id
        except ValueError:
            print(
                "\033[31mTrip ID must be an integer. Please enter a valid trip ID. \033[0m")


def update_activity():
    id_ = input("\033[34mEnter activity id:  \033[0m")
    if activity := Activity.find_by_id(id_):
        try:
            activity.activity_name = get_valid_activity_name()
            activity.description = get_valid_description()
            activity.price = get_valid_price()
            activity.day = get_valid_day()
            activity.trip_id = get_valid_trip_id()

            activity.update()
            print("\033[32mActivity updated successfully! \033[0m")

        except ValueError as exc:
            print(f"\033[31mError updating activity: {exc} \033[0m")
        except Exception as exc:
            print(f"\033[31mError updating activity: {exc} \033[0m")
    else:
        print(f"\033[31mActivity {id_} not found. \033[0m")


def delete_activity():
    id_ = input("\033[34mEnter activity id:  \033[0m")
    if activity := Activity.find_by_id(id_):
        activity.delete()
        print(f"\033[32mActivity id {id_} deleted. \033[0m")
    else:
        print(
            f"\033[31mActivity id {id_} not found. Please verify id is an integer and matches a valid activity. \033[0m")


def filter_activities_by_trip_id():
    try:
        trip_id = int(
            input("\033[34mEnter trip ID to filter activities: \033[0m"))
        activities = Activity.filter_by_trip_id(trip_id)
        if activities:
            for activity in activities:
                print(activity)
        else:
            print(f'\033[31mNo activities found for trip ID {trip_id}\033[0m')
    except ValueError:
        print("\033[31mInvalid trip ID. Please enter a valid integer\033[0m")


def search_activity_by_name():
    activity_name = input("\033[34mEnter activity name to search:  \033[0m")

    activity = Activity.find_by_activity_name(activity_name)

    if activity:
        print(f"Activity found: {activity}")

        trips_with_activity = Trip.get_trips_with_activity(activity.id)

        if trips_with_activity:
            print("Trips containing this activity:")
            for trip in trips_with_activity:
                print(trip)
        else:
            print("No trips found containing this activity.")
    else:
        print("\033[31mActivity not found. \033[0m")
