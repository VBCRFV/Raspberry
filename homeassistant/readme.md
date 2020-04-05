# home assistant.
Домашняя автоматизация с открытым исходным кодом, которая ставит на первое место локальное управление и конфиденциальность. <br>
Приведено в действие мировым сообществом тинкеров и любителей энтузиастов. <br>
Идеально подходит для запуска на Raspberry Pi или на локальном сервере.<br>



## Установка home assistant.
Ставим venv.
```
apt-get install python3-venv -y
```
Создаем виртуальное окружение(в зарание выбраной дериктории например /srv или /usr).
```
python3 -m venv homeassistant 
```
Активируем виртуальное окружение.
```
cd homeassistant
source bin/activate 
```
Устанавливаем Home Assistant.
```
python3 -m pip install homeassistant 
```
Запускаем Home Assistant.
```
hass --open-ui 
```
Ждём строку 'Starting Zeroconf broadcast' и идём по адресу.
```
http://ip:8123
```
## Запуск home assistant.
### Простой запуск.
```
cd /srv/homeassistant
source bin/activate
hass --open-ui
```
### Запуск одной команодой.
создаём файл /srv/homeassistant/run <br>
```
cd /srv/homeassistant
source bin/activate
hass --open-ui
```
делаем его исполняемым <br>
```
chmod +x /srv/homeassistant/run
```
запускаем <br>
```
/srv/homeassistant/run 
```
### Запуск в фоне(screen).
устанавливаем screen <br>
```
apt install screen 
```
создаём\редактируем файл /srv/homeassistant/run <br>
```
cd /srv/homeassistant
source bin/activate
screen -dmS hass hass --open-ui
```
запускаем <br>
```
/srv/homeassistant/run 
```
просмотр запущенных сеансов
```
screen -ls
```
подключение к запущеному сеансу.
```
screen -r hass
```
свернуть сеанс <br>
[Ctrl]+[A],[D] <br>
### Автоапуск в фоне(screen).
Содаём файл /etc/systemd/system/getty@tty1.service.d/autologin.conf <br>
```
[Service]
ExecStart=
ExecStart=-/sbin/agetty --autologin имяпользователя --noclear I 38400 linux
```
добаляем строку в файл %имяпользователя%/.bashrc <br>
```

/srv/homeassistant/run 
```
## Настройка home assistant.
При запуске [hass --open-ui ] в домашней директории пользователя создаётся директория .homeassistant с конфигурацией. <br>
пример конфигурации по умолчанию. configuration.yaml <br>
```
# Configure a default setup of Home Assistant (frontend, api, etc)
default_config:

# Uncomment this if you are using SSL/TLS, running in Docker container, etc.
# http:
#   base_url: example.duckdns.org:8123

# Text to speech
tts:
  - platform: google_translate

group: !include groups.yaml
automation: !include automations.yaml
script: !include scripts.yaml
scene: !include scenes.yaml

```

# hassio.
home assistant vs hassio https://sprut.ai/client/article/1758 <br>