import os


def write_file(working_directory, file_path, content):
    try:
        working_directory_abs = os.path.abspath(working_directory)
        full_path = os.path.join(working_directory_abs, file_path)

        norm_full_path = os.path.normpath(full_path)
        is_common_path = os.path.commonpath([norm_full_path, working_directory_abs]) == working_directory_abs
        if not is_common_path:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        # nonexistent file is also False....
        # if not os.path.isfile(norm_full_path):
        # so different approach

        file_dir = os.path.dirname(norm_full_path)
        # full match -> not a file
        if os.path.commonpath([file_dir, norm_full_path]) == norm_full_path:
            return f'Error: Cannot write to "{file_path}" as it is a directory'

        if not os.path.exists(file_dir):
            os.makedirs(file_dir, exist_ok=True)
        
        with open(norm_full_path, 'w') as f:
            f.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    
    except Exception as e:
        return f'Error: {e} in write_file()'
