#!/bin/bash
#
# Testing string verification

echo $1

if [ $1=='[a-z]*' ]
then
	echo $1 starts with a letter
else
	echo $1 does not start with a letter
fi

