#------------------------------------------------#
#         2.3 - Directories and Filenames        #
#------------------------------------------------#

pwd
mkdir recipes
cd recipes
pwd
mkdir pie cookies
ed pie/apple
ed cookies/chocChip


# ls is good, but it doesn't look in subdirectories

ls
file *
ls recipes
ls recipes/pie


# du - disc usage

du
du -a
du -a | grep choc
