import tkinter as tk  # 匯入 tkinter 主模組，負責 GUI 元件建立
from tkinter import filedialog, messagebox  # 匯入檔案選擇和訊息對話框功能
from pdf_merger import merge_pdf_files  # 匯入自訂的 PDF 合併功能


class PDFMergerApp:
    def __init__(self, root):
        self.root = root  # 儲存傳入的主視窗物件
        self.root.title("PDF Merger Tool")  # 設定視窗標題為 "PDF Merger Tool"
        self.pdf_files = []  # 建立一個空清單，用來存放使用者選擇的 PDF 路徑

        # 建立主框架，放置所有子元件
        self.main_frame = tk.Frame(root)

        # 建立顯示狀態或說明的 Label，放在主框架內
        self.label = tk.Label(
            self.main_frame,
            text="No PDF files selected",  # 初始顯示文字
            anchor="center",  # 文字置中對齊
            justify="center",  # 文字多行置中
            font=("Arial", 12)  # 字型為 Arial，字級 12
        )
        self.label.pack(pady=10, fill="x")  # 使用 pack 佈局，垂直方向留 10 像素空白，水平撐滿框架寬度

        # 建立一個框架用來水平放置按鈕
        btn_frame = tk.Frame(self.main_frame)
        btn_frame.pack(pady=5)  # 按鈕框架上下留 5 像素空白

        # 建立「選擇 PDF 檔案」按鈕，放入按鈕框架
        self.select_btn = tk.Button(
            btn_frame,
            text="Select PDF Files",  # 按鈕顯示文字
            command=self.select_files,  # 按下按鈕時執行 select_files 函式
            font=("Arial", 11),  # 字型 Arial，字級 11
            padx=10,  # 左右內距 10 像素
            pady=5    # 上下內距 5 像素
        )
        # 使用 grid 佈局，放在第 0 列第 0 欄，左右間距 10
        self.select_btn.grid(row=0, column=0, padx=10)

        # 建立「合併 PDFs」按鈕，初始不可按，放入按鈕框架
        self.merge_btn = tk.Button(
            btn_frame,
            text="Merge PDFs",  # 按鈕文字
            command=self.merge_pdfs,  # 按下按鈕執行 merge_pdfs 函式
            state=tk.DISABLED,  # 初始狀態為不可用
            font=("Arial", 11),  # 字型 Arial，字級 11
            padx=10,  # 左右內距 10
            pady=5    # 上下內距 5
        )
        # 使用 grid 佈局，放在第 0 列第 1 欄，左右間距 10
        self.merge_btn.grid(row=0, column=1, padx=10)

        # 把主框架放在主視窗的第 1 列第 1 欄（3x3 格子中央），並讓它可以水平垂直伸展
        self.main_frame.grid(row=1, column=1, sticky="nsew")

    def select_files(self):
        # 呼叫檔案開啟對話框，允許多選 PDF
        files = filedialog.askopenfilenames(
            title="Select PDF Files",  # 對話框標題
            filetypes=[("PDF files", "*.pdf")],  # 篩選只顯示 PDF
        )
        if files:  # 如果有選檔案
            self.pdf_files = list(files)  # 轉成列表並存起來
            # 更新狀態文字顯示已選檔案數量
            self.label.config(text=f"Selected {len(self.pdf_files)} files")
            self.merge_btn.config(state=tk.NORMAL)  # 啟用合併按鈕
        else:  # 如果沒選任何檔案或取消
            self.label.config(text="No PDF files selected")  # 更新狀態文字
            self.merge_btn.config(state=tk.DISABLED)  # 禁用合併按鈕

    def merge_pdfs(self):
        if not self.pdf_files:  # 若沒有選擇檔案
            messagebox.showwarning(
                "Warning", "Please select PDF files first")  # 跳出警告視窗
            return  # 結束此函式

        # 呼叫另存新檔對話框，讓使用者選擇合併檔案儲存位置及檔名
        save_path = filedialog.asksaveasfilename(
            defaultextension=".pdf",  # 預設副檔名是 .pdf
            filetypes=[("PDF files", "*.pdf")],  # 檔案格式篩選
            title="Save Merged PDF"  # 對話框標題
        )
        if not save_path:  # 若使用者取消儲存
            return  # 結束此函式

        try:
            merge_pdf_files(self.pdf_files, save_path)  # 呼叫合併函式，把檔案列表與儲存路徑傳入
            messagebox.showinfo(
                # 成功訊息視窗
                "Success", f"PDFs merged successfully!\nSaved to: {save_path}")
        except Exception as e:
            messagebox.showerror(
                "Error", f"Failed to merge PDFs:\n{e}")  # 發生錯誤時顯示錯誤訊息
