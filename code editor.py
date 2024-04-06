import tkinter as tk
from tkinter import scrolledtext

class CodeEditorIDE:
    def __init__(self, root):
        self.root = root
        self.root.title("CodeEditorIDE")

        self.text_area = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, width=80, height=20)
        self.text_area.pack(expand=True, fill=tk.BOTH)

        self.run_button = tk.Button(self.root, text="Run Code", command=self.run_code)
        self.run_button.pack()

        self.input_entry = tk.Entry(self.root)
        self.input_entry.pack()

        self.result_text = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, width=80, height=10)
        self.result_text.pack(expand=True, fill=tk.BOTH)

        self.status_bar = tk.Label(self.root, text="Ready", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def run_code(self):
        code_to_execute = self.text_area.get("1.0", tk.END)

        # Get user input from the Entry widget
        user_input = self.input_entry.get()

        # Simulate execution by printing code and user input
        result = f"Code: {code_to_execute}\nUser Input: {user_input}"

        self.result_text.config(state=tk.NORMAL)
        self.result_text.delete("1.0", tk.END)
        self.result_text.insert(tk.END, result)
        self.result_text.config(state=tk.DISABLED)
        self.update_status_bar("Code executed successfully")

    def update_status_bar(self, message):
        self.status_bar.config(text=message)

if __name__ == "__main__":
    root = tk.Tk()
    ide = CodeEditorIDE(root)
    root.mainloop()
