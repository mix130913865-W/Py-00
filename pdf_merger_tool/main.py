import tkinter as tk  # 匯入 tkinter 模組，用來建立 GUI 視窗
from gui import PDFMergerApp  # 從 gui 模組匯入 PDFMergerApp 類別，負責主程式介面


def main():
    root = tk.Tk()  # 建立主視窗物件（Tkinter 的根視窗）
    root.geometry("450x250")  # 設定視窗大小，寬450像素，高250像素

    # 設定主視窗的 Grid 版面配置為 3x3 格子
    for i in range(3):
        root.grid_rowconfigure(i, weight=1)  # 第 i 列給予伸縮權重為1，讓格子可以拉伸
        root.grid_columnconfigure(i, weight=1)  # 第 i 欄也給予伸縮權重1

    # 建立 PDFMergerApp 實例，傳入主視窗 root
    app = PDFMergerApp(root)
    # 啟動 Tkinter 的事件迴圈，開始監聽使用者操作
    root.mainloop()


# 判斷目前檔案是否為主程式執行（非被 import）
if __name__ == "__main__":
    main()  # 執行 main 函式，啟動整個應用程式
