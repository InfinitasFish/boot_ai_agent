import argparse


parser = argparse.ArgumentParser(description='dummy tester')
parser.add_argument('user_arg', type=str, help='User arg placeholder')

if __name__ == '__main__':
    args = parser.parse_args()
    print('Executing dummy file')
    if args:
        print(args.user_arg)

