import os
import subprocess

def check_files_exist(files):
    return all(os.path.exists(file) for file in files)

def compile_files(sources, output):
    try:
        subprocess.run(["gcc", *sources, "-o", output], check=True)
        return True
    except subprocess.CalledProcessError:
        return False

def run_executable(executable):
    try:
        result = subprocess.run(["./" + executable], check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError:
        return None

# Test for Task 1
task1_files = ["greetings.h", "greetings.c", "main.c"]
if check_files_exist(task1_files):
    if compile_files(["greetings.c", "main.c"], "hello"):
        output = run_executable("hello")
        print("Task 1 Output:", output)
    else:
        print("Task 1 Compilation Failed")
else:
    print("Task 1 Files Missing")

# Test for Task 2
task2_files = ["math_operations.h", "math_operations.c", "print_operations.h", "print_operations.c", "main.c"]
if check_files_exist(task2_files):
    if compile_files(["math_operations.c", "print_operations.c", "main.c"], "math_printer"):
        output = run_executable("math_printer")
        print("Task 2 Output:", output)
    else:
        print("Task 2 Compilation Failed")
else:
    print("Task 2 Files Missing")

# Test for Task 3
task3_files = ["array_utils.h", "array_utils.c", "utils.h", "utils.c", "main.c"]
if check_files_exist(task3_files):
    if compile_files(["array_utils.c", "utils.c", "main.c"], "array_util_demo"):
        output = run_executable("array_util_demo")
        print("Task 3 Output:", output)
    else:
        print("Task 3 Compilation Failed")
else:
    print("Task 3 Files Missing")