from bs4 import BeautifulSoup
import requests
from colorama import Fore
from collections import defaultdict

# Official source names are:
# attackontitanmanga.com -> AoT
# mangelo.com -> Mangelo
# zeroscans.com & leviatanscans.com -> ZeroLeviatan
# mangaeffect.com -> Effect
# manhuaplus.com -> Plus
# readmng.com -> ReadMng
# mangadex.org -> MangaDex
# mangkakalot.com -> Kakalot


# Each list within the mangas list has the following parameters: Name, Link, Source, Latest Chapter Read
mangas = [['Attack on Titan', 'https://attackontitanmanga.com/', 'AoT', 134],
          ['Solo Leveling', 'https://manganelo.com/manga/pn918005', 'Mangelo', 127],
          ['Tales of Demons and Gods', 'https://manganelo.com/manga/hyer5231574354229', 'Mangelo', 302.5],
          ['The Great Mage Returns After 4000 Years', 'https://manganelo.com/manga/go922760', 'Mangelo', 58],
          ['Second Life Ranker', 'https://zeroscans.com/comics/188504-second-life-ranker', 'ZeroLeviatan', 68],
          ['I am the Sorcerer King', 'https://leviatanscans.com/comics/i-am-the-sorcerer-king', 'ZeroLeviatan', 117],
          ['Descent of the Demonic Master', 'https://mangaeffect.com/manga/the-descent-of-the-demonic-master/', 'Effect', 74],
          ['Chronicles of Heavenly Demon', 'https://www.readmng.com/chronicles-of-heavenly-demon-3', 'ReadMng', 121],
          ['Iruma-Kun', 'https://www.readmng.com/mairimashita-iruma-kun', 'ReadMng', 174],
          ['Kingdom', 'https://www.readmng.com/kingdom', 'ReadMng', 661],
          ['Solo Auto Hunting', 'https://mangaeffect.com/manga/solo-auto-hunting/', 'Effect', 49],
          ["The Scholar's Reincarnation", 'https://www.readmng.com/the-scholars-reincarnation', 'ReadMng', 149],
          ["Lessa", 'https://mangakakalot.com/read-qu0ei158524508422', 'Kakalot', 0],
          ["Demon Magic Emperor", 'https://manhuaplus.com/manga/demon-magic-emperor/', 'Plus', 142],
          ["Leveling Up, by Only Eating!", 'https://mangadex.org/title/48217/leveling-up-by-only-eating', 'MangaDex', 45],
          ]

# On most sites the desired element will be an anchor 'a' tag. However, this default dict allows us to specify exceptions
source_elements = defaultdict(lambda: 'a')
source_elements['ZeroLeviatan'] = 'span'
source_elements['ReadMng'] = 'span'

# Now the i_or_cls parameter of finder comes from this neat dictionary
# Now the i_or_cls parameter of finder comes from this neat dictionary
source_methods = {'AoT': 9, 'Mangelo': 'chapter-name text-nowrap', 'ZeroLeviatan': 'text-muted text-sm',
                  'Effect': 113, 'ReadMng': 'val', 'Plus': 102, 'MangaDex': 'text-truncate', 'Kakalot': 63}


# The i_or_cls parameter defined in source_methods will decide whether to find by index or class
# This process will use the typing of that same item to do so
def finder(not_parsed, el, i_or_cls):
    parsed = BeautifulSoup(not_parsed.content, 'html.parser')
    typ = type(i_or_cls)
    # If the source_methods dictionary a class, typ will have str type.
    # If the same dictionary holds index, typ will have int type
    if typ is str:
        tag = parsed.find(el, {'class': i_or_cls})
    elif typ is int:
        tag = parsed.findAll(el)[i_or_cls]
    else:
        tag = 'Error'

    # Iterates over all words to find the chapter number and saves that number as an int if possible and if not, a float
    numbers = []
    for word in tag.text.split():
        word = word.replace(":", "")
        try:
            numbers.append(int(word.strip()))
        except ValueError:
            try:
                numbers.append(float(word.strip()))
            except ValueError:
                pass
    if numbers:
        output = str(numbers[0])
    else:
        output = "0"

    # Posting the link directly to the chapter if possible, and to the chapter list if not
    if el == 'a':
        return output, tag.attrs['href']
    return output, not_parsed.url


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
        if ch_soup.find("div", {"class": "col-2 col-lg-1 ml-1 text-right text-truncate order-lg-8 text-warning"}).text.strip()[:2] == "in":
            ch -= 1
    return str(ch)


def a():
    for manga in mangas:
        latest_chapter, link = manga_strip(manga)
        # The below if-else statement changes the color of the output when the latest chapter is greater than the latest read
        # If intending to access file through CLI w/o iPython, change color to "NEW " for the ~if~ and "" for the ~else~
        if float(latest_chapter) > manga[3]:
            color = Fore.LIGHTYELLOW_EX
            # The placeholder enables the feature of only showing links for items with a new chapter
            link_placeholder = link
        else:
            color = Fore.LIGHTBLUE_EX
            link_placeholder = ""
        print(color + f"{manga[0]}: {manga[3]} -> {latest_chapter} {Fore.CYAN} {link_placeholder}")


def n():
    for manga in mangas[::-1]:
        latest_chapter, link = manga_strip(manga)
        # Only renders if there is a new chapter
        if float(latest_chapter) > manga[3]:
            print(Fore.LIGHTMAGENTA_EX + f"{manga[0]}: {manga[3]} -> {latest_chapter} Copy to see it:{Fore.CYAN} {link}")
