#! /bin/sh

sudo systemctl start irrigation.service
echo ""
sudo systemctl start irrigation_sub.service
echo ""
sudo systemctl start manual_control.service
echo ""
sudo systemctl start manual_mode.service
# echo ""
# sudo systemctl start plant_mapping.service