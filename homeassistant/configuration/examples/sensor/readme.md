# раздел sensor: в файле./configuration.yaml

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
