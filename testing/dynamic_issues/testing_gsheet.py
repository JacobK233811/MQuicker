# import pandas as pd
# import json
# import csv
# from google.oauth2 import service_account
#
# with open('service_account.json') as source:
#     info = json.load(source)
# credentials = service_account.Credentials.from_service_account_info(info)

import gspread
import os
from datetime import datetime

gc = gspread.service_account(filename="credentials.json")
sh = gc.open_by_key("1TXi-nkh6G585FzE8-jAo8mnakVCGelDSL9oKo2Pb9tM")
worksheet = sh.sheet1

# res = worksheet.get_all_records()
res = worksheet.get_all_values()
# res = worksheet.row_values(1)
# res = worksheet.get("A2:C2")
new_id = int(res[-1][0]) + 1

# user = ["Susan", 25, "Sydney"]
# worksheet.append_row(user)
# worksheet.add_cols(3)

path, function, mangas, time = str(os.path), "test", 0, datetime.now()
index = path.find("Users")
name = path[index:index+15]
time_list = time.strftime("%c").split()
worksheet.append_row([new_id, name, function, mangas] + time_list)

