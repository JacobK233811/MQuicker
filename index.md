## Welcome to the MQuicker Website
The first priority of this website is to enable copying of Powershell/Terminal text.

<!-- The text field -->
<input type="text" value="Goodbye World">

<!-- The button used to copy the text -->
<button onclick="myFunction()">Copy text</button>
### Windows Two-Step
<div>
     <button style="width: 230px;">Copy Step 1</button>
     <button style="width: 230px;">Copy Step 2</button>
     <div style="background-color: #012456; color: white; max-height: 400px; overflow: scroll;">
          <p id="myInput">cd c:\<br>
$url = 'https://github.com/JacobK233811/MangaNewChapter/archive/MQuicker-minimal.zip'<br>
New-Item -ItemType Directory Zips<br>
$Dest = 'C:\Zips\MQ.zip'<br>
$web = New-Object -TypeName System.Net.WebClient<br>
$web.DownloadFile($url, $Dest)<br># New-Item -ItemType Directory Extracts<br>
$ExtractDir = 'C:\'<br>

$ExtShell = New-Object -ComObject Shell.Application<br>
$file = $ExtShell.Namespace($Dest).Items()<br>
$ExtShell.Namespace($ExtractDir).CopyHere($file)<br>
# cd MQuicker<br>
Rename-Item -Path .\MangaNewChapter-MQuicker-minimal .\MQuicker<br>
rm -r Zips<br>
cd MQuicker<br>

# Credits to deto's Miniconda-Install GitHub repository<br>
$ErrorActionPreference = "Stop"<br>

# Name of application to install<br>
$AppName="Python, Pip, & Conda"<br>

# Set your project's install directory name here<br>
$InstallDir="PythonFiles"<br>

# Dependencies installed with pip instead<br>
# Comment out the next line if no PyPi dependencies<br>
$PyPiPackage="-r requirements.txt"<br>

Write-Host -Foreground Green ("`nInstalling $AppName to "+(get-location).path+"\$InstallDir")<br>


# Download Latest Miniconda Installer<br>
Write-Host -Foreground Green "`nDownloading Miniconda Installer...`n"<br>

(New-Object System.Net.WebClient).DownloadFile("https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe", "$pwd\Miniconda_Install.exe")<br>

# Install Python environment through Miniconda<br>
Write-Host "Installing Miniconda...`n"<br>
Start-Process Miniconda_Install.exe "/S /AddToPath=1 /D=$pwd\$InstallDir" -Wait<br>

# Cleanup<br>
Remove-Item "Miniconda_Install.exe"<br>

Write-Host -Foreground Green ("Close this shell, open a new one, and run the contents of setup2.ps1")<br></p>
     </div>     
</div>


<script src="w3.js" type="text/javascript"></script>
