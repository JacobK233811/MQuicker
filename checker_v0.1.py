from bs4 import BeautifulSoup
import requests
from colorama import Fore

mangas = [['Attack on Titan', 'https://attackontitanmanga.com/', 'AoT', 134.0],
          ['Solo Leveling', 'https://manganelo.com/manga/pn918005', 'Mangelo', 125.0],
          ['Tales of Demons and Gods', 'https://manganelo.com/manga/hyer5231574354229', 'Mangelo', 299.1],
          ['The Great Mage Returns After 4000 Years', 'https://manganelo.com/manga/go922760', 'Mangelo', 55.0],
          ['Second Life Ranker', 'https://zeroscans.com/comics/188504-second-life-ranker', 'ZeroLeviatan', 68.0],
          ['I am the Sorcerer King', 'https://leviatanscans.com/comics/i-am-the-sorcerer-king', 'ZeroLeviatan', 114.0],
          ['Descent of the Demonic Master', 'https://mangaeffect.com/manga/the-descent-of-the-demonic-master/', 'Effect', 71.0],
          ['Chronicles of Heavenly Demon', 'https://www.readmng.com/chronicles-of-heavenly-demon-3', 'ReadMng', 118.0],
          ['Iruma-Kun', 'https://www.readmng.com/mairimashita-iruma-kun', 'ReadMng', 166.0],
          ['Kingdom', 'https://www.readmng.com/kingdom', 'ReadMng', 658.0],
          ['Solo Auto Hunting', 'https://mangaeffect.com/manga/solo-auto-hunting/', 'Effect', 48.0],
          ["The Scholar's Reincarnation", 'https://www.readmng.com/the-scholars-reincarnation', 'ReadMng', 3.0],
          ]

for manga in mangas:
    webpage = requests.get(manga[1])
    soup = BeautifulSoup(webpage.content, 'html.parser')
    if manga[2] == "Mangelo":
        latest_chapter = soup.find('a', {'class': 'chapter-name text-nowrap'}).text.split()[-1]
    elif manga[2] == "AoT":
        latest_chapter = soup.findAll('a')[9].text.split()[-1]
    elif manga[2] == "ZeroLeviatan":
        latest_chapter = soup.find('span', {'class': 'text-muted text-sm'}).text.strip()
    elif manga[2] == "Effect":
        latest_chapter = soup.findAll('a')[113].text.split()[-1]
    elif manga[2] == "ReadMng":
        latest_chapter = soup.find('span', {'class': 'val'}).text.split()[-1]
    # If intending to access file through CLI, change color to "NEW " for the ~if~ and "" for the ~else~
    if float(latest_chapter) > manga[3]:
        color = Fore.LIGHTYELLOW_EX
    else:
        color = Fore.LIGHTBLUE_EX
    print(color + f"{manga[0]}: {float(latest_chapter)} <- {manga[-1]}")






