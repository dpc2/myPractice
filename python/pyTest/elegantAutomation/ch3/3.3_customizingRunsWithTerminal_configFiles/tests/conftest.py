from pytest import fixture


# This is basically just argparse
def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        # default="dev"
        help="Environment to run tests against"
    )

@fixture(scope='session')
def env(request):
    return