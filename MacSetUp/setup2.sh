cd $HOME/MQuicker/MacSetUp
pip3 install virtualenv==20.0.31
virtualenv mq
source "./mq/bin/activate"
python3 -m pip install -U pip
echo -e "\033[1;33mPlease exercise patience as the following packages install."
python3 -m pip install -r "../requirements.txt"
mv "./launch.sh" $HOME
echo "Congratulations on Setting Up MQuicker!!"
cd ..
python3 checker.py
