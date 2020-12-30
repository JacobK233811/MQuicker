<head>
     <link rel="shortcut icon" type="image/png" href="/mquicker_icon.png">
</head>
## Welcome to the MQuicker Website
<p>The first priority of this website is to enable copying of Powershell/Terminal text into its appropriate program for the MQuicker install. If you would like more details on the aim of this project or the setup process, <a href="https://github.com/JacobK233811/MangaNewChapter#manganewchapter">please see here</a>. When pasting text into Windows Powershell, use the right click. Scroll down to the section that best describes your situation and copy & paste the steps into your Powershell/Terminal. For the Two-Step Installs, run the first step, close terminal, and then run the second step. To join our Discord community, <a href="https://discord.gg/f7r8Emws8G">use this link</a>. Anyone there will happily help you with installation or discuss manga with you.</p>
### Windows Two-Step
<div>
     <button style="width: 250px;" onclick="CopyToClipboard('wstep1');return false;">Copy Step 1</button>
     <button class="button" style="width: 250px;" onclick="CopyToClipboard('wstep2');return false;">Copy Step 2</button>
     <br><br>
     <div style="background-color: #012456; color: white; max-height: 400px; overflow: scroll; padding: 10px;">
          <p id="wstep1">cd c:\<br>
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

Write-Host -Foreground Green ("Close this shell, open a new one, and run the contents of setup2.ps1")<br>
# End Step 1 <br></p>
     </div>
     <br>
     <div style="background-color: #012456; color: white; max-height: 400px; overflow: scroll; padding: 10px;">
          <p id="wstep2">Set-ExecutionPolicy Unrestricted -Scope CurrentUser -Force<br>
cd c:\MQuicker\WindowsSetUp<br>
pip install virtualenv==20.0.31<br>
virtualenv mq<br>
.\mq\Scripts\activate<br>
Write-Host -Foreground Green ("`Please exercise patience as the following packages install.")<br>
pip install -r "..\requirements.txt"<br>
Invoke-Expression "ls $env:USERPROFILE\OneDrive\Desktop" -ErrorVariable isnotonedrive<br>
if (!isnotonedrive) {mv ".\MQuicker - For Desktop.lnk" ($env:USERPROFILE + "\OneDrive\Desktop")} else {mv ".\MQuicker - For Desktop.lnk" ($env:USERPROFILE + "\Desktop")}<br>
mv ".\MQuicker - For Desktop.lnk" ($env:USERPROFILE + "\Desktop")<br>
Write-Host ("`nCongratulations on Setting Up MQuicker!!")<br>
cd ..<br>
python checker.py<br>
# End Step 2 <br></p>
     </div>     
</div>

### Mac Two-Step 
<div>
     <button style="width: 250px;" onclick="CopyToClipboard('mstep1');return false;">Copy Step 1</button>
     <button class="button" style="width: 250px;" onclick="CopyToClipboard('mstep2');return false;">Copy Step 2</button>
     <br><br>
     <div style="background-color: #f4f4f4; color: black; max-height: 400px; overflow: scroll; padding: 10px;">
          <p id="mstep1">setopt interactivecomments<br>
               cd $HOME<br>
url='https://github.com/JacobK233811/MangaNewChapter/archive/MQuicker-minimal.zip'<br>
mkdir Zips<br>
Dest=$HOME/Zips/MQ.zip<br>

curl $url -L -o $Dest<br>

# mkdir Extracts<br>
ExtractDir=$HOME<br>
cd Zips<br>
unzip -q MQ.zip -d $ExtractDir<br>
# cd $ExtractDir<br>
cd ..<br>
rm -r Zips<br>
mv "./MangaNewChapter-MQuicker-minimal" './MQuicker'<br>
cd MQuicker<br>

# Credits to detos Miniconda-Install GitHub repository<br>
set -e<br>

# Name of application to install<br>
AppName="Python, Pip, & Conda"<br>

# Set your projects install directory name here<br>
InstallDir="PythonFiles"<br>

# Install the package from PyPi<br>
# Comment out next line if installing locally<br>
PyPiPackage="-r requirements.txt"<br>

echo<br>
echo "Installing $AppName"<br>

echo<br>
echo "Installing into: $(pwd)/$InstallDir"<br>
echo<br>

# Miniconda doesnt work for directory structures with spaces<br>
if [[ $(pwd) == *" "* ]]<br>
then<br>
    &nbsp;&nbsp;&nbsp;&nbsp;echo "ERROR: Cannot install into a directory with a space in its path" >&2<br>
    &nbsp;&nbsp;&nbsp;&nbsp;echo "Exiting..."<br>
    &nbsp;&nbsp;&nbsp;&nbsp;echo<br>
    &nbsp;&nbsp;&nbsp;&nbsp;exit 1<br>
fi<br>

rm "PythonFiles/create.txt"<br>
# Test if new directory is empty.  Exit if its not<br>
if [ -d $(pwd)/$InstallDir ]; then<br>
    &nbsp;&nbsp;&nbsp;&nbsp;if [ "$(ls -A $(pwd)/$InstallDir)" ]; then<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;echo "ERROR: Directory is not empty" >&2<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;echo "If you want to install into $(pwd)/$InstallDir, "<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;echo "clear the directory first and run this script again."<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;echo "Exiting..."<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;echo<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;exit 1<br>
    &nbsp;&nbsp;&nbsp;&nbsp;fi<br>
fi<br>

# Download and install Miniconda<br>
set +e<br>
curl "https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh" -o Miniconda_Install.sh<br>
if [ $? -ne 0 ]; then<br>
    &nbsp;&nbsp;&nbsp;&nbsp;curl "https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh" -o Miniconda_Install.sh<br>
fi<br>
set -e<br>

bash Miniconda_Install.sh -b -f -p $InstallDir<br>

# Cleanup<br>
rm Miniconda_Install.sh<br>

source "./PythonFiles/bin/activate"<br>
conda init zsh<br>

echo "Close this shell, open a new one, and run the contents of setup2.sh"<br>
# End Step 1<br></p>
     </div>
     <br>
     <div style="background-color: #f4f4f4; color: black; max-height: 400px; overflow: scroll; padding: 10px;">
          <p id="mstep2">cd $HOME/MQuicker<br>
          source "./PythonFiles/bin/activate"<br>
          cd MacSetUp<br>
pip3 install virtualenv==20.0.31<br>
virtualenv mq<br>
source "./mq/bin/activate"<br>
python3 -m pip install -U pip<br>
python3 -m pip install -U setuptools<br>
echo -e "\033[1;33mPlease exercise patience as the following packages install.\033[0,0m"<br>
python3 -m pip install -r "../requirements.txt"<br>
mv "./launch.sh" $HOME<br>
echo "Congratulations on Setting Up MQuicker!!"<br>
cd ..<br>
python3 checker.py<br>
# End Step 2<br></p>
     </div>     
</div>

<h3 id="mos">Mac One-Step (Python users only)</h3>
<div>
     <button style="width: 500px;" onclick="CopyToClipboard('mstep3');return false;">Copy Step 1</button>
     <br><br>
     <div style="background-color: #f4f4f4; color: black; max-height: 400px; overflow: scroll; padding: 10px;">
          <p id="mstep3">cd $HOME<br>
url='https://github.com/JacobK233811/MangaNewChapter/archive/MQuicker-minimal.zip'<br>
mkdir Zips<br>
Dest=$HOME/Zips/MQ.zip<br>

curl $url -L -o $Dest<br>

ExtractDir=$HOME<br>
cd Zips<br>
unzip -q MQ.zip -d $ExtractDir<br>
cd ..<br>
rm -r Zips<br>
mv "./MangaNewChapter-MQuicker-minimal" './MQuicker'<br>
cd MQuicker<br>

cd $HOME/MQuicker/MacSetUp<br>
pip3 install virtualenv==20.0.31<br>
virtualenv mq<br>
source "./mq/bin/activate"<br>
python3 -m pip install -U pip<br>
python3 -m pip install -U setuptools<br>
echo -e "\033[1;33mPlease exercise patience as the following packages install.\033[0,0m"<br>
python3 -m pip install -r "../requirements.txt"<br>
mv "./launch.sh" $HOME<br>
echo "Congratulations on Setting Up MQuicker!!"<br>
cd ..<br>
python3 checker.py<br>
# End Step 1<br></p>
     </div>
</div>

<script src="//cdnjs.cloudflare.com/ajax/libs/clipboard.js/1.4.0/clipboard.min.js">(function(){
    new Clipboard('#copy-button');
})();</script>
<script src="w3.js"></script>
<script>
function CopyToClipboard(id)
{
var r = document.createRange();
r.selectNode(document.getElementById(id));
window.getSelection().removeAllRanges();
window.getSelection().addRange(r);
document.execCommand('copy');
window.getSelection().removeAllRanges();
     
/* Alert the copied text */
alert("Copied the code for this step.");
}
</script>
