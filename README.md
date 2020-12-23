# MangaNewChapter
Stop clicking through endless links to see if there is a new chapter available. This Python script lets you list all your favorite mangas and then checks each one's latest chapter against your most recently read chapter. Currently supports web comics from Mangelo, ReadMng, Zero and Leviatan Scans, Manga Effect, Mankakalot, and MangaDex.

When <a href="#su">setting up for yourself</a>, follow the linked 4 steps.

The current recommended use is to open AnacondaPrompt, create an iPython shell, import the file , and use either the a() function to see all the manga on your list, the n() function to only see manga with new chapters, or the s() function to save results to a .txt file.

<img src="mcheck_ex.png"/>

<a href="https://youtu.be/AyZsZzuTAPg/" target="_blank">For Demo Video Ctrl+Click Here</a>

<h1 id="su">Four Steps to Set Up on Windows</h1>
<ol>
  <li>Download this GitHub Repository by Clicking the Green "Code" Button followed by Download ZIP. Then extract the files to the desired location. </li>
  <li><a href="https://docs.conda.io/en/latest/miniconda.html">Get the 3.8 64-bit Version of Python</a> (use Ctrl+Click for a new tab) for Windows </li>
  <li>Open Anaconda Prompt Program and Navigate the Folder called MangaNewChapter-main by Using <p style="background-color: black; color: white">cd Downloads\MangaNewChapter-main</p> until arrival. Then run <p style="background-color: black; color: white">pip install -r requirements.txt</p> </li>
  <li>Run <p style="background-color: black; color: white">python nc.py</p>. For color, use <p style="background-color: black; color: white">ipython</p> followed by <p style="background-color: black; color: white">import checker</p> and then <p style="background-color: black; color: white">checker.a()</p> </li>
</ol>

<h1 id="su">Four Steps to Set Up on Mac</h1>
<ol>
  <li>Download this GitHub Repository by Clicking the Green "Code" Button followed by Download ZIP. Note the folder location (it is usually Downloads/MangaNewChapter-main). </li>
  <li><a href="https://docs.conda.io/en/latest/miniconda.html">Get the 3.8 64-bit Version of Python from the pkg installer.</a> (use Ctrl+Click for a new tab) for Mac </li>
  <li>Open Terminal Program and Navigate the Folder called MangaNewChapter-main by Using <p style="background-color: black; color: white">cd Downloads\MangaNewChapter-main</p> until arrival. Then run <p style="background-color: black; color: white">pip install -r requirements.txt</p> </li>
  <li>Run <p style="background-color: black; color: white">python nc.py</p>. For color, use <p style="background-color: black; color: white">ipython</p>
</ol>

# Codes

### Status - The main difference between the three lies with automatic aligning of your latest chapter read with the latest released for utd. The other two depend upon Change Current.
<ul>
  <li>utd = up to date</li>
  <li>wip = work in progess</li>
  <li>yts = yet to start</li>
</ul>

### Source - There is a select list of supported manga sites that is continuously growing. Names are case-sensitive.
<ul>
  <li>attackontitanmanga.com -> AoT</li>
  <li>mangelo.com -> Mangelo</li>
  <li>zeroscans.com & leviatanscans.com -> ZeroLeviatan</li>
  <li>mangaeffect.com -> Effect</li>
  <li>readmng.com -> ReadMng</li>
  <li>mangadex.org -> MangaDex</li>
  <li>mangkakalot.com -> Kakalot</li>
  <li>pmscans.com & manhuaplus.com -> WP</li>
  <li>lhtranslation.net -> lh</li>
  <li>asurascans.com -> asura</li>
 </ul>
 
# Function Directory
<ol>
  <li>a() - Shows all manga on your list with the latest chapter released.</li>
  <li>n() - Shows all manga on your list where you have not read the latest chapter released.</li>
  <li>s() - Saves all manga on your list with the latest chapter released to a text file named MM/DD/YY.txt within the saved folder.</li>
  <li>change_current() - Iterates through every manga on your list and lets you change the latest chapter read and status. Easily skip through with the Enter key.</li>
  <li>add() - Add a manga to your list by providing the Name (no requirements), Link (include the https://), Source Code (see Source in Codes above), Current Chapter, and Status Code.</li>
    <li>primer() - Adjusts the initial list.txt file containing which mangas you'd like to track and latest.txt file containing what chapter you are on (both found within the saved folder).</li>
</ol>

