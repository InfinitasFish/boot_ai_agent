import os
import subprocess


def run_python_file(working_directory, file_path, args=None):

    try:
        working_directory_abs = os.path.abspath(working_directory)
        full_path = os.path.join(working_directory_abs, file_path)
        norm_full_path = os.path.normpath(full_path)

        is_common_path = os.path.commonpath([norm_full_path, working_directory_abs]) == working_directory_abs
        if not is_common_path:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(norm_full_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        # kinda hardcoded check for .py
        if not os.path.basename(file_path)[-3:] == '.py':
            return f'Error: "{file_path}" is not a Python file'
        
        # running .py file with args
        command = ['python3', norm_full_path]
        if args:
            command.extend(args)
        # https://docs.python.org/3/library/subprocess.html#subprocess.CompletedProcess
        completed_command = subprocess.run(command, capture_output=True, text=True, timeout=30)

        result_string = ''
        if completed_command.returncode != 0:
            result_string += f"Process exited with code {completed_command.returncode}\n"
        if not (completed_command.stdout or completed_command.stderr):
            result_string += 'No output produced'
        else: 
            result_string += f'STDOUT:\n{completed_command.stdout}\nSTDERR:\n{completed_command.stderr}'

        return result_string

    except Exception as e:
        return f"Error: executing Python file: {e}"


# p = '/home/infik/ai_agent/functions/dummy.py'
# print(run_python_file(os.path.dirname(p), os.path.basename(p), args=['how are you brother']))

