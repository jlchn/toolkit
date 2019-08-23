#!/usr/bin/env python

import socket
import subprocess
import sys
import datetime from datetime

subprocess.call('clear', shell=True)

ip_to_scan = raw_input('server ip to scan: ')

print('start scan open ports on:', ip_to_scan)
