#!/usr/bin/env python

import serial
import datetime
import time
import signal
import sys

datetimeformat = "%Y-%m-%d %H:%M:%S"

def timestamp_to_date(now):
    """Fonction qui transforme une date de format <timestamp POSIX> en format <datetimeformat> (declare a la ligne 4).

    Args:
        now: une date sous format <timestamp POSIX>.

    Return:
        Retourne la date sous le format <datetimeformat>.

    """
    return datetime.datetime.fromtimestamp(int(now)).strftime(datetimeformat)
def signal_handler(sig, frame):
	print("ctrl-c catch")
	global working
	working = False

DATE=timestamp_to_date(time.time())
working = True
signal.signal(signal.SIGINT, signal_handler)
with open(DATE+".txt","w")as file:


	ser = serial.Serial(
	 port='/dev/ttyACM0',
	 baudrate = 9600,
	 parity=serial.PARITY_NONE,
	 stopbits=serial.STOPBITS_ONE,
	 bytesize=serial.EIGHTBITS,
	 timeout=1
	)
	counter=0



	while working:
	    x=ser.readline()
	    print(x)

	    file.write(str(x) + "\n")



if working == False:
	print("exit")
