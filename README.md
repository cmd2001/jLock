# jLock
Python Script to Open SJTU Dormitory Smart Lock

可以解锁交大智能寝室门锁的Python代码

本项目旨在提供一个思路原形 以便大家后续开发接入 iOS自动化/米家/Apple Homekit

## 使用教程

### 环境依赖

```
pysjtu
requests
```

可通过 `python3 -m pip install -r ./requirements.txt` 一键安装

### 配置修改

打开`config.py`

```python
JACCOUNT_USERNAME = 'Amagi_Yukisaki' # 这里填入你的jAccount用户名 不含'@sjtu.edu.cn'
JACCOUNT_PASSWORD = 'PASSW0RD' # 这里填入你的jAccount密码
ROOM_ID = '00112233445566778899aabbccddeeff' # 扫描你的门上的二维码 识别结果'roomid='后面的字符串
```

### 运行

`python3 ./main.py`即可开门！

## 二次开发

鼓励大家利用本项目二次开发 将交大智能门锁接入各大智能家居平台

## 鸣谢

[@PhotonQuantum](https://github.com/PhotonQuantum) for [pysjtu](https://github.com/PhotonQuantum/pysjtu)

## 许可证

MIT许可