# Python Put/Fetch CLI Tool

## Objective: To build a command line tool for storing and fetching values. The tool must open an interactive session that accepts _put_, _fetch_, and _exit_ commands.    

### Requirements: 
- [x] When ready to accept a command, it must output the string "> " as a command prompt.
- [x] The _put_ command: 
  - [x] Should accept a key and a value
  - [x] Value should be stored with key
  - [x] If the key already exists in the system, the old value should be discarded
  - [x] If successful, the command should output the string "ok".
- [x] The _fetch_ command:
  - [x] Should accept a key and then output the value associated with the key
  - [x] If the key does not exist it should output "Value not found"
- [x] The _exit_ command:
  - [x] Should output the string "Bye!" and then exit the program
- [x] If any other command is entered, it should output the string "Unknown command. Known
commands are: put, fetch, exit".
- [x] If a command has the wrong number of arguments or is otherwise malformed, it should output
the string "Invalid syntax."   


### Running the program 
To run the program, simply type `./key-value.py` from the terminal

### Running the tests
I used Python's built in unit test framework "unittest" to create the tests, and I also used the coverage tool to test the code coverage. 
 - To run the tests, type `./tests.py`
 - To install coverage tool type `pip install -r requirements.txt`
 - To run coverage tool type `coverage run tests.py`
 - Then to generate a coverage report type `coverage report`
