from pathlib import *
import time

variables = {}
empty_lines = []
index = 0

def create_var(name, value):
    math_operation = False
    
    if value == "null":
        value = 0
        variables[name] = value

    elif value.startswith("int."):
        math_operation = True
        start_ixd = value.find("(") + 1
        end_ixd = value.find(")")
        value_convert = value[start_ixd:end_ixd]
        if value_convert in variables:
            value_convert = variables[value_convert]
            
        try:
            value_convert = int(value_convert)
            variables[name] = value_convert
        except:
            terminal_write("Dot.Convert.Error: Cannot convert string to an integer. Err_cd: 4")
            
    elif value.startswith('"') and value.endswith('"'):
        math_operation = True
        value = value[1:-1]
        value = str(value)
        variables[name] = value
        
    elif value.startswith("bool."):
        math_operation = True
        start_ixd = value.find("(") + 1
        end_ixd = value.find(")")
        value = value[start_ixd:end_ixd]
        if value == "True":
            variables[name] = True
        elif value == "False":
            variables[name] = False
    
    elif "+" in value or "-" in value or "*" in value or "/" in value:
        math_operation = True
        if "+" in value:
            op = "+"
        elif "-" in value:
            op = "-"
        elif "*" in value:
            op = "*"
        elif "/" in value:
            op = "/"

        argument_one, argument_two = value.split(op)
        argument_one = argument_one.strip()
        argument_two = argument_two.strip()

        if argument_one in variables:
            argument_one = variables.get(argument_one)
        else:
            try:
                argument_one = float(argument_one)
            except:
                if argument_one.startswith('"') and argument_one.endswith('"'):
                    argument_one = argument_one[1:-1]
                else:
                    terminal_write("Dot.Type.Error: Wrong type assigned. Please ensure that the text value is in quotation marks. Err_cd: 5")

        if argument_two in variables:
            argument_two = variables.get(argument_two)
        else:
            try:
                argument_two = float(argument_two)
            except:
                if argument_two.startswith('"') and argument_two.endswith('"'):
                    argument_two = argument_two[1:-1]
                else:
                    terminal_write("Dot.Type.Error: Wrong type assigned. Please ensure that the text value is in quotation marks. Err_cd: 5")

        if op == "+":
            result = argument_one + argument_two
        elif op == "-":
            result = argument_one - argument_two
        elif op == "*":
            result = argument_one * argument_two
        elif op == "/":
            result = argument_one / argument_two

        try:
            variables[name] = float(result)
        except:
            variables[name] = result
    
    else:
        try:
            value = float(value)
            variables[name] = value
        except:
            terminal_write("Dot.Type.Error: Cannot store the variable as float. Err_cd: 6")

    if type(value) == str and value.startswith('"') == False and value.endswith('"') == False and math_operation == False:
        terminal_write("Dot.Type.Error: Wrong type assigned. Please ensure that the text value is in quotation marks. Err_cd: 5")
            
def string_var_operations(name, name2):
    variable_1 = str(variables[name])
    variable_2 = str(variables[name2])
    value = variable_1 + variable_2
    print(value)
    create_var(name, value)
                

def var_type_get(name):
    try:
        value = variables[name]
        value = type(value)
        terminal_write(value)
    except:
        terminal_write("Dot.Syntax.Error: Given variable does not exist. Please ensure that the variable exist. Err_cd: 8")

def console_read_line(text, name):
    input_var = input(text)
    name = name
    value = input_var
    try:
        value = float(value)
        create_var(name, value)
    except:
        value = f'"{value}"'
        create_var(name, value)

def terminal_write(argument):
    print(argument)
    
def loop_start(repetitions, start_index):
    i = start_index + 1
    loop_block = []

    while lines[i] != "loop.end":
        loop_block.append(lines[i])
        i += 1

    for _ in range(repetitions):
        for i in loop_block:
            parse_and_execute(i)

def else_start(start_index_else):
    index = 0
    i = start_index_else + 1
    commands_if_false = []
    try:
        while lines[i] != "condition.end":
            commands_if_false.append(lines[i])
            i += 1

        for _ in range(len(commands_if_false)):
            parse_and_execute(commands_if_false[index])
            index += 1
    
    except:
        terminal_write("Dot.Syntax.Error: No proper condition given, no else statement present or no condition.end statement present. Please ensure the correctness of the given code. Err_cd: 10")

def if_start(condition, start_index):
    index = 0
    i = start_index + 1
    commands_if_true = []
    try:
        while lines[i] != "else:":
            commands_if_true.append(lines[i])
            i += 1

        start_index_else = i

        if "==" in condition:
            value1, value2 = condition.split("==")
            if value1 in variables:
                value1 = variables[value1]
            elif value2 in variables:
                value2 = variables[value2]
    
            if value1 == value2:
                for i in range(len(commands_if_true) - 1):
                    parse_and_execute(commands_if_true[index])
                    index += 1

            else:
                else_start(start_index_else)

        elif "!=" in condition:
            value1, value2 = condition.split("!=")
            if value1 in variables:
                value1 = variables[value1]
            elif value2 in variables:
                value2 = variables[value2]
                
            if value1 != value2:
                for i in range(len(commands_if_true) - 1):
                    parse_and_execute(commands_if_true[index])
                    index += 1
            
            else:
                else_start(start_index_else)

        elif ">" in condition:
            value1, value2 = condition.split(">")
            if value1 in variables:
                value1 = variables[value1]
            elif value2 in variables:
                value2 = variables[value2]

            if value1 > value2:
                for i in range(len(commands_if_true) - 1):
                    parse_and_execute(commands_if_true[index])
                    index += 1
            
            else:
                else_start(start_index_else)

        elif "<" in condition:
            value1, value2 = condition.split("<")
            if value1 in variables:
                value1 = variables[value1]
            elif value2 in variables:
                value2 = variables[value2]
                
            if value1 < value2:
                for i in range(len(commands_if_true) - 1):
                    parse_and_execute(commands_if_true[index])
                    index += 1
            
            else:
                else_start(start_index_else)

        elif ">=" in condition:
            value1, value2 = condition.split(">=")
            if value1 in variables:
                value1 = variables[value1]
            elif value2 in variables:
                value2 = variables[value2]

            if value1 >= value2:
                for i in range(len(commands_if_true) - 1):
                    parse_and_execute(commands_if_true[index])
                    index += 1
            else:
                else_start(start_index_else)

        elif "<=" in condition:
            value1, value2 = condition.split("<=")
            if value1 in variables:
                value1 = variables[value1]
            elif value2 in variables:
                value2 = variables[value2]

            if value1 <= value2:
                for i in range(len(commands_if_true) - 1):
                    parse_and_execute(commands_if_true[index])
                    index += 1
            else:
                else_start(start_index_else)
    
    except:
        terminal_write("Dot.Syntax.Error: No proper condition given, no else statement present or no condition.end statement present. Please ensure the correctness of the given code. Err_cd: 10")

def parse_and_execute(command):
    
    if command == "loop.end":
        return
    
    elif command.startswith("terminal.write."):
        start_ixd = command.find("(") + 1
        end_ixd = command.find(")")
        argument = command[start_ixd:end_ixd]
        
        if argument.startswith(('"')) and argument.endswith(('"')):
            argument = argument[1:-1]
            terminal_write(argument)
            
        elif argument in variables:
            argument_var = variables.get(argument)
            terminal_write(argument_var)

        else:
            terminal_write("Dot.Value.Error: No proper argument given. Err_cd: 2")
    
    elif "=" in command:
        name, value = command.split(" = ", 1)
        name = name.strip()
        create_var(name, value)
        
    elif command.startswith("type."):
        start_ixd = command.find("(") + 1
        end_ixd = command.find(")")
        name = command[start_ixd:end_ixd]
        var_type_get(name)
    
    elif command.startswith("terminal.readline."):
        start_ixd = command.find("(") + 1
        end_ixd = command.find(")")
        text_raw = command[start_ixd:end_ixd]
        name, text = text_raw.split("|")
        
        if text.startswith('"') and text.endswith('"'):
            text = text[1:-1]
            console_read_line(text, name)
        
        else:
            terminal_write("Dot.Syntax.Error: Cannot execute terminal.readline.() using the given argument. Please ensure that the argument is in quotation marks. Err_cd: 7")
    
    elif command == "dot.(help)":
        terminal_write("dot.(exit) - terminates Dot")
        terminal_write("terminal.write.(argument) - writes the given argument in the terminal.")
        terminal_write("terminal.readline.(name|question) - aks the user for a value")
        terminal_write("name = value - creates a variable with the given name and value (with either float or string data type)")
        terminal_write("name = int.(value) - creates a variable with a given name and value in the integer data type")
        terminal_write("type.(name) - displays the type of a given variable")
        terminal_write("program.sleep.(argument) - stops the program for a given amount of time.")
        
    elif command.startswith("loop."):
        start_ixd = command.find("(") + 1
        end_ixd = command.find(")")
        repetitions = int(command[start_ixd:end_ixd]) - 1

        loop_start(repetitions, index)
        
        
    elif command == "":
        empty_lines.append("_")

    elif command.startswith("program.sleep."):
        start_ixd = command.find("(") + 1
        end_ixd = command.find(")")
        try:
            sleep_time = float(command[start_ixd:end_ixd])
            time.sleep(sleep_time)
        except:
            terminal_write(f"{sleep_time} is not an integer or float. Cannot execute the program.sleep.(argument) command.")

    elif command.startswith("if."):
        start_ixd = command.find("(") + 1
        end_ixd = command.find("):")
        condition = command[start_ixd:end_ixd]
        if_start(condition, index)

    elif command == "dot.(runfile)":
        pass

    elif command == "pass":
        pass

    elif command == "condition.end":
        pass
    
    else:
        terminal_write(f"Line {index + len(empty_lines)}. Dot.Syntax.Error: {command} command does not exist. Err_cd: 3")
        
terminal_write("Dot v. 1.0")
terminal_write("Enter dot.(help) for help.")

while True:

    command = input("<.>>> ")
    
    if command == ("dot.(runfile)"):
        index = 0
        lines = []
        file_path = input("Enter the file's path: ")
        file_name = input("Enter the file's name: ")
        if file_path == "cancel" or file_name == "cancel":
            continue
        
        file_final = Path(file_path) / file_name
        with open(file_final, "r") as f:
            lines = [line.strip() for line in f]

        start_time = time.perf_counter()
        for index, i in enumerate(lines):
            parse_and_execute(i)
        end_time = time.perf_counter()
        print(f"Executed in {end_time - start_time:.6f} seconds.")
        
    if command == "dot.(exit)":
        quit()
    
    if not command:
        argument = "Dot.Syntax.Error: Cannot enter a blank line. Err_cd: 1"
        terminal_write(argument)
        
    parse_and_execute(command)
