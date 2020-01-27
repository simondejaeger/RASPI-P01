#!/bin/bash

COUNT=0  #itération actuelle
I=$(($1/$2))  #nombre d'iterations, $1= temps de timelapse et $2= temps entre chaques photo, double parenthèse car appel fonction math

while [ $COUNT -lt $I ] #-lt = lower than (-le lower equals,-ge greather equals,-gt greather than,-eq equal,-ne non equal) 
do
	DATE=$(TZ="Europe/Paris" date +"%Y-%m-%d_%H:%M:%S")
	sudo raspistill -o /home/pi/camera/$DATE.jpg
	COUNT=$(($COUNT+1))
	sleep $(($2/1000)) #parce que ici on compte en secondes
done

echo "travail terminé"




