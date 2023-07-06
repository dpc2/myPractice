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

