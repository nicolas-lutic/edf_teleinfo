edf_teleinfo
============


Enable serie port
sudo nano /boot/cmdline.txt

replace this line  :
```shell
dwc_otg.lpm_enable=0 console=ttyAMA0,115200 kgdboc=ttyAMA0,115200 console=tty1
root=/dev/mmcblk0p2 rootfstype=ext4 elevator=deadline rootwait
```
by : 
```shell
dwc_otg.lpm_enable=0 console=tty1 root=/dev/mmcblk0p2 rootfstype=ext4
elevator=deadline rootwait
```
```shell
sudo nano /etc/inittab
```
comment :
```shell
T0:23:respawn:/sbin/getty -L ttyAMA0 115200 vt100
```
Restart the Raspberry
```shell
sudo reboot
```

Test : 
Port série :
```shell
stty -F /dev/ttyAMA0 1200 sane evenp parenb cs7 clocal -crtscts

echo A > /dev/ttyAMA0
cat /dev/ttyAMA0

echo B > /dev/ttyAMA0
cat /dev/ttyAMA0
```
######### Supervisor 

```shell
sudo apt-get install supervisor

sudo vi  /etc/supervisor/supervisord.conf

[program:tiRpiRomToCsv.py]
command=/usr/bin/tiRpiRomToCsv.py
process_name=tiRpiRomToCsv
stdout_logfile=NONE

sudo supervisorctl
restart
```

######### Send Mail with raspberry


```bash
sudo apt-get install ssmtp mailutils mpack

vi /etc/ssmtp/ssmtp.conf
```

```bash
mailhub=smtp.gmail.com:587
hostname=ENTER YOUR RPI'S HOST NAME HERE
AuthUser=YOU@gmail.com
AuthPass=PASSWORD
useSTARTTLS=YES
```


