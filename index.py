#!/usr/bin/env python 

#create dict for storing values
thisdict = {
  
}

#function will split input into separate words and then add the last 2 words as key-value pair to the dict
def put_value(input):
  split = input.split(" ", 2)
  thisdict.update({split[1]: split[2]})

#function will fetch and print out the value of the key
def fetch_value(input):
  print(thisdict[input])

#function takes first word of input and calls appropriate put or fetch function 
def put_or_fetch(value):
    
    if value.startswith("put"):
      put_value(value)
    elif value.startswith("fetch"):
      fetch_value(value)
    

user_input = input("> ")

while user_input != "exit":
  put_or_fetch(user_input)
  user_input = input("> ")
  
print("Bye!")

  
      
put_or_fetch(user_input)  

