#!/bin/bash
#
# Command substitution

# Using backticks is deprecated:
# `command`

# Preferred method: using $(command)

ls -l $(which passwd)

exit 0

