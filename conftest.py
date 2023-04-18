import pytest

from app import app as application


@pytest.fixture
def app():
    return application

@pytest.fixture
def one():
    print('42')
    return 42
