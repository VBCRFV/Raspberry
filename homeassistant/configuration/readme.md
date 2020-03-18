# ./configuration.yaml - файл конфигурации Home assistant
# http:
```
http:
  base_url: https://domen.duckdns.org
  ssl_key: /home/user/.homeassistant/privkey.pem
  ssl_certificate: /home/user/.homeassistant/fullchain.pem
```
## google_assistant:
```
google_assistant:
  project_id: project_homeassistant 
  service_account: !include SERVICE_ACCOUNT.JSON
  report_state: true
  exposed_domains:
    - switch
    - light
```
google_assistant: - как бы не пародоксально это звучало: настройка google assistant. <br>
project_id: - id проекта [https://console.actions.google.com/]. <br>
service_account: - google service account key [https://console.cloud.google.com/apis/credentials/serviceaccountkey]. <br>
report_state: - Сообщать в Google Assistant о изменениях.
exposed_domains: - Список сущностей(выключатели,лапочки) передоваемых Сообщать в Google. <br>
подробнее: [https://www.home-assistant.io/integrations/google_assistant/] . <br>
## lovelace
```
lovelace:
	mode: yaml
```
lovelace: настройка интерфейса (авто или нет). <br>
mode: yaml - Отключает автоинтерфейс. (теперь интерфейс берется из файла ui-lovelace.yaml, его нужно создать). <br>
## binary_sensor:
```
binary_sensor:
  - platform: ping 			# сенсор ping. (пинует ip адрес)
    host: 192.168.0.254		# ip адрес
    name: Router			# Кого пингуем (название для интерфеса)
    count: 2				# Количество повторов в запросе.
    scan_interval: 300		# Интервал между запросами.
```
binary_sensor: - бинарный сенсор. <br>
 platform: ping 		# сенсор ping. (пинует ip адрес)
 host: 192.168.0.254	# ip адрес
 name: Router			# Кого пингуем (название для интерфеса)
 count: 2				# Количество повторов в запросе.
 scan_interval: 300		# Интервал между запросами.
## sensor:
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
