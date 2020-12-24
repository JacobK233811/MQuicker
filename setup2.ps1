cd c:\Extracts\MQuicker
pip install virtualenv
virtualenv mq
.\mq\Scripts\activate
Write-Host ("`Please exercise patience as the following packages install.")
pip install -r requirements.txt
Write-Host ("`nCongratulations on Setting Up MQuicker!!")
python nc.py
