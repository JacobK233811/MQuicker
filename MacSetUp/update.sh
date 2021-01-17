cd $HOME/MQuicker
url='https://jacobk233811.github.io/MQuicker/checker.py'
rm checker.py
Dest=$HOME/MQuicker/checker.py

curl $url -L -o $Dest
