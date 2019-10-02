#!/usr/bin/python3

import sys
import difflib
import time
import json

try: 
    data_source = json.load(open("data.json", "r"))
except FileNotFoundError:
    print("Unrecognized file")

def get_input():
    while True:
        user_input = input("Enter a word: ")
        if (isinstance(user_input, str)) and (user_input != ""):
            print("Desired word: {}".format(user_input))
            break
        else:
            print("Unrecognized input")
            continue
    return user_input.strip()

def find_matches(input_str):
    matches = difflib.get_close_matches(input_str, data_source, n=4, cutoff=0.6)
    if matches:
        if (difflib.SequenceMatcher(None, input_str, matches[0]).ratio() != 1.0):
            print("Are you looking for word [{}]? ".format(matches[0]))
            return -1
        return matches
    else:
        print("No matches found")
        return -1

def print_definition(input_list):
    if (input_list != -1):
        print("Possible matches: ")
        for item in input_list:
            print("Word: {}, Definition: {}".format(item, data_source[item]))
    else:
        print("Try again")

print_definition(find_matches(get_input()))

