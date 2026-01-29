# A1-COMP4190

## How to run the program

### Two different ways

#### The normal way

- Each programming question has its own file
- Since there are 4 different programming questions, the files are:
  - Q1.py
  - Q2.py
  - Q3.py
  - Q4.py
- Each of these file has a function called main().
- And inside main(), there are named variables that will be used as an input to the function.
- You can change those named variables to your desired input.
- To run the program, you can write `python {file_name}` in the terminal

#### Quicker way, with pytest

- You need to have pytest in your system, in order to run the unit tests
- There's a file called test_cases.json, this consist of all test cases for all Q1-Q4.py
  - Q1 key is called problem_one_cases
  - Q2 key is called problem_two_cases
  - Q3 key is called problem_three_cases
  - Q4 key is called problem_four_cases
- To run your own test cases, you can easily change the values in the test_cases.json and type `pytest` in the terminal
- You can see all the passed test cases in the terminal
