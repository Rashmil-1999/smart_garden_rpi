#! /bin/sh

sudo systemctl enable irrigation.service
sudo systemctl enable irrigation_sub.service
sudo systemctl enable manual_control.service
sudo systemctl enable manual_mode.service