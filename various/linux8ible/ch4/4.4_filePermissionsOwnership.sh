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
