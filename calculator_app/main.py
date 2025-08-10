# calculator_app.py
import tkinter as tk
from gui import CalculatorGUI


def main():
    # 初始化主視窗
    root = tk.Tk()  # 建立主視窗
    app = CalculatorGUI(root)  # 建立計算機 GUI
    root.mainloop()  # 啟動事件迴圈


if __name__ == "__main__":
    main()
