from selenium import webdriver
from seleniumbase import Driver

class Browser():

		chrome = Driver(browser='chrome', headless=False)

		def maximise_window(self):
				self.chrome.maximize_window()

		def close_browser(self):
				self.chrome.quit()