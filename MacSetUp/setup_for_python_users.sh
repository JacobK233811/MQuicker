cd $HOME
url='https://github.com/JacobK233811/MangaNewChapter/archive/MQuicker-minimal.zip'
mkdir Zips
Dest=$HOME/Zips/MQ.zip

curl $url -L -o $Dest

# mkdir Extracts
ExtractDir=$HOME
cd Zips
unzip -q MQ.zip -d $ExtractDir
# cd $ExtractDir
cd ..
rm -r Zips
mv "./MangaNewChapter-MQuicker-minimal" './MQuicker'
cd MQuicker

cd $HOME/MQuicker/MacSetUp
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
python3 checker.py
