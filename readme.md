#installation
- sudo apt-get update && sudo apt-get upgrade
- sudo apt-get install git
- git clone https://github.com/simondejaeger/RASPI-P01
- sudo cp /RASPI-P01/IP_AT_START.service /etc/systemd/system/IP_AT_START.service
- sudo systemctl daemon-reload
- sudo systemctl enable IP_AT_START
- sudo systemctl start IP_AT_START
- systemctl status IP_AT_START
- sudo reboot
