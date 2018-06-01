#!/usr/bin/env python

#Importing Selenium Modules
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

#Importing unittest automation framework
import unittest

#Importing Misc Python Modules
import time, sys, os

#Importing logging module
import logging

#Enhancing Console Log & File Log
logging.basicConfig(level=logging.DEBUG, format='| %(asctime)s | %(levelname)-5s <-> %(message)s ', filename="login_logfile.log", datefmt='%m/%d/%y %H:%M:%S', filemode='w')
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter(fmt='| %(asctime)s | %(levelname)-5s <-> %(message)s', datefmt='%m/%d/%y %H:%M:%S')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

class SetupCleanup(unittest.TestCase):
	"""
	Class to run Setup before running testcase & Cleanup at the end of the testcase
	"""
	browser = 'chrome'
	
	def setUp(self):
		"""
		Function to initialize webdriver & opens the browser
		"""
		print "\n"
		logging.debug("Running Setup")
		if str(self.browser).lower() == 'chrome':
			if os.name == 'posix':
				self.driver = webdriver.Chrome(str(self.path) + "/chromedriver")
			elif os.name == 'nt':
				self.driver = webdriver.Chrome(str(self.path) + "/chromedriver.exe") #D:/E_Scripts/Selenium_Drivers
		elif str(self.browser).lower() == 'firefox':
			#self.driver = webdriver.Firefox()
			if os.name == 'posix':
				self.driver = webdriver.Firefox()(str(self.path) + "/chromedriver")
			elif os.name == 'nt':
				self.driver = webdriver.Firefox()
		elif str(self.browser).lower() == 'ie':
			if os.name == 'posix':
				self.driver = webdriver.Ie(str(self.path) + "/chromedriver")
			elif os.name == 'nt':
				self.driver = webdriver.Ie(str(self.path) + "/IEDriverServer.exe")

		self.driver.get("http://mail.google.com")
		if str(self.browser).lower() == 'ie':
			print "sleep"
			time.sleep(5)
		try:
			headingText = WebDriverWait(self.driver, 90).until(EC.presence_of_element_located((By.ID, "headingText")))
		except TimeoutException:
			logging.error("Failed to load web page within 90secs")
			return 1
		return 0

	def tearDown(self):
		"""
		Function to close the tab and quit the browser
		"""
		logging.debug("Running Cleanup")
		self.driver.close()
		self.driver.quit()
		logging.debug("Cleanup is successful")
		return 0
		
class LoginCheck(SetupCleanup):
	"""
	Class to login with given credentials and check all elements are present or not
	"""
	
	def test_LoginCheck(self):
		"""
		Function to test login and elements after login
		"""

		user_login_form_title= self.driver.find_element_by_xpath('//*[@id="view_container"]/div/div/div[1]/content/div')
		message = user_login_form_title.text
		logging.info("User Logging To Gmail: " + str(message))
		if str(message) != 'Sign in\nto continue to Gmail':
			logging.error("Mismatch in Gmail User Login Form Message")
			return 1
        
		logging.info("Entering the username & password and click on Login button for logging in")
		username = self.driver.find_element_by_id("identifierId")
		username.clear()
		username.send_keys(str(self.email))
		time.sleep(3)
		next = self.driver.find_element_by_xpath("//*[@id=\"identifierNext\"]/content/span")
		next.click()
		time.sleep(5)
		password = self.driver.find_element_by_name("password")
		password.clear()
		password.send_keys(str(self.passwd))
		time.sleep(3)
		loginbutton = self.driver.find_element_by_id("passwordNext")
		loginbutton.click()
		
		logging.info("Waiting for login and check for all elements presences")
		try:
			google = WebDriverWait(self.driver, 90).until(EC.presence_of_element_located((By.ID, "gbq1")))
		except TimeoutException:
			logging.error("Failed to load gmail login page within 90secs")
			return 1
		logging.info("Google found in Main Page")
		google_color = google.value_of_css_property("color")
		google_font = google.value_of_css_property("font-size")
		logging.info("Google element color: " + str(google_color) + "\t\t\t & Google Font Size is: " + str(google_font))
		
		try:
			gmail = self.driver.find_element_by_xpath("//*[@id=\":i\"]")
		except NoSuchElementException:
			logging.error("Failed to locate gmail element")
			return 1
		logging.info("Gmail element found in Main Page")
		gmail_color = google.value_of_css_property("color")
		gmail_font = google.value_of_css_property("font-size")
		logging.info("Gmail element color: " + str(gmail_color) + "\t\t\t & Font Size is: " + str(gmail_font))
		
		try:
			compose = self.driver.find_element_by_xpath("/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div[1]/div[2]/div/div/div/div[1]/div/div")
		except NoSuchElementException:
			logging.error("Failed to locate compose element")
			return 1
		logging.info("Compose element found in Main Page")
		compose_color = google.value_of_css_property("color")
		compose_font = google.value_of_css_property("font-size")
		logging.info("Compose element color: " + str(compose_color) + "\t\t\t & Font Size is: " + str(compose_font))
		time.sleep(5)
		
		compose.click()
		time.sleep(3)
		email = self.driver.find_element_by_name("to")
		time.sleep(1)
		email.send_keys(str(self.email))
		time.sleep(3)
		subject = self.driver.find_element_by_name("subjectbox")
		time.sleep(1)
		subject.send_keys("Test completed successfully please check the login_logfile.log file")
		time.sleep(3)
		subject.send_keys(Keys.TAB)
		subject.send_keys(Keys.CONTROL + Keys.RETURN)
		time.sleep(3)
		
		return 0
		
if __name__ == '__main__':
	if len(sys.argv) == 5:
		SetupCleanup.browser = sys.argv[1]
		SetupCleanup.path = sys.argv[2]
		SetupCleanup.email = sys.argv[3]
		SetupCleanup.passwd = sys.argv[4]
	elif len(sys.argv) == 4:
		SetupCleanup.browser = 'chrome'
		SetupCleanup.path = sys.argv[1]
		SetupCleanup.email = sys.argv[2]
		SetupCleanup.passwd = sys.argv[3]
	elif len(sys.argv) != 5 or len(sys.argv) != 4:
		print "Usage: python login_to_gmail.py <browser> <path> <email> <password>"
		print ""
		print "browser  : Type of Browser. Eg: chrome or firefox or ie"
		print "path     : Path of drivers where it was located Eg: D:\E_Scripts\Selenium_Drivers"
		print "email    : Email ID to login to Gmail Eg: mrtej.teja6@gmail.com"
		print "passwd   : Password of Gmail Account Eg: password"
		print ""
		print "Eg: python login_to_gmail.py chrome D:/E_Scripts/Selenium_Drivers email@gmail password"
		print ""
		sys.exit(1)
		
	suite = unittest.TestSuite()
	suite.addTest(LoginCheck('test_LoginCheck'))

	result = unittest.TestResult()
	suite.run(result)
	print "\nunittest results: \n" + str(result)
	
	print "\n"
	print "========================"
	print "Test Completed"
	print "========================"