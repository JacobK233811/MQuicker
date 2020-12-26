cd c:\
$url = 'https://github.com/JacobK233811/MangaNewChapter/archive/MQuicker-minimal.zip'
New-Item -ItemType Directory Zips
$Dest = 'C:\Zips\MQ.zip'
$web = New-Object -TypeName System.Net.WebClient
$web.DownloadFile($url, $Dest)

# New-Item -ItemType Directory Extracts
$ExtractDir = 'C:\'

$ExtShell = New-Object -ComObject Shell.Application
$file = $ExtShell.Namespace($Dest).Items()
$ExtShell.Namespace($ExtractDir).CopyHere($file)
# cd MQuicker
Rename-Item -Path .\MangaNewChapter-MQuicker-minimal .\MQuicker
rm -r Zips
cd MQuicker

# Credits to deto's Miniconda-Install GitHub repository
$ErrorActionPreference = "Stop"

# Name of application to install
$AppName="Python, Pip, & Conda"

# Set your project's install directory name here
$InstallDir="SetUp"

# Dependencies installed with pip instead
# Comment out the next line if no PyPi dependencies
$PyPiPackage="-r requirements.txt"

Write-Host ("`nInstalling $AppName to "+(get-location).path+"\$InstallDir")


# Download Latest Miniconda Installer
Write-Host "`nDownloading Miniconda Installer...`n"

(New-Object System.Net.WebClient).DownloadFile("https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe", "$pwd\Miniconda_Install.exe")

# Install Python environment through Miniconda
Write-Host "Installing Miniconda...`n"
Start-Process Miniconda_Install.exe "/S /AddToPath=1 /D=$pwd\$InstallDir" -Wait

# Cleanup
Remove-Item "Miniconda_Install.exe"

Write-Host ("Close this shell, open a new one, and run the contents of setup2.ps1")
