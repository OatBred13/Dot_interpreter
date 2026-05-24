# Dot Language Interpreter

Dot Language Interpreter is a simple interpreter for my programming language Dot, written in Python.

# Features
- Variables (creating new variables, deleting variables, getting the type of variables)
- Variable types (integer, float, string, bool)
- Basic math operations (addition, subtraction, multiplication, division)
- Terminal I/O (`terminal.write.(argument)`, `terminal.readline.(variable name|argument)`)
- Loops (`loop.(n)`)
- Error handling

# Console mode
<.>>> x = "Hello World!"

<.>>> terminal.write.(x)

Hello World!

# Executing scripts
<.>>> dot.(runfile)

Enter the file's path: scripts/

Enter the file's name: script.txt

# Error list
- Empty line error (only in console mode): *Dot.Syntax.Error: Cannot enter a blank line. Err_cd: 1*
- No proper argument given (for `terminal.write.(argument)`): *Dot.Value.Error: No proper argument given. Err_cd: 2*, Fix: Enter text with quotation marks or enter an existing variable name

- Non-existing command (both for console and execution mode): *Line (line number). Dot.Syntax.Error: (non_existing_command) command does not exist. Err_cd: 3*, Fix: Check if the command is written properly

- Cannot convert str to int (both for console and execution mode): *Dot.Convert.Error: Cannot convert string to an integer. Err_cd: 4*, Fix: Enter a number as a string

- A string saved into a variable **without** quotation marks (both for console and execution mode): *Dot.Type.Error: Wrong type assigned. Please ensure that the text value is in quotation marks. Err_cd: 5*, Fix: Enter the text in quotation marks

- Cannot save variable as a float (both in console and execution mode): *Dot.Type.Error: Cannot store the variable as float. Err_cd: 6*, Fix: Add int.(n), bool.(True/False) before the value or use the same fix as to Err_cd: 5

- Argument in `terminal.readline.(variable_name|argument)` not being in quotation marks (both in console and execution mode): *Dot.Syntax.Error: Cannot execute terminal.readline.() using the given argument. Please ensure that the argument is in quotation marks. Err_cd: 7*, Fix: Make sure the argument is in quotation marks

- Variable does not exist (both in console and execution mode): *Dot.Syntax.Error: Given variable does not exist. Please ensure that the variable exist. Err_cd: 8*, Fix: make sure the variable exist

# Installation of the interpreter
In the terminal, enter this command:

`git clone https://github.com/OatBred13/Dot_interpreter.git`

Or download through the web version of GitHub

# Running the interpreter

You can open the interpreter in two ways. One is through any code editor, and the second one is through the Windows Terminal. To open it using the Windows Terminal, the folder in which the Dot interpreter is located must be found. Then these commands are entered into the terminal:

`cd path of the folder with the Dot interpreter`

`python Dot.py` or `py Dot.py`

For both methods **a working Python interpreter is required**

# Example code and its execution

## C:\users\user_name\documents\scripts\script.txt

`counter = int.(0)`



`loop.(10000)`

`counter = counter + 1`

`loop.end`



`terminal.write.(counter)`

## Console
<.>>> dot.(runfile)

Enter the file's path: C:\users\user_name\documents\scripts

Enter the file's name: script.txt

## Output
10000.0

Executed in 0.019416 seconds.


## Future goals

- Add if and else statements
- Add lists and dictionaries
- Add functions

## Contributing

Pull requests or modifications to the Dot interpreter is welcome! For major changed though, please open an issue first.

## License

This project is licensed under the MIT license
