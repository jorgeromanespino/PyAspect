#
import argparse

#
def execute_module():
    # argparse config
    parser = argparse.ArgumentParser(description='Aspect command line interface')
    parser.add_argument('--helloworld', help='Just printing hello world', action="store_true")

    # Parse args
    args = parser.parse_args()

    # Command pattern
    if (args.helloworld):
        # python atadbcli.py --deletetables
        print('Just printing hello world!...')

#
if __name__ == "__main__":
    execute_module()
