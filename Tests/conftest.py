import pytest
from selenium import webdriver


@pytest.fixture()
def browser():
    print("creating chrome driver")
    my_browser = webdriver.Chrome()
    #my_browser.implicitly_wait(10)
    yield my_browser
    print("\nclosing chrome driver")
    my_browser.quit()
