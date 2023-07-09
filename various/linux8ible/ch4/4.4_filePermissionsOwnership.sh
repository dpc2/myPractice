#------------------------------------------------------#
#  4.4 - Understanding File Permissions and Ownership  #
#------------------------------------------------------#

# Permission bits for a regular file:
-rwxrwxrwx

# - prefix is for regular files, but there's also:
# d - directory
# l - symbolic link
# b - block device
# c - character device
# s - socket
# p - pipe

# -rwxrwxrwx
#  \ /\ /\ /
#   |  |  |
#   |--|--|--- file owner's permissions
#      |--|--- file group's permissions
#         |--- permissions for all others

# See permissions for any file or directory
ls -l
ls -ld test/



#--- Changing permissions with chmod (numbers) ---#
# r=4, w=2, x=1

chmod 777 file
chmod 755 file
chmod 644 file
chmod 000 file

# Using chmod recursively
chmod -R 755 $HOME/myapps



#--- Changing permissions with chmod (letters) ---#
# With letters you can change permissions for:
# u: user
# g: group
# o: other
# a: all users

touch myFile
chmod 777 myFile
chmod a-w myFile	# r-xr-xr-x
chmod o-x myFile	# rwxrwxrx-
chmod go-rwx		# rwx------

touch otherFile
chmod 000 otherFile
chmod u+rw otherFile	# rw-------
chmod a+x otherFile	# --x--x--x
chmod ug+rx otherFile	# r-xr-x---


# Using letters to change permissions recursively generally
# works better than using numbers, because you can change
# bits selectively

chmod -R o-w $HOME/myapps



#--- Setting default permission with umask ---#
umask
# 0022

umask 777 ; touch file1 ; mkdir dir01 ; ls -ld file1 dir1
umask 000 ; touch file2 ; mkdir dir02 ; ls -ld file2 dir2
umask 022 ; touch file3 ; mkdir dir03 ; ls -ld file3 dir3



#--- Changing file ownership ---#
sudo touch /home/joe/memo.txt
chown joe /home/joe/memo.txt	# Only the user is changed, not the group
ls -l /home/joe/memo.txt

chown joe:joe /home/joe/memo.txt
ls -l /home/joe/memo.txt
ls -l /home/joe/memo.txt

# Using chown recursively
chown -R joe:joe /media/myusb

