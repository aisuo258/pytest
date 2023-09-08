import os
import common.util

def test_01():
    yaml_u = common.util.YamlUtil()
    a = {"name": "aisuo259"}
    yaml_u.write_yaml(a)
    assert a["name"] == 'aisuo259'

