root 用户执行 init.sh 安装 gammu gammu-smsd, cp gammurc 到/etc

gammurc中有相关配置


## 配置
将gammurc文件复制到 /etc

gammu-detect 检测硬件

udevadm info /dev/ttyUSB0 查看usb设备的id 查看ID_PATH

或者使用 ls -l /sys/class/tty/ 查看


## 编辑文件添加绑定:
sudo vim /etc/udev/rules.d/99-com.rules 编辑此文件绑定usb串口

SUBSYSTEM=="tty", ENV{ID_PATH}=="platform-3f980000.usb-usb-0:1.4:1.0", SYMLINK+="ttyUSB_sms_5650"

SUBSYSTEM=="tty", ENV{ID_PATH}=="platform-3f980000.usb-usb-0:1.2:1.0", SYMLINK+="ttyUSB_sms_6910"

SUBSYSTEM=="tty", ENV{ID_PATH}=="platform-3f980000.usb-usb-0:1.3:1.0", SYMLINK+="ttyUSB_sms_6912"

SUBSYSTEM=="tty", ENV{ID_PATH}=="platform-3f980000.usb-usb-0:1.5:1.0", SYMLINK+="ttyUSB_sms_6913"

##  sim 检查
gammu --identify

gammu -s 1 --identify

gammu -s 2 --identify

gammu -s 3 --identify
