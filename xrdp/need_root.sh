#!/bin/bash
apt install -y xrdp
systemctl start xrdp.service
systemctl enable xrdp.service
gpasswd -a xrdp ssl-cert

cd $(dirname $0)
cp 10-network-manager.pkla 46-allow-update-repo.pkla 45-allow-colord.pkla /etc/polkit-1/localauthority/50-local.d
systemctl restart network-manager.service
