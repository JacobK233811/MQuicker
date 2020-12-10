from bs4 import BeautifulSoup
from colorama import Fore

# Modules for dynamic JS websites

from PyQt5.QtWebEngineWidgets import QWebEnginePage
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
import sys


def dynamic_finder(url_path):
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
    tag = soupy.a
    output = tag.text

    return output, tag.attrs['href']


print(dynamic_finder("https://www.fb.com"))
print(dynamic_finder("https://www.apple.com"))
print(dynamic_finder("https://www.a.co"))
print(dynamic_finder("https://www.netflix.com"))
print(dynamic_finder("https://www.google.com"))
