#!/usr/bin/env python

import socket
import subprocess
import sys
from datetime import datetime

subprocess.call('clear', shell=True)

ip_to_scan = raw_input('server ip to scan: ')
print('start scan open ports on:', ip_to_scan)

start_time = datetime.now()

for port in range(1, 1025):
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print "Opening Port: {}".format(port)
        sock.close()

except KeyboardInterrupt:
    sys.exit()
except socket.error:
    print "Cannot connect to server"
    sys.exit()

end_time = datetime.now()
print ('Completed in: ', end_time - start_time)
