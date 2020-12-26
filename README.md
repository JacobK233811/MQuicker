# MangaNewChapter
Stop clicking through endless links to see if there is a new chapter available. This Python script lets you list all your favorite mangas and then checks each one's latest chapter against your most recently read chapter. Currently supports web comics from Mangelo, ReadMng, Zero and Leviatan Scans, Manga Effect, Mankakalot, MangaDex, LHTranslation, and Asura Scans.

When <a href="#su">setting up for yourself</a>, follow the linked 4 steps.

Windows Users who use the Two-Step Powershell Install can run in one click! Mac Users should go through the Four-Step Install and then navigate to the MangaNewChapter-main folder within terminal with <em>cd \<other folders\>/MangaNewChapter-main</em>. Then they can run <em>python3 checker.py</em>. Two-Step Install for Mac needs further testings, but is available <a href="#2m">here</a>.

<img src="mcheck_ex.png"/>

<a href="https://youtu.be/AyZsZzuTAPg/" target="_blank">For Demo Video Ctrl+Click Here</a>

<h1 id="su">Two Step Windows Set Up</h1>
Note: It is highly recommended to use Ctrl+Click to open each of these in a new tab and then copy their contents into Windows Powershell program on your computer.
<ol>
  <a href="setup.ps1"><li>Download the ZIP file and Miniconda</li></a>
  <a href="setup2.ps1"><li>Install required packages and run the file</li></a>
  Note: During the second step, several Python windows will open and then close one-by-one. Please do not be alarmed by this as it is a normal part of set up.
</ol>
<a href="launch.ps1">After setting up in this way, you can click here whenever you'd like to look for new chapters, or just find the launch.ps1 file on your computer :)</a> <p>Also, a shortcut to this program called "MQuicker - For Windows Desktop" is included within C:\Extracts\MQuicker.
I recommend moving it to your Desktop, and <a href="https://www.top-password.com/blog/set-ps1-script-to-open-with-powershell-by-default/">setting PowerShell as the default program to open .ps1</a> by right clicking the icon, selecting Open With -> Choose Another App -> Always Use this App to Open .ps1 Files -> More Apps -> Look for an App on Your PC and then find and choose powershell.exe to easily access MQuicker from the Desktop.
(I found Powershell in C:\Windows\System32\WindowsPowerShell\v1.0) Alternatively, right click the shortcut and select "Run with Powershell"</p>


<h1>Four Step Set Up on Mac</h1>
<ol>
  <li>Download this GitHub Repository by <a href="https://github.com/JacobK233811/MangaNewChapter/archive/main.zip">Clicking the Green "Code" Button followed by Download ZIP</a>. Note the folder location (it is usually Downloads/MangaNewChapter-main). </li>
  <li><a href="https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.pkg">Get the 3.8 64-bit Version of Python from the pkg installer.</a> (use Ctrl+Click for a new tab) for Mac </li>
  <li>Open Terminal Program and Navigate to the Folder called MangaNewChapter-main by Using <em>cd Downloads\MangaNewChapter-main</em> until arrival. Then run <em>pip3 install -r requirements.txt</em> Only do this in set up.</li>
  <li>Run <em>python3 checker.py</em>. This process will be how you normally access the program, preceded by naviagting to the MangaNewChapter-main folder.</li>
</ol>

<h1 id="2m">Two Step Set Up on Mac (Experimental)</h1>
Note: It is highly recommended to use Ctrl+Click to open each of these in a new tab and then copy their contents into Terminal program on your computer.
<ol>
  <a href="setup.sh"><li>Download the ZIP file and Miniconda</li></a>
  <a href="setup2.sh"><li>Install required packages and run the file</li></a>
  Note: During the second step, several Python windows will open and then close one-by-one. Please do not be alarmed by this as it is a normal part of set up.
</ol>
<a href="launch.sh">After setting up in this way, you can click here whenever you'd like to look for new chapters, or just find the launch.ps1 file on your computer :)</a> <p>Also, a shortcut to this program called "MQuicker - For Mac Desktop" is included within C:\Extracts\MQuicker.
I recommend moving it to your Desktop, and setting Terminal as the default program to open .sh by right clicking the icon, selecting Open With -> Choose Another App -> Always Use this App to Open .sh Files -> More Apps -> Look for an App on Your PC and then find and choose Terminal to easily access MQuicker from the Desktop.</p>

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
 
### Tier - My personal rankings of the "starter pack" manga as seen in tier.txt. Intended to help selective new readers choose only the best. Found as (#) in manga names.
<ol>
  <li>The Top Tier reserved for my favorites.</li>
  <li>The Middle Tier for all the manga I really liked.</li>
  <li>The Bottom Tier holds manga that I liked some parts and not others. </li>
 </ol>
 Note: I read and enjoyed all manga within the initial list.txt file so don't take this to mean Tier 2 or 3 are low quality.
 
### Categories - My personal categories for the "starter pack" manga as seen in categories.txt. Intended to help readers identify preferences. Found as \[Abcd\] in manga names.
<ol>
  <li>System Leveling - Worlds where there exists a system of some sort that allows "players" or "hunters" to level up and become physically stronger.</li>
  <li>Culivator Reincarnation - The main character reincarnated and uses his knowledge to cultivate faster. More fantastical/magical than below.</li>
  <li>Martial Reincarnation - The main character reincarnated and uses his knowledge to train faster. More realistic than above.</li>
  <li>Plot Heavy - Stories where the action takes a backseat to adventure and character development.</li>
  <li>Underdog Cultivator - Someone, typically the weakest character, miraculously acquires an artifact or method to rise up and become the strongest.</li>
  <li>Virtual Reality Game - Worlds where there exists a very popular VR game that the main character enters and becomes famous within.</li>
 </ol>
 Note: Order of categories does not mark my preferences.
 
# Function Directory
<ol>
  <li>a() - Shows all manga on your list with the latest chapter released.</li>
  <li>n() - Shows all manga on your list where you have not read the latest chapter released.</li>
  <li>s() - Saves all manga on your list with the latest chapter released to a text file named MM/DD/YY.txt within the saved folder.</li>
  <li>change_current() - Iterates through every manga on your list and lets you change the latest chapter read and status. Easily skip through with the Enter key.</li>
  <li>add() - Add a manga to your list by providing the Name (no requirements), Link (include the https://), Source Code (see Source in Codes above), Current Chapter, and Status Code.</li>
  <li>primer() - Adjusts the initial list.txt file containing which mangas you'd like to track and latest.txt file containing what chapter you are on (both found within the saved folder).</li>
</ol>

