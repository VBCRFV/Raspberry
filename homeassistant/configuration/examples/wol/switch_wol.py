#!/usr/bin/python3
from wakeonlan import send_magic_packet
import sys

def ping(ip):
    import os
    return int(not bool(os.system("ping -c 1 " + ip + " > /dev/null")))

if __name__ == "__main__":
  if len(sys.argv) == 4:
    ip = sys.argv[2]
    mac = sys.argv[3]
    if sys.argv[1] == 'off':
      pass
    elif sys.argv[1] == 'on':
      send_magic_packet(mac)
    elif sys.argv[1] == 'state':
      print(ping(ip))
  else:
    print('Кол-во аргументов, не равно трём.')
    print('Пример: switch_wol.py on 192.168.0.1 MA-C0-AD-DR-ES-S0')
    print(sys.argv)