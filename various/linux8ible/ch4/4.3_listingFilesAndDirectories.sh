#------------------------------------------#
#    4.3 - Listing Files and Directories   #
#------------------------------------------#

alias ls

# Adding random file types to view --color=auto option
touch scriptx.sh apple
chmod 755 scriptx.sh
mkdir myStuff
ln -s apple pointerToApple
ls

# Number of characters shown for a directory reflects
# the size of the file containing information about
# the directory, not the size of the files contained.

# An s in owner, group, or both (-rwsr-xr-x, -rwxr-sr-x,
# -rwsr-sr-x): ownership of the running process is assigned
# to the application's user/group instead of the user\'s.

# A t at the end (drwxrwwxr-t): the sticky bit is set for
# that directory. Other users and groups can add files
# but are prevented from deleting other's files.

# A plus sign + at the end (-rw-rw-r--+): extended
# attributes, such as Access Control Lists (ASLs) are
# set on the file. A . indicates SELinux.


#--- Identifying Directories ---#
# Environment variable that stores the home directory
$HOME
~

# Current directory
.
# Directory one level up
..
# Environment variable for current working directory
$PWD
# Env variable for last working directory
$OLDPWD


# Other ls options

# Show all
ls -a

# List all, by most recently modified
ls -at

# List files and append file-type indicators
ls -F

# Hide certain files/directories using --hide= option
ls --hide=g*

# List info about directory instead of its contents
ls -ld ~/test

# Create multiple directory layers:
mkdir -p ~/test/documents/memos/

# List files recursively from the current directory down
ls -R

# List files by size
ls -S

