#导入模块
import socket

#创建实例
sk = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#访问的服务器端ip和port
ip_port = ("127.0.0.1",8888)

#定义一个循环不断发送消息
while True:
    #输入发送的消息
    msg_input = input("请输入发送的消息：")
    # 消息发送
    # client.send(msg_input.encode())
    if msg_input == 'exit':
        break
    #数据发送
    sk.sendto(msg_input.encode(),ip_port)
# 发送关闭信息
sk.close()


