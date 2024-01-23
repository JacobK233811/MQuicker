# Modules for dynamic JS websites
from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets
from PyQt5.QtWebEngineWidgets import QWebEngineView as QWebView
import sys
import os
from colorama import Fore, Back
from datetime import datetime
from itertools import zip_longest
from bs4 import BeautifulSoup

# Pertains to dynamic_finder. The run count is used for indexing within dynamic_finder and dynamic_indexes for insertion
dynamic_run_count = 0
dynamic_happened = False
# The following declarations help properly update_latest for the dynamics
dynamic_ch_use = 0
dynamic_chapters = []
dynamic_sources = ["WP", "asura", "Zero", "MangaDex", "InManga"]


dest_current = []
dest_dynamic_indexes = []

from standard.utils import num_puller
from standard.config import source_elements, source_methods

def finisher(ans, dynamic_mangas, latest_chapters, current, dynamic_indexes, mangas_len):
    
    # Runs dynamic website handling, updates latest.txt, and exits
    global dynamic_happened, dynamic_chapters
    dest_current = current
    dest_dynamic_indexes = dynamic_indexes
        
    # included within scope to allow access to dynamic_mangas variable
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
            global dynamic_run_count
            drc = dynamic_run_count
            dms = dynamic_mangas

            title_of = "unknown"
            print(Fore.GREEN + 'Loaded [%d chars] %s' % (len(html), "Dynamically"))

            try:
                soupy = BeautifulSoup(html, 'html.parser')
                
                title_of = soupy.find("title").text
                elem_clas = lambda src: soupy.find(source_elements[src], class_=source_methods[src]).a

                if "Asura" in title_of:
                    tag = elem_clas("asura")
                elif "InManga" in title_of:
                    tag = elem_clas("InManga")
                    # presently dysfunctional due to slow page load               

                else:
                    tag = soupy.find(source_elements["WP"], class_=source_methods["WP"]).a

                chapter_num = num_puller(tag.text)[0]
                dynamic_chapters.append(chapter_num)
                chapter_link = tag.attrs["href"]
                index_ = dest_dynamic_indexes[dynamic_run_count]

                try:
                    previous = num_puller(dest_current[index_])[0]
                except IndexError:
                    previous = 0

                if previous < chapter_num - 5:
                    url_num_loc = chapter_link.find("-", -7) + 1
                    chapter_link = chapter_link[:url_num_loc] + f"{previous + 1}/"

                print(Fore.LIGHTYELLOW_EX + f"{dms[drc][0]}: {previous} -> {chapter_num} {Fore.LIGHTBLUE_EX} {chapter_link}")
            except AttributeError as e:
                print(f"{Fore.LIGHTRED_EX}Dynamic Website {title_of} Unable to Load Completely Because {e}.")
                dynamic_chapters.append(-1) 
            dynamic_run_count += 1

            if not self.fetch_next():
                QtWidgets.qApp.quit()

        def handle_load_finished(self):
            self.toHtml(self.process_current_page)

    d_urls = [m[1] for m in dynamic_mangas]
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

    print(Fore.LIGHTGREEN_EX + "Updating...")
    # global latest_chapters, current
    if ans == "n":
        dynamic_chapters = dynamic_chapters[::-1]
        latest_chapters = latest_chapters[::-1]
        current = current[::-1]
    elif ans == "s" and dynamic_chapters[-2:] != [-1] * 2:
        with open(f'saved/{datetime.strftime(datetime.now(), "%m%d%y")}.txt', "at", encoding="utf-8") as file_access:
            file_access.write(
                "\n\n".join(['\nDynamics', "\n".join([str(lst) for lst in dynamic_mangas]), str(dynamic_chapters)]))
    update_latest(latest_chapters, dest_current, dynamic_chapters, mangas_len)
    print(Fore.LIGHTGREEN_EX + "Done!" + Fore.RESET)
    
    return dest_current, dest_dynamic_indexes

def update_latest(news, olds, dynamic_chapters, mangas_len):
    # Changes the latest chapter read for up-to-date mangas to the last chapter released
    with open("saved/latest.txt", "wt", encoding="utf-8") as latest:
        global dynamic_ch_use
        for old, new in zip_longest(olds, news[:mangas_len]):
            if old is None:
                latest.write("0 yts\n")
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