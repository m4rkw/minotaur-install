#!/usr/bin/env python

import os
import sys

n_devices = len(os.popen("lspci |grep 'VGA compatible controller: NVIDIA Corporation'").read().rstrip().split("\n"))

if n_devices == 0:
  print "fatal: no Nvidia devices found"
  sys.exit(1)

with open("/etc/miner-startup.sh","w") as f:
  f.write("#!/bin/bash\n")
  f.write("sleep 10\n")
  f.write("export DISPLAY=:0\n")
  f.write("xhost +si:localuser:miner\n")

  for i in range(0, n_devices):
    f.write("nvidia-settings -a '[gpu:%d]/GPUPowerMizerMode=1'\n" % (i))
    f.write("nvidia-smi --id=%d --persistence-mode=1\n" % (i))

  f.write("sleep 5\n")
  f.write("/usr/bin/sudo -u miner /usr/bin/screen -dmS ex /home/miner/excavator.sh\n")
  f.write("sleep 5\n")
  f.write("mkdir /var/run/minotaur\n")
  f.write("chown miner:miner /var/run/minotaur\n")
  f.write("mkdir /var/run/gpustatd\n")
  f.write("chown miner:miner /var/run/gpustatd\n")
  f.write("mkdir /var/run/excavataur\n")
  f.write("chown miner:miner /var/run/excavataur\n")
  f.write("/usr/bin/sudo -u miner /usr/bin/screen -dmS exv /home/miner/excavataur.sh\n")
  f.write("/usr/bin/sudo -u miner /usr/bin/screen -dmS fan /home/miner/gpustatd.sh\n")
  f.write("#/usr/bin/sudo -u miner /usr/bin/screen -dmS min /home/miner/minotaur.sh\n")
  f.write("/usr/bin/sudo -u miner /usr/bin/screen -dmS gs /home/miner/gs.sh\n")
