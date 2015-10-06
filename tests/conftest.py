import pytest


@pytest.fixture(scope='class')
def conf_class(request):
    request.cls.token = request.config.option.token
    request.cls.account_name = request.config.option.account_name


def pytest_addoption(parser):
    parser.addoption(
        '--token',
        dest='token',
        help='API token')

    parser.addoption(
        '--account-name',
        dest='account_name',
        help='Quaderno account name')
