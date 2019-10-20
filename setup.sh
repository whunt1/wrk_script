#!/bin/sh

echo "==================================="
echo "          WRK SETUP TOOL"
echo "-----------------------------------"

wget https://raw.githubusercontent.com/whunt1/wrk_script/master/wrk
wget https://raw.githubusercontent.com/whunt1/wrk_script/master/wrk.sh
chmod +x wrk
chmod +x wrk.sh

echo "-----------------------------------"
echo "Download comple!"
echo "Run ./wrk.sh to config!"
echo "-----------------------------------"
echo "        WRK Setup Complete"
echo "==================================="
