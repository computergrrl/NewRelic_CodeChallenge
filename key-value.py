#!/usr/bin/env python3

#create dict for storing values
stored_values = {
}

#function to put key value pair in dict
def put_value(key, value):
  stored_values.update({key: value})
  print("ok")

#function to fetch value from dict
def fetch_value(key):
  print(stored_values[key]) if key in stored_values else print("Value Not Found")

#function to parse input to usable data
def parse_input(input):
  split = input.split()
  return split
  
#evaluate the array and call appropriate function
def eval_array(arr):
  length = len(arr)
  valid_options = ["put", "fetch", "exit"]
  if length > 0 and arr[0] not in valid_options:
    print("Unknown command. Known commands are: put, fetch, exit")
  elif length == 3 and arr[0] == "put":
    put_value(arr[1], arr[2])
  elif length == 2 and arr[0] == "fetch":
    fetch_value(arr[1])
  else:
    print("Invalid syntax")

#prompt user
user_input = input("> ")

#until user enters "exit" continue to prompt
while user_input != "exit":
  eval_array(parse_input(user_input))
  user_input = input("> ")
  
print("Bye!")
