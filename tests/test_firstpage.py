import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = None


@pytest.fixture(scope='module')
def setup_module():
    global driver
    driver = webdriver.Firefox("../vunetAssignment/Libraries")
    driver.get("https://website.grader.com/")
    time.sleep(3)
    cookie = driver.find_element_by_xpath("//a[contains(text(),'Accept')]")
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Accept')]")))
    cookie.click()

    yield
    driver.quit()


def test_website_grade(setup_module):
    driver.find_element_by_xpath("//input[@data-test-id='url']").send_keys("https://www.guru99.com/")
    driver.find_element_by_xpath("//input[@data-test-id='email']").send_keys("essarkemurthy@gmail.com")
    driver.find_element_by_xpath("//button[@data-test-id='homepage-button-submit']").click()

    # while driver.find_elements_by_xpath("//input[@type='url']").is_displayed():
    #     driver.find_element_by_xpath("//input[@type='url']").send_keys("https://www.guru99.com/")
    time.sleep(5)
    x = driver.find_element_by_xpath(
        "//div[@class='left-column']//i18n-string[text()='Performance']/../../div[2][@class='score']").text
    print(x)
    print(type(x))
    y = x.split('/')
    # driver.quit()
    score_percent = int(y[0]) / int(y[1])
    print(score_percent)
    assert score_percent > 0.07
