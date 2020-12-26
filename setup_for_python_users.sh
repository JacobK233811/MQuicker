cd 'c:/'
url='https://github.com/JacobK233811/MangaNewChapter/archive/MQuicker-minimal.zip'
mkdir Zips
Dest='C:/Zips'

wget $url -P $Dest

# mkdir Extracts
ExtractDir='C:/'
cd Zips
unzip -q main.zip -d $ExtractDir
# cd $ExtractDir
cd ..
rm -r Zips
mv "./MangaNewChapter-MQuicker-minimal" './MQuicker'
cd MQuicker

cd "c:/MQuicker"
pip install virtualenv==20.0.31
virtualenv mq
source "./mq/Scripts/activate"
echo "Please exercise patience as the following packages install."
pip install -r requirements.txt
mv "./MQuicker - For Mac Desktop.lnk" ($HOME + "/Desktop")
echo "Congratulations on Setting Up MQuicker!!"
python checker.py
