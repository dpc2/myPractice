#------------------------------------------------#
#         	  2.7 - Devices         	 #
#------------------------------------------------#
#
# In Unix, everything is a file: discs, tape drivers,
# line printers, terminals, etc.
# A magnetic tape would be /dev/mt0, you could run:
cp /dev/mt0 junk
# to copy the contents of the tape to a file

# Even the cpu is a file
ls /dev/cpu

ls -l /dev

# Results in:
# brw-rw----   1 root  disk      259,     0 Sep 26 15:13 nvme0n1
# brw-rw----   1 root  disk      259,     1 Sep 26 15:13 nvme0n1p1
# brw-rw----   1 root  disk      259,     2 Sep 26 15:13 nvme0n1p2
# brw-rw----   1 root  disk      259,     3 Sep 26 15:13 nvme0n1p5
# brw-rw----   1 root  disk      259,     4 Sep 26 15:13 nvme0n1p6
# crw-r-----   1 root  kmem       10,   144 Sep 26 15:13 nvram
# crw-r-----   1 root  kmem        1,     4 Sep 26 15:13 port

# Major and minor device numbers: 259 is major (same device),
# 0-4 is minor different instances of the device.

# /etc/mount reports correspondence between device files and directories:
# It is now /usr/bin/mount
/usr/bin/mount

# /bin, /dev, and /etc are always kept on the root system. When the system
# starts, only the root system is available

# It is illegal to make a link to a file in another subsystem. Inodes are not 
# unique in different file systems.

# df: disc free space
df


# Logging in gets us a terminal through which the characters you type are sent
# and received. The terminal is also a device.
tty

