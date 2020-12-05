# root 执行

## 配置
# 将此文件复制到 /etc
# gammu-detect 检测硬件
# udevadm info /dev/ttyUSB0 查看usb设备的id 查看ID_PATH
# 或者使用 ls -l /sys/class/tty/ 查看

# sim 检查
#  gammu --identify
#  gammu -s 1 --identify
#  gammu -s 2 --identify
#  gammu -s 3 --identify

# 短信文件夹
mkdir -p /home/sms/inbox/5650
mkdir -p /home/sms/inbox/6910
mkdir -p /home/sms/inbox/6912
mkdir -p /home/sms/inbox/6913
mkdir -p /home/sms/inbox/3601
mkdir -p /home/sms/inbox/8059
mkdir -p /home/sms/inbox/test
chmod -R 777 /home/sms

apt install gammu
apt install gammu-smsd

cp ./conf/gammurc /etc/gammurc

cp ../conf/gammu-6910.service /etc/systemd/system/gammu-6910.service
cp ../conf/gammu-6912.service /etc/systemd/system/gammu-6912.service
cp ../conf/gammu-6913.service /etc/systemd/system/gammu-6913.service
cp ../conf/gammu-5650.service /etc/systemd/system/gammu-5650.service

systemctl daemon-reload

systemctl start gammu-6910
systemctl start gammu-6912
systemctl start gammu-6913
systemctl start gammu-5650

cp ./conf/99-com.rules /etc/udev/rules.d/99-com.rules
