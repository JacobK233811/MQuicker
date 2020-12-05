from bs4 import BeautifulSoup
from colorama import Fore

# Modules for dynamic JS websites

from PyQt5.QtWebEngineWidgets import QWebEnginePage
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
import sys


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


def dynamic_finder(url_path, el, cls):
    class Page(QWebEnginePage):
        def __init__(self, url):
            self.app = QApplication(sys.argv)
            QWebEnginePage.__init__(self)
            self.html = ''
            self.loadFinished.connect(self._on_load_finished)
            self.load(QUrl(url))
            self.app.exec_()

        def _on_load_finished(self):
            self.toHtml(self.callable)
            print(Fore.YELLOW + 'Dynamic Load finished')

        def callable(self, html_str):
            self.html = html_str
            self.app.quit()

    page = Page(url_path)
    soupy = BeautifulSoup(page.html, 'html.parser')
    tag = soupy.find(el, class_=cls).a
    output = num_puller(tag.text)[0]

    return output, tag.attrs['href']


print(dynamic_finder("https://manhuaplus.com/manga/apotheosis/#", 'li', 'wp-manga-chapter'))
print(dynamic_finder("https://manhuaplus.com/manga/apotheosis/#", 'li', 'wp-manga-chapter'))
