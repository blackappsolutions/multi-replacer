#!/usr/bin/env python3

import os
import sys

mappingTable = {}


def do_replace(dirpath, file):
    # Read in the file
    with open(dirpath + "/" + file, 'r') as inputFile:
        filedata = inputFile.read()

    # Replace the target string
    for key in mappingTable:
        filedata = filedata.replace(key, mappingTable[key])

    # Write the file out again
    with open(dirpath + "/" + file, 'w') as outputFile:
        outputFile.write(filedata)


def main():
    if len(sys.argv) < 4:
        print(
            f"Usage: {sys.argv[0]} FILE_EXTENSION FOLDER MAPPING_FILE\n"
            f" E.g.: {sys.argv[0]} properties test test/mapping.txt"
        )
        exit(1)

    fileMask = sys.argv[1]
    folder = sys.argv[2]
    mappingFile = sys.argv[3]

    with open(mappingFile) as mappingTableFile:
        for line in mappingTableFile:
            if not line.startswith('#'):
                (key, val) = line.split()
                mappingTable[key] = val

    # print(mappingTable)

    for dirpath, dnames, fnames in os.walk(folder):
        for file in fnames:
            if file.endswith(fileMask):
                do_replace(dirpath, file)


if __name__ == "__main__":
    main()
