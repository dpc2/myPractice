#------------------------------------------#
#    	    5.2 - Finding Files    	   #
#------------------------------------------#

# Find commands by name
locate xxx
# Find files based on attributes
find xxx
# Search within text files
grep xxx


#--- Using locate to find files by name ---#

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



#--- Searching for files with 'find' ---#

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


# Finding files by permission, matching exactly
find /usr/bin -perm 755 -ls

# With a hyphen (-), all 3 permission bits must match
# but the other 6 don't have to. -type d: directories
find /usr/bin -perm -222 -type d -ls

# With a slash (/), any permission bit can match
find /myreadonly -perm /222 -type f

# This is good for finding files with open write permission
# for other, regardless of how the rest is set
find . -perm -002 -type f -ls


# Finding files by date and time
# Date and time stamps for when a file is:
# - Created
# - Accessed
# - Content is modified
# - Metadata is changed
#	- Owner, group, timestamp, file size,
#	- permissions, other info stored in inode

# We might search for file data or metachanges for the
# following reasons:

# Config file was changed, but you're not sure which one:
find /etc/ -mmin -10

# You suspect your system was compromised 3 days ago, you
# want to check if any commands had their ownership or
# permissions changed:
find /bin /usr/bin /sbn /usr/sbin -ctime -3

# You want to find files in your FTP server or web server
# that have not been accessed in 300+ days
find /var/ftp /var/www -atime +300

# -atime, -ctime, -mtime: days since accessed, changed,
# or had metadata changed
# -amin, -cmin, -mmin: same thing in minutes


# Using not and or when finding files
# Search shared directory for files owned by joe or chris
find /var/allusers \( -user joe -o -user chris \) -ls

# Search for files owned by joe, but not in the group joe
find /var/allusers -user joe -not -group joe -ls

# Search for files owned by joe and also 1MB+ in size
find /var/allusers -user joe -and -size +1M -ls



# Finding files and executing commands
find [options] -exec command {} \;
find [options] -ok command {} \;

# Find any file named passwd under /etc and include that
# name in the output of an echo command:
find /etc -iname passwd -exec echo "I found {}" \;

# Find every file under /usr/share that is +5MB. Display
# size of each file with du, sort the output from largest
# to smallest
find /usr/share -size +5M -exec du {} \; | sort -nr

# Find all files that belong to joe in a shared folder
# and its sub directories, move them to /tmp/joe with
# confirmation
find /var/allusers -user joe -ok mv {} /tmp/joe/ \;



#--- Searching in files with grep ---#
# With grep you can search a single file or whole
# directory structure of files recursively.
# You can also use grep to search standard output.

# Find text strings in one or more files:
grep desktop /etc/services
# Case insensitive
grep -i desktop /etc/services

# Searching for lines that don't contain a string
grep -vi tcp /etc/services

# Searching a directory recursively for files containing
# a certain string, and listing the files
grep -rli peerdns /usr/share/doc/

# Recursively searching, returning each line of each file
# containing the text, with color
grep -ri --color root /etc/sysconfig/

# Searching the output of a command using the pipe symbol
ip addr show | grep inet

