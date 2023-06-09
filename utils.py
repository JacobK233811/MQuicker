from config import mangas, current

import os
import sys
import gspread
from google.auth.exceptions import TransportError
from cryptography.fernet import Fernet
from colorama import Fore, Back
from datetime import datetime

def num_puller(body):
    # Iterates over all words to find the chapter number and saves that number as an int if possible and if not, a float
    numbers = []
    for word in body.split():
        word = word.replace(":", "")
        try:
            numbers.append(int(word.strip()))
        except ValueError:
            try:
                numbers.append(float(word.strip()))
            except ValueError:
                pass
    return numbers or [-1]

def set_changes():
    # Sets the mangas and current lists to the recent adjustments in case of subsequent calls to a, n, or s
    with open("saved/list.txt", "rt", encoding="utf-8") as new_list:
        mangas = [line.split("|") for line in new_list.readlines()]
    with open("saved/latest.txt") as new_latest:
        current = new_latest.readlines()

    return mangas, current

try:
    # Saving data on file use to a Google Sheet
    try:
        gc = gspread.service_account(filename="access/credentials.json")
    except FileNotFoundError:
        # Create credentials.json file on first use
        with open('access/lock.json', 'rb') as lock, open('access/key.key', 'rb') as key:
            c_lock = lock.read()
            c_key = key.read()
        gatekeeper = Fernet(c_key)
        with open("access/credentials.json", "wt", encoding="utf-8") as c:
            c.write(gatekeeper.decrypt(c_lock).decode())
        gc = gspread.service_account(filename="access/credentials.json")

    sh = gc.open_by_key("1TXi-nkh6G585FzE8-jAo8mnakVCGelDSL9oKo2Pb9tM")
    worksheet = sh.sheet1
    mangas_len, time = len(mangas), datetime.now()
    pname, time_list = os.path.expanduser("~"), time.strftime("%c").split()
    with open("user.txt", encoding="utf-8") as username:
        lines = username.readlines()
        uname = lines[0].strip()
        uid = lines[1].strip()

    sh2 = gc.open_by_key("1o2HEEjF4mh8s_eQfTVyMqhd5POOPJMxdLkuA7iORQ64")
    worksheet2 = sh2.sheet1

    sh3 = gc.open_by_key("1eG1rgmkOGj6xAMNgLB24uvA4ocjxnDYUKr7svitpLVE")
    worksheet3 = sh3.sheet1
except TransportError:
    input(Fore.LIGHTRED_EX + "No Internet Access. Please run again when you have connected to WiFi. " +
                            "Press enter to acknowledge.  " + Fore.RESET)
    sys.exit(1)

def add_to_sheet(function, mnum=mangas_len, mlst=[]):
    res = worksheet.get_all_values()
    new_id = int(res[-1][0]) + 1
    if uname != "Fill":
        name = uname
    else:
        name = pname

    if function != "rate":
        worksheet.append_row([new_id, name, uid, function, mnum] + time_list)

        if function == "primer" or function == "add manga":
            res = worksheet2.get_all_values()
            new_id = int(res[-1][0]) + 1
            worksheet2.append_row([new_id, name, uid] + mlst)
    else:
        for rating in mlst:
            res = worksheet3.get_all_values()
            new_id = int(res[-1][0]) + 1
            worksheet3.append_row([new_id, name, uid] + rating)