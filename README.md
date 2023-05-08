# UART-RTx for PC

## 概要

PC/RaspberryPiのUART線から出てくる生信号を直接ロジアナで観測するために作成したコードたちです。
つまりUARTプロトコルを電圧の上下のレベルでリバースエンジニアリングするために使っています。

FPGA-UARTデバッグが必要になった時には、PC/RaspberryPiをFPGA対向デバイスとして使えると良いでしょう。



## 動作環境

動作確認済みの実機環境
- PC
  - CPU: Intel Core i7-12700
  - OS: Ubuntu 22.04.2 LTS
- Python 3.10.6
- QinHeng Electronics CH340 serial converter


## サンプル


### 例1: 1 octetづつTx(送信)したい場合

```
from aelib import uart

u0 = uart.uart(dev='/dev/ttyUSB0', baudrate = 115200, timeout = 15)
u0.open()

u0.tx(1)
u0.tx(2)
u0.tx(77)

u0.close()

```

### 例2: 1 octetづつRx(受信)したい場合

```
import time
from aelib import uart

u0 = uart.uart(dev='/dev/ttyS0', baudrate = 115200, timeout = 240)
u0.open()

while True:
    rx_data = u0.rx()
    if True == rx_data['is_valid']:
        print ('0x%02X, %s' % (rx_data['int'], rx_data['byte']))
    else:
        time.sleep (1)

u0.close()
```

### 例3: ファイルをTx(送信)したい場合

```
from aelib import uart

u0 = uart.uart(dev='/dev/ttyUSB0', baudrate = 115200, timeout = 15)
u0.open()

u0.tx_file(filename = '/tmp/file.bin')

u0.close()

```

### 例4: ファイルをRx(受信)したい場合

```
from aelib import uart

u0 = uart.uart(dev='/dev/ttyUSB0', baudrate = 115200, timeout = 15)
u0.open()

u0.rx_file(filename = './recv.bin', n_byte = 1048576)

u0.close()

```

**注意**

ファイルのRx(受信)では事前に受信したいファイルのサイズをn_byteで指定する必要があります。
上記の例では ```n_byte = 1048576```を指定することで1Mbyteのファイルを受信することを指定しています。


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

### とあるubuntu22 PCでの/dev/serial

```
hamada@ci01:~/git/pyuart$ ls -l /dev/serial/by-id/usb-1a86_USB_Serial-if00-port0
lrwxrwxrwx 1 root root 13  4月 30 14:58 /dev/serial/by-id/usb-1a86_USB_Serial-if00-port0 -> ../../ttyUSB0
```

## 練習問題

### 問1. 次の信号線の電圧を見てUARTプロトコルでなんと言っているか答えてください

```
HHHHHHLLHHLLHHLHLHLHLHHHLHLHHLLLHHLHLHHLHLHHLHLLLLLLLHLHLHLHLHHHLHHHHHHH
```

解答:

```
       0x66,      0x75,      0x63,      0x6B,      0x40,      0x75
HHHHHH LLHHLLHHLH LHLHLHHHLH LHHLLLHHLH LHHLHLHHLH LLLLLLLHLH LHLHLHHHLH HHHHHH
```
