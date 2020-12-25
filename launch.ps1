Set-ExecutionPolicy Unrestricted -Scope CurrentUser -Force
cd c:\Extracts\MQuicker
.\mq\Scripts\activate
Write-Host -ForegroundColor Green ("`nWelcome to MQuicker!")
python nc.py
