# ./configuration.yaml - файл конфигурации Home assistant/
## http: - настройка http
```
http:
  base_url: https://domen.duckdns.org
  ssl_key: /srv/homeassistant/lib/ssl/privkey.pem
  ssl_certificate: /srv/homeassistant/lib/ssl/fullchain.pem
```
base_url: - внешний адрес Home assistant. <br>
ssl_key: - ssl ключ. <br>
ssl_certificate: - ssl сертификат. <br>
## google_assistant: - настройка google assistant.
```
google_assistant:
  project_id: project_homeassistant 
  service_account: !include SERVICE_ACCOUNT.JSON
  report_state: true
  exposed_domains:
    - switch
    - light
```
project_id: - [id проекта](https://console.actions.google.com/ "подробнее на console.actions.google.com"). <br>
service_account: - [google service account key](https://console.cloud.google.com/apis/credentials/serviceaccountkey "подробнее на console.actions.google.com"). <br>
report_state: - Сообщать в Google Assistant о изменениях. <br>
exposed_domains: - Список сущностей(выключатели,лапочки) передоваемых Сообщать в Google. <br>
подробнее: [www.home-assistant.io](https://www.home-assistant.io/integrations/google_assistant/). <br>
## lovelace - настройка интерфейса (авто или нет).
```
lovelace:
	mode: yaml
```
mode: yaml - Отключает автоинтерфейс. (теперь интерфейс берется из файла ui-lovelace.yaml, его нужно создать). <br>
## binary_sensor: - бинарный сенсор. 
```
binary_sensor:
  - platform: ping
    host: 192.168.0.254
    name: Router
    count: 2
    scan_interval: 300
```
 platform: ping - сенсор ping. (пинует ip адрес). <br>
 host: - ip адрес. <br>
 name: - Кого пингуем (название для интерфеса). <br>
 count: - Количество повторов в запросе. <br>
 scan_interval: - Интервал между запросами. <br>
## sensor: - какой либо датчик.
```
sensor:
  - platform: systemmonitor			# Системный монитор
    resources:					# Ресурсы(ниже)
    - type: processor_use			# Процессор.
    - type: memory_use_percent			# Оператива.
    - type: disk_free				# Диск.
      arg: /					# Какой именно раздел.
	  
  - platform: command_line						# shell запрос.
    name: CPU Temperature						# Имя для интерфейса.
    command: "cat /sys/class/thermal/thermal_zone0/temp"		# Температура GPU.
    unit_of_measurement: "°C"						#
    value_template: '{{ value | multiply(0.001) | round(1) }}'		#
```
