import pytest

'''
pytest的case，不支持可选参数的
'''


@pytest.mark.parametrize("aa, bb", [(1, 1)])
# @pytest.mark.parametrize("aa, bb", [(2, 2)])
def test(aa, bb, cc=None):
    print(aa, bb, cc)
