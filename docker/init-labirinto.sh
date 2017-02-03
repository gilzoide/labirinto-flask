#!/bin/sh

service mongodb start

if [ $TESTE = "false" ]; then
	python run.py
else
	pip install -r test-requirements.txt
	nosetests
fi

exit
