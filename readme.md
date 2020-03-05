# Репозиторий общего назначения Raspberry.

##

| Модель | Год выпуска | CPU |
|---|:---:|:---:|
| Pi 1 A | 2013 | Broadcom BCM2835 |
| Pi 1 A+ | 2014 | Broadcom BCM2835 |

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