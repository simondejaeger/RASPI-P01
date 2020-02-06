#installation
- télécharger raspiban lite .zip
- copier image avec etcher sur carte micro sd
- se connecter sur écran hdmi, internet rj45 et clavier usb
- login "pi" pswd "raspberry" (écrire "rqspberry" car clavier pas encore configuré
- changer clavier (belgian) avec sudo raspi-config (attention "-" pas au même endroit (à))
- sudo apt-get update
- sudo apt-get upgrade
- autoriser ssh avec raspi-config
- "hostname -I" et noter IP
- commencer liaison ssh avec ordinateur
- sudo apt-get install git
- git clone https://github.com/simondejaeger/RASPI-P01
- sudo cp RASPI-P01/IP_AT_START.service /etc/systemd/system/
- ouvrir ip_at_start.py ajouter infos manquantes mail rec mail env et mdp 
- sudo systemctl daemon-reload
- sudo systemctl enable IP_AT_START
- sudo systemctl start IP_AT_START
- systemctl status IP_AT_START
- autoriser serial via "sudo raspi-config"
- "dmesg" après avoir branché arduino sur usb pour voir le nom du port usb concerné
- le cas échéant, modifier le nom du port usb en ouvrant serial2... dans nano
- sudo apt-get install python3-pip
- cd RASPI-P01
- sudo pip3 install -r requirements.txt
- sudo apt-get install python3-matplotlib
- sudo reboot


