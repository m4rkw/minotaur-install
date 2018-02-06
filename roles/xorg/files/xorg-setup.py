#!/usr/bin/env python

import os
import re
import sys

devices = []

for line in os.popen("lspci |grep 'VGA compatible controller: NVIDIA Corporation'").read().rstrip().split("\n"):
  match = re.match("^(.*?) VGA compatible controller: NVIDIA Corporation (.*?) \[(.*?)\]", line)

  if match:
    pci0 = int(match.group(1).split(':')[0])
    pci1 = int(match.group(1).split(':')[1].split('.')[0])
    pci2 = int(match.group(1).split(':')[1].split('.')[1])

    devices.append({
      "pci0": pci0,
      "pci1": pci1,
      "pci2": pci2,
      "model": match.group(3)
    })

if len(devices) == 0:
  print "fatal: no Nvidia GPUs found"
  sys.exit(1)

with open("/etc/X11/xorg.conf","w") as f:
  f.write("Section \"ServerLayout\"\n")
  f.write("    Identifier      \"Layout0\"\n")
  f.write("    Screen          0 \"Screen0\" 0 0\n")
  for i in range(1, len(devices)):
    f.write("    Screen          %d \"Screen%d\" RightOf \"Screen%d\"\n" % (i, i, i-1))
  f.write("    Option          \"Xinerama\" \"0\"\n")
  f.write("EndSection\n")

  for i in range(0, len(devices)):
    f.write("Section \"Device\"\n")
    f.write("    Identifier      \"Device%d\"\n" % (i))
    f.write("    Driver          \"nvidia\"\n")
    f.write("    VendorName      \"NVIDIA Corporation\"\n")
    f.write("    BoardName       \"%s\"\n" % (devices[i]['model']))
    f.write("    Option          \"UseEDID\" \"false\"\n")
    f.write("    Option          \"AllowEmptyInitialConfiguration\" \"yes\"\n")
    f.write("    Option          \"ConnectToAcpid\" \"off\"\n")
    f.write("    Option          \"NoLogo\" \"1\"\n")
    f.write("    Option          \"Coolbits\" \"28\"\n")
    f.write("    Option          \"RegistryDwords\" \"PowerMizerEnable=0x1; PerfLevelSrc=0x2222; PowerMizerDefaultAC=0x1\"\n")
    f.write("    BusID           \"PCI:%d:%d:%d\"\n" % (devices[i]['pci0'], devices[i]['pci1'], devices[i]['pci2']))
    f.write("EndSection\n")

  for i in range(0, len(devices)):
    f.write("Section \"Monitor\"\n")
    f.write("    Identifier     \"Monitor%d\"\n" % (i))
    f.write("    VendorName     \"Unknown\"\n")
    f.write("    ModelName      \"Unknown\"\n")
    f.write("    HorizSync      28.0 - 33.0\n")
    f.write("    VertRefresh    43.0 - 72.0\n")
    f.write("    Option         \"DPMS\"\n")
    f.write("EndSection\n")

  for i in range(0, len(devices)):
    f.write("Section \"Screen\"\n")
    f.write("    Identifier     \"Screen%d\"\n" % (i))
    f.write("    Device         \"Device%d\"\n" % (i))
    f.write("    Monitor        \"Monitor%d\"\n" % (i))
    f.write("    DefaultDepth   24\n")
    f.write("    SubSection     \"Display\"\n")
    f.write("        Depth          24\n")
    f.write("    EndSubSection\n")
    f.write("EndSection\n")
