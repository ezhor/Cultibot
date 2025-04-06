python -m venv ./
source ./bin/activate

pip install moviepy
pip install python-telegram-bot --upgrade
pip install opencv-contrib-python-headless
pip install "python-telegram-bot[job-queue]"
pip install pytz

deactivate

sudo cp ./services/* /etc/systemd/system/
sudo systemctl daemon-reload

sudo systemctl enable Cultibot-Picture.timer
sudo systemctl start Cultibot-Picture.timer
sudo systemctl enable Cultibot-Telegram-Bot.service
sudo systemctl start Cultibot-Telegram-Bot.service
