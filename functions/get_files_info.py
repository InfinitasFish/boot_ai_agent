import os


def get_files_info(working_directory, directory):
    # dont like it but here we are
    try:

        # quite interesting, that os.path.abspath is smart enough to return valid abspath
        # I guess it's based on the filepath, from which python is running, e.g.
        # cd ~/ai_agent | python3 functions/get_files_info.py 
        # will return /home/infik/ai_agent/working_directory , which is valid
        
        working_directory_path = os.path.abspath(working_directory)
        full_path = os.path.join(working_directory_path, directory)
        # fixes ../ and others, normalizes path
        norm_full_path = os.path.normpath(full_path)
        is_common_path = os.path.commonpath([norm_full_path, working_directory_path]) == working_directory_path
        if not is_common_path:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        elif not os.path.isdir(norm_full_path):
            return f'Error: "{directory}" is not a directory'

        info_result = ''
        for fpath in os.listdir(norm_full_path):
            full_fpath = os.path.join(norm_full_path, fpath)
            is_dir = os.path.isdir(full_fpath)
            fpath_size = os.path.getsize(full_fpath)
            info_result += f'- {fpath}: file_size={fpath_size} bytes, is_dir={is_dir}\n'

        return info_result

    except Exception as e:
        return f'Error: {e} in get_files_info()'



#get_files_info('calculator', '../')
# print(get_files_info('calculator', '../'))
# print(get_files_info('calculator', 'pkg'))
