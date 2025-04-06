sudo apt install pipx

pipx install moviepy
pipx install python-telegram-bot --upgrade
pipx install opencv-python
pipx install "python-telegram-bot[job-queue]"
pipx install pytz

sudo cp ./services/* /etc/systemd/system/
sudo systemctl daemon-reload

sudo systemctl enable Cultibot-Picture.timer
sudo systemctl start Cultibot-Picture.timer
sudo systemctl enable Cultibot-Telegram-Bot.service
sudo systemctl start Cultibot-Telegram-Bot.service
