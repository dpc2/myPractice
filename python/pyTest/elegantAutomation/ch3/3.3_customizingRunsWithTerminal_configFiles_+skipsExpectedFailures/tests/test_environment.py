from pytest import mark

# @mark.skip(reason="broken by deploy #something")
@mark.xfail(reason="Env was not QA")
def test_environment_is_qa(app_config):
    # assert env == 'qa'
    base_url = app_config.base_url
    port = app_config.app_port
    assert base_url == 'https://myqa-env.com'
    assert port == 80


@mark.skip(reason="Broken, fixing next sprint")
def test_this_needs_work():
    assert False


def test_environment_is_dev(app_config):
    # assert env == 'dev'
    base_url = app_config.base_url
    port = app_config.app_port
    assert base_url == 'https://mydev-env.com'
    assert port == 8080

    # driver.get(base_url)

@mark.skip(reason="Not a staging env")
def test_environment_is_staging(app_config):
    base_url = app_config.base_url
    assert base_url == 'staging'
    base_url = app_config.base_url
    assert base_url == 'staging'
    base_url = app_config.base_url
    assert base_url == 'staging'
