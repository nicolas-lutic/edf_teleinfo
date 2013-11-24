edf_teleinfo
============


Enable serie port
sudo nano /boot/cmdline.txt

replace this line  :
dwc_otg.lpm_enable=0 console=ttyAMA0,115200 kgdboc=ttyAMA0,115200 console=tty1
root=/dev/mmcblk0p2 rootfstype=ext4 elevator=deadline rootwait

by : 
dwc_otg.lpm_enable=0 console=tty1 root=/dev/mmcblk0p2 rootfstype=ext4
elevator=deadline rootwait

sudo nano /etc/inittab
comment : 
T0:23:respawn:/sbin/getty -L ttyAMA0 115200 vt100

sudo reboot

Test : 
Port série :
stty -F /dev/ttyAMA0 1200 sane evenp parenb cs7 clocal -crtscts

echo A > /dev/ttyAMA0
cat /dev/ttyAMA0

echo B > /dev/ttyAMA0
cat /dev/ttyAMA0
