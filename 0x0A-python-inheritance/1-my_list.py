#!/usr/bin/python3
"""class MyList that inherits from list
"""


class MyList(list):
    """ assume that all the elements of the list will be of type 
    """
    def print_sorted(self):
        """Prints the  list
        """
        new_list = self[:]
        new_list.sort()
        print("{}".format(new_list))
