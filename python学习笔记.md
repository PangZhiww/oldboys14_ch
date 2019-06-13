老男孩python14期全栈

# 第一部分	基础部分(基础 + 函数) day01---day15

## day 01 / day 02

​		(数据类型 / 变量的命名规则 / if 语句 / while 循环 / 格式化输出 / 运算符)	

### 一 . 变量的命名规范 :

`````
字母, 数字, 下划线组成
不能是关键字
不能是数字, 更不能是纯数字组成
不要用中文
不要太长
要有意义
区分大小写
推荐驼峰和下划线命名方法
`````

### 	二. 数据类型

  1. #### int 类型

     * 整数	可以进行 + - * / % // 运算

       

  2. #### str 类型

     * 字符串 + *

       

  3. #### bool 类型

     * 取值 
     * True
     * False

4. #### 用户交互

   * s = input("提示语")	接收到的是字符串类型

   * 类型转换: int(str)

     

5. #### if 语句

   * if 条件

     ​	代码块

     else:

     ​	代码块

   * if 条件

     ​	代码块

     elif 条件

     ​	代码块

     elif 条件

     ​	代码块

     ......

     else:

     ​	代码块

   

6. #### 循环语句 while循环

   * while 条件:

     ​	代码块(循环体)

   * 执行流程

     1. 判断条件是否为真, 如果为真, 执行代码块
     2. 再次判断条件是否为真 ....
     3. 当条件为假, 执行else, 跳出循环, 循环结束

     

7. #### 格式化输出

   * %s 字符串的占位符, 可以放置任何内容.

   * %d 数字的占位符, 可以放置任何内容.

     

8. #### 运算符---逻辑运算

   * ( ) --> not --> and ---> or

   * and : 并且的意思, 左右两端的值必须都是真, 运算结果才是真

   * or : 或者的意思, 左右两端有一个是真, 结果就是真. 只有全部为假, 结果才是假

   * not : 非得意思, 原来是假, 现在是真. 非真既假, 非假既真

   * break    结束循环    停止当前本层循环

   * continut    结束当前本次循环, 继续执行下一次循环. 

   * ````
     print(X or Y) X or Y 如果 x=0 那么就是 Y 否则就是 X
     print(X and Y) X or Y 如果 x=0 那么就是 X 否则就是 Y
     ````

   * 

9. PS

   

## day03

( 基本数据类型概述 )

### 一. 数据类型

1. int 整数
2. bool 布尔
3. tuple 元祖, 只读列表, 不能更改
4. dict  字典: 一对一的存储的数据
   1. key: value	{"东阳": "大秧歌","joy": "周杰伦"}
5. set: 集合    储存不重复的内容
6. str 字符串
7. list 列表
   1. ["大秧歌", "东阳哥"]



### 二. 类型转换

1. #### int 类型

   * int()

   * bit_length( )	求二进制的长度

2. #### bool 类型

   * 你想转换成什么, 就用什么把目标包裹起来	bool()

3. #### str 类型

   1. ##### str 索引和切片

      * 索引: 起始下标是 0 (从左到右), -1 从右向左

      * 切片: s[起始位置: 结束位置: 步长]

        ​	特点: 顾头不顾尾

   2. ##### 字符串的常用操作; 常用方法    * 字符串不可变

      * upper() 转换为大写
      * strip() 去掉空格
      * replace() 替换
      * split() 切割
      * format() 格式化输出
      * startswith() 判断是否以XXX开头
      * endswith() 判断是否以XXX结尾
      * find() 查找, 差找不到返回 -1
      * len() 内置函数, 求字符串长度    直接使用, 不用使用 . (点) 来操作

   3. ##### 迭代

      1. ````
         for 变量 in 可迭代对象:
         	循环体
         else:
         	循环体
         ````

      2. .



## day 04 list / tuple常用功能

​	(list常用功能 / 常用方法 / list 的嵌套 / tuple 元祖 / rang() / )

### 一. list 常用功能

1. 增
   * append ()
   * insert()    (位置,"XXX")放入指定位置
   * extend([ ])    迭代添加
2. 删
   * remove()
   * pop()
   * clear()
   * 
3. 改
4. 查



## day 05



## day 06 



# 第二部分 面向对象 day16 -- day 29

## day16



## day 17



## day 18



# 第三部分 网络编程与并发编程	day30 -- day 40 (女神老师)

## day 30 	 tcp协议socket初识

### 一、引子

```
# qq 微信 飞秋 网游 微博 歪歪  _基于应用的网络程序
# 百度 微博 知乎 博客园 网易   _基于浏览器的网络程序

# 网络编程中的 - C/S 架构
    # c client  客户端
    # s server  服务端
# 网络编程中的 - B/S 架构
    # b broser  浏览器
    # s server  服务端
    # 不需要额外的安装客户端了,只需要一个网址就可以访问
    # 轻量级  - 使用成本低
# B/S架构是C/S架构的一种特殊形式
# 手机上 : 浏览器 app

# 两个py程序想要通信
    # 写文件
# 在不同机器上的两个py程序之间想要通信
    # 网络

# 网络的发展史
    # 网卡\网口
    # 两台机器之间 插上网线就可以通信
    # 网卡上 - mac地址
    # ip地址
        # 是4个点分十进制  - ipv4协议
            # 0.0.0.0 - 255.255.255.255
            # 127.0.0.1 本机
            # 内网字段 192.168.****
                    #  10.****
                    #  172.***
        # 6个点分十进制  - ipv6协议
            # 0.0.0.0.0.0  - 255.255.255.255.255.255
    # 交换机
        # 广播
        # 单播
        # 组播
    # arp协议 : 通过IP地址获取某一台机器的mac地址
    # 子网掩码
        # 子网掩码 和 ip地址进行 按位 与 运算 就能得出一个机器所在的网段
        # 192.168.21.36
        # 11000000.10101000.00010101.00100100
        # 255.255.255.0   255.255.0.0
        # 11111111.11111111.11111111.00000000
        # 11000000.10101000.00010101.00000000
        # 192.168.21.0 网段
    # 网关地址 : 整个局域网中的机器能沟通过网关ip与外界通信
    # 网段 : 子网掩码 和 ip地址进行 按位 与 运算
    # 端口 : 0-65535
        # 8000-酷狗音乐  22-ssh  3306-mysql
        # python 网络应用  8000
        # ip地址+端口号 : 在全网找到唯一的一台机器+唯一的应用
        # 我们选择端口 : 8000之后
    # tcp协议
        # 全双工的通信协议
            # 一旦连接建立起来,那么连接两端的机器能够随意互相通信
            # 面向连接的通信方式
            # 数据安全不容易丢失
            # 建立连接的 三次握手 ******
            # 断开连接的 四次挥手 ******
```

### 二、socket 模块

```
socket.socket(family=AF_INET,type=SOCK_STREAM,proto=0,fileno=None)
```

##### 	参数说明

| **family** | 地址系列应为AF_INET(默认值),AF_INET6,AF_UNIX,AF_CAN或AF_RDS。 （AF_UNIX 域实际上是使用本地 socket 文件来通信） |
| ---------- | ------------------------------------------------------------ |
| **type**   | 套接字类型应为SOCK_STREAM(默认值),SOCK_DGRAM,SOCK_RAW或其他SOCK_常量之一。 **SOCK_STREAM** 是基于TCP的，有保障的（即能保证数据正确传送到对方）面向连接的SOCKET，多用于资料传送。  **SOCK_DGRAM** 是基于UDP的，无保障的面向消息的socket，多用于在网络上发广播信息。 |
| **proto**  | 协议号通常为零,可以省略,或者在地址族为AF_CAN的情况下,协议应为CAN_RAW或CAN_BCM之一。 |
| **fileno** | 如果指定了fileno,则其他参数将被忽略,导致带有指定文件描述符的套接字返回。 与socket.fromfd()不同,fileno将返回相同的套接字,而不是重复的。 这可能有助于使用socket.close()关闭一个独立的插座。 |

### 三、基于TCP协议的socket模块

##### server 代码案例

``````
import socket

sk = socket.socket()    # 买手机
sk.bind("ip",port_端口号)   # 绑定手机卡
sk.bind(('127.0.0.1',8898))   # 绑定手机卡   有了手机号
sk.listen()     # 监听 等着有人给我打电话

conn,addr = sk.accept()     # 接听别人的电话   connection - 连接, address - 地址
ret = conn.recv(1024)     # 听别人说话 括号内是1024的整数倍  听别人说多少字节
print(ret)
conn.send(b"hello")     # 和别人说话, 必须传一个bytes类型
conn.close()    # 挂电话
sk.close()      # 关机
``````



##### client 端案例

``````
import socket

sk = socket.socket()  # 买手机
sk.connect(("127.0.0.1", 8898))  # 拨号

sk.send(b"hello word")
ret = sk.recv(1024)  # 听别人说话
print(ret)  # 和别人说话, 必须传一个bytes类型
sk.send(bytes("中午吃什么?",encoding=("utf-8")))
ret = sk.recv(1024)
print(ret.decode("utf-8"))
sk.close()
``````

##### 注:

​	tcp是基于链接的，必须先启动服务端，然后再启动客户端去链接服务端

#### 问题：有的同学在重启服务端时可能会遇到端口被占用的问题

##### win 系统方法

![img](https://images2017.cnblogs.com/blog/827651/201711/827651-20171109174833325-1552312354.png)

* ``````
  #加入一条socket配置，重用ip和端口
  import socket
  from socket import SOL_SOCKET,SO_REUSEADDR
  sk = socket.socket()
  sk.setsockopt(SOL_SOCKET,SO_REUSEADDR,1) #就是它，在bind前加
  sk.bind(('127.0.0.1',8898))  #把地址绑定到套接字
  sk.listen()          #监听链接
  conn,addr = sk.accept() #接受客户端链接
  ret = conn.recv(1024)   #接收客户端信息
  print(ret)              #打印客户端信息
  conn.send(b'hi')        #向客户端发送信息
  conn.close()       #关闭客户端套接字
  sk.close()        #关闭服务器套接字(可选)
  ``````

  ##### 其他系统方法 :
  
  * Unix系统可以找到占用端口的进程
  * lsof -i:8898
  * kill it

## day 31	udp的socket服务和黏包现象

### 一、基于UDP协议的socket模块

##### server 端

```
import socket
udp_sk = socket.socket(type=socket.SOCK_DGRAM)   #创建一个服务器的套接字
udp_sk.bind(('127.0.0.1',9000))        #绑定服务器套接字
msg,addr = udp_sk.recvfrom(1024)
print(msg)
udp_sk.sendto(b'hi',addr)                 # 对话(接收与发送)
udp_sk.close()                         # 关闭服务器套接字
```

##### 服务端说明 :

* udp的server 不需要进行监听也不需要建立连接
* 在启动服务之后只能被动的等待客户端发送消息过来
* 客户端发送消息的同时还会自带地址信息
* 消息回复的时候, 不仅需要发送消息, 还需要把自己的地址填写过去

##### client 端

```
import socket
ip_port=('127.0.0.1',9000)
udp_sk=socket.socket(type=socket.SOCK_DGRAM)
udp_sk.sendto(b'hello',ip_port)
back_msg,addr=udp_sk.recvfrom(1024)
print(back_msg.decode('utf-8'),addr)
```



### 二、基于UDP协议的QQ 聊天

#### server 端

``````
import socket

sk = socket.socket(type=socket.SOCK_DGRAM)
sk.bind(("127.0.0.1", 8080))
while 1:
    msg, addr = sk.recvfrom(1024)
    print(addr)
    print(msg.decode("utf-8"))
    info = input(">>>").encode("utf-8")
    sk.sendto(info, addr)
sk.close()
``````



#### client 端

``````
import socket

sk = socket.socket(type=socket.SOCK_DGRAM)
ip_prot = ("127.0.0.1", 8080)
while 1:
    info = input("大哥:")
    info = ("\033[32m来自大哥的消息: %s\033[0m" % info).encode("utf-8")
    sk.sendto(info, ip_prot)
    msg, addr = sk.recvfrom(1024)
    print(msg.decode("utf-8"))
sk.close()
``````



### 三、时间服务器

#### server 端

``````
# _*_coding:utf-8_*_
from socket import *
from time import strftime

ip_port = ('127.0.0.1', 9000)
bufsize = 1024

tcp_server = socket(AF_INET, SOCK_DGRAM)
tcp_server.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
tcp_server.bind(ip_port)

while True:
    msg, addr = tcp_server.recvfrom(bufsize)
    print('===>', msg)

    if not msg:
        time_fmt = '%Y-%m-%d %X'
    else:
        time_fmt = msg.decode('utf-8')
    back_msg = strftime(time_fmt)

    tcp_server.sendto(back_msg.encode('utf-8'), addr)

tcp_server.close()

server
``````



#### client 端

``````
#_*_coding:utf-8_*_
from socket import *
ip_port=('127.0.0.1',9000)
bufsize=1024

tcp_client=socket(AF_INET,SOCK_DGRAM)



while True:
    msg=input('请输入时间格式(例%Y %m %d)>>: ').strip()
    tcp_client.sendto(msg.encode('utf-8'),ip_port)

    data=tcp_client.recv(bufsize)

client
``````



### 四、黏包现象

​	同时执行多条命令之后，得到的结果很可能只有一部分，在执行其他命令的时候又接收到之前执行的另外一部分结果，这种显现就是黏包。

1. #### TCP协议

   ##### server端

   ```
   #_*_coding:utf-8_*_
   from socket import *
   import subprocess
   
   ip_port=('127.0.0.1',8888)
   BUFSIZE=1024
   
   tcp_socket_server=socket(AF_INET,SOCK_STREAM)
   tcp_socket_server.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
   tcp_socket_server.bind(ip_port)
   tcp_socket_server.listen(5)
   
   while True:
       conn,addr=tcp_socket_server.accept()
       print('客户端',addr)
   
       while True:
           cmd=conn.recv(BUFSIZE)
           if len(cmd) == 0:break
   
           res=subprocess.Popen(cmd.decode('utf-8'),shell=True,
                            stdout=subprocess.PIPE,
                            stdin=subprocess.PIPE,
                            stderr=subprocess.PIPE)
   
           stderr=res.stderr.read()
           stdout=res.stdout.read()
           conn.send(stderr)
           conn.send(stdout)
   
   tcp - server
   ```

   ##### client 端

   ```
   #_*_coding:utf-8_*_
   import socket
   BUFSIZE=1024
   ip_port=('127.0.0.1',8888)
   
   s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
   res=s.connect_ex(ip_port)
   
   while True:
       msg=input('>>: ').strip()
       if len(msg) == 0:continue
       if msg == 'quit':break
   
       s.send(msg.encode('utf-8'))
       act_res=s.recv(BUFSIZE)
   
       print(act_res.decode('utf-8'),end='')
   
   tcp - client
   ```

   

2. #### UDP协议

   ##### server 端

   ```
   #_*_coding:utf-8_*_
   from socket import *
   import subprocess
   
   ip_port=('127.0.0.1',9000)
   bufsize=1024
   
   udp_server=socket(AF_INET,SOCK_DGRAM)
   udp_server.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
   udp_server.bind(ip_port)
   
   while True:
       #收消息
       cmd,addr=udp_server.recvfrom(bufsize)
       print('用户命令----->',cmd)
   
       #逻辑处理
       res=subprocess.Popen(cmd.decode('utf-8'),shell=True,stderr=subprocess.PIPE,stdin=subprocess.PIPE,stdout=subprocess.PIPE)
       stderr=res.stderr.read()
       stdout=res.stdout.read()
   
       #发消息
       udp_server.sendto(stderr,addr)
       udp_server.sendto(stdout,addr)
   udp_server.close()
   
   udp - server
   ```

   ##### client 端

   ```
   from socket import *
   ip_port=('127.0.0.1',9000)
   bufsize=1024
   
   udp_client=socket(AF_INET,SOCK_DGRAM)
   
   
   while True:
       msg=input('>>: ').strip()
       udp_client.sendto(msg.encode('utf-8'),ip_port)
       err,addr=udp_client.recvfrom(bufsize)
       out,addr=udp_client.recvfrom(bufsize)
       if err:
           print('error : %s'%err.decode('utf-8'),end='')
       if out:
           print(out.decode('utf-8'), end='')
   
   udp - client
   ```

   #### 结论 :

   ##### 只有TCP有粘包现象，UDP永远不会粘包

   TCP会出现黏包现象, 但是不丢包

   UDP不会出现黏包现象, 但是会丢包

   

### 五、黏包成因

1. #### TCP协议中的数据传递

   ##### tcp协议的拆包机制 :

   - 当发送端缓冲区的长度大于网卡的MTU时，tcp会将这次发送的数据拆成几个数据包发送出去。

   - MTU是Maximum Transmission Unit的缩写。意思是网络上传送的最大数据包。MTU的单位是字节。 大部分网络设备的MTU都是1500。如果本机的MTU比网关的MTU大，大的数据包就会被拆开来传送，这样会产生很多数据包碎片，增加丢包率，降低网络速度。

     

   ##### 面向流的通信特点和Nagle算法

   - TCP（transport control protocol，传输控制协议）是面向连接的，面向流的，提供高可靠性服务。
     收发两端（客户端和服务器端）都要有一一成对的socket，因此，发送端为了将多个发往接收端的包，更有效的发到对方，使用了优化方法（Nagle算法），将多次间隔较小且数据量小的数据，合并成一个大的数据块，然后进行封包。
     这样，接收端，就难于分辨出来了，必须提供科学的拆包机制。 即面向流的通信是无消息保护边界的。 
     对于空消息：tcp是基于数据流的，于是收发的消息不能为空，这就需要在客户端和服务端都添加空消息的处理机制，防止程序卡住，而udp是基于数据报的，即便是你输入的是空内容（直接回车），也可以被发送，udp协议会帮你封装上消息头发送过去。 
     可靠黏包的tcp协议：tcp的协议数据不会丢，没有收完包，下次接收，会继续上次继续接收，己端总是在收到ack时才会清除缓冲区内容。数据是可靠的，但是会粘包。

     

   ##### **基于tcp协议特点的黏包现象成因** 

   - 发送端可以是一K一K地发送数据，而接收端的应用程序可以两K两K地提走数据，当然也有可能一次提走3K或6K数据，或者一次只提走几个字节的数据。
     也就是说，应用程序所看到的数据是一个整体，或说是一个流（stream），一条消息有多少字节对应用程序是不可见的，因此TCP协议是面向流的协议，这也是容易出现粘包问题的原因。
     而UDP是面向消息的协议，每个UDP段都是一条消息，应用程序必须以消息为单位提取数据，不能一次提取任意字节的数据，这一点和TCP是很不同的。
     怎样定义消息呢？可以认为对方一次性write/send的数据为一个消息，需要明白的是当对方send一条信息的时候，无论底层怎样分段分片，TCP协议层会把构成整条消息的数据段排序完成后才呈现在内核缓冲区。

     socket数据传输过程中的用户态与内核态说明

     

   例如基于tcp的套接字客户端往服务端上传文件，发送时文件内容是按照一段一段的字节流发送的，在接收方看了，根本不知道该文件的字节流从何处开始，在何处结束

   此外，发送方引起的粘包是由TCP协议本身造成的，TCP为提高传输效率，发送方往往要收集到足够多的数据后才发送一个TCP段。若连续几次需要send的数据都很少，通常TCP会根据优化算法把这些数据合成一个TCP段后一次发送出去，这样接收方就收到了粘包数据。

   

2. #### UDP不会发生黏包

   UDP（user datagram protocol，用户数据报协议）是无连接的，面向消息的，提供高效率服务。 
   不会使用块的合并优化算法，, 由于UDP支持的是一对多的模式，所以接收端的skbuff(套接字缓冲区）采用了链式结构来记录每一个到达的UDP包，在每个UDP包中就有了消息头（消息来源地址，端口等信息），这样，对于接收端来说，就容易进行区分处理了。 即面向消息的通信是有消息保护边界的。 
   对于空消息：tcp是基于数据流的，于是收发的消息不能为空，这就需要在客户端和服务端都添加空消息的处理机制，防止程序卡住，而udp是基于数据报的，即便是你输入的是空内容（直接回车），也可以被发送，udp协议会帮你封装上消息头发送过去。 
   不可靠不黏包的udp协议：udp的recvfrom是阻塞的，一个recvfrom(x)必须对唯一一个sendinto(y),收完了x个字节的数据就算完成,若是y;x数据就丢失，这意味着udp根本不会粘包，但是会丢数据，不可靠。

   

3. #### 补充说明

   * 用UDP协议发送时，用sendto函数最大能发送数据的长度为：65535- IP头(20) – UDP头(8)＝65507字节。用sendto函数发送数据时，如果发送数据长度大于该值，则函数会返回错误。（丢弃这个包，不进行发送） 

   * 用TCP协议发送时，由于TCP是数据流协议，因此不存在包大小的限制（暂不考虑缓冲区的大小），这是指在用send函数时，数据长度参数不受限制。而实际上，所指定的这段数据并不一定会一次性发送出去，如果这段数据比较长，会被分段发送，如果比较短，可能会等待和下一次数据一起发送。

     

4. #### 会发生黏包的两种情况

   1. ##### 情况一 发送方的缓存机制

      * 发送端需要等缓冲区满才发送出去，造成粘包（发送数据时间间隔很短，数据了很小，会合到一起，产生粘包）

      * 服务端

        ```````
        #_*_coding:utf-8_*_
        from socket import *
        ip_port=('127.0.0.1',8080)
        
        tcp_socket_server=socket(AF_INET,SOCK_STREAM)
        tcp_socket_server.bind(ip_port)
        tcp_socket_server.listen(5)
        
        
        conn,addr=tcp_socket_server.accept()
        
        
        data1=conn.recv(10)
        data2=conn.recv(10)
        
        print('----->',data1.decode('utf-8'))
        print('----->',data2.decode('utf-8'))
        
        conn.close()
        
        服务端
        ```````

      * 客户端

        ``````
        #_*_coding:utf-8_*_
        import socket
        BUFSIZE=1024
        ip_port=('127.0.0.1',8080)
        
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        res=s.connect_ex(ip_port)
        
        
        s.send('hello'.encode('utf-8'))
        s.send('egg'.encode('utf-8'))
        
        客户端
        ``````

   2. ##### 情况二 接收方的缓存机制

      * 接收方不及时接收缓冲区的包，造成多个包接收（客户端发送了一段数据，服务端只收了一小部分，服务端下次再收的时候还是从缓冲区拿上次遗留的数据，产生粘包） 

      * 服务端

        ``````
        #_*_coding:utf-8_*_
        from socket import *
        ip_port=('127.0.0.1',8080)
        
        tcp_socket_server=socket(AF_INET,SOCK_STREAM)
        tcp_socket_server.bind(ip_port)
        tcp_socket_server.listen(5)
        
        
        conn,addr=tcp_socket_server.accept()
        
        
        data1=conn.recv(2) #一次没有收完整
        data2=conn.recv(10)#下次收的时候,会先取旧的数据,然后取新的
        
        print('----->',data1.decode('utf-8'))
        print('----->',data2.decode('utf-8'))
        
        conn.close()
        
        服务端
        ``````

      * 客户端

        ``````
        #_*_coding:utf-8_*_
        import socket
        BUFSIZE=1024
        ip_port=('127.0.0.1',8080)
        
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        res=s.connect_ex(ip_port)
        
        
        s.send('hello egg'.encode('utf-8'))
        
        客户端
        ``````

5. #### 总结

   黏包现象只发生在tcp协议中：

   1. .从表面上看，黏包问题主要是因为发送方和接收方的缓存机制、tcp协议面向流通信的特点。
   2. 实际上，**主要还是因为接收方不知道消息之间的界限，不知道一次性提取多少字节的数据所造成的**





## day 32	解决黏包问题与struct模块

### 一、黏包问题解决方案

1. #### 解决方案一

   问题的根源在于，接收端不知道发送端将要传送的字节流的长度，所以解决粘包的方法就是围绕，如何让发送端在发送数据前，把自己将要发送的字节流总大小让接收端知晓，然后接收端来一个死循环接收完所有数据。

   ![img](https://images2017.cnblogs.com/blog/827651/201801/827651-20180107211210612-35513522.png)

   

   * ##### 服务端

     ``````
     #_*_coding:utf-8_*_
     import socket
     sk = socket.socket()
     sk.bind(("127.0.0.1",8080))
     sk.listen()
     
     conn,addr = sk.accept()
     while 1:
         cmd = input(">>>")
         if cmd == "q":
             conn.send(b"q")
             break
         conn.send(cmd.encode("gbk"))
         num = conn.recv(1024).decode("utf-8")
         # print(num)
         conn.send(b"ok!")
         res = conn.recv(int(num)).decode("gbk")
         print(res)
     
     conn.close()
     sk.close()
     
     服务端
     ``````

     

   * ##### 客户端

     ``````
     #_*_coding:utf-8_*_
     import socket
     import subprocess
     
     sk = socket.socket()
     sk.connect(("127.0.0.1",8080))
     while 1:
         cmd = sk.recv(1024).decode("gbk")
         if cmd == "q":
             break
         res = subprocess.Popen(
             cmd,shell=True,
             stdout=subprocess.PIPE,
             stderr=subprocess.PIPE
         )
         std_out = res.stdout.read()
         std_err = res.stderr.read()
         # print(str(len(std_out)+len(std_err)).encode("utf-8"))
         sk.send(str(len(std_out)+len(std_err)).encode("utf-8"))
         sk.recv(1024)
         sk.send(std_out)
         sk.send(std_err)
     
     sk.close()
     
     客户端
     ``````

     * 好处:
       * 确定了到底要接收多大的数据
       * 要在文件中配置一个配置项: 就是每次recv的大小  buffer(缓冲默认大小) = 4096
       * 当我们要发送大数据的时候, 要明确的告诉接收方要发送多大的数据.
       * 多用在文件传输的过程中
         * 大文件的传输, 一定是按照字节读的, 每次固定字节
         * 传输过程中, 一边读一边传, 接收端, 一边收一边写
         * send 这个大文件之前, 35672字节 send(4096) 35672-4096-4096
         * recv 这个大文件, recv 35672字节 recv(2048) 35672-2048-2048
     * 不好的地方
       * 多了一次交互
       * send 和 sendto 在超过一定范围的时候, 都会报错

   * 存在的问题

     * 程序的运行速度远快于网络传输速度，所以在发送一段字节前，先用send去发送该字节流长度，这种方式会放大网络延迟带来的性能损耗



## day 33	hmac的检验客户端合法性和socketserver模块



## day 34	ftp 作业

### server 端

``````
import socket
import struct
import json
import subprocess
import os

class MYTCPServer:
    address_family = socket.AF_INET

    socket_type = socket.SOCK_STREAM

    allow_reuse_address = False

    max_packet_size = 8192

    coding='utf-8'

    request_queue_size = 5

    server_dir='file_upload'

    def __init__(self, server_address, bind_and_activate=True):
        """Constructor.  May be extended, do not override."""
        self.server_address=server_address
        self.socket = socket.socket(self.address_family,
                                    self.socket_type)
        if bind_and_activate:
            try:
                self.server_bind()
                self.server_activate()
            except:
                self.server_close()
                raise

    def server_bind(self):
        """Called by constructor to bind the socket.
        """
        if self.allow_reuse_address:
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind(self.server_address)
        self.server_address = self.socket.getsockname()

    def server_activate(self):
        """Called by constructor to activate the server.
        """
        self.socket.listen(self.request_queue_size)

    def server_close(self):
        """Called to clean-up the server.
        """
        self.socket.close()

    def get_request(self):
        """Get the request and client address from the socket.
        """
        return self.socket.accept()

    def close_request(self, request):
        """Called to clean up an individual request."""
        request.close()

    def run(self):
        while True:
            self.conn,self.client_addr=self.get_request()
            print('from client ',self.client_addr)
            while True:
                try:
                    head_struct = self.conn.recv(4)
                    if not head_struct:break

                    head_len = struct.unpack('i', head_struct)[0]
                    head_json = self.conn.recv(head_len).decode(self.coding)
                    head_dic = json.loads(head_json)

                    print(head_dic)
                    #head_dic={'cmd':'put','filename':'a.txt','filesize':123123}
                    cmd=head_dic['cmd']
                    if hasattr(self,cmd):
                        func=getattr(self,cmd)
                        func(head_dic)
                except Exception:
                    break

    def put(self,args):
        file_path=os.path.normpath(os.path.join(
            self.server_dir,
            args['filename']
        ))

        filesize=args['filesize']
        recv_size=0
        print('----->',file_path)
        with open(file_path,'wb') as f:
            while recv_size < filesize:
                recv_data=self.conn.recv(self.max_packet_size)
                f.write(recv_data)
                recv_size+=len(recv_data)
                print('recvsize:%s filesize:%s' %(recv_size,filesize))


tcpserver1=MYTCPServer(('127.0.0.1',8080))

tcpserver1.run()






#下列代码与本题无关
class MYUDPServer:

    """UDP server class."""
    address_family = socket.AF_INET

    socket_type = socket.SOCK_DGRAM

    allow_reuse_address = False

    max_packet_size = 8192

    coding='utf-8'

    def get_request(self):
        data, client_addr = self.socket.recvfrom(self.max_packet_size)
        return (data, self.socket), client_addr

    def server_activate(self):
        # No need to call listen() for UDP.
        pass

    def shutdown_request(self, request):
        # No need to shutdown anything.
        self.close_request(request)

    def close_request(self, request):
        # No need to close anything.
        pass

 服务端
``````



### client 端

``````
import socket
import struct
import json
import os



class MYTCPClient:
    address_family = socket.AF_INET

    socket_type = socket.SOCK_STREAM

    allow_reuse_address = False

    max_packet_size = 8192

    coding='utf-8'

    request_queue_size = 5

    def __init__(self, server_address, connect=True):
        self.server_address=server_address
        self.socket = socket.socket(self.address_family,
                                    self.socket_type)
        if connect:
            try:
                self.client_connect()
            except:
                self.client_close()
                raise

    def client_connect(self):
        self.socket.connect(self.server_address)

    def client_close(self):
        self.socket.close()

    def run(self):
        while True:
            inp=input(">>: ").strip()
            if not inp:continue
            l=inp.split()
            cmd=l[0]
            if hasattr(self,cmd):
                func=getattr(self,cmd)
                func(l)


    def put(self,args):
        cmd=args[0]
        filename=args[1]
        if not os.path.isfile(filename):
            print('file:%s is not exists' %filename)
            return
        else:
            filesize=os.path.getsize(filename)

        head_dic={'cmd':cmd,'filename':os.path.basename(filename),'filesize':filesize}
        print(head_dic)
        head_json=json.dumps(head_dic)
        head_json_bytes=bytes(head_json,encoding=self.coding)

        head_struct=struct.pack('i',len(head_json_bytes))
        self.socket.send(head_struct)
        self.socket.send(head_json_bytes)
        send_size=0
        with open(filename,'rb') as f:
            for line in f:
                self.socket.send(line)
                send_size+=len(line)
                print(send_size)
            else:
                print('upload successful')




client=MYTCPClient(('127.0.0.1',8080))

client.run()

客户端
``````



## day 35	进程

# 第四部分 前端基础	day41 -- day 52 (哪吒_qimi)

## day 41 HTML 标签

### 一.  HTML

 1. #### ftp	UPLOAD|ooxx.av|1024  -->  http协议

 2. #### HTML 标签结构

    * HTML

      ​		<!DOCTYPE html> --> 声明为HTML5文档

      ​		head  -->  给浏览器看的内容

      ​		title --> 标题

      ​		style --> css样式

      ​		link --> css文件

      ​		script --> Js

      ​		meta --> 元素可提供有关页面的元信息（mata-information）,针对搜索引						擎和更新频度的描述和关键词。
      
      `````
      <!--2秒后跳转到对应的网址，注意引号-->
      	<meta http-equiv="refresh", 								content="2;URL=https://www.oldboyedu.com">
      <!--指定文档的编码类型-->
      	<meta http-equiv="content-Type" charset=UTF8">
      <!--告诉IE以最高级模式渲染文档-->
      	<meta http-equiv="x-ua-compatible" content="IE=edge">
      
      	keywords -- 关键字
      	description -- 描述
      	<meta name="keywords" content="meta总结,html meta,meta属		性,meta跳转">
    	<meta name="description" content="老男孩教育Python学院">
      `````

      ​	body  -->  给用户看的内容
      
      

 3. #### HTML标签的语法

     1. ``````
        <head 属性1=值1 属性2=值2></head>
        <body></body>
        标签的属性

        ``````
        

4. #### 标签的属性

     * id：定义标签的唯一ID，HTML文档树中唯一
     * class：为html元素定义一个或多个类名（classname）(CSS样式类名)
     * style：规定元素的行内样式（CSS样式）

 5. #### HTML 注释方法

     * <!--注释内容-->

 6. #### Body标签中的常用标签

     1. ##### 常用标签的分类

        ``````
        独占一行的    块儿级标签
        	h1~h6	标题
        	p	段落
        	div
        	hr	分割线
        	li
        	tr
        ``````

        ``````
        <h1>我是一级标题</h1>
        <h2>我是二级标题</h2>
        <h3>我是三级标题</h3>
        <h4>我是四级标题</h4>
        <h5>我是五级标题</h5>
        <h6>我是六<br>级标题</h6>
        ``````

        

        ``````
        在一行显示的  行内标签/内联标签 
        	<a></a>	连接
        	<span></span>
        	img	图片
        	b/i/u/s
        	<br>	换行
        ``````

        ``````
        <b id="b1">加粗</b>
        <i>斜体</i>
        <u>下划线</u>
        <s>删除</s>
        <img src="https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=3803137380,2419499331&fm=26&gp=0.jpg" alt="加载不出来的时候显示">
            <img src="lp.jpg" alt="新垣结衣" title="鼠标移上去">
        ``````

     2. ##### 其他常用标签

        1. ###### img 标签

           ```
           <img src="图片的路径" alt="图片未加载成功时的提示" title="鼠标悬浮时提示信息" width="宽" height="高(宽高两个属性只用一个会自动等比缩放)">
           ```

        2. ###### a 标签

           ```
           <a href="http://www.oldboyedu.com" target="_blank" >点我</a>
           
           href属性指定目标网页地址。该地址可以有几种类型：
           	绝对URL - 指向另一个站点（比如 		href="http://www.jd.com）
           	相对URL - 指当前站点中确切的路		径（href="index.htm"）
           	锚URL - 指向页面中的锚			（href="#top"）
           
           
           target：
           
           	_blank表示在新标签页中打开目标网页
           	_self表示在当前标签页中打开目标网页
           ```

        3. ###### 列表

           1. ###### 无序列表

              ``````
              <ul type="disc">
                <li>第一项</li>
                <li>第二项</li>
              </ul>
              ``````

              ###### 	type 属性:

              * disc（实心圆点，默认值）

              * circle（空心圆圈）

              * square（实心方块）

              * none（无样式）

                

           2. ###### 有序列表

              ``````
              <ol type="1" start="2">
                <li>第一项</li>
                <li>第二项</li>
              </ol>
              ``````

              ###### type 属性

              * 1 数字列表，默认值
              * A 大写字母
              * a 小写字母
              * Ⅰ大写罗马
              * ⅰ小写罗马

              

           3. ###### 标题列表

              ``````
              <dl>
                <dt>标题1</dt>
                <dd>内容1</dd>
                <dt>标题2</dt>
                <dd>内容1</dd>
                <dd>内容2</dd>
              </dl>
              ``````

        4. ##### 表格

           ``````
           <table>
             <thead>
             <tr>
               <th>序号</th>
               <th>姓名</th>
               <th>爱好</th>
             </tr>
             </thead>
             <tbody>
             <tr>
               <td>1</td>
               <td>Egon</td>
               <td>杠娘</td>
             </tr>
             <tr>
               <td>2</td>
               <td>Yuan</td>
               <td>日天</td>
             </tr>
             </tbody>
           </table>
           ``````

           ###### 属性

           * border: 表格边框.
           * cellpadding: 内边距
           * cellspacing: 外边距.
           * width: 像素 百分比.（最好通过css来设置长宽）
           * rowspan: 单元格竖跨多少行
           * colspan: 单元格横跨多少列（即合并单元格）

     3. #####  标签的嵌套

        1. ###### 标签可以嵌套标签

           ###### 	注意事项：

           * 尽量不要用内联标签包块儿级标签
           * p标签不能嵌套p标签
           * p标签不能嵌套div标签

     4. ##### 获取用户输入的标签

        1. ###### form 标签

           表单属性

           | 属性           | 描述                                                       |
           | -------------- | ---------------------------------------------------------- |
           | accept-charset | 规定在被提交表单中使用的字符集（默认：页面字符集）。       |
           | action         | 规定向何处提交表单的地址（URL）（提交页面）。              |
           | autocomplete   | 规定浏览器应该自动完成表单（默认：开启）。                 |
           | enctype        | 规定被提交数据的编码（默认：url-encoded）。                |
           | method         | 规定在提交表单时所用的 HTTP 方法（默认：GET）。            |
           | name           | 规定识别表单的名称（对于 DOM 使用：document.forms.name）。 |
           | novalidate     | 规定浏览器不验证表单。                                     |
           | target         | 规定 action 属性中地址的目标（默认：_self）。              |

            

        2. ###### input 标签

           * type

             1. text	文本
             2. password    密码
             3. email
             4. date    日期

             

             1. checkbox 	多选
             2. radio     单选

             

             1. button --> 普通按钮 --> 通常用JS给它绑定事件
             2. submit --> 提交按钮 --> 默认将form表单的数据提交
             3. reset   --> 重置按钮 --> 将当前form中的输入框都清空
             
             | type属性值 | 表现形式     | 对应代码                                     |
             | ---------- | ------------ | -------------------------------------------- |
             | text       | 单行输入文本 | <input type=text" />                         |
             | password   | 密码输入框   | <input type="password"  />                   |
             | date       | 日期输入框   | <input type="date" />                        |
             | checkbox   | 复选框       | <input type="checkbox" checked="checked"  /> |
             | radio      | 单选框       | <input type="radio"  />                      |
             | submit     | 提交按钮     | <input type="submit" value="提交" />         |
             | reset      | 重置按钮     | <input type="reset" value="重置"  />         |
             | button     | 普通按钮     | <input type="button" value="普通按钮"  />    |
             | hidden     | 隐藏输入框   | <input type="hidden"  />                     |
             | file       | 文本选择框   | <input type="file"  />                       |
             
             ###### 属性说明:
             
             * name：表单提交时的“键”，注意和id的区别
             * value：表单提交时对应项的值
               - type="button", "reset", "submit"时，为按钮上显示的文本年内容
               - type="text","password","hidden"时，为输入框的初始值
               - type="checkbox", "radio", "file"，为输入相关联的值
             * checked：radio和checkbox默认被选中的项
             * readonly：text和password设置只读
             * disabled：所有input均适用

        3. ##### select标签

           ``````
           <form action="" method="post">
             <select name="city" id="city">
               <option value="1">北京</option>
               <option selected="selected" value="2">上海</option>
               <option value="3">广州</option>
               <option value="4">深圳</option>
             </select>
           </form>
           ``````

           ###### 属性:

           * multiple：布尔属性，设置后为多选，否则默认单选
           * disabled：禁用
           * selected：默认选中该项
           * value：定义提交时的选项值

        4. ###### label 标签

           ``````
           <form action="">
             <label for="username">用户名</label>
             <input type="text" id="username" name="username">
           </form>
           ``````

           ###### 说明

           * label 元素不会向用户呈现任何特殊效果。
           * <label> 标签的 for 属性值应当与相关元素的 id 属性值相同。

        5. ##### textarea 标签

           ``````
           <textarea name="memo" id="memo" cols="30" rows="10">
             默认内容
           </textarea>
           ``````

           ###### 属性说明:

           * name：名称
           * rows：行数
           * cols：列数
           * disabled：禁用

        6. ##### form 表单提交数据的注意事项

           ​	{"k1":"v1"}

           1. form 标签必须把获取用户输入的标签抱起来
           2. input 不是from, form标签必须有action属性和method
           3. form 中的获取用户输入的标签必须要有name属性

 7. ### 备注

      1. #### 特殊字符

          ``````
          空格 &nbsp
          >	&gt
          <	&lt
          &	&amp
          ¥	&yen
          版权	&copy
          注册	&reg
          ``````

          

## day 42 html 与 css



