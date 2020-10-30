from bs4 import BeautifulSoup
import requests
from colorama import Fore


# Each list within the mangas list has the following parameters: Name, Link, Source, Latest Chapter Read, Element, Index or Class
mangas = [['Attack on Titan', 'https://attackontitanmanga.com/', 'AoT', 134, 'a', 9],
          ['Solo Leveling', 'https://manganelo.com/manga/pn918005', 'Mangelo', 125, 'a', 'chapter-name text-nowrap'],
          ['Tales of Demons and Gods', 'https://manganelo.com/manga/hyer5231574354229', 'Mangelo', 299.1, 'a', 'chapter-name text-nowrap'],
          ['The Great Mage Returns After 4000 Years', 'https://manganelo.com/manga/go922760', 'Mangelo', 55, 'a', 'chapter-name text-nowrap'],
          ['Second Life Ranker', 'https://zeroscans.com/comics/188504-second-life-ranker', 'ZeroLeviatan', 68, 'span', 'text-muted text-sm'],
          ['I am the Sorcerer King', 'https://leviatanscans.com/comics/i-am-the-sorcerer-king', 'ZeroLeviatan', 114, 'span', 'text-muted text-sm'],
          ['Descent of the Demonic Master', 'https://mangaeffect.com/manga/the-descent-of-the-demonic-master/', 'Effect', 71, 'a', 113],
          ['Chronicles of Heavenly Demon', 'https://www.readmng.com/chronicles-of-heavenly-demon-3', 'ReadMng', 118, 'span', 'val'],
          ['Iruma-Kun', 'https://www.readmng.com/mairimashita-iruma-kun', 'ReadMng', 166, 'span', 'val'],
          ['Kingdom', 'https://www.readmng.com/kingdom', 'ReadMng', 658, 'span', 'val'],
          ['Solo Auto Hunting', 'https://mangaeffect.com/manga/solo-auto-hunting/', 'Effect', 48, 'a', 113],
          ["The Scholar's Reincarnation", 'https://www.readmng.com/the-scholars-reincarnation', 'ReadMng', 3, 'span', 'val'],
          ]


# The i_or_cls parameter defined as the last item of a manga list above will decide to find by index or class
# This process will use the typing of that same last item to do so
def finder(parsed, el, i_or_cls):
    typ = type(i_or_cls)
    # If the user inputted a class, typ will have str type. If the user inputted an index, typ will have int type
    if typ is str:
        tag = parsed.find(el, {'class': i_or_cls})
    elif typ is int:
        tag = parsed.findAll(el)[i_or_cls]
    else:
        tag = 'Error'
    return tag.text.split()[-1]


for manga in mangas:
    webpage = requests.get(manga[1])
    soup = BeautifulSoup(webpage.content, 'html.parser')
    # Finder function enables one line to check any new properly defined list item (see line 6 comment)
    latest_chapter = finder(soup, manga[4], manga[5])
    # The below if-else statement changes the color of the output when the latest chapter is greater than the latest read
    # If intending to access file through CLI, change color to "NEW " for the ~if~ and "" for the ~else~
    if float(latest_chapter) > manga[3]:
        color = Fore.LIGHTYELLOW_EX
    else:
        color = Fore.LIGHTBLUE_EX
    print(color + f"{manga[0]}: {latest_chapter} <- {manga[3]}")
