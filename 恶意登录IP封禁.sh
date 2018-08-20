#!/bin/bash

#this script will be used to monitoring the ssh login,if someone want to crack the password,it will be forbidden login#

#author:Ricardo#
#phone:13548644245#
#version:1.0#
#time:2018-06-28# 

while true
do
	IP_list=($(cat /var/log/secure|awk '{print $6,$11}'|egrep '^Failed'|sort|uniq -c|awk '{if($1>10) print $3}'))
	for i in ${!IP_list[@]}
	do
		if cat /etc/hosts.deny|egrep "${IP_list[i]}" &>/dev/null
		then
			:
		else

			sed -i  "$ a sshd:${IP_list[i]}:deny" /etc/hosts.deny
		fi
	done
sleep 5
done
