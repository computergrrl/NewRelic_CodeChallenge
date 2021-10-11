#!/usr/bin/env python3

stored_values = {
}

def put_value(key, value):
    """function to put value in stored_values dict"""
    stored_values.update({key: value})
    return "ok"
  
def fetch_value(key):
    """function to fetch value from stored_values dict"""
    if key in stored_values:
      return stored_values[key] 
    else:
      return "Value not found"

def parse_input(input):
    """parse the input from user prompt and return array of strings"""
    split = input.split()
    return split

def eval_array(arr):
    """evaluate the array and call appropriate function"""
    length = len(arr)
    valid_options = ["put", "fetch", "exit"]
    message = ""
    if length > 0 and arr[0] not in valid_options:
      message = "Unknown command. Known commands are: put, fetch, exit"
    elif length == 3 and arr[0] == "put":
      message = put_value(arr[1], arr[2])
    elif length == 2 and arr[0] == "fetch":
      message = fetch_value(arr[1])
    else:
      message = "Invalid syntax"
    return message

if __name__ == '__main__':
    user_input = input("> ")

    """until user types in "exit" continue 
    to prompt and call eval_array"""
    while user_input != "exit":
      print(eval_array(parse_input(user_input)))
      user_input = input("> ")

    print("Bye!")
