cd "c:/MQuicker/MacSetUp"
pip install virtualenv==20.0.31
virtualenv mq
source "./mq/Scripts/activate"
echo -e "\033[1;33mPlease exercise patience as the following packages install."
pip install -r "../requirements.txt"
mv "./MQuicker - For Desktop.lnk" ($HOME + "/Desktop")
echo "Congratulations on Setting Up MQuicker!!"
cd ..
python checker.py
