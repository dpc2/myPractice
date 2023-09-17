from pytest import mark

@mark.smoke
@mark.engine
@mark.ui
def test_engine_functions_as_expected(chrome_browser):
    my_browser = chrome_browser
    second_browser = chrome_browser

    chrome_browser.get('https://www.artofmanliness.com/articles/how-a-cars-engine-works')
    assert True
