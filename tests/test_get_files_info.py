from functions.get_files_info import get_files_info


if __name__ == '__main__':
    test_case_1 = {'working_dir': 'calculator', 'dir': '.', 'exp': 
    '- main.py: file_size=719 bytes, is_dir=False\n- tests.py: file_size=1331 bytes, is_dir=False\n- pkg: file_size=44 bytes, is_dir=True'}
    result_1 = get_files_info(test_case_1['working_dir'], test_case_1['dir'])
    print(result_1)

    test_case_2 = {'working_dir': 'calculator', 'dir': 'pkg', 'exp': 
    '- calculator.py: file_size=1721 bytes, is_dir=False\n- render.py: file_size=376 bytes, is_dir=False'}
    result_2 = get_files_info(test_case_2['working_dir'], test_case_2['dir'])
    print(result_2)

    test_case_3 = {'working_dir': 'calculator', 'dir': '/bin', 'exp':
    'Error: Cannot list "/bin" as it is outside the permitted working directory'}
    result_3 = get_files_info(test_case_3['working_dir'], test_case_3['dir'])
    print(result_3)

    test_case_4 = {'working_dir': 'calculator', 'dir': '../', 'exp':
    'Error: Cannot list "../" as it is outside the permitted working directory'}
    result_4 = get_files_info(test_case_4['working_dir'], test_case_4['dir'])
    print(result_4)
