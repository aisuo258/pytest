import pytest

@pytest.fixture(autouse=True)
def url_all():
    return 'url'

@pytest.mark.parametrize('name', ['张三', '李四', '王五'])
def test_name(name):
   print(url_all)
   print(name)

if __name__ == "__main__":
    pytest.main(['test_my/test_02.py','-vs'])