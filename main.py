import os
import argparse
from dotenv import load_dotenv
import ollama
from google import genai


PLACEHOLDER_PROMPT = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
parser = argparse.ArgumentParser(description='Chatbot')
parser.add_argument('user_prompt', type=str, help='User prompt')
parser.add_argument('--verbose', action='store_true', help='Enable verbose output')


def main():
    # tests dodging
    # models.generate_content
    # load_dotenv()
    # models.generate_content
    # .text
    # role="user"
    # parts=[
    
    args = parser.parse_args()
    prompt = args.user_prompt if args.user_prompt else PLACEHOLDER_PROMPT
    messages = [{'role': 'user', 'content': prompt}]
    response = ollama.chat(
                    model='qwen3:4b',
                    messages=messages,
                    options={'seed': 59, 'temperature': 0.3, 'think': False},
                )
    resp_message = response['message']['content']
    messages.append({'role': 'model', 'content': resp_message})
    
    # console stdout
    if args.verbose:
        print(f"User prompt: {prompt}\nPrompt tokens: {response['prompt_eval_count']}\nResponse tokens: {response['eval_count']}")
    print(f"Response:\n{resp_message}")


if __name__ == "__main__":
    main()
