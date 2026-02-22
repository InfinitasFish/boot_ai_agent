from functions.get_file_content import get_file_content


if __name__ == '__main__':
    big_file_case = get_file_content('calculator', 'lorem.txt')
    print(len(big_file_case), big_file_case[-128:], sep='\n')

    real_file_case = get_file_content('calculator', 'main.py')
    print(real_file_case)

    real_file_case_2 = get_file_content('calculator', 'pkg/calculator.py')
    print(real_file_case_2)

    not_file_case = get_file_content('calculator', '/bin/cat')
    print(not_file_case)

    unexisting_file_case = get_file_content('calculator', 'pkg/does_not_exist.py')
    print(unexisting_file_case)
