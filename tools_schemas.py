from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.run_python_file import run_python_file
from functions.write_file import write_file



get_files_info_schema = {
      'type': 'function',
      'function': {
        'name': 'get_files_info',
        'description': 'for each file get path, size, and wheter it\'s a dir',
        'parameters': {
          'type': 'object',
          'properties': {
            'directory': {
              'type': 'string',
              'description': 'Directory path to list files from, relative to the working directory (default is the working directory itself)',
            },
          },
          'required': ['directory'],
        },
      },
    }


get_file_content_schema = {
      'type': 'function',
      'function': {
        'name': 'get_file_content',
        'description': 'get file content, truncated for large files',
        'parameters': {
          'type': 'object',
          'properties': {
            'file_path': {
              'type': 'string',
              'description': 'File path to get content from, relative to the working directory (default is the working directory itself)',
            },
          },
          'required': ['file_path'],
        },
      },
    }


run_python_file_schema = {
      'type': 'function',
      'function': {
        'name': 'run_python_file',
        'description': 'run .py file with arguments (if any)',
        'parameters': {
          'type': 'object',
          'properties': {
            'file_path': {
              'type': 'string',
              'description': 'File path to .py file to run, relative to the working directory (default is the working directory itself)',
            },
            'args': {
              'type': 'list',
              'description': 'List of arguments for .py file (default is None)',
            },
          },
          'required': ['file_path'],
        },
      },
    }


write_file_schema = {
      'type': 'function',
      'function': {
        'name': 'write_file',
        'description': 'write provided content to the file, creates new file if it doesn\'t exist',
        'parameters': {
          'type': 'object',
          'properties': {
            'file_path': {
              'type': 'string',
              'description': 'File path to write content to, relative to the working directory (default is the working directory itself)',
            },
            'content': {
              'type': 'string',
              'description': 'Content which will be written into file',
            },
          },
          'required': ['file_path', 'content'],
        },
      },
    }


