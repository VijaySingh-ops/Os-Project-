from tkinter import ttk

def setup_styles():
    style = ttk.Style()
    style.theme_use('clam')
    style.configure('TFrame', background='#f4f4f4')
    style.configure('TLabel', background='#f4f4f4', font=('Segoe UI', 11))
    style.configure('Header.TLabel', font=('Segoe UI', 16, 'bold'), background='#222', foreground='white')
    style.configure('TButton', padding=6)
    style.configure('Treeview', font=('Segoe UI', 10), rowheight=25)
    style.map('TButton', background=[('active', '#00529b')], foreground=[('active', 'white')])