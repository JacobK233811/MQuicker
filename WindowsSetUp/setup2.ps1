Set-ExecutionPolicy Unrestricted -Scope CurrentUser -Force
cd c:\MQuicker\WindowsSetUp
pip install virtualenv==20.0.31
virtualenv mq
.\mq\Scripts\activate
Write-Host -Foreground Green ("`Please exercise patience as the following packages install.")
pip install -r "..\requirements.txt"
Invoke-Expression "ls $env:USERPROFILE\OneDrive\Desktop" -ErrorVariable isnotonedrive
if (!$isnotonedrive) {mv ".\MQuicker - For Desktop.lnk" ($env:USERPROFILE + "\OneDrive\Desktop")} else {mv ".\MQuicker - For Desktop.lnk" ($env:USERPROFILE + "\Desktop")}
Write-Host ("`nCongratulations on Setting Up MQuicker!!")
cd ..
python checker.py
