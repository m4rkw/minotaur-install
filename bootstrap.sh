#!/bin/bash
if [ "$USER" != "root" ] ; then
  echo "this script must be run as root."
  exit 1
fi
yum -y install python-pip
yum -y install git
pip install ansible
