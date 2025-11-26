#!/bin/bash
read -p "enter port to search: " port;
sudo netstat -tuanp | grep $port
#opgave 7
