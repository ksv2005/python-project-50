from gendiff.scripts.gendiff import generate_json_diff, generate_yaml_diff
import os


# testing plain json difference
def test_json_gendiff():
    FILE1_NAME = os.path.abspath("tests/fixtures/file1.json")
    FILE2_NAME = os.path.abspath("tests/fixtures/file2.json")
    FILE_RIGHT_NAME = os.path.abspath("tests/fixtures/right1.txt")
    assert generate_json_diff(FILE1_NAME, FILE2_NAME) == open(FILE_RIGHT_NAME).read()


# testing plain yaml difference
def test_yaml_gendiff():
    FILE1_NAME = os.path.abspath("tests/fixtures/file1.yaml")
    FILE2_NAME = os.path.abspath("tests/fixtures/file2.yaml")
    FILE_RIGHT_NAME = os.path.abspath("tests/fixtures/right1.txt")
    assert generate_yaml_diff(FILE1_NAME, FILE2_NAME) == open(FILE_RIGHT_NAME).read()
