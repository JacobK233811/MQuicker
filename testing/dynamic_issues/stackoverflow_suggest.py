import sys
from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets
from bs4 import BeautifulSoup


class WebPage(QtWebEngineWidgets.QWebEnginePage):
    def __init__(self):
        super(WebPage, self).__init__()
        self.loadFinished.connect(self.handle_load_finished)

    def start(self, urls):
        self._urls = iter(urls)
        self.fetch_next()

    def fetch_next(self):
        try:
            url = next(self._urls)
        except StopIteration:
            return False
        else:
            self.load(QtCore.QUrl(url))
        return True

    def process_current_page(self, html):
        print('Loaded [%d chars] %s' % (len(html), "Dynamically"))
        soupy = BeautifulSoup(html, 'html.parser')
        tag = soupy.find("li", class_="wp-manga-chapter").a
        print(tag.text)
        if not self.fetch_next():
            QtWidgets.qApp.quit()

    def handle_load_finished(self):
        self.toHtml(self.process_current_page)
        # soupy = BeautifulSoup(self.html, "html.parser")
        # print(soupy.find("li", class_="wp-manga-chapter").a)


urls = ["https://manhuaplus.com/manga/apotheosis/#", "https://www.pmscans.com/manga/leveling-up-by-only-eating/"]
app = QtWidgets.QApplication(sys.argv)
webpage = WebPage()
webpage.start(urls)
sys.exit(app.exec_())
