#!/usr/bin/env bash

nmap -v -sP 192.168.0.0/24 | grep -v 'host down\|Host is up'
