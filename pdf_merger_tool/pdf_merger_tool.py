import tkinter as tk
from tkinter import filedialog, messagebox
from pypdf import PdfReader, PdfWriter


class PDFMergerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Merger Tool")

        self.pdf_files = []

        # Main frame to center the content
        self.main_frame = tk.Frame(root)

        # Label to show status or instructions
        self.label = tk.Label(
            self.main_frame,
            text="No PDF files selected",
            anchor="center",
            justify="center",
            font=("Arial", 12)
        )
        self.label.pack(pady=10, fill="x")

        # Frame to hold the buttons side by side
        btn_frame = tk.Frame(self.main_frame)
        btn_frame.pack(pady=5)

        # Button to select PDF files
        self.select_btn = tk.Button(
            btn_frame,
            text="Select PDF Files",
            command=self.select_files,
            font=("Arial", 11),
            padx=10,
            pady=5
        )
        self.select_btn.grid(row=0, column=0, padx=10)

        # Button to merge PDFs (disabled initially)
        self.merge_btn = tk.Button(
            btn_frame,
            text="Merge PDFs",
            command=self.merge_pdfs,
            state=tk.DISABLED,
            font=("Arial", 11),
            padx=10,
            pady=5
        )
        self.merge_btn.grid(row=0, column=1, padx=10)

        # Place the main frame in the center cell of a 3x3 grid
        self.main_frame.grid(row=1, column=1, sticky="nsew")

    def select_files(self):
        # Open file dialog to select multiple PDF files
        files = filedialog.askopenfilenames(
            title="Select PDF Files",
            filetypes=[("PDF files", "*.pdf")],
        )
        if files:
            self.pdf_files = list(files)
            self.label.config(text=f"Selected {len(self.pdf_files)} files")
            self.merge_btn.config(state=tk.NORMAL)
        else:
            self.label.config(text="No PDF files selected")
            self.merge_btn.config(state=tk.DISABLED)

    def merge_pdfs(self):
        # Warn if no files selected
        if not self.pdf_files:
            messagebox.showwarning("Warning", "Please select PDF files first")
            return

        # Ask where to save the merged PDF
        save_path = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf")],
            title="Save Merged PDF"
        )
        if not save_path:
            return

        writer = PdfWriter()
        try:
            # Read each PDF and add pages to writer
            for pdf in self.pdf_files:
                reader = PdfReader(pdf)
                for page in reader.pages:
                    writer.add_page(page)

            # Write all pages to the output file
            with open(save_path, "wb") as f:
                writer.write(f)

            messagebox.showinfo("Success", f"PDFs merged successfully!\nSaved to: {save_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to merge PDFs:\n{e}")


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("450x250")

    # Configure root window grid: 3x3 with center expandable
    for i in range(3):
        root.grid_rowconfigure(i, weight=1)
        root.grid_columnconfigure(i, weight=1)

    app = PDFMergerApp(root)
    root.mainloop()
