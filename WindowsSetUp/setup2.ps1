Set-ExecutionPolicy Unrestricted -Scope CurrentUser -Force
cd c:\MQuicker\WindowsSetUp
pip install virtualenv==20.0.31
virtualenv mq
.\mq\Scripts\activate
Write-Host -Foreground Yellow ("`Please exercise patience as the following packages install.")
pip install -r "..\requirements.txt"
mv ".\MQuicker - For Desktop.lnk" ($env:USERPROFILE + "\OneDrive\Desktop")
Write-Host ("`nCongratulations on Setting Up MQuicker!!")
cd ..
python checker.py
