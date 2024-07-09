from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

# Path to the GeckoDriver executable
driver_path = '/snap/bin/geckodriver'

# Path to the Firefox binary
firefox_binary_path = '/usr/bin/firefox'

# Set up Firefox options
options = Options()
options.binary_location = firefox_binary_path

# Set up the GeckoDriver service
service = Service(executable_path=driver_path)

# Initialize the WebDriver
driver = webdriver.Firefox(service=service, options=options)

# Your test code here
driver.get('http://www.example.com')
print(driver.title)

# Clean up
driver.quit()

from selenium import webdriver
path = '/usr/bin/firefox'
driver = webdriver.FirefoxOptions()
driver.get("http://selenium.dev")

driver.quit()
