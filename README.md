# New Relic Code Challenge

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

      
### Notes:   
I initially was going to create this program with JavaScript, but then realized after writing some initial pseudocode that I would be better off using a language that had built in methods for interacting with the command line, so I decided to use Python. This was a challenge to me since I was unfamilar with Python and had to do a crash course on it over the weekend. Being unfamiliar with the language presented some obstacles, as I was unfamiliar with all of the ins and outs of PEP 8 - and I got stuck for a bit figuring out which testing library to use. I looked into doctest, Pytest and unittest and in the end (after overcoming some import issues) I decided to use unittest.     
     
I realize that I could have written more tests, to get a better percentage of coverage, and also could have broken up the testing into several different classes, but for the scope of this project, and also put a cap to the time spent on this project I decided to stick with the one class and not get to carried away with testing for this challenge.


