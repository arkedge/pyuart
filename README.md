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