#!/usr/bin/env python
import argparse
import json


def generate_diff(file1, file2):
    result = ["{"]
    with open(file1) as f1:
        file1_data = json.load(f1)
    with open(file2) as f2:
        file2_data = json.load(f2)
    for key in sorted(file1_data):
        if key in file2_data:
            if file1_data[key] == file2_data[key]:
                result.append(f"\t{key}: {file1_data[key]}")
            else:
                result.append(f"\t- {key}: {file1_data[key]}")
                result.append(f"\t+ {key}: {file2_data[key]}")
        else:
            result.append(f"\t- {key}: {file1_data[key]}")
    for key in sorted(file2_data):
        if key not in file1_data:
            result.append(f"\t+ {key}: {file2_data[key]}")
    result.append("}")
    return "\n".join(result)


def main():
    parser = argparse.ArgumentParser(prog="gendiff",
                                     description="Compares two configuration "
                                                 "files and shows a "
                                                 "difference.")
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument('-f', '--format',
                        help='set format of output')
    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file))


if __name__ == '__main__':
    main()
