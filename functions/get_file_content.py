import os


READ_MAX_CHARS = 10000

def get_file_content(working_directory, file_path):
    try:
        working_directory_abs = os.path.abspath(working_directory)
        full_path = os.path.join(working_directory_abs, file_path)

        norm_full_path = os.path.normpath(full_path)
        is_common_path = os.path.commonpath([norm_full_path, working_directory_abs]) == working_directory_abs

        if not is_common_path:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        elif not os.path.isfile(norm_full_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        file_contents = ''
        with open(norm_full_path, 'r') as f:
            file_contents = f.read(READ_MAX_CHARS)
            # checking whether the file is larger than limit
            if f.read(1):
                file_contents += f'[...File "{file_path}" truncated at {READ_MAX_CHARS} characters]'
    
        return file_contents

    except Exception as e:
        return f'Error: {e} in get_file_content()'

