from pypdf import PdfReader, PdfWriter  # 匯入 pypdf 的 PDF 讀取與寫入類別


def merge_pdf_files(pdf_paths, output_path):
    """
    合併多個 PDF 檔案並輸出到指定路徑。

    參數:
    pdf_paths: list[str]，PDF 檔案路徑清單
    output_path: str，合併後 PDF 輸出路徑

    回傳:
    無，若合併失敗會拋出例外
    """
    writer = PdfWriter()  # 建立一個 PdfWriter 實例，用來寫入合併後的 PDF 頁面

    for pdf_path in pdf_paths:  # 依序讀取傳入的每個 PDF 檔案路徑
        reader = PdfReader(pdf_path)  # 用 PdfReader 讀取該 PDF 檔案
        for page in reader.pages:  # 逐頁取得該 PDF 的每一頁
            writer.add_page(page)  # 把每一頁加入到 PdfWriter 裡面

    # 開啟指定的輸出路徑（以二進位寫入模式）
    with open(output_path, "wb") as f:
        writer.write(f)  # 將合併後的所有頁面寫入該輸出檔案
