cd $HOME/MQuicker
source "./PythonFiles/bin/activate"
cd MacSetUp
pip3 install virtualenv==20.0.31
virtualenv mq
source "./mq/bin/activate"
python3 -m pip install -U pip
python3 -m pip install -U setuptools
echo -e "\033[1;33mPlease exercise patience as the following packages install.\033[0,0m"
python3 -m pip install -r "../requirements.txt"
mv "./launch.sh" $HOME
echo "Congratulations on Setting Up MQuicker!!"
cd ..
arch -x86_64 python3 checker.py
