import yaml

global PATH
PATH = './extract.yml'

class YamlUtil(object):

    def read_yaml(self, path=PATH):
        with open(path, 'r') as yf:
            res = yaml.load(stream=yf, Loader=yaml.FullLoader)
            return res
    
    def write_yaml(self, data, path=PATH) -> None:
        with open(path, 'a', encoding='utf8') as yf:
            res = yaml.dump(data=data, stream=yf, allow_unicode=True)

