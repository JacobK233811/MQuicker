cd "c:\Extracts\MQuicker"
pip install virtualenv==20.0.31
virtualenv mq
source ".\mq\Scripts\activate"
echo "Please exercise patience as the following packages install."
pip install -r requirements.txt
echo "Congratulations on Setting Up MQuicker!!"
python checker.py
