cd "c:/MQuicker/MacSetUp"
pip install virtualenv==20.0.31
virtualenv mq
source "./mq/Scripts/activate"
echo "Please exercise patience as the following packages install."
pip install -r "../requirements.txt"
mv "./MQuicker - For Desktop.lnk" ($HOME + "/Desktop")
echo "Congratulations on Setting Up MQuicker!!"
python checker.py
