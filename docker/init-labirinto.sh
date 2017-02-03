#!/bin/sh

mongod --dbpath /db &

python run.py

exit
