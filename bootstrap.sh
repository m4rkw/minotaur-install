#!/bin/bash
if [ "$USER" != "root" ] ; then
  echo "this script must be run as root."
  exit 1
fi
yum -y install epel-release
yum -y install python-pip
yum -y install git
pip install ansible
git clone https://github.com/m4rkw/minotaur-install.git
cd minotaur-install
ansible-playbook -i 'localhost,' -c local playbooks/server.yml
