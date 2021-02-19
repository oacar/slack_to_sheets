from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

def append_to_sheets(rows):
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    if len(rows[0])!=3:
        pass
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                '/Users/omeracar//Downloads/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
#    result = sheet.values().get(spreadsheetId='1MI-6aQDmTEfEEhYclf9gKzGBHqlOIaSnKf6THs-334Q',
#    range='Sheet1!A1:B2').execute()
#    values = result.get('values', [])
#    rows = [['omer','ssss']]
    print('hello')
    sheet.values().append(
        spreadsheetId='1MI-6aQDmTEfEEhYclf9gKzGBHqlOIaSnKf6THs-334Q',
        range="Sheet1!A:Z",
        body={
            "majorDimension": "ROWS",
            "values": rows
        },
        valueInputOption="USER_ENTERED"
    ).execute()

def main():
    rows = [['1','2','3']]
    append_to_sheets(rows)
if __name__ == '__main__':
    main()