## Welcome to the MQuicker Website
<p>The first priority of this website is to enable copying of Powershell/Terminal text into its appropriate program for the MQuicker install. If you would like more details on the aim of this project or the setup process, <a href="https://github.com/JacobK233811/MQuicker#mquicker">please see here</a>. When pasting text into Windows Powershell, use the right click. Scroll down to the section that best describes your situation and copy & paste the steps into your Powershell/Terminal. <br><br>For the Two-Step Installs, <b>run the first step, close terminal, and then run the second step.</b> <br><br>To join our Discord community, <a href="https://discord.gg/f7r8Emws8G">use this link</a>. Anyone there will happily help you with installation or discuss manga with you.<br><br>Choose Show All to see it work and Primer to customize for yourself on first use.</p>
### Windows Two-Step
<ul>
  <li>Run the first step, close Powershell, and then run the second step.</li>
  <li>If at any time during install it seems as if the program has gotten stuck, try clicking on the window and pressing enter once. Sometimes, working on other tasks or clicking out of the tab will pause the process.</li>
  <li>It is highly recommended to use <b>Ctrl+Click</b> to open each of these in a new tab and then copy their contents into Windows Powershell program on your computer. The link on the right side will make the process smoother and does the same job as the other two combined.</li>
  <li>Find Windows Powershell by clicking the Windows button on your computer and typing Powershell.</li>
  <li>To paste text into Powershell, <b>use your right click.</b></li>
  <li>During the second step, several Python windows will open and then close one-by-one. Please do not be alarmed by this as it is <b>a normal part of set up.</b></li>
  <li>Once the program has started, you make selections by typing in the number that corresponds with the desired action.</li>
</ul>
<ol>
<div>
     <button style="width: 250px;" onclick="CopyToClipboard('wstep1');return false;">Copy Step 1<br>Download ZIP file & Miniconda</button>
     <button class="button" style="width: 250px;" onclick="CopyToClipboard('wstep2');return false;">Copy Step 2<br>Install Required Packages & Run Script</button>
     <br>
     <p>Finding the launch.ps1 file within <em>C:\MQuicker\WindowsSetUp</em> and running it in Powershell will open MQuicker. Also, <b>a shortcut to this program</b> called "MQuicker - For Desktop" should appear on your Desktop (specifically <em>C:\Users\YOURNAME\(OneDrive)\Desktop</em>).
<a href="https://www.top-password.com/blog/set-ps1-script-to-open-with-powershell-by-default/">Setting PowerShell as the default program to open .ps1</a> by right clicking the icon, selecting Open With -> Choose Another App -> Always Use this App to Open .ps1 Files -> More Apps -> Look for an App on Your PC and then find and choose powershell.exe (the .exe usually is not shown) to easily access MQuicker from the Desktop. Following this, opening the shortcut will run the program.
(I found Powershell in C:\Windows\System32\WindowsPowerShell\v1.0) Alternatively, right click the shortcut and select "Run with Powershell"</p>
     <br>
     <br><br>
     <div style="background-color: #012456; color: white; max-height: 400px; overflow: scroll; padding: 10px;">
          <p id="wstep1">cd c:\<br>
$url = 'https://github.com/JacobK233811/MQuicker/archive/MQuicker-minimal.zip'<br>
New-Item -ItemType Directory Zips<br>
$Dest = 'C:\Zips\MQ.zip'<br>
$web = New-Object -TypeName System.Net.WebClient<br>
$web.DownloadFile($url, $Dest)<br># New-Item -ItemType Directory Extracts<br>
$ExtractDir = 'C:\'<br>

$ExtShell = New-Object -ComObject Shell.Application<br>
$file = $ExtShell.Namespace($Dest).Items()<br>
$ExtShell.Namespace($ExtractDir).CopyHere($file)<br>
# cd MQuicker<br>
Rename-Item -Path .\MQuicker-MQuicker-minimal .\MQuicker<br>
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

rm "PythonFiles\.gitkeep"
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
     <button style="width: 500px;" onclick="CopyToClipboard('comment');return false;">Allow Comments First</button>
     <br>
     <button style="width: 250px;" onclick="CopyToClipboard('mstep1');return false;">Copy Step 1</button>
     <button class="button" style="width: 250px;" onclick="CopyToClipboard('mstep2');return false;">Copy Step 2</button>
     <br><br>
     <div style="background-color: #f4f4f4; color: black; max-width: 200px; padding: 3px 100px; margin: 5px auto;">
                                                                                                              <p id="comment">setopt interactivecomments</p>
                                                                                                              </div><br>
     <ul>
  <li>Run the first step, close Terminal, and then run the second step.</li>
  <li>If at any time during install it seems as if the program has gotten stuck, try clicking on the window and pressing enter once. Sometimes, working on other tasks or clicking out of the tab will pause the process.</li>
  <li>It is highly recommended to use <b>Cmd+Click</b> to open each of these in a new tab and then copy their contents into Terminal program on your computer. The link on the right side will make the process smoother and does the same job as the other two combined.</li>
  <li>Find Terminal by going to Spotlight Search (magnifying glass in the top right of the screen) on your computer and typing Terminal.</li>
  <li>To paste text into Terminal, use Cmd+V. You may not see all of the lines if you scroll up, but that is simply Terminal limiting your scrolling. They are there.</li>
  <li>The program looks best in dark mode and if you are not a regular Terminal user, it makes sense to associate opening Terminal with starting MQuicker. You can do both by clicking Preferences in the top left of your screen or simply pressing Cmd+, within Terminal. <a href="https://www.maketecheasier.com/customize-mac-terminal/">This guide explains the process.</a> I recommend following the steps in the first section, "Tweaking Terminal's Theme," and <b>choosing Pro before running the second step</b>. The second section, "Login Commands," should run the command <em>sh launch.sh</em> if you intend to use this feature. Only set this after installation is completed.</li>
  <li>Once the program has started, you make selections by typing in the number that corresponds with the desired action.</li>
</ul>
     <div style="background-color: #f4f4f4; color: black; max-height: 400px; overflow: scroll; padding: 10px;">
          <p id="mstep1">cd $HOME<br>
url='https://github.com/JacobK233811/MQuicker/archive/MQuicker-minimal.zip'<br>
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
mv "./MQuicker-MQuicker-minimal" './MQuicker'<br>
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

rm "PythonFiles/.gitkeep"<br>
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
<ul>
  <li>It is highly recommended to <b>use Cmd+Click</b> to open each of these in a new tab and their copy their contents into Terminal program on your computer. The link on the right side will make the process smoother and does the same job as the other two combined.</li>
  <li>Find Terminal by going to Spotlight Search (magnifying glass in the top right of the screen) on your computer and typing Terminal.</li>
  <li>To paste text into Terminal, use Cmd+V. You may not see all of the lines if you scroll up, but that is simply Terminal limiting your scrolling. They are there.</li>
  <li>The program looks best in dark mode and if you are not a regular Terminal user, it makes sense to associate opening Terminal with starting MQuicker. You can do both by clicking Preferences in the top left of your screen or simply pressing Cmd+, within Terminal. <a href="https://www.maketecheasier.com/customize-mac-terminal/">This guide explains the process.</a> I recommend following the steps in the first section, "Tweaking Terminal's Theme," and <b>choosing Pro before running the second step</b>. The second section, "Login Commands," should run the command <em>sh launch.sh</em> if you intend to use this feature. Only set this after installation is completed.</li>
  <li>Once the program has started, you make selections by typing in the number that corresponds with the desired action.</li>
</ul>
<div>
     <button style="width: 500px;" onclick="CopyToClipboard('mstep3');return false;">Copy Step 1</button>
     <br><br>
     <div style="background-color: #f4f4f4; color: black; max-height: 400px; overflow: scroll; padding: 10px;">
          <p id="mstep3">cd $HOME<br>
url='https://github.com/JacobK233811/MQuicker/archive/MQuicker-minimal.zip'<br>
mkdir Zips<br>
Dest=$HOME/Zips/MQ.zip<br>

curl $url -L -o $Dest<br>

ExtractDir=$HOME<br>
cd Zips<br>
unzip -q MQ.zip -d $ExtractDir<br>
cd ..<br>
rm -r Zips<br>
mv "./MQuicker-MQuicker-minimal" './MQuicker'<br>
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
