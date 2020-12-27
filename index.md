## Welcome to the MQuicker Website
The first priority of this website is to enable copying of Powershell/Terminal text.
### Windows Two-Step
<div>
     <button style="width: 250px;" onclick="CopyToClipboard('wstep1');return false;">Copy Step 1</button>
     <button class="button" style="width: 250px;" onclick="CopyToClipboard('wstep2');return false;">Copy Step 2</button>
     <br>
     <div style="background-color: #012456; color: white; max-height: 400px; overflow: scroll;">
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

Write-Host -Foreground Green ("Close this shell, open a new one, and run the contents of setup2.ps1")<br></p>
     </div>
     <br>
     <div style="background-color: #012456; color: white; max-height: 400px; overflow: scroll;">
          <p id="wstep2">Set-ExecutionPolicy Unrestricted -Scope CurrentUser -Force<br>
cd c:\MQuicker\WindowsSetUp<br>
pip install virtualenv==20.0.31<br>
virtualenv mq<br>
.\mq\Scripts\activate<br>
Write-Host -Foreground Green ("`Please exercise patience as the following packages install.")<br>
pip install -r "..\requirements.txt"<br>
mv ".\MQuicker - For Desktop.lnk" ($env:USERPROFILE + "\Desktop")<br>
Write-Host ("`nCongratulations on Setting Up MQuicker!!")<br>
cd ..<br>
python checker.py</p>
     </div>     
</div>

### Mac Two-Step 
<div>
     <button style="width: 250px;" onclick="CopyToClipboard('mstep1');return false;">Copy Step 1</button>
     <button class="button" style="width: 250px;" onclick="CopyToClipboard('mstep2');return false;">Copy Step 2</button>
     <br>
     <div style="background-color: white; color: black; max-height: 400px; overflow: scroll;">
          <p id="mstep1">cd $HOME<br>
url='https://github.com/JacobK233811/MangaNewChapter/archive/MQuicker-minimal.zip'<br>
mkdir Zips<br>
Dest=$HOME/Zips<br>

curl $url -L -o $Dest<br>

# mkdir Extracts<br>
ExtractDir=$HOME<br>
cd Zips<br>
unzip -q MQuicker-minimal.zip -d $ExtractDir<br>
# cd $ExtractDir<br>
cd ..<br>
rm -r Zips<br>
mv "./MangaNewChapter-MQuicker-minimal" './MQuicker'<br>
cd MQuicker<br>

# Credits to deto's Miniconda-Install GitHub repository<br>
set -e<br>

# Name of application to install<br>
AppName="Python, Pip, & Conda"<br>

# Set your project's install directory name here<br>
InstallDir="PythonFiles"<br>

# Install the package from PyPi<br>
# Comment out next line if installing locally<br>
PyPiPackage="-r requirements.txt"<br>

echo<br>
echo "Installing $AppName"<br>

echo<br>
echo "Installing into: $(pwd)/$InstallDir"<br>
echo<br>

# Miniconda doesn't work for directory structures with spaces<br>
if [[ $(pwd) == *" "* ]]<br>
then<br>
    <p>echo "ERROR: Cannot install into a directory with a space in its path" >&2<br>
    echo "Exiting..."<br>
    echo<br>
    exit 1</p>
fi<br>

rm "PythonFiles/create.txt"<br>
# Test if new directory is empty.  Exit if it's not<br>
if [ -d $(pwd)/$InstallDir ]; then<br>
    <p>if [ "$(ls -A $(pwd)/$InstallDir)" ]; then
        <p>echo "ERROR: Directory is not empty" >&2<br>
        echo "If you want to install into $(pwd)/$InstallDir, "<br>
        echo "clear the directory first and run this script again."<br>
        echo "Exiting..."<br>
        echo<br>
        exit 1</p>
    fi</p>
fi<br>

# Download and install Miniconda<br>
set +e<br>
curl "https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh" -o Miniconda_Install.sh<br>
if [ $? -ne 0 ]; then<br>
    curl "https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh" -o Miniconda_Install.sh<br>
fi<br>
set -e<br>

bash Miniconda_Install.sh -b -f -p $InstallDir<br>

# Cleanup<br>
rm Miniconda_Install.sh<br>

source "./PythonFiles/bin/activate"<br>
conda init zsh<br>

echo "Close this shell, open a new one, and run the contents of setup2.sh"<br></p>
     </div>
     <br>
     <div style="background-color: white; color: black; max-height: 400px; overflow: scroll;">
          <p id="mstep2">Set-ExecutionPolicy Unrestricted -Scope CurrentUser -Force<br>
cd c:\MQuicker\WindowsSetUp<br>
pip install virtualenv==20.0.31<br>
virtualenv mq<br>
.\mq\Scripts\activate<br>
Write-Host -Foreground Green ("`Please exercise patience as the following packages install.")<br>
pip install -r "..\requirements.txt"<br>
mv ".\MQuicker - For Desktop.lnk" ($env:USERPROFILE + "\Desktop")<br>
Write-Host ("`nCongratulations on Setting Up MQuicker!!")<br>
cd ..<br>
python checker.py</p>
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
}
</script>
