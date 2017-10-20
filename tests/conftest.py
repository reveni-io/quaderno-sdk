import pytest


@pytest.fixture(scope='class')
def conf_class(request):
    request.cls.token = request.config.option.token
    request.cls.api_host = request.config.option.api_host


def pytest_addoption(parser):
    parser.addoption(
        '--token',
        dest='token',
        help='API token')

    parser.addoption(
        '--api-host',
        dest='api_host',
        help='API host')
