# Network scanning tools
## How to use
pythonランタイムのパッケージにscapyを入れる。
```pip install scapy```, または ```conda install scapy```

## 概要
ホストスキャンは```PingScanner.py``` または```ArpScan``` ( ```ArpScan```のほうが高速 )
ポートスキャンは```PortScan.py```を利用。  
語句の意味が分からないは使用しないほうがいいと思います

## PingScanner.py
使用法
```bash
python PingScanner.py
```
処理画面
```
Input this hosts IP addr :192.168.1.2
Netmask :255.255.255.0
192.168.1.0/24
Trying to 192.168.1.1
Begin emission:
..Finished sending 1 packets.
.*
Received 4 packets, got 1 answers, remaining 0 packets
Trying to 192.168.1.2
...
```
実行結果
```
....
192.168.1.1     is up
192.168.1.3     is up
192.168.1.4     is up
192.168.1.9     is up
```

## ArpScan.py
使い方
```bash
python ArpScanner.py
```
実行画面
```
Input this IP address: 192.168.1.2
Input this netmask: 255.255.255.0
Scanning on: 192.168.1.0/24

Begin emission:
..*.........*........*..............*.............................................................................................................................................................................................................................................Finished sending 256 packets.
................................................................................
Received 354 packets, got 4 answers, remaining 252 packets
```
結果
```
192.168.1.1 is up
192.168.1.9 is up
192.168.1.4 is up
192.168.1.3 is up
```
## PortScan.py
使い方
```bash
python PortScan.py localhost
```
処理中はなにも出ないので注意

結果
```
1       2       3       4       5       6       7       8       9       10      11      12      13      14      15      16      17      18      19      20      21      22      23      24      25      26      27       28      29      30      31      32      33      34      35      36      37      38      39      40      41      42      43      44      45      46      47      48      49      50      51      52      53       54      55      56      57      58      59      60      61      62      63      64      65      66      67      68      69      70      71      72      73      74      75      76      77      78      79 ...
```
今回はポート開けていないので面白い結果は特にありません。
