#------------------------------------------------#
#             2.2 - What's in a file?            #
#------------------------------------------------#

file /bin /bin/ed /usr/src/cmd/ed.c /usr/man/man1/ed.1


# od spits out a file's contents in 16-bit (2-byte) 
# chunks in octal

od /bin/ed


# Files are extremely versatile. od produces text on it
# standard input, which can be used anywhere text can.
od -c junk >temp
ed ch2.1
r temp
.
q

