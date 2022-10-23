import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_language_browser(browser):
	link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
	browser.get(link)
	time.sleep(30)
	assert browser.find_element(By.CSS_SELECTOR, "button.btn"), f"button not found"
	 