#------------------------------------------------------#
#       4.5 - Moving, Copying, and Removing Files      #
#------------------------------------------------------#

mv abc def
mv abc ~
mv ~/myMemo/ ~/Documents/

cp abc def
cp abc ~
cp -r /usr/share/doc/bash-completion* /tmp/a/
# -a option: archive - retains original date/time stamps
cp -ra /usr/share/doc/bash-completion* /tmp/b/

rmdir ~/nothing/
rm -r ~/bigdir/
rm -rf ~/hugedir/

# Overriding -i option
# Running rm unaliased
\rm bigdir

# Create backup of original file with the mv command
touch ~/testdir/ && echo "Hello World!" >~/testdir/
mv -b abc ~/testdir/

