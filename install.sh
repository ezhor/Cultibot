python -m venv ./
sudo ./bin/pip install moviepy
sudo ./bin/pip install python-telegram-bot --upgrade
sudo ./bin/pip install opencv-python
sudo ./bin/pip install "python-telegram-bot[job-queue]"
sudo ./bin/pip install pytz

sudo cp ./services/* /etc/systemd/system/

sudo systemctl daemon-reload

sudo systemctl enable Cultibot-Picture.timer
sudo systemctl start Cultibot-Picture.timer
sudo systemctl enable Cultibot-Telegram-Bot.service
sudo systemctl start Cultibot-Telegram-Bot.service
