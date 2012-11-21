import argparse

def parse_args():
    desc='N-body utilities.'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('-i', '--input', type=str, help='Input file')
    args = parser.parse_args()
    if args.input == None:
        parser.print_help()
        sys.exit(0)

    input_file = args.input
    options = dict()
    options['input_file'] = input_file
    return options
