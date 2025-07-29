import tkinter as tk


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")  # Set the window title
        # Set the background color of the window
        self.root.configure(bg="black")

        self.expression = ""  # This string will keep track of the current mathematical expression

        # Make the first row expandable
        self.root.grid_rowconfigure(0, weight=1)
        # Make the first column expandable
        self.root.grid_columnconfigure(0, weight=1)

        # Create a frame with black background
        self.frame = tk.Frame(root, bg="black")
        # Create a frame to hold the calculator UI
        self.frame.grid(row=0, column=0, sticky="nsew")

        # Create an Entry widget to display the input and results
        self.entry = tk.Entry(self.frame,
                              font=("Arial", 24),
                              bd=10,
                              relief=tk.GROOVE,
                              justify="right",
                              bg="#222222",
                              fg="white",
                              insertbackground="white")  # Set the cursor color to black
        # Place the Entry widget at the top spanning 4 columns, with some padding
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Bind the entry to detect changes in text
        self.entry.bind("<KeyRelease>", self.on_entry_change)

        # Define the calculator buttons as tuples: (text, row, column, optional colspan)
        buttons = [
            ("1", 1, 0), ("2", 1, 1), ("3", 1, 2), ("÷", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("×", 2, 3),
            ("7", 3, 0), ("8", 3, 1), ("9", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
            ("C", 5, 0, 4)  # Clear button spans all 4 columns on row 5
        ]

        # Loop through each button definition and create a Button widget
        for (text, row, col, *span) in buttons:
            # Determine if the button spans multiple columns
            colspan = span[0] if span else 1
            tk.Button(
                self.frame,
                text=text,
                width=10,
                height=2,
                font=("Arial", 18),
                bg="#333333",
                fg="white",
                activebackground="#555555",
                activeforeground="white",
                # Pass the button text to on_click when pressed
                command=lambda t=text: self.on_click(t)
                # Position the button in the grid
            ).grid(row=row, column=col, columnspan=colspan, sticky="nsew")

        for i in range(6):  # Configure all rows and columns to expand
            self.frame.grid_rowconfigure(i, weight=1)
        for i in range(4):  # Configure all columns to expand
            self.frame.grid_columnconfigure(i, weight=1)

    def on_entry_change(self, event):
        # This method is called when the entry text changes
        self.expression = self.entry.get()

    def on_click(self, char):
        # Handle button click events based on the button text

        if char == "=":
            # When '=' is clicked, try to evaluate the expression string
            try:
                # Evaluate the math expression
                result = str(eval(self.expression))
                self.entry.delete(0, tk.END)          # Clear the entry display
                self.entry.insert(tk.END, result)     # Show the result
                # Store result as the new expression (for further calculations)
                self.expression = result
            except:
                # If there is any error in evaluation (e.g., syntax error), display 'Error'
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
                self.expression = ""                   # Reset expression on error

        elif char == "C":
            # Clear button clears the entire expression and display
            self.expression = ""
            self.entry.delete(0, tk.END)

        else:
            # Handle visual divide symbol
            if char == "÷":
                self.expression += "/"
            elif char == "×":
                self.expression += "*"
            else:
                self.expression += str(char)

            display_text = self.expression.replace("/", "÷").replace("*", "×")
            # Update the entry display with the current expression
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, display_text)


if __name__ == "__main__":
    root = tk.Tk()       # Create the main window
    # Initialize the calculator app with the main window
    app = Calculator(root)
    root.mainloop()       # Start the Tkinter event loop to run the app
