#------------------------------------------------#
#                2.4 - Permissions               #
#------------------------------------------------#

# super user
su

# encrypt a file
# crypt xxx
mcrypt xxx

# Check users against the password file
grep danny /etc/passwd

# ls -l gives more information
ls -l /etc/passwd

# /etc/group has group information
ls -l /etc/group

# newgrp changes group permissions
newgrp


# password can be changed with /bin/passwd
ls -l /bin/passwd

# --> -rwsr-xr-x 1 root root 63960 Feb  7  2020 /bin/passwd
# passwd is a "set-uid" program, it uses the set-uid bit.
# If its permissions were -rwsrwxrwx, any user could modify
# it to do something dangerous.


# /bin/who is a bit more ordinary
ls -l /bin/who


# Diretory permissions work similarly, -d option asks for directory info
ls -ld .

# You cannot write to a directory
who >.
# bash: .: Is a directory


# rm permissions are based on the directory the file is contained in
rm temp3

# For directories, --x is searching, not executing.

# chmod: 4: read, 2: write, 1: execute
chmod 666 temp3

# Turn on execution
chmod +x myCommand
# Turn off write permissions
chmod -w myFile

# Removing write permissions from directory ensures files are not deleted
cd
date >temp
chmod -w .
ls -ld .
rm temp
chmod +w .
rm temp

# permissions and modicition dates are stored in something called i-nodes