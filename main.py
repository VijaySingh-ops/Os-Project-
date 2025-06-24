import tkinter as tk
from tkinter.font import Font
from file_manager_app import FileManagerApp

def main():
    root = tk.Tk()
    # Set a professional default font for better UI
    default_font = Font(family="Segoe UI", size=10)
    root.option_add("*Font", default_font)
    FileManagerApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()