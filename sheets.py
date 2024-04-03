from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from time import sleep
import re
import datetime
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

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

driver.find_element(By.NAME, 'password').send_keys('tereda_0ffthemaps' + Keys.RETURN)

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




# Close the browser
driver.quit()

# get the number before the / sign
number = element.text.split('/')[0]



# Hitelesítési adatok betöltése
SERVICE_ACCOUNT_FILE = 'creds2.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

credentials = Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# A Google Sheets API inicializálása
service = build('sheets', 'v4', credentials=credentials)

# A Google Táblázat azonosítójának és az olvasni kívánt tartományok megadása
spreadsheet_id = '1oPz0p-HIC_mpVTbgDUoB_p8xezHl3H_SUH_u2ILpZzs'
range_name = 'Terra barik!G3' # Például 'Sheet1' munkalap A1 és A2 cellái közötti tartomány
range_name_pavi = 'Pavi barik!G3' # Például 'Sheet1' munkalap A1 és A2 cellái közötti tartomány

# Adatok kiolvasása
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=spreadsheet_id,
                            range=range_name).execute()
values = result.get('values', [])

if not values:
    print('Nincsenek adatok.')
else:
    for row in values:
        # Nyomtasd ki a sorokat
        print(row)

terra = row[0]



# Adatok kiolvasása
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=spreadsheet_id,
                            range=range_name_pavi).execute()
values = result.get('values', [])

if not values:
    print('Nincsenek adatok.')
else:
    for row in values:
        # Nyomtasd ki a sorokat
        print(row)

pavi = row[0]

#convert pavi and terra to int
pavi = int(pavi)
terra = int(terra)

tickets = pavi + terra


number_of_sold_tickets = int(number) 


number_of_sold_tickets =number_of_sold_tickets -1 + tickets
# get the current date and time
now = datetime.datetime.now()


# Load the HTML template
with open('index.html', 'r') as file:
    html_content = file.read()

# change line 28 from         <div class="number"> 4 </div> to the actual number of sold tickets
html_content = re.sub(r'<div class="number">.*</div>', f'<div class="number">{number_of_sold_tickets}</div>', html_content)

# change line 29 from         <div>legutolsó frissítés: 2023.03.18 21:27</div> to the actual date and time
html_content = re.sub(r'<div>legutolsó frissítés: .*</div>', f'<div>legutolsó frissítés: {now.strftime("%Y.%m.%d %H:%M")}</div>', html_content)

# Save the updated content to 'index.html'
with open('index.html', 'w') as file:
    file.write(html_content)