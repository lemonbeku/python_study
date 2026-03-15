# Elements of the Python Language
## Interactive Python
Python can run interactively through the terminal or command line.
Platforms:
- Windows with Powershell
- macOs with Terminal
- Linux
When Python starts, you see the chevron prompt:
```python
>>>
```
This prompt means:
- Python is ready to accept commands
You can think of this as talking directly to Python. Python waits for instructions and executes whatever statements you enter

## Assignment Statements
Example:
```python
x = 1
```
Meaning:
- Python creates a memory location 
- Names it `x`
- Stores the value `1`
The equals sign (`=`) in programming means assignment, not mathematical equality -> Take the value on the right, store it in the variable on the left

## Printing Values
Example:
```python
print(x)
```
Meaning: 
- Retrieve the value stored in `x`
- Display it on the screen

## Updating Variables
Example:
```python
x = x + 1
```
Steps:
1. Retrieve the value in `x`
2. Add 1
3. Store the result back in x
```python
x = 1
x = x + 1
print(x)
```
Output: 
```python
2
```

## Syntax Errors
If Python code is written incorrectly, Python produces a syntax error. 
Example causes:
- Misspelled keywords
- Missing parentheses
- Incorrect structure
Python will display an error message such as:
```python
SyntaxError
```

## Programming Like Writing
Programming can be compared to writing a story
- Alphabet is like Characters, Words like Vocabulary, Sentences like Lines of Code, Paragraphs like Code Blocks, Story like Program
- Programs are built step-by-step just like written text

## Reserved Words
Reserved words are words that Python already uses for specific purposes.
Examples:
```python
if
for
while
import
pass
assert
global
from
```
Rules:
- These words cannot be used as variable names
- They must be used according to Python's rules
Example:
```python
import = 5
```
This will cause an error because `import` is reserved

Analogy
Imagine Python is like a dog listening to conversation
Most words are ignored:
- You said "Which president should I choose Spot? This one or that one ", the dog wont listen at all. 
Certain words trigger a reaction.
For dogs
- walk
- food
- treat
These are like reserved words
For Python:
- for
- while
- import
When Python sees these words, they must be used correctly

## Lines of Code
Each line in Python is an instruction
Example:
```python
x = 2
x = x + 2
print(x)
```
Execution steps:
1. Store 2 in x
2. Add 2
3. Print the result
Output:
```python 
4
```

## Programming Components
### Operators
Symbols used to perform operations
Examples:
```python
+ addition
= assignment
```
Examples:
```python
x = x + 1
```
### Functions 
Functions perform actions
Example:
```python
print()
```
### Parameters
Value passed into functions
Example:
```python
print(x)
```
x is the parameter

## Interactive Mode vs Scripts
### Interactive Mode
Commands are typed directly into Python
```python
>>> x = 1
>>> print(x)
```
Used for experimenting and for testing code in Console

### Scripts
For larger programs, code is written in files.
Python files use the extension `.py`
Example:
```
program.py
```
Script Example
```python
x = 1
x = x + 1
print(x)
```
Python runs the file from top to bottom

A script is A stored set of python instructions written in a text file
How to Execute
1. Write code in a `.py` file
2. save the file
3. Run it with Python
```python
python program.py
```
Python will read the instructions and execute them sequential.

# References
[[Python Michigan]]
