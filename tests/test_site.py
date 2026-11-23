import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

BASE_URL = os.environ.get("BASE_URL", "http://localhost:8095")

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    d = webdriver.Chrome(options=options)
    yield d
    d.quit()

def test_page_title(driver):
    driver.get(BASE_URL)
    assert "FA23-BCT-057" in driver.title

def test_heading_and_student_details(driver):
    driver.get(BASE_URL)
    heading = driver.find_element(By.ID, "main-heading").text
    info = driver.find_element(By.ID, "student-info").text
    assert heading == "Automated CI/CD Web Application"
    assert "Muhammad Junaid" in info
    assert "FA23-BCT-057" in info

def test_button_click(driver):
    driver.get(BASE_URL)
    driver.find_element(By.ID, "action-btn").click()
    assert driver.find_element(By.ID, "btn-output").text == "Button clicked successfully!"

def test_textbox_input_and_submit(driver):
    driver.get(BASE_URL)
    box = driver.find_element(By.ID, "user-input")
    box.send_keys("Hello Cloud Computing")
    driver.find_element(By.ID, "submit-btn").click()
    assert driver.find_element(By.ID, "submitted-text").text == "Hello Cloud Computing"
    driver.save_screenshot("screenshot.png")
