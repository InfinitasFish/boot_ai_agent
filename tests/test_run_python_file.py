from functions.run_python_file import run_python_file



if __name__ == '__main__':
    calc_main_case = run_python_file("calculator", "main.py")
    print(calc_main_case)

    calc_exp_main_case = run_python_file("calculator", "main.py", ["3 + 5"])
    print(calc_exp_main_case)

    calc_tests_case = run_python_file('calculator', 'tests.py')
    print(calc_tests_case)

    outside_file_case = run_python_file('calculator', '../main.py')
    print(outside_file_case)

    nonexistent_file_case = run_python_file("calculator", "nonexistent.py")
    print(nonexistent_file_case)

    not_py_file_case = run_python_file('calculator', 'lorem.txt')
    print(not_py_file_case)

