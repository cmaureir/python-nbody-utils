#!/usr/bin/env python
from src.parser import parse_args
from src.nbody  import nbody
from src.reader import read_file

def main():
    # Options parser
    options = parse_args()
    # Reading input file
    data, n = read_file(options['input_file'])
    # N-body object
    nb = nbody(data, n)

    print(nb.get_core_radius(nb.get_density_centre()))

if __name__ == "__main__":
    main()
