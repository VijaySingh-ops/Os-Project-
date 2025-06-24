import os
import shutil
from tkinter import LEFT, RIGHT, BOTH, Y, Frame, StringVar, END, messagebox, filedialog, Listbox, Scrollbar, VERTICAL, ttk

from file_ops import list_files, delete_file, open_file
from previewer import Previewer
from styles import setup_styles

class FileManagerApp:         #define the main class of file manager
    def __init__(self, root):
        self.root = root
        self.root.title("Professional File Manager")
        self.root.geometry("900x600")
        self.root.minsize(700, 500)

        self.supported_extensions = ['.pdf', '.doc', '.docx', '.jpg', '.jpeg']

        setup_styles()

        # Main frames
        self.main_frame = ttk.Frame(root)
        self.main_frame.pack(fill=BOTH, expand=True)

        # Left panel
        self.left_panel = ttk.Frame(self.main_frame, width=300)
        self.left_panel.pack(side=LEFT, fill=Y, padx=(10,5), pady=10)

        # Right panel
        self.right_panel = ttk.Frame(self.main_frame)
        self.right_panel.pack(side=RIGHT, fill=BOTH, expand=True, padx=(5,10), pady=10)

        # Directory selection
        self.current_directory = StringVar()
        self.current_directory.set(os.path.expanduser("~"))

        dir_frame = ttk.Frame(self.left_panel)
        dir_frame.pack(fill='x')

        self.dir_label = ttk.Label(dir_frame, text="Current Directory:")
        self.dir_label.pack(side=LEFT, padx=(0,5), pady=5)
        self.dir_display = ttk.Label(dir_frame, textvariable=self.current_directory, foreground='#0066cc', cursor='hand2')
        self.dir_display.pack(side=LEFT, fill='x', expand=True)
        self.dir_display.bind("<Button-1>", self.change_directory)

        # File listbox with scrollbar
        self.file_listbox = Listbox(self.left_panel, font=('Segoe UI', 11), selectmode='browse')
        self.file_listbox.pack(side=LEFT, fill=Y, expand=True)
        self.file_listbox.bind("<<ListboxSelect>>", self.on_file_select)

        scroll = Scrollbar(self.left_panel, orient=VERTICAL, command=self.file_listbox.yview)
        scroll.pack(side=LEFT, fill=Y)
        self.file_listbox.config(yscrollcommand=scroll.set)

        # Buttons under file list
        btn_frame = ttk.Frame(self.left_panel)
        btn_frame.pack(fill='x', pady=10)

        self.open_btn = ttk.Button(btn_frame, text="Open File", command=self.open_file)
        self.open_btn.pack(fill='x', pady=3)
        self.delete_btn = ttk.Button(btn_frame, text="Delete File", command=self.delete_file)
        self.delete_btn.pack(fill='x', pady=3)
        self.refresh_btn = ttk.Button(btn_frame, text="Refresh", command=self.refresh_file_list)
        self.refresh_btn.pack(fill='x', pady=3)
        self.add_btn = ttk.Button(btn_frame, text="Add Files", command=self.add_files)
        self.add_btn.pack(fill='x', pady=3)

        # Preview area on right panel
        preview_header = ttk.Label(self.right_panel, text="File Preview", style='Header.TLabel')
        preview_header.pack(side='top', fill='x')

        self.preview_container = Frame(self.right_panel, background='white', relief='sunken', borderwidth=1)
        self.preview_container.pack(fill=BOTH, expand=True, pady=10)

        self.previewer = Previewer(self.preview_container)

        # Load initial files
        self.refresh_file_list()

    def change_directory(self, event=None):
        selected_dir = filedialog.askdirectory(initialdir=self.current_directory.get(), title="Select Directory")
        if selected_dir:
            self.current_directory.set(selected_dir)
            self.refresh_file_list()

    def refresh_file_list(self):
        self.file_listbox.delete(0, END)
        self.files = list_files(self.current_directory.get(), self.supported_extensions)
        for f in self.files:
            self.file_listbox.insert(END, f)
        self.previewer.clear_preview()

    def on_file_select(self, event):
        selection = self.file_listbox.curselection()
        if not selection:
            return
        idx = selection[0]
        filename = self.files[idx]
        filepath = os.path.join(self.current_directory.get(), filename)
        ext = os.path.splitext(filename)[1].lower()

        if ext in ['.jpg', '.jpeg']:
            self.previewer.show_image_preview(filepath)
        elif ext in ['.pdf', '.doc', '.docx']:
            self.previewer.show_file_icon_preview(ext)
        else:
            self.previewer.clear_preview()

    def open_file(self):
        selection = self.file_listbox.curselection()
        if not selection:
            messagebox.showwarning("No Selection", "Please select a file to open.")
            return
        idx = selection[0]
        filename = self.files[idx]
        filepath = os.path.join(self.current_directory.get(), filename)
        open_file(filepath)

    def delete_file(self):
        selection = self.file_listbox.curselection()
        if not selection:
            messagebox.showwarning("No Selection", "Please select a file to delete.")
            return
        idx = selection[0]
        filename = self.files[idx]
        filepath = os.path.join(self.current_directory.get(), filename)
        confirm = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete '{filename}'?")
        if confirm:
            if delete_file(filepath):
                self.refresh_file_list()

    def add_files(self):
        target_dir = self.current_directory.get()
        file_paths = filedialog.askopenfilenames(title="Select files to add")
        if not file_paths:
            return
        for file_path in file_paths:
            try:
                shutil.copy2(file_path, target_dir)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to copy {file_path}:\n{e}")
        self.refresh_file_list()