#!/usr/bin/env python

import socket
import subprocess
import sys
import time

subprocess.call('clear', shell=True)

ip_to_scan = raw_input('server ip to scan: ')
print 'start scan open ports on:', ip_to_scan

start_time = time.time()

try:
    for port in range(1, 10000):
      sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      sock.settimeout(3)
      result = sock.connect_ex((ip_to_scan, port))
      if result == 0:
        print("Opening Port: {}".format(port))
      sock.close()

except KeyboardInterrupt:
    sys.exit()
except socket.error:
    print("Cannot connect to server")
    sys.exit()

end_time = time.time()
print 'Completed in: ', end_time - start_time
