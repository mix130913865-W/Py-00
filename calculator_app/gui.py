# gui.py
import tkinter as tk  # 引入 tkinter 模組
from logic import evaluate_expression  # 引入運算模組


class CalculatorGUI:
    def __init__(self, root):  # 初始化計算機 GUI
        self.root = root  # 設定主視窗
        self.root.title("計算機")  # 設定視窗標題
        self.root.configure(bg="black")  # 背景顏色設為黑色

        self.expression = ""  # 儲存目前的運算字串

        # 設定主視窗的 row 與 column 可擴展
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        # 建立框架容器，背景為黑色
        self.frame = tk.Frame(root, bg="black")
        self.frame.grid(row=0, column=0, sticky="nsew")

        # 建立輸入框，設定字型、背景色、文字對齊等
        self.entry = tk.Entry(self.frame,  # 輸入框
                              font=("Arial", 24),  # 字型大小
                              bd=10,  # 邊框大小
                              relief=tk.GROOVE,  # 邊框樣式
                              justify="right",  # 文字右對齊
                              bg="#222222",  # 輸入框背景色
                              fg="white",  # 文字顏色
                              insertbackground="white")  # 游標為白色
        # 輸入框跨4欄置頂，並有外距
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        # 綁定鍵盤釋放事件，更新expression
        self.entry.bind("<KeyRelease>", self.on_entry_change)

        # 定義按鈕 (文字, row, column, 可選欄跨度)
        buttons = [
            ("1", 1, 0), ("2", 1, 1), ("3", 1, 2), ("÷", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("×", 2, 3),
            ("7", 3, 0), ("8", 3, 1), ("9", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
            ("C", 5, 0, 4)  # 清除鍵，跨4欄
        ]

        # 建立並放置按鈕元件
        for (text, row, col, *span) in buttons:  # 解包按鈕資訊
            colspan = span[0] if span else 1  # 如果有欄跨度則使用，否則默認為1
            tk.Button(
                self.frame,  # 建立按鈕
                text=text,  # 按鈕顯示文字
                width=10,  # 按鈕寬度
                height=2,  # 按鈕高度
                font=("Arial", 18),  # 字型大小
                bg="#333333",  # 按鈕背景色
                fg="white",  # 按鈕文字顏色
                activebackground="#555555",  # 按下時背景色
                activeforeground="white",  # 按下時文字顏色
                command=lambda t=text: self.on_click(t)  # 點擊事件處理
                # 放置按鈕，跨欄時使用 columnspan
            ).grid(row=row, column=col, columnspan=colspan, sticky="nsew")

        # 設定所有列與欄可擴展，保持按鈕尺寸跟視窗同步調整
        for i in range(6):  # 6行
            self.frame.grid_rowconfigure(i, weight=1)
        for i in range(4):  # 4列
            self.frame.grid_columnconfigure(i, weight=1)

    def on_entry_change(self, event):
        """
        當輸入框文字變動時更新 expression 變數。
        支援直接在輸入框輸入運算式。
        """
        self.expression = self.entry.get()

    def on_click(self, char):
        """
        按鈕點擊事件處理器。
        根據按鈕字元更新 expression 或執行計算。
        """
        if char == "=":
            # 按下等號時，呼叫 logic 模組計算
            result = evaluate_expression(self.expression)
            self.entry.delete(0, tk.END)  # 清空輸入框
            self.entry.insert(tk.END, result)  # 顯示計算結果
            if result == "Error":
                self.expression = ""  # 計算錯誤時清除運算式
            else:
                self.expression = result  # 成功則更新 expression 為結果
        elif char == "C":
            # 按下清除鍵，清空輸入框與運算式
            self.expression = ""
            self.entry.delete(0, tk.END)
        else:
            # 將視覺化的除號與乘號轉成 Python 可運算字元
            if char == "÷":
                self.expression += "/"
            elif char == "×":
                self.expression += "*"
            else:
                self.expression += str(char)

            # 顯示時用除號和乘號替代 / 和 *
            display_text = self.expression.replace("/", "÷").replace("*", "×")
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, display_text)
