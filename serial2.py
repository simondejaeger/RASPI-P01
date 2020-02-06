#!/usr/bin/env python

import serial
import datetime
import time
import signal
import matplotlib.pyplot as plt

datetimeformat = "%Y-%m-%d_%H:%M:%S"


def timestamp_to_date(now):
    """Fonction qui transforme une date de format <timestamp POSIX> en format <datetimeformat> (declare a la ligne 4).

    Args:
        now: une date sous format <timestamp POSIX>.

    Return:
        Retourne la date sous le format <datetimeformat>.

    """
    return datetime.datetime.fromtimestamp(int(now)).strftime(datetimeformat)


def signal_handler(sig, frame):
    print("End of the meal")
    global working
    working = False


if __name__ == "__main__":
    DATE = timestamp_to_date(time.time())
    working = True
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTSTP, signal_handler)
    drink = []
    meal = []
    count = []

    with open(DATE + ".txt", "w")as file:

        texte = input("entrez nom, repas et boisson \n")
        file.write(texte + '\n')
        ser = serial.Serial(
            port='/dev/ttyUSB0',
            baudrate=9600,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=1
        )

        while working:
            x = ser.readline().decode('utf-8')
            file.write(x)
            print(x)
            x = x.split("\t")
            if len(x) > 4:
                drink.append(float(x[1]))
                meal.append(float(x[4]))
                if len(count) == 0:
                    count.append(0)
                else:
                    count.append(count[-1] + 1)

    if not working:
        print("Plotting data")
        plt.figure(figsize=(20,10))
        plt.plot(count, drink, linewidth=0.50, label='verre')
        plt.plot(count, meal, linewidth=0.50, label='assiete')
        plt.xlabel('time')
        plt.ylabel('poid')
        plt.title(texte)
        plt.legend()
        plt.savefig(DATE + '.png')


