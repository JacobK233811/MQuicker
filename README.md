# MangaNewChapter
Stop clicking through endless links to see if there is a new chapter available. This Python script lets you list all your favorite mangas and then checks each one's latest chapter against your most recently read chapter. Currently supports web comics from Mangelo, ReadMng, Zero and Leviatan Scans, Manga Effect, Mankakalot, and MangaDex.

When <a href="#su">setting up for yourself</a>, download the repository as a zip file, extract it, follow instructions in installation.txt, and change the contents of the mangas lists with primer(), add(), and change_current(). Keep in mind which sources are supported.

The current recommended use is to open AnacondaPrompt, create an iPython shell, import the file , and use either the a() function to see all the manga on your list, the n() function to only see manga with new chapters, or the s() function to save results to a .txt file.

<img src="mcheck_ex.png"/>

<a href="https://youtu.be/AyZsZzuTAPg/" target="_blank">For Demo Video Ctrl+Click Here</a>

<h1 id="su">Four Steps to Set Up</h1>
<ol>
  <li>Download this GitHub Repository by Clicking the Green "Code" Button followed by Download ZIP. Then extract the files to the desired location. </li>
  <li><a href="https://docs.conda.io/en/latest/miniconda.html">Get the Latest Version of Python</a> (use Ctrl+Click for a new tab) for your Operating System </li>
  <li>Open Anaconda Prompt and Navigate the Folder called MangaNewChapter-main by Using cd folder1\folder2 until arrival. Then run "pip install -r requirements.txt" </li>
  <li>Run "python nc.py". For color, use "ipython" followed by "import checker" and then "checker.a()" </li>
</ol>
# Codes
+Status - The main difference between the three lies with automatic aligning of your latest chapter read with the latest released for utd. The other two depend upon Change Current.
  -utd = up to date
  -wip = work in progess
  -yts = yet to start
+Source - There is a select list of supported manga sites that is continuously growing. Names are case-sensitive.
  -attackontitanmanga.com -> AoT
  -mangelo.com -> Mangelo
  -zeroscans.com & leviatanscans.com -> ZeroLeviatan
  -mangaeffect.com -> Effect
  -readmng.com -> ReadMng
  -mangadex.org -> MangaDex
  -mangkakalot.com -> Kakalot
  -pmscans.com & manhuaplus.com -> WP
  -lhtranslation.net -> lh
  -asurascans.com -> asura
# Function Directory
<ul>
  <li>primer() - Adjusts the initial list.txt file containing which mangas you'd like to track and latest.txt file containing what chapter you are on.</li>
  <li>change_current() - Iterates through every manga on your list and lets you change the latest chapter read and status. Easily skip through with the Enter key.</li>
  <li>add() - Add a manga to your list by providing the Name (no requirements), Link (include the https://), Source Code (see Source in Codes above), Current Chapter, and Status Code.</li>
  <li>a() - Shows all manga on your list with the latest chapter released.</li>
  <li>n() - Shows all manga on your list where you have not read the latest chapter released.</li>
  <li>s() - Saves all manga on your list with the latest chapter released to a text file named MM/DD/YY.txt within the saved folder.</li>
