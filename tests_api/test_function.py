import pytest
import requests


@pytest.fixture
def url(request):
    return request.config.getoption("--url")


@pytest.fixture
def status_code(request):
    return request.config.getoption("--status_code")


def pytest_addoption(parser):
    parser.addoption("--url", default="https://ya.ru", help="Target url")
    parser.addoption("--status_code", default=200, type=int, help="Target status_code")


def test_status_code_of_entered_url(url, status_code):
    r = requests.get(url)
    actual_status_code = r.status_code
    assert actual_status_code == status_code