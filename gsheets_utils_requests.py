import pandas as pd
import requests
# from config import *

class GoogleSheetsClient:
    def __init__(self, client_id: str, client_secret: str, refresh_tkn: str):
        r = self.get_access_token(client_id, client_secret, refresh_tkn)
        data = r.json()
        self.token = data["access_token"]
        self.token_type = data["token_type"]

        print("Successfully connected!")


    def get_access_token(self, client_id: str, client_secret: str, refresh_tkn: str):
        url = "https://oauth2.googleapis.com/token"
        data = {
            "grant_type": "refresh_token",
            "refresh_token": refresh_tkn,
            "client_id": client_id,
            "client_secret": client_secret
        }
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        r = requests.post(url, data=data, headers=headers)
        print(r.text)

        return r

    def connect_to_spreadsheet(self, sheet_id: str, range_name: str):
        # Constructing the URL with the required parameters
        url = f"https://sheets.googleapis.com/v4/spreadsheets/{sheet_id}/values:batchGet"
        params = {
        # Select your sheet and range you wish to ingest
            "ranges": range_name,
            "valueRenderOption": "FORMATTED_VALUE"
        }

        # Making the GET request to the Google Sheets API
        response = requests.get(url, headers={"Authorization": "Bearer " + self.token}, params=params)
        # Handling the response
        if response.status_code == 200:

            return response
        else:
            raise Exception(f"API Request Failed: {response.status_code} {response.text}")
    

    def get_sheet_data(self, sheet_id, range_name):
        response = self.connect_to_spreadsheet(sheet_id, range_name)
        json_data = response.json()
        values = json_data['valueRanges'][0]['values']

        # Convert the JSON data to a pandas DataFrame.
        # df = pd.DataFrame(values[1:], columns=values[0])

        return values

