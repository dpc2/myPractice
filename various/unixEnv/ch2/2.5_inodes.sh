#------------------------------------------------#
#                  2.5 - Inodes                  #
#------------------------------------------------#

date >junk2
ls -l junk2
ls -lu junk2
ls -lc junk2

# Changing content does not change usage time (-lu)
# Changing permissions only changes the inode change time (-lc)
chmod 444 junk2
ls -lc junk2

# -t sorts according to time, can be combined with -lu or -lc
ls -lut


# The system's internal name for a file is its inode number
ls -i

# The i-node is stored in the first two bytes of a directory,
# before the name. Can't od directories in modern distros
od -c "myFile"

# -d dumps the data in decimal by byte pairs rather than octal
od -d "myFile"


# ln command is used to link to an existing file, so you can give
# two names to the same file so it can appear in two directories.
# They will have the same i-number.
ln junk linktojunk
ls -li
rm linktojunk
ls -li


# cp makes a copy of files, changes are not duplicated.
cp junk copyofJunk
chmod -w copyofJunk
rm copyofJunk
