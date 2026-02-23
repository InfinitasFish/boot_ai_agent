# course is using google.genai but I will crutch it up with ollama instead

import os
import argparse
import ollama

from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.run_python_file import run_python_file
from functions.write_file import write_file
from tools_schemas import get_files_info_schema, get_file_content_schema, run_python_file_schema, write_file_schema
from prompts import system_prompt, placeholder_prompt

MAX_AGENT_ITER = 20

parser = argparse.ArgumentParser(description='Chatbot')
parser.add_argument('user_prompt', type=str, help='User prompt')
parser.add_argument('--verbose', action='store_true', help='Enable verbose output')

tools_list = [get_files_info_schema, get_file_content_schema, run_python_file_schema, write_file_schema]


def call_function(function_call, verbose=False):
    function_name = function_call.function.name or ''
    function_args = function_call.function.arguments or ''
    if verbose:
        print(f"Calling function: {function_name}({function_args})")
    else:
        print(f" - Calling function: {function_name}")

    # could be get getattr() or globals(), but using simple mapping
    # https://stackoverflow.com/questions/22021037/convert-string-into-a-function-call#22021058
    function_map = {'get_files_info': get_files_info, 'get_file_content': get_file_content, 
        'run_python_file': run_python_file, 'write_file': write_file}

    if function_name not in function_map:
        msg_content = f"error: Unknown function: {function_name}\n"
        print(msg_content)
        message = {'role': 'tool', 'tool_name': function_name, 'content': msg_content}
        return message

    # override working_directory argument
    function_args = dict(function_args) if function_args else {}
    function_args['working_directory'] = './calculator'
    function_result = function_map[function_name](**function_args)

    function_args_str = ', '.join([f'{arg}={val}' for arg, val in function_args.items()])
    msg_content = f'result of calling {function_name}({function_args_str}) ->\n{function_result}\n'
    print(msg_content)
    # https://docs.ollama.com/capabilities/tool-calling#python
    message = {'role': 'tool', 'tool_name': function_name, 'content': msg_content}
    return message



def main():
    args = parser.parse_args()
    start_prompt = args.user_prompt if args.user_prompt else placeholder_prompt
    messages = [
        {'role': 'system', 'content': system_prompt}, 
        {'role': 'user', 'content': start_prompt}]
    
    # agent loop
    max_iter_exceed = False
    for i in range(MAX_AGENT_ITER):

        response = ollama.chat(
                        model='qwen3:4b',
                        messages=messages,
                        tools=tools_list,
                        options={'seed': 59, 'temperature': 0.3, 'think': True},
                    )
        resp_message = response['message']['content']

        if args.verbose:
            role = messages[-1]['role']
            prompt = messages[-1]['content']
            print(f"{role} last prompt: {prompt}\nPrompt total tokens: {response['prompt_eval_count']}\nResponse tokens: {response['eval_count']}\n")
        print(f"Response:\n{resp_message}\n")

        messages.append(response['message'])

        # checking for tool calls, if any -> call a appropriate function 
        if 'tool_calls' in response['message']:
            for call in response['message']['tool_calls']:
                call_result = call_function(call, verbose=args.verbose)
                messages.append(call_result)  
        # no function calls -> agent (probably) has done it's task
        else:
            break
        
        if i == (MAX_AGENT_ITER - 1):
            max_iter_exceed = True
    
    if max_iter_exceed:
        print(f'Possibly something went wrong, max iter of {MAX_AGENT_ITER} was exceeded before completing the task')
        exit(1)



if __name__ == "__main__":
    main()
