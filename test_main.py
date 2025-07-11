import json
from main import merge_data

def test_merge_data():
    d1 = json.load(open("data-1.json"))
    d2 = json.load(open("data-2.json"))
    expected = json.load(open("data-result.json"))

    assert merge_data(d1, d2) == expected

