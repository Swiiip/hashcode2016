import argparse


def parse(file):
    """Parse the input file"""
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Parse a file')
    parser.add_argument('file', type=str, help="File to be parsed")
    args = parser.parse_args()
    print(args)
    parse(args.file)
