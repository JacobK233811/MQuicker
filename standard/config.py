from collections import defaultdict

mangas = []

# On most sites the desired element will be an anchor 'a' tag. However, this default dict allows us to specify exceptions
source_elements = defaultdict(lambda: 'a')
source_elements['WP'], source_elements["MR"] = ['li'] * 2
source_elements['Kakalot'], source_elements['asura'], source_elements['Zero'] = ['div'] * 3
source_elements['ManhuaScan'], source_elements['MangaDex'] = ['span'] * 2



# Now the i_or_cls parameter of finder comes from this neat dictionary. Preference toward classes intentionally
source_methods = {'Mangelo': 'chapter-name text-nowrap',
                  'ReadMng': 'chnumber', 'WP': 'wp-manga-chapter',
                  'MR': 'wp-manga-chapter',
                  'Kakalot': 'chapter-list', "lh": "chapter",
                  "asura": "eph-num", "Zero": "col-md-6 col-12",
                  "ManhuaScan": "title", "MangaDex": "chapter-link",
                  "InManga": "list-group-item custom-list-group-item "}

# For later use in the update_latest function
latest_chapters = []
# Current also features throughout for comparison purposes
with open("saved/latest.txt") as f:
    current = f.readlines()

dynamic_sources = ["WP", "asura", "Zero", "MangaDex", "InManga"]
# Live Datastores
dynamic_mangas = []
dynamic_indexes = []
