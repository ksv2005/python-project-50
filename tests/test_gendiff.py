from gendiff.scripts.gendiff import generate_diff
import os


# testing plain json difference
def test_plain_gendiff():
    FILE1_NAME = os.path.abspath("tests/fixtures/file1.json")
    FILE2_NAME = os.path.abspath("tests/fixtures/file2.json")
    FILE_RIGHT_NAME = os.path.abspath("tests/fixtures/right1.txt")
    assert generate_diff(FILE1_NAME, FILE2_NAME) == open(FILE_RIGHT_NAME).read()
