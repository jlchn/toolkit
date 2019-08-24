#!/usr/bin/env bash

sudo apt-get install nmap

nmap <<IP>> -p 1-9999
