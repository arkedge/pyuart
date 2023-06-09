# pyuart

## 概要

UARTデバッグをpythonスクリプトで行うためのモジュールです。これまで
Tera-termやArduino IDEコンソールなどでライトウェイトにUARTデバッグをし
ていた人が、リモートデバッグ環境を構築したり、並列UART高負荷耐久テスト
等々、もう少し突っ込んだUARTデバッグをしたい時に効果を発揮するはずです。

## 動作環境

動作確認済みの実機環境
- Python 3.10.6
- PC
  - CPU: Intel Core i7-12700
  - OS: Ubuntu 22.04.2 LTS
- Raspberry Pi 4 Model B Rev 1.5
  - CPU: BCM2835
  - OS: Ubuntu 22.04.2 LTS
- USB-TTL converter
  - QinHeng Electronics CH340 serial converter
  - Future Technology Devices International, Ltd FT232 Serial (UART) IC

## 前提

```1 Byte == 1 Octet == 8 bit```

## Installation

```
pip install pyuart
sudo chmod 666 /dev/ttyUSB0
```

上記例のデバイスファイル名 ```/dev/ttyUSB0```は環境依存です。ご自身の環境に対応したデバイスファイル名をご指定ください。


## サンプル

```pyuart```モジュールの操作方法のサンプルコードを以下にメモしておきます。
このサンプルを見るだけで動かすことができるはずですが、詳細な説明は後日記載する予定です。


### 例1: 1 octetづつTx(送信)したい場合

```:test_tx.py
from pyuart import uart

u0 = uart(dev='/dev/ttyUSB0', baudrate = 115200, timeout = 15)
u0.open()

u0.tx(1)
u0.tx(2)
u0.tx(77)

u0.close()

```

### 例2: 1 octetづつRx(受信)したい場合

```:test_rx.py
from pyuart import uart

u0 = uart(dev='/dev/ttyS0', baudrate = 115200, timeout = 240)
u0.open()

for data in u0.rx():
    print (data)

u0.close()

```

※: rx()メソッドはジェネレータです。

### 例3: ファイルをTx(送信)したい場合

```:sample.tx.file.py
from pyuart import uart

u0 = uart(dev='/dev/ttyUSB0', baudrate = 115200, timeout = 15)
u0.open()

u0.tx_file(filename = '/tmp/file.bin')

u0.close()

```

### 例4: ファイルをRx(受信)したい場合

```sample.rx.file.py
from pyuart import uart

u0 = uart(dev='/dev/ttyUSB0', baudrate = 115200, timeout = 15)
u0.open()

u0.rx_file(filename = './recv.bin', n_byte = 1048576)

u0.close()

```

**ファイルRxでの注意事項**

UARTを使ったデータ通信では受け取るファイルのサイズは上位プロトコル層で定義しておかなければファイルサイズを事前に知ることができません。
そのため上位プロトコルを定義していない本モジュールでは、ファイルのRx(受信)実行時に受信ファイルサイズをn_byteで指定する必要があります。
上記のサンプル例では ```n_byte = 1048576```を指定しています。これは1MB(1048576 Byte)のファイルを受信することを指定しています。

(なお、この文章では```1 octet = 1 byte```を仮定しています)



### 例5: 並列Txの実行 (MPI利用)

```mpi.tx.py
#!/usr/bin/env python3
from mpi4py import MPI
from pyuart import uart

comm = MPI.COMM_WORLD
proc_id = comm.Get_rank()
nproc = comm.Get_size()
hostname = MPI.Get_processor_name()

devfile = "/dev/ttyUSB%d" % proc_id
print(devfile, flush=True)

u0 = uart(dev=devfile, baudrate = 115200, timeout = 15)
u0.open()
u0.tx(123)

u0.close()

```

並列実行は```make mpirun```や以下のようにmpirunコマンドを使います。
```
 mpirun -np 4 --oversubscribe mpi.tx.py
```




## 注意

Ubuntu 22ではCH341チップを使ったUSB-serialコンバーターはそのままでは動きません。
```
sudo apt remove brltty
```
にてbrlttyを削除してから使用しましょう。


[参考|https://stackoverflow.com/questions/70123431/why-would-ch341-uart-is-disconnected-from-ttyusb]

```
For Ubuntu 22.04 the simplest solution is to remove the package brltty
via sudo apt remove brltty, since its unnecessary unless you're using
a braille e-reader, however unsure if it could cause errors later on.
```

## 参考

### ubuntu22 PCでの/dev/serialの一例

```
arkedge@ci01:~/git/pyuart$ ls -l /dev/serial/by-id/usb-1a86_USB_Serial-if00-port0
lrwxrwxrwx 1 root root 13  4月 30 14:58 /dev/serial/by-id/usb-1a86_USB_Serial-if00-port0 -> ../../ttyUSB0
```

