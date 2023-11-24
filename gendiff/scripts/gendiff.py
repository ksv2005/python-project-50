#!/usr/bin/env python
import argparse
from json import load
from yaml import safe_load


def generate_diff(file1_data, file2_data):
    result = ["{"]
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


# generates plain difference between two json files
def generate_json_diff(file1, file2):
    with open(file1) as f1:
        file1_data = load(f1)
    with open(file2) as f2:
        file2_data = load(f2)
    return generate_diff(file1_data, file2_data)


# generates plain difference between two yaml files
def generate_yaml_diff(file1, file2):
    result = ["{"]
    with open(file1) as f1:
        file1_data = safe_load(f1)
    with open(file2) as f2:
        file2_data = safe_load(f2)

    return generate_diff(file1_data, file2_data)


def getFilesExtension(file1, file2):
    if file1.split(".")[-1] in ["yml", "yaml"] and file2.split(".")[-1] in ["yml", "yaml"]:
        return "yaml"
    else:
        return "json"


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
    filename1, filename2 = args.first_file, args.second_file
    print(generate_yaml_diff(filename1, filename2)
          if getFilesExtension(filename1, filename2) == "yaml"
          else generate_json_diff(filename1, filename2))


if __name__ == '__main__':
    main()
