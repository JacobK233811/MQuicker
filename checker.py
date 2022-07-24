from bs4 import BeautifulSoup
import requests
from colorama import Fore, Back
from collections import defaultdict
from datetime import datetime
from itertools import zip_longest
import os
import gspread
import webbrowser
from google.auth.exceptions import TransportError
from cryptography.fernet import Fernet

# Modules for dynamic JS websites
from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets
from PyQt5.QtWebEngineWidgets import QWebEngineView as QWebView
import sys

# Each list within the mangas list has the following parameters: Name, Link, Source
with open("saved/list.txt", "rt", encoding="utf-8") as m_list:
    mangas = [line.split("|") for line in m_list.readlines()]
if not mangas:
    mangas = [['Attack on Titan', 'https://attackontitanmanga.com/', 'AoT|\n'],
              ['Solo Leveling', 'https://w3.sololeveling.net/', 'Solo'],
              ['Tales of Demons and Gods', 'https://manganelo.com/manga/hyer5231574354229', 'Mangelo|\n'],
              ['The Great Mage Returns After 4000 Years', 'https://manganelo.com/manga/go922760', 'Mangelo|\n'],
              ['Second Life Ranker', 'https://zeroscans.com/comics/188504-second-life-ranker', 'ZeroLeviatan|\n'],
              ['I am the Sorcerer King', 'https://leviatanscans.com/comics/i-am-the-sorcerer-king', 'ZeroLeviatan|\n'],
              ['Descent of the Demonic Master', 'https://mangaeffect.com/manga/the-descent-of-the-demonic-master/',
               'Effect|\n'],
              ['Chronicles of Heavenly Demon', 'https://www.readmng.com/chronicles-of-heavenly-demon-3', 'ReadMng|\n'],
              ['Iruma-Kun', 'https://www.readmng.com/mairimashita-iruma-kun', 'ReadMng|\n'],
              ['Kingdom', 'https://www.readmng.com/kingdom', 'ReadMng|\n'],
              ['Solo Auto Hunting', 'https://mangaeffect.com/manga/solo-auto-hunting/', 'Effect|\n'],
              ["The Scholar's Reincarnation", 'https://www.readmng.com/the-scholars-reincarnation', 'ReadMng|\n'],
              ["LESSA - Servant of Cosmos", 'https://mangakakalot.com/read-qu0ei158524508422', 'Kakalot|\n'],
              ["Demon Magic Emperor", 'https://mangadex.org/title/43692/demonic-emperor', 'MangaDex|\n'],
              ["Leveling Up, by Only Eating!", 'https://mangadex.org/title/48217/leveling-up-by-only-eating',
               'MangaDex|\n'],
              ["Apothesis", "https://mangadex.org/title/23001/apotheosis-ascension-to-godhood", "MangaDex|\n"],
              ["Yuan Zun", "https://mangakakalot.tv/manga/yuan_zun", "Kakalot|\n"],
              ["Martial Peak", "https://manganelo.com/manga/martial_peak", "Mangelo|\n"],
              ["Legendary Moonlight Sculptor", "https://www.readmng.com/Dalbic-Jogaksa-2/", "ReadMng|\n"]
              ]

# Set up the saved folder if it doesn't exist yet
try:
    os.mkdir("saved")
except FileExistsError:
    pass
os.system("clear")
os.system("Cls")
print(Fore.LIGHTGREEN_EX + "Welcome to MQuicker!" + Fore.RESET)
with open("MQuicker_Mascot.txt", "rt", encoding="utf-8") as mascot:
    print(mascot.read())

# On most sites the desired element will be an anchor 'a' tag. However, this default dict allows us to specify exceptions
source_elements = defaultdict(lambda: 'a')
source_elements['ZeroLeviatan'], \
    source_elements["asura"], source_elements["ManhuaScan"] = ['span'] * 3
source_elements['WP'] = 'li'
source_elements['Kakalot'] = 'div'
source_elements['Solo'] = 'td'
source_elements["Sword"] = 'h3'

# Now the i_or_cls parameter of finder comes from this neat dictionary. All except AoT & Apoth use classes intentionally
source_methods = {'AoT': 9, 'Mangelo': 'chapter-name text-nowrap', 'ZeroLeviatan': 'text-muted text-sm',
                  'ReadMng': 'chnumber', 'WP': 'wp-manga-chapter',
                  'MangaDex': 'text-truncate', 'Kakalot': 'chapter-list', "lh": "chapter",
                  "asura": "epcur epcurlast", "Apoth": 6, "Solo": "", "Sword": "elementor-post__title",
                  'ManhuaScan': 'title'}

# For later use in the update_latest function
latest_chapters = []
# Current also features throughout for comparison purposes
with open("saved/latest.txt") as f:
    current = f.readlines()

# Pertains to dynamic_finder. The run count is used for indexing within dynamic_finder and dynamic_indexes for insertion
dynamic_mangas = []
dynamic_run_count = 0
dynamic_indexes = []
dynamic_happened = False
# The following declarations help properly update_latest for the dynamics
dynamic_ch_use = 0
dynamic_chapters = []


# The following three functions pertain to .txt file handling to keep new users from having to ever open a text file
# Progressive input statements provide a clean text editing experience with proper formatting and alignment
# Deters user error or frustration with sensitive entries. Next code section starts at line 175
def primer():
    # Choosing which manga of the base list to keep and setting their current chapter/status for that one-by-one
    if not input(
            f"{Fore.LIGHTYELLOW_EX}Are you sure? This is a somewhat long process meant only for first-time users." +
            f"\n{Fore.LIGHTRED_EX}Press enter to cancel. {Fore.LIGHTGREEN_EX}Typing anything else will begin the " +
            f"priming procedure.  {Fore.RESET}"):
        return "Interrupt"

    if input(
            f"{Fore.LIGHTMAGENTA_EX}Are you comfortable entering a first name or user name? " +
            f"{Fore.LIGHTGREEN_EX}Type anything for yes {Fore.LIGHTRED_EX}or enter for no.  {Fore.RESET}"):
        with open("user.txt", "wt", encoding="utf-8") as user:
            written_name = input(f"{Fore.LIGHTWHITE_EX}Please enter your name.  {Fore.RESET}")
            generated_id = str(max([int(row[2]) for row in worksheet.get_all_values()[1:]]) + 1)
            user.write(written_name + "\n" + generated_id)
            global uname, uid
            uname = written_name
            uid = generated_id

    with open("saved/list.txt", "wt", encoding="utf-8") as names, \
            open("saved/latest.txt", "wt", encoding="utf-8") as numbers:
        keep_counter = 0
        keep_list = []
        for manga in mangas:
            title = manga[0]
            if input(f"\n\n{Fore.LIGHTYELLOW_EX}Would you like to keep {title} on your list? " +
                     f"\n{Fore.LIGHTGREEN_EX}Type anything for yes {Fore.LIGHTRED_EX}or enter for no.  {Fore.RESET}"):
                keep_list.append(title)
                keep_counter += 1
                names.write("|".join(manga))
                print(f"{Fore.GREEN}Note: If you would like to quickly set up a new \"0 yts\" manga, "
                      + "please press enter without any input for both of the following")
                verify_status(numbers)
    add_to_sheet("primer", keep_counter, keep_list)
    print(f"{Fore.LIGHTGREEN_EX}Well Done! You've primed your personal MQuicker.{Fore.RESET}")
    set_changes()


def add():
    # Quickly add new manga information in both list.txt and latest.txt
    add_counter = 0
    add_list = []
    with open("saved/list.txt", "at", encoding="utf-8") as names, \
            open("saved/latest.txt", "at", encoding="utf-8") as numbers:
        continuation = "Yep"
        while continuation:
            add_counter += 1
            print(f"{Fore.LIGHTWHITE_EX}Please enter all of the following information for the manga you'd like to add")
            title = input(f'{Fore.RESET}Name  ')
            add_list.append(title)
            while True:
                link_var, source_var = input('Link  '), input('Source (see supported source codes)  ')
                if link_var[:8] == "https://" and "." in link_var and source_var in source_methods:
                    break
                else:
                    print(f"{Fore.LIGHTRED_EX}Please enter a valid link and supported source code.  {Fore.RESET}")
            names.write(f"{title}|{link_var}|{source_var}|\n")
            # numbers.write(f"{input('Current Chapter  ')} {input('Status (yts/wip/utd)  ')}\n")
            verify_status(numbers)
            continuation = input(
                f"{Fore.LIGHTRED_EX}Press enter to quit {Fore.LIGHTGREEN_EX}or type anything into the input to continue adding manga  ")
    add_to_sheet("add manga", add_counter, add_list)
    set_changes()


def change_current():
    # Allows for a fast run-through of all manga on the list and provides the option to update status and chapter
    change_counter = 0
    with open("saved/latest.txt", "rt", encoding="utf-8") as numbers_read:
        chapters = [line for line in numbers_read.readlines()]
    with open("saved/latest.txt", "wt", encoding="utf-8") as numbers:
        for i, manga in enumerate(mangas):
            if chapters[i].split()[1] != "utd" and input(
                    f"\n{Fore.LIGHTMAGENTA_EX}Would you like to update {manga[0]}'s current chapter? " +
                    f"{Fore.LIGHTWHITE_EX}Right now it is {chapters[i]}" +
                    f"{Fore.LIGHTGREEN_EX}Type anything for yes {Fore.LIGHTRED_EX}or simply press enter for no.  {Fore.RESET}"):
                change_counter += 1
                verify_status(numbers)
            else:
                numbers.write(chapters[i])
    add_to_sheet("change current", change_counter)
    set_changes()


# Rate/Recommend Interlude
def rate():
    # The rate function collects user ratings to help build a database for a future recommend feature
    rate_list = []
    for manga in mangas:
        if input(f"\n{Fore.LIGHTYELLOW_EX}Would you like to rate {manga[0]}? " +
                 f"{Fore.LIGHTGREEN_EX}Type anything for yes {Fore.LIGHTRED_EX}or simply press enter for no.  {Fore.RESET}"):
            ratings = [manga[0]]
            for scale in ["Overall", "Plot", "Action", "Romance", "Comedy", "Art"]:
                ratings.append(float(input(
                    f"\n{Fore.LIGHTMAGENTA_EX}How would you rate {manga[0]}'s {scale} on a scale of 1 - 10? {Fore.RESET}")))
            for boolean in ["Family Friendly", "Happy"]:
                ratings.append(float(input(f"\n{Fore.LIGHTMAGENTA_EX}Did you find {manga[0]} {boolean} " +
                                           f"{Fore.LIGHTGREEN_EX}Type 1 for yes {Fore.LIGHTRED_EX}and 0 for no  {Fore.RESET}")))
            rate_list.append(ratings)
    add_to_sheet("rate", mlst=rate_list)


# The following three functions construct the core of this application's three query types: all, new, and save
# Each one goes through the list of manga, calling other functions in this .py file for various functionality
# Users call these whenever they want to check for new chapters and each one caters to a different need
# Near every line of code comes into play on the call of one of these functions. Next sections starts line 270
def a():
    # Simply outputs chapter information for every include manga within list.txt
    for i, manga in enumerate(mangas):
        if manga[2] == "WP":
            dynamic_indexes.append(i)
            dynamic_mangas.append(manga)
            latest_chapters.append("9999")
            continue
        latest, link = manga_strip(manga)
        latest_chapters.append(latest)
        try:
            previous = num_puller(current[i])[0]
        except IndexError:
            previous = 0
        # The below if-else statement changes the color of the output when the latest chapter is greater than the latest read
        # If intending to access file through CLI w/o iPython, change color to "NEW " for the ~if~ and "" for the ~else~
        if float(latest) > previous:
            color = Fore.LIGHTYELLOW_EX
            # The placeholder enables the feature of only showing links for items with a new chapter
            if current[i].split()[1] == "utd":
                link_placeholder = link
                # Automatically opens the latest chapter
                webbrowser.open_new_tab(link)
            else:
                # link_placeholder = wip_link_switch(manga, previous)
                link_placeholder = manga[1]
        else:
            color = Fore.CYAN
            link_placeholder = ""
        print(color + f"{manga[0]}: {previous} -> {latest} {Fore.LIGHTBLUE_EX} {link_placeholder}")
    finisher("a")
    add_to_sheet("all")


def n():
    # Outputs chapter information for only the mangas which have a new chapter to show
    global current
    current = current[::-1]
    for i, manga in enumerate(mangas[::-1]):
        if manga[2] == "WP":
            dynamic_indexes.append(i)
            dynamic_mangas.append(manga)
            latest_chapters.append("9999")
            continue
        latest, link = manga_strip(manga)
        latest_chapters.append(latest)
        try:
            previous = num_puller(current[i])[0]
        except IndexError:
            previous = 0
        # Only renders if there is a new chapter
        if float(latest) > previous:
            if current[i].split()[1] != "utd":
                link = manga[1]
            else:
                # Automatically opens the latest chapter
                webbrowser.open_new_tab(link)
            print(Fore.LIGHTMAGENTA_EX + f"{manga[0]}: {previous} -> {latest} Copy to see it:  {Fore.LIGHTBLUE_EX} {link}")
        elif i % 5 == 0 and i != 0:
            print(Fore.LIGHTGREEN_EX + "Loading...")
    finisher("n")
    add_to_sheet("new")


def s():
    # Outputs chapter information for every manga into a text file for later reference
    with open(f'saved/{datetime.strftime(datetime.now(), "%m%d%y")}.txt', "wt", encoding="utf-8") as file_access:
        for i, manga in enumerate(mangas):
            if manga[2] == "WP":
                dynamic_indexes.append(i)
                dynamic_mangas.append(manga)
                latest_chapters.append("9999")
                continue
            latest, link = manga_strip(manga)
            latest_chapters.append(latest)
            try:
                previous = num_puller(current[i])[0]
            except IndexError:
                previous = 0
            # The below if-else statement adds NEW to the output when the latest chapter is greater than the latest read
            if float(latest) > previous:
                if current[i].split()[1] != "utd":
                    link = manga[1]
                color = "NEW "
                # The placeholder enables the feature of only showing links for items with a new chapter
                link_placeholder = " + Link: " + link
            else:
                color = ""
                link_placeholder = ""
            file_access.write(color + f"{manga[0]}: {previous} -> {latest}{link_placeholder}\n\n")
            if i % 4 == 0 and i != 0:
                print(Fore.LIGHTGREEN_EX + "Loading...")
    finisher("s")
    add_to_sheet("save")


# The following three functions pertain to sending HTTP requests to websites to get their html content
# Ends with the desired most recent chapter number. Next and final section start on line 346
def manga_strip(manga):
    # Pulling all the necessary info out of the manga list for quick reference
    source_url = manga[1]
    element = source_elements[manga[2]]
    method = source_methods[manga[2]]

    webpage_request = requests.get(source_url)
    # Finder function enables one line to check any new properly defined list item (see line 16 comment)
    latest_chapter, link = finder(webpage_request, element, method)

    # In case it is a local reference to the chapter page (as with MangaDex)
    if link[:8] != "https://":
        if "readmng" in source_url:
            link = source_url + "/" + link.split("/")[-1]
        else:
            link = source_url + link
        
    latest_chapter = psych_handler(latest_chapter, link, manga[2])

    return latest_chapter, link


# The i_or_cls parameter defined in source_methods will decide whether to find by index or class
# This process will use the typing of that same item to do so.
def finder(not_parsed, el, i_or_cls):
    # Makes use of bs4 to get the right tag, it's text, and the number from that text
    parsed = BeautifulSoup(not_parsed.content, 'html.parser')
    typ = type(i_or_cls)
    # If the source_methods dictionary a class, typ will have str type.
    # If the same dictionary holds index, typ will have int type
    if typ is str:
        try:
            tag = parsed.find(el, class_=i_or_cls).a
            # Sometimes, a useless anchor tag child exists and creates a None value
            if tag is None:
                tag = parsed.find(el, class_=i_or_cls)
        except AttributeError:
            tag = parsed.find(el, class_=i_or_cls)
    elif typ is int:
        tag = parsed.findAll(el)[i_or_cls]
    else:
        tag = 'Error'

    # Iterates over all words to find the chapter number and saves that number as an int if possible and if not, a float
    try:
        numbers = num_puller(tag.text)
        if numbers:
            output = str(numbers[0])
        else:
            output = "0"
    except AttributeError:
        output = "-1"

    # Posting the link directly to the chapter if possible, and to the chapter list if not
    try:
        if tag.name == 'a':
            return output, tag.attrs['href']
    except AttributeError:
        print(Fore.LIGHTRED_EX + "The following comic did not load." + Fore.RESET)
    return output, not_parsed.url


def psych_handler(lc, lk, source):
    # Some websites post teaser chapters that have no content. This counteracts that by setting the chapter back one.
    try:
        ch = int(lc)
    except ValueError:
        ch = float(lc)
    ch_web = requests.get(lk)
    ch_soup = BeautifulSoup(ch_web.content, 'html.parser')
    if source == "AoT":
        if ch_soup.strong.text[:14] == "We will update":
            ch -= 1
    if source == "MangaDex":
        try:
            if ch_soup.find("div", {
                "class": "col-2 col-lg-1 ml-1 text-right text-truncate order-lg-8 text-warning"}).text.strip()[
               :2] == "in":
                ch -= 1
        except AttributeError:
            pass
    if source == "Solo":
        if ch_soup.findAll("strong")[1].text[:5] == "=====":
            ch -= 1
    return str(ch)


# The following three functions close out the program
# This is the last section
def finisher(ans):
    # Runs dynamic website handling, updates latest.txt, and exits
    d_urls = [m[1] for m in dynamic_mangas]
    global dynamic_happened
    if d_urls and not dynamic_happened:
        dynamic_happened = True
        print(Fore.LIGHTGREEN_EX + "Handling Dynamic Websites...")
        # To suppress error messages in calls of PyQt5 WebEngine
        os.environ["QTWEBENGINE_CHROMIUM_FLAGS"] = "--disable-logging"
        try:
            app = QtWidgets.QApplication(sys.argv)
            fixer = QWebView()  # used to resolve PyQt5 caching errors
            webpage = WebPage()
            webpage.start(d_urls)
            app.exec_()
        except AttributeError:
            print(f"{Fore.LIGHTRED_EX}Dynamic Websites Unable to Load.")

    global current, latest_chapters, dynamic_chapters
    print(Fore.LIGHTGREEN_EX + "Updating...")
    if ans == "n":
        dynamic_chapters = dynamic_chapters[::-1]
        latest_chapters = latest_chapters[::-1]
        current = current[::-1]
    elif ans == "s" and dynamic_chapters[-2:] != [-1] * 2:
        with open(f'saved/{datetime.strftime(datetime.now(), "%m%d%y")}.txt', "at", encoding="utf-8") as file_access:
            file_access.write(
                "\n\n".join(['\nDynamics', "\n".join([str(lst) for lst in dynamic_mangas]), str(dynamic_chapters)]))
    update_latest(latest_chapters, current)
    print(Fore.LIGHTGREEN_EX + "Done!" + Fore.RESET)
    #
    # sys.exit(0)


class WebPage(QtWebEngineWidgets.QWebEnginePage):
    # Creates a QtWebEngine to load in JavaScript dependent elements with chapter information
    def __init__(self):
        super(WebPage, self).__init__()
        self.loadFinished.connect(self.handle_load_finished)

    def start(self, urls):
        self._urls = iter(urls)
        self.fetch_next()

    def javaScriptConsoleMessage(self, level, msg, line, sourceID):
        # To suppress error messages in calls of PyQt5 WebEngine
        pass

    def fetch_next(self):
        try:
            url = next(self._urls)
        except StopIteration:
            return False
        else:
            self.load(QtCore.QUrl(url))
        return True

    def process_current_page(self, html):
        global dynamic_run_count, latest_chapters
        drc = dynamic_run_count
        dms = dynamic_mangas

        print(Fore.GREEN + 'Loaded [%d chars] %s' % (len(html), "Dynamically"))
        try:
            soupy = BeautifulSoup(html, 'html.parser')
            tag = soupy.find("li", class_="wp-manga-chapter").a
            chapter_num = num_puller(tag.text)[0]
            dynamic_chapters.append(chapter_num)
            chapter_link = tag.attrs["href"]
            index_ = dynamic_indexes[dynamic_run_count]

            try:
                previous = num_puller(current[index_])[0]
            except IndexError:
                previous = 0

            if previous < chapter_num - 5:
                url_num_loc = chapter_link.find("-", -7) + 1
                chapter_link = chapter_link[:url_num_loc] + f"{previous + 1}/"

            print(Fore.LIGHTYELLOW_EX + f"{dms[drc][0]}: {previous} -> {chapter_num} {Fore.LIGHTBLUE_EX} {chapter_link}")
            dynamic_run_count += 1
        except AttributeError:
            print(f"{Fore.LIGHTRED_EX}Dynamic Website Unable to Load Completely.")
            dynamic_chapters.append(-1)
            dynamic_run_count += 1

        if not self.fetch_next():
            QtWidgets.qApp.quit()

    def handle_load_finished(self):
        self.toHtml(self.process_current_page)


def update_latest(news, olds):
    # Changes the latest chapter read for up-to-date mangas to the last chapter released
    with open("saved/latest.txt", "wt", encoding="utf-8") as latest:
        global dynamic_ch_use

        for old, new in zip_longest(olds, news[:mangas_len]):
            if old is None:
                latest.write(f"0 yts\n")
            else:
                label = old.split()[1]
                if label == "wip" or label == "yts" or new == -1:
                    latest.write(old)
                elif label == "utd" and new != "9999":
                    latest.write(f"{new} utd\n")
                else:
                    try:
                        # Spot fix for utd dynamic websites
                        dynamic_chapter = dynamic_chapters[dynamic_ch_use]
                        if dynamic_chapter == -1:
                            raise IndexError
                        latest.write(f"{dynamic_chapter} utd\n")
                    except IndexError:
                        latest.write(old)

            if new == "9999":
                dynamic_ch_use += 1

    # latest.txt abbreviations: utd = up to date, wip = work in progress, yts = yet to start
    return None


# Doesn't quite belong in any section. An incredibly useful tool sprinkled in different functions.
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
    return numbers


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


def set_changes():
    global mangas, current
    # Sets the mangas and current lists to the recent adjustments in case of subsequent calls to a, n, or s
    with open("saved/list.txt", "rt", encoding="utf-8") as new_list:
        mangas = [line.split("|") for line in new_list.readlines()]
    with open("saved/latest.txt") as new_latest:
        current = new_latest.readlines()


def verify_status(number_file):
    while True:
        status = input(f"\n{Fore.LIGHTWHITE_EX}Which chapter are you on?  {Fore.RESET}"), \
                 input(
                     f"{Fore.LIGHTMAGENTA_EX}Are you yet to start (yts), work in progress (wip), or up to date (utd)?\n" +
                     f"{Fore.LIGHTWHITE_EX}Please enter the corresponding three letter code found in parentheses.  {Fore.RESET}")
        if "" in status:   # status == ("", "") or
            number_file.write(" ".join(["0", "yts"]) + "\n")
            break
        elif status[0].replace(".", "").isnumeric() and status[1] in ["yts", "wip", "utd"]:
            number_file.write(" ".join(status) + "\n")
            break
        else:
            print(f"{Fore.LIGHTRED_EX}Please enter a number for the chapter and one of yts, wip, or utd for the code.  {Fore.RESET}")
    return status


options = {"1": a, "2": n, "3": s, "4": change_current, "5": add, "6": primer, "7": rate}
display_opt = (f"{Back.RESET}1: {Fore.LIGHTCYAN_EX}Show All{Fore.RESET}, 2: {Fore.LIGHTCYAN_EX}Show New{Fore.RESET}, " +
               f"3: {Fore.LIGHTCYAN_EX}Save Results{Fore.RESET}, " +
               f"4: {Fore.LIGHTCYAN_EX}Change Current{Fore.RESET}, 5: {Fore.LIGHTCYAN_EX}Add Manga{Fore.RESET}, " +
               f"6: {Fore.LIGHTCYAN_EX}Primer{Fore.RESET}, 7: {Fore.LIGHTCYAN_EX}Rate{Fore.RESET}, 8: Close  ")
option = input(display_opt)
while option != "8":
    try:
        if not option or option not in options:
            option = input(display_opt)
            continue
        options[option]()
        print("\n")
        option = input(display_opt)
    except requests.exceptions.ConnectionError:
        option = input("Connection to Internet Failed... 8: Close  ")