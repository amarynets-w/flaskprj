import pytest


@pytest.fixture
def one():
    print('12')
    return 12