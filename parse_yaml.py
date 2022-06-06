import yaml, requests


def parse_yaml(url):
    yaml_content = requests.get(url)
    content_list = yaml.safe_load(yaml_content.text)
    for dicts in content_list:
        for key, value in dicts.items():
            if dicts[key]["permission"] == "admin":
                return dicts[key]["name"]


if __name__ == '__main__':
    print(parse_yaml('http://upload.itcollege.ee/~aleksei/eksam.yaml'))
