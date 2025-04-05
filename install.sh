sudo apt install pip
sudo pip install moviepy
sudo pip install python-telegram-bot --upgrade
sudo pip install opencv-python
sudo pip install "python-telegram-bot[job-queue]"
sudo pip install pytz

sudo cp ./services/* /etc/systemd/system/

sudo systemctl enable Cilantro-Picture.timer
sudo systemctl start Cilantro-Picture.timer
sudo systemctl enable Cilantro-Telegram-Bot.service
sudo systemctl start Cilantro-Telegram-Bot.service
