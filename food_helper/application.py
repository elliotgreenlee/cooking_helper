"""
Elliot Greenlee

11/23/2018

application.py
"""

import argparse
import os
import pickle
import logging


class Application:
    def __init__(self):
        self.meals = {}
        self.ingredients = {}
        self.recipes = {}
        
    def run(self):
        # TODO: while loop while q or exit or something has not been typed in to start with
        return


def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument("init_type", help="'create' to create new or 'load' to load an existing helper")
    parser.add_argument("filepath", help="name of the file to retrieve or create. overwriting not allowed.")
    args = parser.parse_args()
    
    try:
        if args.init_type == 'create':
            if os.path.isfile(args.filepath):
                raise InputError(args, "a file with that name already exists at that location.")
            else:
                application = Application()
                
                application.run()

                pickle.dump(application, open(args.filepath, "wb"))
        elif args.init_type == 'load':
            if os.path.isfile(args.filepath):
                application = pickle.load(open(args.filepath, "rb"))
                
                application.run()

                pickle.dump(application, open(args.filepath, "wb"))
            else:
                raise InputError(args, "a file with that name does not exist at that location.")
        else:
            raise InputError(args, "init_type argument should be one of 'create' or 'load'.")
    except InputError as err:
        print(err.message)
        print("This occurred for input <{}>.".format(err.input_expression))
        
        
class InputError(Exception):
    """Exception raised for errors in the input.

    Attributes:
        input_expression -- input which created the error
        message -- explanation of the error
    """

    def __init__(self, input_expression, message):
        self.input_expression = input_expression
        self.message = message
    

if __name__ == "__main__":
    main()
