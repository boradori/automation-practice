import pytest

from components import (
    Header
)


@pytest.fixture(scope='session')
def header(session_driver):
    return Header(session_driver)
