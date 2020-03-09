#导入模块
import socket

#创建实例
client = socket.socket()
#访问的服务器端ip和port
ip_port = ("127.0.0.1",8888)
#连接主机
client.connect(ip_port)

#定义一个循环不断发送消息

while True:
    print("等待服务器发送信号...")
    # 接受主机信息
    data = client.recv(1024)
    # 打印接收的数据
    # 此处的byte型数据代指python3.x以上
    print("接收服务器发送的信息：{}".format(data.decode()))
    #输入发送的消息
    msg_input = input("请输入发送的消息：")
    #消息发送
    client.send(msg_input.encode())
    print(msg_input)
    if msg_input == 'exit':
        break
    # data = client.recv(1024)
    # print(22,data.decode())




