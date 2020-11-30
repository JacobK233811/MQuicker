from bs4 import BeautifulSoup
import requests
from colorama import Fore
from collections import defaultdict
from datetime import datetime
from itertools import zip_longest

# Official source names are:
# attackontitanmanga.com -> AoT
# mangelo.com -> Mangelo
# zeroscans.com & leviatanscans.com -> ZeroLeviatan
# mangaeffect.com -> Effect
# manhuaplus.com -> Plus (DME), Plus2 (Apo), Plus3 (YZ)
# readmng.com -> ReadMng
# mangadex.org -> MangaDex
# mangkakalot.com -> Kakalot


# Each list within the mangas list has the following parameters: Name, Link, Source, Latest Chapter Read
mangas = [['Attack on Titan', 'https://attackontitanmanga.com/', 'AoT'],
          ['Solo Leveling', 'https://manganelo.com/manga/pn918005', 'Mangelo'],
          ['Tales of Demons and Gods', 'https://manganelo.com/manga/hyer5231574354229', 'Mangelo'],
          ['The Great Mage Returns After 4000 Years', 'https://manganelo.com/manga/go922760', 'Mangelo'],
          ['Second Life Ranker', 'https://zeroscans.com/comics/188504-second-life-ranker', 'ZeroLeviatan'],
          ['I am the Sorcerer King', 'https://leviatanscans.com/comics/i-am-the-sorcerer-king', 'ZeroLeviatan'],
          ['Descent of the Demonic Master', 'https://mangaeffect.com/manga/the-descent-of-the-demonic-master/', 'Effect'],
          ['Chronicles of Heavenly Demon', 'https://www.readmng.com/chronicles-of-heavenly-demon-3', 'ReadMng'],
          ['Iruma-Kun', 'https://www.readmng.com/mairimashita-iruma-kun', 'ReadMng'],
          ['Kingdom', 'https://www.readmng.com/kingdom', 'ReadMng'],
          ['Solo Auto Hunting', 'https://mangaeffect.com/manga/solo-auto-hunting/', 'Effect'],
          ["The Scholar's Reincarnation", 'https://www.readmng.com/the-scholars-reincarnation', 'ReadMng'],
          ["LESSA - Servant of Cosmos", 'https://mangakakalot.com/read-qu0ei158524508422', 'Kakalot'],
          ["Demon Magic Emperor", 'https://mangadex.org/title/43692/demonic-emperor', 'MangaDex'],
          ["Leveling Up, by Only Eating!", 'https://mangadex.org/title/48217/leveling-up-by-only-eating', 'MangaDex'],
          ["Apothesis", "https://mangadex.org/title/23001/apotheosis-ascension-to-godhood", "MangaDex"],
          ["Yuan Zun", "https://mangakakalot.tv/manga/yuan_zun", "Kakalot"],
          ["Martial Peak", "https://manganelo.com/manga/martial_peak", "Mangelo"],
          ["Legendary Moonlight Sculptor", "https://www.readmng.com/Dalbic-Jogaksa-2/", "ReadMng"]
          ]
"""
with open("saved/latest.txt", "wt", encoding="utf-8") as f:
  for manga in checker.mangas:
    f.write(str(manga[3]) + ' utd' + '\n')
  
Run the above in iPython to initialize the new latest chapter system if still using the old manga[3] one
  """

# On most sites the desired element will be an anchor 'a' tag. However, this default dict allows us to specify exceptions
source_elements = defaultdict(lambda: 'a')
source_elements['ZeroLeviatan'] = 'span'
source_elements['ReadMng'] = 'span'
source_elements['Effect'] = 'li'
source_elements['Kakalot'] = 'div'

# Now the i_or_cls parameter of finder comes from this neat dictionary
# Now the i_or_cls parameter of finder comes from this neat dictionary
source_methods = {'AoT': 9, 'Mangelo': 'chapter-name text-nowrap', 'ZeroLeviatan': 'text-muted text-sm',
                  'Effect': 'wp-manga-chapter', 'ReadMng': 'val',
                  'MangaDex': 'text-truncate', 'Kakalot': 'chapter-list'}


# The i_or_cls parameter defined in source_methods will decide whether to find by index or class
# This process will use the typing of that same item to do so
def finder(not_parsed, el, i_or_cls):
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
    numbers = num_puller(tag.text)
    if numbers:
        output = str(numbers[0])
    else:
        output = "0"

    # Posting the link directly to the chapter if possible, and to the chapter list if not
    if el == 'a':
        return output, tag.attrs['href']
    return output, not_parsed.url


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


def manga_strip(manga):
    # Pulling all the necessary info out of the manga list for quick reference
    source_url = manga[1]
    element = source_elements[manga[2]]
    method = source_methods[manga[2]]
    webpage = requests.get(source_url)

    # Finder function enables one line to check any new properly defined list item (see line 16 comment)
    latest_chapter, link = finder(webpage, element, method)
    if link[:8] != "https://":
        link = source_url + link
    latest_chapter = psych_handler(latest_chapter, link, manga[2])
    # In case it is a local reference to the chapter page (as with MangaDex)
    return latest_chapter, link


def psych_handler(lc, lk, source):
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
            if ch_soup.find("div", {"class": "col-2 col-lg-1 ml-1 text-right text-truncate order-lg-8 text-warning"}).text.strip()[:2] == "in":
                ch -= 1
        except AttributeError:
            pass
    return str(ch)


def update_latest(news, olds):
    with open("saved/latest.txt", "wt", encoding="utf-8") as latest:
        for old, new in zip_longest(olds, news):
            if old is None:
                latest.write(f"0 yts\n")
            else:
                label = old.split()[1]
                if label == "utd":
                    latest.write(f"{new} utd\n")
                elif label == "wip" or label == "yts":
                    latest.write(old)

    # latest.txt abbreviations: utd = up to date, wip = work in progress, yts = yet to start
    return None


# def wip_link_switch(manga, chapter):
#     source_url = manga[1]
#     element = source_elements[manga[2]]
#     method = source_methods[manga[2]]
#     webpage = requests.get(source_url)
#     soup = BeautifulSoup(webpage.content, 'html.parser')
#
#     # try:
#     try:
#         link = soup.find(element, class_=method).find("a", title=f" {manga[0]}: Chapter: {chapter}")
#     except AttributeError:
#         link = soup.find(element, class_=method, title=f"{manga[0]}: Chapter: {chapter}")
#
#     if link[:8] != "https://":
#         link = source_url + link
#     # except Exception:
#
#     return link


def a():
    latest_chapters = []
    for i, manga in enumerate(mangas):
        latest, link = manga_strip(manga)
        latest_chapters.append(latest)
        with open("saved/latest.txt") as f:
            current = f.readlines()
        try:
            previous = num_puller(current[i])[0]
        except IndexError:
            previous = 0
        # The below if-else statement changes the color of the output when the latest chapter is greater than the latest read
        # If intending to access file through CLI w/o iPython, change color to "NEW " for the ~if~ and "" for the ~else~
        if float(latest) > previous:
            color = Fore.LIGHTYELLOW_EX
            # The placeholder enables the feature of only showing links for items with a new chapter
            if current[i].split()[1] != "wip":
                link_placeholder = link
            else:
                # link_placeholder = wip_link_switch(manga, previous)
                link_placeholder = manga[1]
        else:
            color = Fore.LIGHTBLUE_EX
            link_placeholder = ""
        print(color + f"{manga[0]}: {previous} -> {latest} {Fore.CYAN} {link_placeholder}")
    print(Fore.LIGHTGREEN_EX + "Updating...")
    update_latest(latest_chapters, current)
    print(Fore.GREEN + "Done!")


def n():
    latest_chapters = []
    for i, manga in enumerate(mangas[::-1]):
        latest, link = manga_strip(manga)
        latest_chapters.append(latest)
        with open("saved/latest.txt") as f:
            current = f.readlines()[::-1]
        try:
            previous = num_puller(current[i])[0]
        except IndexError:
            previous = 0
        # Only renders if there is a new chapter
        if float(latest) > previous:
            if current[i].split()[1] == "wip":
                link = manga[1]
            print(Fore.LIGHTMAGENTA_EX + f"{manga[0]}: {previous} -> {latest} Copy to see it:{Fore.CYAN} {link}")
        elif i % 5 == 0:
            print(Fore.LIGHTGREEN_EX + "Loading...")
    print(Fore.LIGHTGREEN_EX + "Updating...")
    update_latest(latest_chapters[::-1], current[::-1])
    print(Fore.GREEN + "Done!")


def s():
    latest_chapters = []
    with open(f'saved/{datetime.strftime(datetime.now(), "%m%d%y")}.txt', "wt", encoding="utf-8") as f:
        for i, manga in enumerate(mangas):
            latest, link = manga_strip(manga)
            latest_chapters.append(latest)
            with open("saved/latest.txt") as file:
                current = file.readlines()
            try:
                previous = num_puller(current[i])[0]
            except IndexError:
                previous = 0
            # The below if-else statement adds NEW to the output when the latest chapter is greater than the latest read
            if float(latest) > previous:
                if current[i].split()[1] == "wip":
                    link = manga[1]
                color = "NEW "
                # The placeholder enables the feature of only showing links for items with a new chapter
                link_placeholder = " + Link: " + link
            else:
                color = ""
                link_placeholder = ""
            f.write(color + f"{manga[0]}: {previous} -> {latest}{link_placeholder}\n\n")
            if i % 4 == 0:
                print(Fore.LIGHTGREEN_EX + "Loading...")
    print(Fore.LIGHTGREEN_EX + "Updating...")
    update_latest(latest_chapters, current)
    print(Fore.GREEN + "Done!")
