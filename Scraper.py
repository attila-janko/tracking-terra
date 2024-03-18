from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from time import sleep

# Instantiate an Options object
options = Options()

# Add your options
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')
options.add_argument('--start-maximized')
options.add_argument('--disable-infobars')
options.add_argument('--disable-extensions')

# Instantiate a Chrome driver
service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service, options=options)

# URL of the login page
login_url = 'https://admin.cooltix.hu/login'

# URL of the page you want to scrape after logging in
target_url = 'https://admin.cooltix.hu/'

# Open the login page
driver.get(login_url)
sleep(2)

# Fill in the username and password and submit the form
driver.find_element(By.NAME, 'email').send_keys('tos.kop.aa@gmail.com'+ Keys.RETURN)
sleep(2)

driver.find_element(By.NAME, 'password').send_keys('c1gostekkes' + Keys.RETURN)

# Wait for login to complete, you might need to add explicit waits here
sleep(2) # Implicit wait, just for demonstration

# Go to the target page
driver.get(target_url)

sleep(2) # Implicit wait, just for demonstration

# Now you can use BeautifulSoup to parse the page source
soup = BeautifulSoup(driver.page_source, 'html.parser')

print(soup.prettify())
# Use the same logic to find your element
element = soup.find('p', class_='sc-bdvvtL glsYBK')


print(element.text)

# get the number before the / sign
number = element.text.split('/')[0]

#export the number to a file
with open('number.txt', 'w') as file:
    file.write(number)