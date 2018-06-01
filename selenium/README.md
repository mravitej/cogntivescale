# selenium

PREREQUISITES:
On Windows:
Mandatory
Python 2.7 –  Download and set path in  the system variable

Setting up selenium

Open Command Prompt (windows)

Install selenium by using command  : 

“pip install -U selenium”

or follow instruction mentioned link "https://pypi.org/project/selenium/"

Install Browser Drivers:

Chrome driver – Download chrome driver for selenium - ChromeDriver 2.39
				"https://sites.google.com/a/chromium.org/chromedriver/downloads"
				
Firfox  - Download firefox driver for selenium. - geckodriver-v0.20.1-win64.zip
				"https://github.com/mozilla/geckodriver/releases"
				
Internet explorer driver – Download Internet explorer driver for selenium. this driver supports for windows 7 - IEDriverServer_x64_3.9.0.zip
				"http://selenium-release.storage.googleapis.com/index.html?path=3.9/"

Now Unzip/extract all drivers and copy in one folder (don't create any sub folders)

6.RUNNING THE TESTS:

Use the following command to run the selenium script

COMMAND:
python <filename.py> <browser_name> <path_where_browser_drivers_located> <gmail_email_id> <password>

eg: python login_to_gmail.py chrome D:/drivers email_example@gmail.com password


browser_name can be one of following but make sure that browser’s driver file are present in same folder which the path was mentioned
firefox
chrome
ie


7.TEST RESULTS:

Now the test results are saved in the login_logfile from where the test is executed
 
8. AUTHOR
Ravi Teja Mygapula