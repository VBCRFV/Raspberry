# home assistant.
Домашняя автоматизация с открытым исходным кодом, которая ставит на первое место локальное управление и конфиденциальность. <br>
Приведено в действие мировым сообществом тинкеров и любителей энтузиастов. <br>
Идеально подходит для запуска на Raspberry Pi или на локальном сервере.<br>



## Установка home assistant.
Ставим venv.
```
apt-get install python3-venv -y
```
Создаем виртуальное окружение(в зарание выбраной дериктории например /usr).
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