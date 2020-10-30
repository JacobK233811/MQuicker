from bs4 import BeautifulSoup
import requests
from colorama import Fore
from collections import defaultdict
from time import sleep


# Each list within the mangas list has the following parameters: Name, Link, Source, Latest Chapter Read
mangas = [['Attack on Titan', 'https://attackontitanmanga.com/', 'AoT', 134],
          ['Solo Leveling', 'https://manganelo.com/manga/pn918005', 'Mangelo', 125],
          ['Tales of Demons and Gods', 'https://manganelo.com/manga/hyer5231574354229', 'Mangelo', 299.1],
          ['The Great Mage Returns After 4000 Years', 'https://manganelo.com/manga/go922760', 'Mangelo', 55],
          ['Second Life Ranker', 'https://zeroscans.com/comics/188504-second-life-ranker', 'ZeroLeviatan', 68],
          ['I am the Sorcerer King', 'https://leviatanscans.com/comics/i-am-the-sorcerer-king', 'ZeroLeviatan', 114],
          ['Descent of the Demonic Master', 'https://mangaeffect.com/manga/the-descent-of-the-demonic-master/', 'Effect', 71],
          ['Chronicles of Heavenly Demon', 'https://www.readmng.com/chronicles-of-heavenly-demon-3', 'ReadMng', 118],
          ['Iruma-Kun', 'https://www.readmng.com/mairimashita-iruma-kun', 'ReadMng', 166],
          ['Kingdom', 'https://www.readmng.com/kingdom', 'ReadMng', 658],
          ['Solo Auto Hunting', 'https://mangaeffect.com/manga/solo-auto-hunting/', 'Effect', 48],
          ["The Scholar's Reincarnation", 'https://www.readmng.com/the-scholars-reincarnation', 'ReadMng', 3],
          ]

# On most sites the desired element will be an anchor 'a' tag. However, this default dict allows us to specify exceptions
source_elements = defaultdict(lambda: 'a')
source_elements['ZeroLeviatan'] = 'span'
source_elements['ReadMng'] = 'span'

# Now the i_or_cls parameter of finder comes from this neat dictionary
source_methods = {'AoT': 9, 'Mangelo': 'chapter-name text-nowrap', 'ZeroLeviatan': 'text-muted text-sm',
                  'Effect': 113, 'ReadMng': 'val'}


# The i_or_cls parameter defined in source_methods will decide whether to find by index or class
# This process will use the typing of that same item to do so
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


def a():
    for manga in mangas:
        webpage = requests.get(manga[1])
        soup = BeautifulSoup(webpage.content, 'html.parser')
        # Finder function enables one line to check any new properly defined list item (see line 6 comment)
        latest_chapter = finder(soup, source_elements[manga[2]], source_methods[manga[2]])
        # The below if-else statement changes the color of the output when the latest chapter is greater than the latest read
        # If intending to access file through CLI, change color to "NEW " for the ~if~ and "" for the ~else~
        if float(latest_chapter) > manga[3]:
            color = Fore.LIGHTYELLOW_EX
            link = manga[1]
        else:
            color = Fore.LIGHTBLUE_EX
            link = ""
        print(color + f"{manga[0]}: {manga[3]} -> {latest_chapter} {link}")


def n():
    # Finder function enables one line to check any new properly defined list item (see line 7 comment)
    print("Please be patient as your chapters load.")
    newest_chapters = [[finder(BeautifulSoup(requests.get(manga[1]).content, 'html.parser'), source_elements[manga[2]],
                               source_methods[manga[2]]), manga[0], manga[3], manga[1]] for manga in mangas
                       if float(finder(BeautifulSoup(requests.get(manga[1]).content, 'html.parser'), source_elements[manga[2]],
                                       source_methods[manga[2]])) > manga[3]]
    for chapter_info in newest_chapters:
        # Remove coloring for CLI use
        print(Fore.LIGHTGREEN_EX + f"{chapter_info[1]}: {chapter_info[2]} -> {chapter_info[0]} Click here to see it: {chapter_info[3]}")
        sleep(0.75)


if input("All or New? (a/n) ") == 'n':
    n()
else:
    a()
