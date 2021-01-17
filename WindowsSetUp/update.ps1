cd c:\MQuicker
$url = 'https://jacobk233811.github.io/MQuicker/checker.py'
rm checker.py
$Dest = 'C:\MQuicker\checker.py'
$web = New-Object -TypeName System.Net.WebClient
$web.DownloadFile($url, $Dest)
