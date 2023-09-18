from pytest import fixture
from config import Config

# This is basically just argparse
def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        # default="dev"
        help="Environment to run tests against, yooo!"
    )

@fixture(scope='session')
def env(request):
    return request.config.getoption("--env")

@fixture(scope='session')
def app_config(env):
    cfg = Config(env)
    return cfg