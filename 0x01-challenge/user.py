#!/usr/bin/python3
"""
User class
"""

if __name__ == "__main__":

    class User():
        """ Documentation """

    def __init__(self):
        """ Documentation """
        self.__email = None

    def email(self, value):
        """ Documentation """
        if type(value) is not str:
            raise TypeError("email must be a string")
        self.__email = value

    @property
    def email(self):
        """ Documentation """
        return self.__email

    u = User()
    u.email = "john@snow.com"
    print(u.email)
