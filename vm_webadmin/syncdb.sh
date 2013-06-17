#!/bin/bash
if test -z $1
then
	echo -e "need app name\n"
	exit
fi
python manage.py sql $1
python manage.py syncdb 
