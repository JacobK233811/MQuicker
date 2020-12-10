import requests     # to get image from the web
import shutil   # to save it locally
from bs4 import BeautifulSoup
from os import mkdir

try:
    mkdir("images")
except FileExistsError:
    pass

start = int(input("Input your current chapter  "))
total = int(input("Input how many chapters you wish to download  "))

for n in range(start, start+total):
    webpage = requests.get(f"https://w3.sololeveling.net/manga/solo-leveling-chapter-{n}/")
    soup = BeautifulSoup(webpage.content, 'html.parser')

    # container = soup.find("div", class_="container")
    # print(container.prettify())
    image_list = soup.findAll("img")

    directory = "solo" + str(n)
    mkdir(f"images/{directory}")

    for i, img in enumerate(image_list):
        a = img.attrs
        # Set up the image URL and filename
        image_url = a["src"]
        filename = "page_" + str(i)

        # Open the url image, set stream to True, this will return the stream content.
        r = requests.get(image_url, stream=True)

        # Check if the image was retrieved successfully
        if r.status_code == 200:
            # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
            r.raw.decode_content = True

            # Open a local file with wb ( write binary ) permission.
            with open(f"images/{directory}/{filename}", 'wb') as f:
                shutil.copyfileobj(r.raw, f)

            print('Image sucessfully Downloaded: ', filename)
        else:
            print('Image Couldn\'t be retreived')
