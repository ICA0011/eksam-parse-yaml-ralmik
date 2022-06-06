import parse_yaml

def test_assignment():
    assert parse_yaml.parse_yaml('http://upload.itcollege.ee/~aleksei/eksam.yaml') == "Toomas Teine"
