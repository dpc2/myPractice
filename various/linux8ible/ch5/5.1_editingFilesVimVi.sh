#------------------------------------------#
#    5.1 - Editing Files with vim and vi   #
#------------------------------------------#

# Alternatives
gedit
nano
jed
joe
kate
kedit
mcedit
nedit


#--- Starting with vi ---#
vi /tmp/test

# Adding text:
# a: add
# A: add at end
# i: insert
# I: insert at beginning
# o: open below
# O: open above

# Moving around in the text:
# Arrow keys
# w: beginning of next word
# W: beginning of next word
# b: beginning of previous word
# B: beginning of previous word
# 0: beginning of current line
# $: end of current line
# H: upper-left corner of screen
# M: first character of middle line
# L: lower-left corner of screen

# Deleting, copying, and changing text:
# ...
# Blablabla

vimtutor



#--- Finding Files ---#

# Find commands by name
locate xxx
# Find files based on attributes
find xxx
# Search within text files
grep xxx


#- Using locate to find files by name -#

# On most Linux systems, updatedb is run once per day to
# gather the names of files throughout the system into a
# database. The 'locate' command searches that db.

# 'locate' cannot find any finds added since the last time
# the database was updated

# Not every file is included in the db. The contents of:
# /etc/updatedb.conf limit which filenames are collected by
# excluding certain mount/filesystem/file types and mount
# points.

locate .bashrc
locate dir_color
# -i: case insensitive
locate -i dir_color

# 'locate' searches the entire file path


#- Searching for files with 'find' -#

# 'find' is a live filesystem search based on file attributes
# You can search by filename, ownership, permission, file size,
# modification times, and others.

find
\$ find /etc
# Send stderr to /dev/null
\$ find /etc 2> /dev/null
\# find /etc
find $HOME -ls


# Finding files by name
find /etc -name passwd
# -iname matches upper and lower case, using * matches anything
# containing passwd
find /etc -iname '*passwd*'


# Finding files by size
find /usr/share -size +10M
find /mostlybig -size -1M
find /bigdata -size +500M -size -5G -exec du -sh {} \;


# Finding files by user
find /home -user chris -ls
find /home \( -user chris -or -user joe \) -ls
find /etc -group ntp -ls
find /var/spool -not -user root -ls


# Finding files by permission
find /usr/bin -perm 755 -ls
