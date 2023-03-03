import argparse
from operations import addNumbers

def main(args):
    # Your code here
    sum = 0
    for n in args.numbers:
        sum = addNumbers(sum, n)
    print(sum)

if __name__ == "__main__":
    # Create the parser
    parser = argparse.ArgumentParser(description='Add an N number of float numbers')

    # Add arguments
    parser.add_argument('numbers', type=float, nargs='+', help='Numbers to add')
    
    # Parse arguments
    args = parser.parse_args()

    # Call the main function with the parsed arguments
    main(args)