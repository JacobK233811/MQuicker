cd $HOME
url='https://github.com/JacobK233811/MQuicker/archive/refs/heads/MQuicker-minimal.zip'
mkdir Zips
Dest=$HOME/Zips/MQ.zip

curl $url -L -o $Dest

ExtractDir=$HOME
cd Zips
unzip -q MQ.zip -d $ExtractDir
cd ..
rm -r Zips
mv "./MangaNewChapter-MQuicker-minimal" './MQuicker'
cd MQuicker

cd $HOME/MQuicker/MacSetUp
python3 -m venv mq
source "./mq/bin/activate"
python3 -m pip install -U pip
python3 -m pip install -U setuptools
echo -e "\033[1;33mPlease exercise patience as the following packages install.\033[0,0m"
arch -x86_64 python3 -m pip install -r "../requirements.txt"
mv "./launch.sh" $HOME
echo "Congratulations on Setting Up MQuicker!!"
cd ..
arch -x86_64 python3 checker.py
# End Step 1
