#!/usr/bin/env python3

#create dict for storing values
thisdict = {
  
}

#function to put key value pair in dict
def put_value(key, value):
  thisdict.update({key: value})
  print("ok")

#function to fetch value from dict
def fetch_value(key):
  print(thisdict[key])

#function to parse input to usable data
def parse_input(input):
  split = input.split(" ")
  return split
  
#evaluate the length of array and call appropriate function
def eval_array(arr):
  length = len(arr)
  if length == 3 and arr[0] == "put":
    put_value(arr[1], arr[2])
  elif length == 2 and arr[0] == "fetch":
    fetch_value(arr[1])
  else:
    print("Invalid input")

#prompt user
user_input = input("> ")

#until user enters "exit" continue to prompt
while user_input != "exit":
  eval_array(parse_input(user_input))
  user_input = input("> ")
  
print("Bye!")
