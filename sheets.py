from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

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

print(terra)

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
