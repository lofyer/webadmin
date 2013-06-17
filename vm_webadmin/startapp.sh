#!/bin/bash
if test -z $1
then
	echo -e "need app name\n"
	exit
fi
python manage.py startapp $1
