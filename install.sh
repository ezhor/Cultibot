python -m venv ./
sudo ./bin/pip install moviepy
sudo ./bin/pip install python-telegram-bot --upgrade
sudo ./bin/pip install opencv-python
sudo ./bin/pip install "python-telegram-bot[job-queue]"
sudo ./bin/pip install pytz

sudo cp ./services/* /etc/systemd/system/

sudo systemctl enable Cilantro-Picture.timer
sudo systemctl start Cilantro-Picture.timer
sudo systemctl enable Cilantro-Telegram-Bot.service
sudo systemctl start Cilantro-Telegram-Bot.service
