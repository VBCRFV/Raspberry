# Репозиторий общего назначения Raspberry.

##

| Модель | Год выпуска | CPU | core | GPU | RAM | WiFi BT | LAN | USB | Audio | Video | GPIO |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Pi 1 A | 2013 | Broadcom BCM2835 | 1x700 | VC_4 | 0.25 | - | - | 1 | I²S, HDMI, 3.5 jack | HDMI, RCA | 26 |
| Pi 1 A+ | 2014 | Broadcom BCM2835 | 1x700 | VC_4 | 0.25 | - | - | 1 | I²S, HDMI, 3.5 jack | HDMI, TRRS | 40 |
| Pi 1 B | 2012 | Broadcom BCM2835 | 1x700 | VC_4 | 0.5 | - | 100 | 2 | I²S, HDMI, 3.5 jack | HDMI, RCA | 26 |
| Pi 1 B+ | 2014 | Broadcom BCM2835 | 1x700 | VC_4 | 0.5 | - | 100 | 4 | I²S, HDMI, 3.5 jack | HDMI, TRRS | 40 |
| Pi 2 B | 2015 | Broadcom BCM2836 | 4x900 | VC_4 | 1 | - | 100 | 4 | I²S, HDMI, 3.5 jack | HDMI, TRRS | 40 |
| Pi 3 A+ | 2018 | Broadcom BCM2837B0 | 4x1400 | VC_4 | 0.5 | 802.11ac 4.2 | - | 1 | I²S, HDMI, 3.5 jack | HDMI, TRRS, DSI | 40 |
| Pi 3 B | 2016 | Broadcom BCM2837 | 4x1200 | VC_4 | 1 | 802.11n 4.1 | 100 | 4 | I²S, HDMI, 3.5 jack | HDMI, TRRS, DSI | 40 |
| Pi 3 B+ | 2018 | Broadcom BCM2837B0 | 4x1400 | VC_4 | 1 | 802.11ac 4.2 | 1000 | 4 | I²S, HDMI, 3.5 jack | HDMI, TRRS, DSI | 40 |
| Pi Zero | 2015 | Broadcom BCM2835 | 1x1000 | VC_4 | 0.5 | - | - | 1 | mini HDMI, GPIO PWM | mini HDMI, GPIO Composite | 40 |
| Pi Zero W | 2017 | Broadcom BCM2835 | 1x1000 | VC_4 | 0.5 | 802.11n 4.0 | - | 1 | mini HDMI, GPIO PWM | mini HDMI, GPIO Composite | 40 |
| Pi 4 B | 2019 | Broadcom BCM2711 | 4x1500 | VC_6 | 1,2,4 | 802.11ac 5.0 | 1000 | 2-2.0, 2-3.0 | I²S, 2 micro HDMI, 3.5 jack | 2 micro HDMI, TRRS, DSI | 40 |
## раздел Boot

### Статический ip при первом запуске.
В файл cmdline.txt, в конец строки, через пробел добавляем строку.
```
ip=10.0.0.1::10.0.0.254:255.255.255.0:rpi:eth0:off
```
10.0.0.1 - ip адрес. <br>
10.0.0.254 - шлюз. <br>
255.255.255.0 - маска. <br>
rpi - ХЗ. <br>
eth0 - интерфейс. <br>
off - ХЗ. <br>

## Raspbian.

### Root SSH
```
echo PermitRootLogin yes >> /etc/ssh/sshd_config 
sudo passwd
    pass
    pass
sudo systemctl enable ssh
sudo systemctl start ssh
```

### Подключаем LCD 3.5
```
raspi-config
    должно быть написано pi жмём [Enter]
    выбираем [3 Boot Options] жмём [Enter]
    выбираем [B1 Desktop / CLI] жмём [Enter]
    выбираем [B2 Console Autologin] жмём [Enter]
    выбираем <Finish> (для перехода вниз нажмите [Tab]) жмём [Enter]
    выбираем <No> жмём [Enter]
wget https://github.com/goodtft/LCD-show/archive/master.zip
unzip master.zip 
echo top >> /home/pi/.bashrc
cd LCD-show-master
./LCD35-show
```

### Fork + Git
    1. создаём локальную папку репозитория. (не забываем про General settings).
    2. Fork, инициализируем локальный репозиторий(из пункта 1).
    3. создаём внешний репозиторий(git).
    4. Fork, инициализируем внешний репозиторий(из пункта 3).
    5. создаём 'readme.md'
    6. создаём коммит 'init: master' и пушим изменения.(master ветка создана локално и origin).
    7. инициализируем 'git flow'.
    8. переходим в ветку 'develop'.
    9. пишем название проекта(или что угодно) в 'readme.md'.
    10. создаём коммит 'init: develop' и пушим изменения.(develop ветка создана локално и origin).
    11. создаём ветку 'feature/govnokod', и начинаем творить(по возможности пишем: локоничные 'коммиты' и исчерпывающие 'дискрипшены').