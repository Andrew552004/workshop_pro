"""
This is the main file of the project. It is the entry point of the application.

Author: Carlos Andrés Sierra <cavirguezs@udistrital.edu.co>
        Andrés Felipe Vanegas <afvanegasb@udistrital.edu.co>
        Last update: 29/05/2024
"""

from .core_subsystem import FinalCatalog, Authentication

CATALOG = FinalCatalog()
MENU_OPTIONS = """
0. Log in the system
1. Register in the system
2. Add a new vehicle
3. Remove a vehicle
4. Search all vehicles
5. Search vehicles by speed
6. Search vehicles by price
7. Restore vehicle
8. Exit
"""


def login():
    """
    Allows the user to log in the system.

    Returns:
        Authentication: The authentication object if login successful, otherwise None.
    """
    username = input("Username: ")
    password = input("Password: ")
    auth = Authentication(username, password)
    if auth.authenticate():
        return auth
    return None


def register():
    """
    Permits a new user to register in the system.

    Returns:
        Authentication: The authentication object if registration is successful, otherwise None.
    """
    username = input("New Username: ")
    password = input("New Password: ")
    manager = Authentication(username, password)
    if manager.register(username, password):
        print("User registered successfully!")
        return manager
    print("Username already exists or an error occurred.")
    return None


def main():
    """The main function of the project."""
    user = None

    print("Welcome to the Vehicle Catalog System")
    print(MENU_OPTIONS)

    while True:
        option = input("Please select an option: ")

        if option == "0":
            print("====== Logging in the system ======")
            user = login()
        elif option == "1":
            print("====== Register in the system ======")
            user = register()
        elif option == "2":
            print("====== Adding a new vehicle ======")
            if user and user.is_grant("add_vehicle"):
                CATALOG.add_vehicle(user.get_username())
            else:
                print("====== Need to be logged in first ======")
        elif option == "3":
            print("====== Removing a vehicle ======")
            if user and user.is_grant("remove_vehicle"):
                CATALOG.remove_vehicle()
            else:
                print("====== Need to be logged in first ======")
        elif option == "4":
            print("====== Searching all vehicles ======")
            if user and user.is_grant("search_vehicle"):
                CATALOG.get_all_vehicles()
            else:
                print("====== Need to be logged in first ======")
        elif option == "5":
            print("====== Searching vehicles by speed ======")
            if user and user.is_grant("search_vehicle"):
                CATALOG.get_vehicles_by_speed()
            else:
                print("====== Need to be logged in first ======")
        elif option == "6":
            print("====== Searching vehicles by price ======")
            if user and user.is_grant("search_vehicle"):
                CATALOG.get_vehicles_by_price()
            else:
                print("====== Need to be logged in first ======")
        elif option == "7":
            print("====== Exiting the system ======")
            break
        else:
            print("Invalid option. Please select a valid option.")

        print("\n" + MENU_OPTIONS + "\n\n")

    print("Thank you for using the Vehicle Catalog System.")


if __name__ == "__main__":
    main()
    