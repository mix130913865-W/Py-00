import tkinter as tk


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")  # Set the window title

        self.expression = ""  # This string will keep track of the current mathematical expression

        # Create an Entry widget to display the input and results
        self.entry = tk.Entry(root, font=("Arial", 24),
                              bd=10, relief=tk.RIDGE, justify="right")
        # Place the Entry widget at the top spanning 4 columns, with some padding
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Define the calculator buttons as tuples: (text, row, column, optional colspan)
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
            ("C", 5, 0, 4)  # Clear button spans all 4 columns on row 5
        ]

        # Loop through each button definition and create a Button widget
        for (text, row, col, *span) in buttons:
            # Determine if the button spans multiple columns
            colspan = span[0] if span else 1
            tk.Button(
                root, text=text, width=10, height=2, font=("Arial", 18),
                # Pass the button text to on_click when pressed
                command=lambda t=text: self.on_click(t)
                # Position the button in the grid
            ).grid(row=row, column=col, columnspan=colspan)

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
            # For numbers, operators, and decimal point, append to the expression string
            self.expression += str(char)
            self.entry.delete(0, tk.END)          # Clear current display
            # Update display with new expression
            self.entry.insert(tk.END, self.expression)


if __name__ == "__main__":
    root = tk.Tk()       # Create the main window
    # Initialize the calculator app with the main window
    app = Calculator(root)
    root.mainloop()       # Start the Tkinter event loop to run the app
