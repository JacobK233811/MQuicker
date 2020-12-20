# MangaNewChapter
Stop clicking through endless links to see if there is a new chapter available. This Python script lets you list all your favorite mangas and then checks each one's latest chapter against your most recently read chapter. Currently supports web comics from Mangelo, ReadMng, Zero and Leviatan Scans, Manga Effect, Mankakalot, and MangaDex.

When <a href="#su">setting up for yourself</a>, download the repository as a zip file, extract it, follow instructions in installation.txt, and change the contents of the mangas lists with primer(), add(), and change_current(). Keep in mind which sources are supported.

The current recommended use is to open AnacondaPrompt, create an iPython shell, import the file , and use either the a() function to see all the manga on your list, the n() function to only see manga with new chapters, or the s() function to save results to a .txt file.

<img src="mcheck_ex.png"/>

<a href="https://youtu.be/AyZsZzuTAPg/" target="_blank">For Demo Video Click Here</a>

<h1 id="su">Four Steps to Set Up</h1>
<ol>
  <li>Download this GitUp Repository by Clicking the Green "Code" Button followed by Download Zip. Then extract the files to the desired location. </li>
  <li><a href="https://docs.conda.io/en/latest/miniconda.html">Get the Latest Version of Python</a> for your Operating System </li>
  <li>Open Anaconda Prompt and Navigate the Folder called MangaNewChapter-main by Using cd folder1\folder2 until arrival. Then run "pip install -r requirements.txt" </li>
  <li>Run "python nc.py". For color, use "ipython" followed by "import checker" and then "checker.a()" </li>
</ol>
