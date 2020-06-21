#!/usr/bin/bash

#Start up Scripts
yum -y update
yum -y install git
yum -y install python3
yum install -y postgresql
yum -y install gcc
yum install -y python3-devel
yum -y install postgresql-devel
amazon-linux-extras install -y nginx1

#User Scripts
cd /home/ec2-user
git clone https://github.com/angeloadkins/python-image-gallery.git
chown -R ec2-user:ec2-user python-image-gallery
su ec2-user -c "cd ~/python-image-gallery && pip3 install -r requirements.txt --user"

