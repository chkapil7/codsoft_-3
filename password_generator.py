import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        
        self.length_label = tk.Label(root, text="Password Length:")
        self.length_label.pack()
        self.length_entry = tk.Entry(root)
        self.length_entry.pack()

        self.include_uppercase = tk.BooleanVar()
        self.include_numbers = tk.BooleanVar()
        self.include_symbols = tk.BooleanVar()

        self.uppercase_check = tk.Checkbutton(root, text="Include Uppercase Letters", variable=self.include_uppercase)
        self.uppercase_check.pack()
        
        self.numbers_check = tk.Checkbutton(root, text="Include Numbers", variable=self.include_numbers)
        self.numbers_check.pack()
        
        self.symbols_check = tk.Checkbutton(root, text="Include Symbols", variable=self.include_symbols)
        self.symbols_check.pack()

        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password)
        self.generate_button.pack()

        self.result_label = tk.Label(root, text="Generated Password:")
        self.result_label.pack()
        self.result_var = tk.StringVar()
        self.result_display = tk.Label(root, textvariable=self.result_var)
        self.result_display.pack()

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length < 1:
                raise ValueError("Length must be at least 1")

            characters = string.ascii_lowercase
            if self.include_uppercase.get():
                characters += string.ascii_uppercase
            if self.include_numbers.get():
                characters += string.digits
            if self.include_symbols.get():
                characters += string.punctuation

            if not characters:
                raise ValueError("No character sets selected")

            password = ''.join(random.choice(characters) for _ in range(length))
            self.result_var.set(password)
        except ValueError as e:
            messagebox.showerror("Error", str(e))

def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
