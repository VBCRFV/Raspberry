# home assistant.
Домашняя автоматизация с открытым исходным кодом, которая ставит на первое место локальное управление и конфиденциальность. <br>
Приведено в действие мировым сообществом тинкеров и любителей энтузиастов. <br>
Идеально подходит для запуска на Raspberry Pi или на локальном сервере.<br>



## Установка home assistant.
Ставим venv.
```
apt-get install python3-venv -y
```
Создаем виртуальное окружение.
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
# http:
```
http:
  base_url: https://domen.duckdns.org
  ssl_key: /home/user/.homeassistant/privkey.pem
  ssl_certificate: /home/user/.homeassistant/fullchain.pem
```
# google_assistant:
```
google_assistant:
  project_id: project_homeassistant 
  service_account: !include SERVICE_ACCOUNT.JSON
  report_state: true
  exposed_domains:
    - switch
    - light
```
# lovelace
```
lovelace:
	mode: yaml 		# Отключает автоинтерфейс. (теперь интерфейс берется из файла ui-lovelace.yaml, его нужно создать)
```
# binary_sensor:
```
binary_sensor:
  - platform: ping 			# сенсор ping. (пинует ip адрес)
    host: 192.168.0.254		# ip адрес
    name: Router			# Кого пингуем (название для интерфеса)
    count: 2				# Количество повторов в запросе.
    scan_interval: 300		# Интервал между запросами.

```
# sensor:
```
sensor:
  - platform: systemmonitor			# Системный монитор
    resources:						# Ресурсы(ниже)
    - type: processor_use			# Процессор.
    - type: memory_use_percent		# Оператива.
    - type: disk_free				# Диск.
      arg: /						# Какой именно раздел.

  - platform: command_line															# shell запрос.
    name: GPU Temperature															# Имя для интерфейса.
    command: "sudo /opt/vc/bin/vcgencmd measure_temp"								# Температура CPU
    unit_of_measurement: "°C"														#
    value_template: '{{ value | replace("temp=", "") | replace("''C", "") }}'		#
																					 
  - platform: command_line															# shell запрос.
    name: CPU Temperature															# Имя для интерфейса.
    command: "cat /sys/class/thermal/thermal_zone0/temp"							# Температура GPU.
    unit_of_measurement: "°C"														#
    value_template: '{{ value | multiply(0.001) | round(1) }}'						#
```

"Из коробки" - даже не ребутится, если это проблема то: оставляем его и переходим к hassio.
# hassio.
home assistant vs hassio https://sprut.ai/client/article/1758 <br>