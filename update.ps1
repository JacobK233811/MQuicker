cd c:\
$url = 'https://github.com/JacobK233811/MangaNewChapter/archive/main.zip'
New-Item -ItemType Directory Zips
$Dest = 'C:\Zips\MQ.zip'
$web = New-Object -TypeName System.Net.WebClient
$web.DownloadFile($url, $Dest)

New-Item -ItemType Directory Extracts
$ExtractDir = 'C:\Extracts'

$ExtShell = New-Object -ComObject Shell.Application
$file = $ExtShell.Namespace($Dest).Items()
$ExtShell.Namespace($ExtractDir).CopyHere($file)
cd Extracts
Rename-Item -Path .\MangaNewChapter-main .\MQuicker-update-folder
cd MQuicker-update-folder
checker.py | Set-Content ..\MQuicker\checker.py
nc.py | Set-Content ..\MQuicker\nc.py
