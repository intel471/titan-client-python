import json
import os

PREFIX = os.path.abspath(os.path.dirname(__file__))

def read_fixture(path):
    with open(path, 'r') as f:
        return json.load(f)
