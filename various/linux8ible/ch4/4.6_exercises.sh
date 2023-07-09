#------------------------------------------#
#   		  Exercises                #
#------------------------------------------#

#--- Exercise 1 ---#
mkdir ~/projects
touch house{1..9}
touch otherFile{1..20}
ls house*


#--- Exercise 2 ---#
mkdir -p projects/houses/doors
mkdir projects/outdoors/vegeation/
touch ~/projects/houses/bungalow.txt
touch ./projects/houses/doors/bifold.txt
touch /home/myUser/projects/outdoors/vegetation/landscape.txt


#--- Exercise 3 ---#
cp house1 house5 projects/houses/


#--- Exercise 4 ---#
cp -ra /usr/share/doc/initscripts* ./projects


#--- Exercise 5 ---#
ls -R ./projects | less


#--- Exercise 6 ---#
rm -f house{6..8}


#--- Exercise 7 ---#
mv house{3..4} projects/houses/doors


#--- Exercise 8 ---#
rm -r projects/houses/doors/


#--- Exercise 9 ---#
chmod 640 projects/house2


#--- Exercise 10 ---#
chmod -R 555 ./projects

