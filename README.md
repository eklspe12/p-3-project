### CLI Vacation Planner
---
## Authors

### Spencer Eklund
- Linkedin https://www.linkedin.com/in/spencer-eklund/
- Github https://github.com/eklspe12

### Jenna Millamena
- Linkedin https://www.linkedin.com/in/jen-millamena-software-engineer/
- Github https://github.com/jmillamena

---
## Introduction

This program serves to help users plan future vacations and activities. Continue reading and you will find instructions for navigating the program as well as detailed descriptions of how each function works.
---
## Getting Started

To start this program, please follow the instructions below:

1. Navigate to the folder that holds all program files.
2. Type “pipenv install” and press enter to install necessary dependencies.
3. Type “pipenv shell” and press enter to start the virtual environment.
4. In your virtual environment, type “python lib/seed.py” and press enter to seed the database. Your terminal should now say “Database seeded”
        *One trip and activity are added to the database by default. You will be able to delete these later.
5. In your virtual environment, type “python lib/cli.py” and press enter to start the program. You should now see a list of 13 different options for planning your trip.
---
## Navigating the Program

To navigate the program menus, you will be required to enter the number associated with the option you would like to select. When the program first loads, you will see the following three options:

- 0.Exit the Program: Closes the menu and brings users back to the program files.

- 1.Trip Menu: Displays all options related to modifying, viewing, or creating trips.

- 2.Activity Menu: Display all options related to modifying, viewing, or creating activities.


### Trip Menu

- 0.Back to main menu: Return user to main program menu.

- 1.Create new trip: Allows users to create a new trip by entering a name and location, then automatically saves trips to the database vacations.db. Once a trip is created it can be edited or deleted, and users can add activities to the trip with options described further down.

- 2.List trips: Retrieves all trips from vacations.db and displays their name and location.

- 3.Delete trips: Asks user for trip id and removes that trip from vacations.db. To verify the trip was deleted, enter the “List trips” option immediately after.

- 4.Update trip: First requests id of trip to be updated, then prompts users to type in whatever changes they would like to make. All changes are reflected in vacations.db. To verify changes took place, enter the “List trips” option immediately after.

- 5.Find trip by id: Requests id of trip to display, then returns details of trip with matching id in vacations.db. 

- 6.Find trip by name: Requests name of trip to display, then returns details of trip with matching name in vacations.db.

### Activity Menu 

- 0.Back to main menu: Returns user to main program menu.

- 1.Create new activity: Allows users to create a new activity by entering a name, description, price, and trip id. The new activity is then stored in vacations.db and can be edited or deleted with methods further down.

- 2.List activities: Retrieves information on all activities from vacations.db and displays it to the user.

- 3.Find activity by id: Requests user enter activity id, then returns activity details of the activity in vacations.db that matches activity id.

- 4.Find activity by name: Requests user enter activity name, the returns activity details of the activity in vacations.db that matched activity name.

- 5.Update an activity: Requests id of activity to be updated, then prompts user to type in changes they would like to make. All changes are reflected on vacation.db. To verify changes, run “List activities” immediately after.

- 6.Delete and activity: Requests activity id then removes activity with matching id from vacations.db. To verify changes, run “List activities” immediately after.

- 7.Filter activities by trip ID: Requests trip ID then returns any activities with matching trip ID.
---
# Files and Functions

## vacations.db
Acts as the database and stores two separate tables; trips and activities.


## itinerary.py
Contains the classes Trip and Activities, each with property setters to confirm data entries are of correct type and functions to be used later by helpers.py. 

### Trip Functions 
- create_table() and drop_table()
These functions are used by seed.py to start the program with a fresh data table called “trips,” consisting of only the example provided.

- save()
Takes in values provided and persists them to trips table on vacations.db. On its own it does nothing, but it will be called later by the create function.

- create()
Takes in its own class, a name, and a location then calls .save() to persist the values on the trips table vacations.db. Values are provided by create_trip() in helpers.py.

- update()
This function allows users to change the values of an already existing trip. New values are provided by update_activity() in helpers.py.

- delete()
Removes a trip of matching ID from vacations.db. ID is provided with delete_trip in helpers.py.

- instance_from_db()
Returns a trip instance and its attributes based on criteria provided by other functions.

- get_all()
Utilizes instance_from_db() to fetch and return all trip instances in the trip table on vacations.db.

- find_by_id()
Takes in an ID then utilizes instance_from_db() to return a trip instance with a matching ID. ID provided by find_trip_by_id () in helpers.py.

- find_by_name()
Takes in a name then utilizes instance_from_db() to return a trip instance with a matching name. Name provided by find_trip_by_name() in helpers.py.

### Activities Functions 
- NOTE: Most functions in Activities class serve the same purpose as they do in the Trip class, except they update the activities table in vacations.db instead of the trips table.

- filter_by_trip_id()
Takes in a trip_id and then utilizes instance_from_db() to return all activity instances in the activity table of vacations.db where the trip_id is a match. Trip_id provided by filter_activities_by_trip_id() in helpers.py.


## helpers.py
These functions allow the user to interact with the database with the help of functions imported from itinerary.py.

- exit_program()
Prints “Goodbye!” and ends the program.

- create_trip()
Requests user input for name and location then uses Trip.create() to persist new trip to trip table on vacations.db

- list_trips()
Calls Trip.get_all() to return all trip instances then prints them in the terminal.

- find_trip_by_name():
Requests user input trip name then calls Trip.find_by_name() to return and print trip of matching name. Prints an error if no trips match name provided.

- find_trip_by_id()
Requests user input trip ID then calls Trip.find_by_id() to return and print trip of matching ID. Prints an error if no trips match the ID provided.

- update_trip()
Requests the user provide ID of trip they would like to update. If the ID exists, requests additional input on what new trip attributes should be, then calls Trip.update() to set new values on the trip table in vacations.db. If the trip ID does not exist, it returns an error.

- delete_trip()
Requests the user provide ID of trip they would like to delete. If the ID exists, the trip instance with a matching ID is removed from the trips table on vacations.db. If the ID does not exist, it returns an error.

- create_activity()
Requests user input for name, description, price, day, and trip_id then uses Activity.create() to persist new activity to activity table on vacations.db.

- list_activities()
Calls Activity.get_all() to return all activity instances then prints them in the terminal.

- find_activity_by_name()
Requests user input activity name then calls Activity.find_by_activity_name() to return and print activity of matching name in the activity table of vacations.db. Returns an error if no activities match the name provided.

- find_activity_by_id()
Requests user input activity ID then calls Activity.find_activity_by_id() to return and print activity of matching ID in activity table of vacations.db. Returns an error if no activities match the ID provided.

- update_activity()
Requests user input activity ID of activity they would like to update then calls Activity.find_by_id to check the ID matches one in the activity table of vacations.db. If the activity ID does not exist, an error is returned. If the activity ID does exist, the user is prompted to enter new information for name, day, price, description, and trip_id which will be reflected on the activity table.

- delete_activity()
Requests user input activity ID of activity they would like to delete, then calls Activity.find_by_id to verify it’s existence on the activity table of vacations.db. If the activity ID does not exist, an error is returned. If the activity does exist, it is deleted from the trip table.

- filter_activities_by_trip_id()
Requests user input trip_id then utilizes Activity.filter_activities_by_trip_id() to return and print all activities with matching trip_id.

## cli.py
Imports functions from helper.py and organizes them in a way that matches what the user sees in their terminal.

## seed.py
Contains the create_table() and drop_table functions imported from itinerary.py, as well as an example trip and activity to populate the newly created tables in vacation.db. To seed the database, run “python lib/seed.py” in your terminal. You should see the message “Database seeded” if run successfully. 
