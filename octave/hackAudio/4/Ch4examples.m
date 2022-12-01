#-----------------------------------------------------------------------------#
#                     4.1: Introduction: Octave Application                   #
#-----------------------------------------------------------------------------#

## Example 4.2 - Execute multiple commands in *Command Window*
##>> width = 4 ...
##height = 6            ## Does not work
##
##>> width = 5, ...     ## Works because of the comma
##height = 7
##
##>> width = 5, ...
##height = 7; ...
##depth = 8             ## Displays width and depth, height is supressed 
##
##>> score1 = 40, ...   ## Displays score1 and score2
##score2 = score1
##
##>> score3 = score4, ... ## Does not work, score4 is not defined
##score4 = 20



## Example 4.3 - Clear the Workspace
##x = 5;
##price = 3;
##timeRemaining = '20 seconds';
##clear x
##clear price timeRemaining
##clear all



## Example 4.4 - Saving and loading variables in the Workspace
##t = [ 5 6 7 ];
##x = 8;
##save test1
##save test2 x
##clear
##load test1
##clear
##load test2



## Example 4.5 - Octave current folder
##oldDir = '/home/danny/Code/Octave/Hack_Audio/Ch4';
##cd(oldDir)
##pwd
##newDir = 'testFolder';
##mkdir(newDir);
##cd(newDir)
##pwd
##cd(oldDir)
##pwd
##ls
##rmdir(newDir);
##ls