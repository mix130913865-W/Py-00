import socket       # 匯入 socket 模組，讓程式能進行網路溝通
import threading    # 匯入 threading 模組，用來處理多位用戶的同時連線

HOST = '127.0.0.1'  # 設定伺服器 IP（本機）
PORT = 55555        # 設定通訊埠（可自訂，只要 client 連一樣的就行）

# 建立伺服器 socket，使用 IPv4 與 TCP 協定
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))  # 綁定 IP 和 PORT
server.listen()            # 開始監聽 client 的連線

clients = []  # 儲存目前連線的所有 client socket
names = []    # 儲存 client 對應的名稱

# 廣播訊息給所有 client


def broadcast(message, sender_client=None):
    for client in clients:
        if client != sender_client:  # 確保不發送給自己
            try:
                client.send(message)  # 傳送訊息給每個 client
            except:
                print("Unable to send a message")  # 如果傳送失敗，可能是 client 已經關閉連線
                clients.remove(client)  # 從列表中移除無法連線的 client


def handle_client(client):  # 處理每個 client 的訊息
    while True:
        try:
            message = client.recv(1024)  # 接收 client 的訊息
            if not message:  # 如果沒有收到訊息，代表 client 已經關閉連線
                if client in clients:
                    # 找到這個 client 在列表中的位置
                    index = clients.index(client)  # 如果沒有訊息，代表 client 已經關閉連線
                    name = names[index]  # 找到對應的名稱
                    clients.remove(client)  # 如果 client 關閉連線，從列表中移除
                    names.remove(name)  # 同時也從名稱列表中移除
                    broadcast(f'{name} has left the chat room.'.encode(
                        'utf-8'))  # 廣播離開訊息
                client.close()  # 關閉 client socket
                break
            index = clients.index(client)  # 找到這個 client 在列表中的位置
            name = names[index]  # 根據位置找到對應的名稱
            # 廣播訊息給所有 client
            broadcast(
                f"{name}: {message.decode('utf-8')}".encode('utf-8'), sender_client=client)
        except:
            # 如果發生錯誤（如 client 離線），移除這個 client
            if client in clients:
                index = clients.index(client)
                name = names[index]
                clients.remove(client)
                names.remove(name)
                broadcast(f"{name} has left the chat room.".encode(
                    'utf-8'), sender_client=None)
            client.close()
            break

# 接收新 client 的主迴圈


def receive():
    while True:
        client, address = server.accept()  # 等待新的 client 連線
        print(f"Connection is from {str(address)}")

        # 請 client 輸入名稱
        client.send("Please enter your name:".encode('utf-8'))
        name = client.recv(1024).decode('utf-8')

        names.append(name)
        clients.append(client)

        print(f"{name} has joined the chatting room")
        broadcast(f"{name} 加入聊天室！".encode('utf-8'))
        client.send(
            "You have successfully joined the chat room.\nenter your message:".encode('utf-8'))

        # 每個 client 各自用一個 thread 處理訊息
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()


# 主程式進入點
print("---Server activated---")
receive()
