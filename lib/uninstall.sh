#!/bin/bash

if [[ `id -u` != 0 ]]
then
echo "Become Root"
exit 1 
fi 

systemctl stop drinkserver.service && systemctl stop drinkwebserver.service

rm -rf /etc/systemd/system/drink*

systemctl daemon-reload

