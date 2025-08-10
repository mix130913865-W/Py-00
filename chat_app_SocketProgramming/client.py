import socket       # 匯入 socket 模組
import threading    # 匯入 threading 模組，用來同時收與發訊息

HOST = '127.0.0.1'  # 伺服器 IP（跟 server.py 一致）
PORT = 55555        # 伺服器 PORT（也要一致）

# 建立 client socket 並連線到 server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

# 負責接收 server 訊息的 thread


def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')  # 收 server 傳來的訊息
            if message == "Please enter your name：":
                # 如果 server 要求輸入名稱，就從使用者那邊取得並傳送
                client.send(input(message).encode('utf-8'))
            else:
                print(message)  # 其他訊息就顯示出來
        except:
            # 如果無法連線，印出錯誤並關閉
            print("server disconnected")
            client.close()
            break

# 負責發送使用者輸入訊息的 thread


def write():
    while True:
        message = input('')           # 取得使用者輸入
        client.send(message.encode('utf-8'))  # 傳給 server
        print(f"You: {message}")


# 啟動收訊息的 thread
receive_thread = threading.Thread(target=receive)
receive_thread.start()

# 啟動發訊息的 thread
write_thread = threading.Thread(target=write)
write_thread.start()
