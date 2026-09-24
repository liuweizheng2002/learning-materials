"""
案例: 网编入门案例, 服务器端给客户端发送消息, 客户端给出回执信息.

服务器端开发流程:
    1. 创建服务器端Socket对象.
    2. 绑定IP地址和端口号.
    3. 设置最大监听数.
    4. 等待客户端申请建立连接.
    5. 给客户端发送消息.
    6. 接收客户端的信息并打印.
    7. 释放资源.

细节:
    客户端和服务器端是通过 字节流(bytes) 的形式实现的.

    命令行输入 ipconfig 或 ipconfig /all 查询本地ipv4地址，测试一般用 '0.0.0.0'  或  '127.0.0.1'  最省事。
"""
# 导包
import socket

# 1. 创建服务器端Socket对象.  ipv4, 字节流(TCP)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 2. 绑定IP地址和端口号. bind() 指绑定，方法只能调用1次.
server_socket.bind(('192.168.1.199', 10086))
# 3. 设置最大监听数. listen() 指监听，方法只能调用1次.（）里面是最大监听次数，上限是128
server_socket.listen(5)
# 4. 等待客户端申请建立连接. 运用拆包的原理，把server_socket用accept()拆开，并用accept_socket和client_info接收
# accept() 指接受(方法只能调用1次）.
accept_socket, client_info = server_socket.accept()

# 5. 给客户端发送消息. send指发送，可以调用多次，表示把括号内的内容发送到accept_socket中，
# b是语法糖, 表示括号内的内容是bytes类型，括号'' 内的内容不能是中文，
accept_socket.send(b'Welcome To Socket!')

# 6. 接收客户端的信息并打印.recv 指接收，括号内是接收的最大字节数，decode 指解码，utf-8指编码
data = accept_socket.recv(1024).decode('utf-8')
print(f'服务器端收到 来自{client_info} 的信息: {data}')
# 7. 释放资源.close指关闭,一般只关闭accept_socket
accept_socket.close()
# server_socket.close()     # 服务器端一般不关闭.

# 扩展: 设置端口号重用, 目的是: 快速重启服务器(服务器关闭后, 立即释放端口).
# 参1: 当前的套接字对象, 参2: 选项名, 参3: 该选项的值
# setsockopt 指设置套接字选项，括号内的三个参数分别是：当前的套接字对象，选项名，该选项的值（0/1/ture/false）
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)