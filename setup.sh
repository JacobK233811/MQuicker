cd 'c:/'
url='https://github.com/JacobK233811/MangaNewChapter/archive/MQuicker-minimal.zip'
mkdir Zips
Dest='C:/Zips'

wget $url -P $Dest

# mkdir Extracts
ExtractDir='C:/'
cd Zips
unzip -q MQuicker-minimal.zip -d $ExtractDir
# cd $ExtractDir
cd ..
rm -r Zips
mv "./MangaNewChapter-MQuicker-minimal" './MQuicker'
cd MQuicker

# Credits to deto's Miniconda-Install GitHub repository
set -e

# Name of application to install
AppName="Python, Pip, & Conda"

# Set your project's install directory name here
InstallDir="SetUp"

# Install the package from PyPi
# Comment out next line if installing locally
PyPiPackage="-r requirements.txt"

echo
echo "Installing $AppName"

echo
echo "Installing into: $(pwd)/$InstallDir"
echo

# Miniconda doesn't work for directory structures with spaces
if [[ $(pwd) == *" "* ]]
then
    echo "ERROR: Cannot install into a directory with a space in its path" >&2
    echo "Exiting..."
    echo
    exit 1
fi

rm "SetUp/create.txt"
# Test if new directory is empty.  Exit if it's not
if [ -d $(pwd)/$InstallDir ]; then
    if [ "$(ls -A $(pwd)/$InstallDir)" ]; then
        echo "ERROR: Directory is not empty" >&2
        echo "If you want to install into $(pwd)/$InstallDir, "
        echo "clear the directory first and run this script again."
        echo "Exiting..."
        echo
        exit 1
    fi
fi

# Download and install Miniconda
set +e
curl "https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh" -o Miniconda_Install.sh
if [ $? -ne 0 ]; then
    curl "https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh" -o Miniconda_Install.sh
fi
set -e

bash Miniconda_Install.sh -b -f -p $InstallDir

# Cleanup
rm Miniconda_Install.sh

echo "Close this shell, open a new one, and run the contents of setup2.sh"
