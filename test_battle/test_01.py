import os

import pytest
import requests
import json



# 从json文件中获取方法，header，body等参数
@pytest.fixture()
def info_all():
    with open('./test_hlj/config.json') as jf:
        info = json.load(jf)
    return info

def login(info_all):
    info = info_all['login']
    info['url'] = info_all['root'] + info['url']
    rep = requests.request(method=info['method'],
                           url=info['url'],
                           headers=info['header'],
                           json=info['body'])
    return rep

# 测试函数
def test_login():
    rep = login()
    print(insert_rep.text)
    assert insert_rep.status_code == 200
    


if __name__ == "__main__":
    print(os.getcwd())
    pytest.main(['-vs'])