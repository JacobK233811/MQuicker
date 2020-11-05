# MangaNewChapter
Stop clicking through endless links to see if there is a new chapter available. This Python script lets you list all your favorite mangas and then checks each one's latest chapter against your most recently read chapter. Currently supports web comics from Mangelo, ReadMng, Zero and Leviatan Scans, Manga Effect, ManhuaPlus, and MangaDex.

Currently searching for a full-stack Django collaborator to help me put it onto the web. Let me know by following if interested.

When setting up for yourself, change the contents of the mangas list of lists to lists with the format \[Name:str, Link:str, Source:str, LatestChapterRead:int\]. Keep in mind which sources are supported and update LatestChapterRead as needed.

The current recommended use is to open AnacondaPrompt, open an iPython shell, import the file (I recommend a short name like mcheck.py), and use either the a() function to see all the manga on your list or the n() function to only see manga with new chapters.

<img src="mcheck_ex.png"/>

<video src="demo.mp4/" controls>Failed to load demo video</video>
