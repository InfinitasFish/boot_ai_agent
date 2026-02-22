from functions.write_file import write_file


if __name__ == '__main__':
    correct_file_case = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print(correct_file_case)

    antoher_correct_file_case =  write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print(antoher_correct_file_case)

    outside_dir_case = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print(outside_dir_case)
