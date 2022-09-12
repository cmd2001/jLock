# jLock

Python Script to Open SJTU Dormitory Smart Lock

可以解锁交大智能寝室门锁的 Python 代码

本项目旨在提供一个思路原形 以便大家后续开发接入 iOS 自动化/米家/Apple Homekit

## 使用教程

### 快速启动本项目

**推荐 Python 版本: 3.9-3.10**

#### 安装依赖

```plain
pysjtu
requests
```

可通过 `python3 -m pip install -r ./requirements.txt` 一键安装

#### 本地配置

修改`src/config.py`

```python
JACCOUNT_USERNAME = 'Amagi_Yukisaki' # 这里填入你的jAccount用户名 不含'@sjtu.edu.cn'
JACCOUNT_PASSWORD64 = 'PASSW0RD' # 这里填入你的jAccount密码的base64编码
ROOM_ID = '00112233445566778899aabbccddeeff' # 扫描你的门上的二维码 识别结果'roomid='后面的字符串，这里扫描结果会是40位，需要删除后8位
```

**密码 base64 编码获取方式**

```plain
(base) Amagi@iMacPro ~ $ python3
Python 3.9.12 (main, Apr  5 2022, 01:53:17)
[Clang 12.0.0 ] :: Anaconda, Inc. on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import base64
>>> base64.b64encode(b'PASSW0RD')
b'UEFTU1cwUkQ='
```

**ROOM_ID 获取方式**

扫描门上二维码，复制`roomid=`后的字符串，**删去最后 8 位**。

### 运行

`python3 ./src/unlock.py`

### 远程部署(基于 Shell)

你需要的物品

- 一台可以 ssh 远程访问的服务器
- 一个可以远程执行 ssh 命令的自动化工具(例: iOS 快捷指令)

推荐使用`venv`为项目创建虚拟环境，并避免对同一服务器上其他应用的影响

**所有命令默认运行在项目根目录下**

#### 创建环境

##### 安装 venv

```shell
sudo apt install python3-venv # for Debian and Ubuntu
sudo yum install python3-virtualenv # for CentOS and Fedora
sudo pacman -S python-virtualenv # for Arch Linux and Manjaro
```

##### 创建虚拟环境

```shell
python3 -m venv venv
```

此操作将在当前目录下创建名为`venv`的文件夹和虚拟环境

##### 安装依赖

```shell
./venv/bin/activate
pip install -r ./requirements.txt -i https://mirror.sjtu.edu.cn/pypi/web/simple
```

#### 修改配置

##### 修改`src/config.py`

同[本地配置](####本地配置)

##### 修改 `scripts/*.sh`

将

```shell
cd /home/automaton/jLock # your project directory
```

修改为你项目根目录的**绝对路径**

#### 运行

调用脚本

```shell
/home/automaton/jLock/scripts/[unlock/status/refresh_session.sh]
```

即可

##### 脚本作用

- `unlock.sh`: 开锁
- `status.sh`: 检查锁的状态，返回`0`表示开启，`1` 表示关闭(仅包含本地脚本开锁的状态，也就是说，如果通过其他方式，比如扫码开锁，这里仍会显示为锁定)
- `refresh_session.sh`: 强行刷新登录状态，可加入 `crontab` 定时任务用于加快每次开锁速度

### 远程部署(基于 Home Assistant)

本部分仍待完善，这里先简单贴一个配置文件

```yaml
switch:
  - platform: command_line
    scan_interval: 0.5
    switches:
      door_lock:
        command_state: /home/automaton/jLock/script/status.sh
        command_on: /home/automaton/jLock/script/unlock.sh
        unique_id: io.yukisaki.jlock.whateveryoulike

lock:
  - platform: template
    name: Door Lock
    value_template: "{{ is_state('switch.door_lock', 'off') }}"
    unlock:
      service: switch.turn_on
      target:
        entity_id: switch.door_lock
    lock:
      service: switch.turn_off
      target:
        entity_id: switch.door_lock
```

## 二次开发

鼓励大家利用本项目二次开发 将交大智能门锁接入各大智能家居平台

## 鸣谢

[@PhotonQuantum](https://github.com/PhotonQuantum) for [pysjtu](https://github.com/PhotonQuantum/pysjtu)

## 许可证

MIT 许可
