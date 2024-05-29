"""
This module has some classes related to users and authentication.

Author: Carlos Andrés Sierra <cavirguezs@udistrital.edu.co>
        Andrés Felipe Vanegas <afvanegasb@udistrital.edu.co>
        Last update: 29/05/2024
"""

import json


class User:
    """This is a data class to represents the User information."""

    def __init__(self, username: str, grants: dict):
        """
        This method initializes a new User instance. It takes two arguments: username and grants, which is a dictionary of user's permissions.
        """
        self.__username = username
        self.__grants = grants

    def get_username(self):
        """This method returns the username."""
        return self.__username

    def is_grant(self, grant: str):
        """This method checks if the user has a specific permission."""
        return self.__grants[grant]


class Authentication:
    """This class is used to validate users authentication."""

    def __init__(self, username: str, password: str):
        """
        Initializes an Authentication object with username, password, and grants.

        Args:
            username (str): The username of the user.
            password (str): The password of the user.
        """
        self.__username = username
        self.__password = password
        # Initialize the grants attribute to None
        self.__grants = None

    def authenticate(self) -> bool:
        """
        Validates user credentials.
        Returns:
            bool: True if authentication succeeds, False otherwise.
        """
        # Open the 'users.json' file for reading
        with open("workshop_pro/core_subsystem/users.json", "r", encoding="UTF-8") as file:
            # Load the user data from the JSON file
            users = json.load(file)
        for user in users:
            # Check if the username and password match the provided credentials
            if (
                user["username"] == self.__username
                and user["password"] == self.__password
            ):
                # If the credentials match, assign the user's permissions to the Authentication object
                self.__grants = user["grants"]
                # Return True to indicate successful authentication
                return True
        # If no matching user is found, return False
        return False

    def userdata(self) -> User:
        # Create and return a new User object with the current username and permissions
        return User(self.__username, self.__grants)

    def register(self, new_username: str, new_password: str) -> bool:
        """
        Registers new users.
        Args:
            new_username (str): The username of the new user.
            new_password (str): The password of the new user.

        Returns:
            bool: True if registration succeeds, False otherwise.
        """
        with open("workshop_pro/core_subsystem/users.json", "r", encoding="UTF-8") as file:
            users = json.load(file)
        for user in users:
            if user["username"] == new_username:
                return False  # Username already exists
        default_grants = {
            "add_vehicle": False,
            "remove_vehicle": False,
            "search_vehicle": True
        }

        new_user = {
            "username": new_username,
            "password": new_password,
            "grants": default_grants
        }
        users.append(new_user)
        with open("workshop_pro/core_subsystem/users.json", "w", encoding="UTF-8") as file:
            json.dump(users, file, ensure_ascii=False, indent=4)
        return True
