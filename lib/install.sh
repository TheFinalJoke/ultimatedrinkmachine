#!/bin/bash

if [[ `id -u` != 0 ]]
then
echo "Become Root"
exit 1 
fi 

### Install dependiences ###
echo "Installing Dependiences"

pip3 install pipenv

cd /usr/local/bin/ultimatedrinkmachine/
pipenv sync

secret=$(pipenv run python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())')
echo "SECRET_KEY=$secret" >> .env

cp /usr/local/bin/ultimatedrinkmachine/linux_services/* /etc/systemd/system/

systemctl enable --now drinkserver.service 
systemctl enable --now drinkwebserver.service

systemctl is-active --quiet drinkserver.service && systemctl is-active --quiet drinkwebserver.service

if [[ $(echo $?) != 0 ]]
then
echo "Somthing happened and the services did not start"
exit 2
fi

echo "It was successful install!"
