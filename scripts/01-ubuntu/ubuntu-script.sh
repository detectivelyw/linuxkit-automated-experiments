#!/bin/bash

output_data_name="gcda-data-ubuntu.tar.gz"
host_ip="10.18.171.176"

sleep 30
uname -r
ls -la
df -h
ps aux
apt update
apt install -y gcc
gcc -v
apt install -y openssh-client
which scp
gcc hello-world.c -o hello-world
./hello-world
mkdir /home/test/
apt install -y wget
wget -p -k https://www.google.com
apt install -y python
python hello-world.py
cp hello-world.c /home/test/
cp hello-world.py /home/test/
cat /home/test/hello-world.c /home/test/hello-world.py > /home/test/hello-world.txt
find -name "hello-world.c"
grep -nr "Hello" /home/test/
mkdir /home/output/
tar -zcvf /home/test.tar.gz /home/test/
tar -zxvf /home/test.tar.gz -C /home/output/
stat /home/test/

cp -r /sys/kernel/debug/gcov/linux/ /home/
tar -zcvf $output_data_name /home/linux/
scp -o StrictHostKeyChecking=no $output_data_name detectivelyw@$host_ip:~/Downloads/
