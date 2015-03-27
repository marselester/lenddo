import os
import json

TEST_DIR = os.path.dirname(__file__)


def json_from_file(filename):
    path_to_file = os.path.join(TEST_DIR, 'json', filename)
    with open(path_to_file) as fh:
        return json.load(fh)
