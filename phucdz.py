import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
import threading

class HaTakiTool:
    def __init__(self, root):
        self.root = root
        self.root.title("HaTaki Tool")
        self.root.geometry("600x400")
        self.root.resizable(True, True)
        
        # Thiết lập dark theme
        self.setup_dark_theme()
        
        # Biến lưu trữ
        self.input_file_path = tk.StringVar()
        self.keyword = tk.StringVar()
        
        # Tạo giao diện
        self.create_widgets()
        
    def setup_dark_theme(self):
        """Thiết lập giao diện dark theme hiện đại"""
        self.root.configure(bg='#2E2E2E')
        
        # Tạo style cho các widget
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Cấu hình style cho các widget
        self.style.configure('TFrame', background='#2E2E2E')
        self.style.configure('TLabel', background='#2E2E2E', foreground='#FFFFFF', font=('Arial', 10))
        self.style.configure('TButton', background='#404040', foreground='#FFFFFF', font=('Arial', 10))
        self.style.configure('TEntry', fieldbackground='#404040', foreground='#FFFFFF', font=('Arial', 10))
        self.style.configure('TProgressbar', troughcolor='#404040', background='#0078D7')
        self.style.configure('Header.TLabel', font=('Arial', 12, 'bold'), foreground='#0078D7')
        
    def create_widgets(self):
        """Tạo các thành phần giao diện"""
        # Frame chính
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Tiêu đề ứng dụng
        title_label = ttk.Label(main_frame, text="HaTaki Tool - Lọc từ khóa trong file txt", style='Header.TLabel')
        title_label.pack(pady=(0, 20))
        
        # Phần 1: Chọn file đầu vào
        file_frame = ttk.Frame(main_frame)
        file_frame.pack(fill=tk.X, pady=10)
        
        file_label = ttk.Label(file_frame, text="Chọn file đầu vào (.txt):")
        file_label.pack(anchor=tk.W)
        
        file_select_frame = ttk.Frame(file_frame)
        file_select_frame.pack(fill=tk.X, pady=5)
        
        self.file_entry = ttk.Entry(file_select_frame, textvariable=self.input_file_path, width=50)
        self.file_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        
        browse_button = ttk.Button(file_select_frame, text="Duyệt", command=self.browse_file)
        browse_button.pack(side=tk.RIGHT)
        
        # Phần 2: Nhập từ khóa cần tìm
        keyword_frame = ttk.Frame(main_frame)
        keyword_frame.pack(fill=tk.X, pady=10)
        
        keyword_label = ttk.Label(keyword_frame, text="Nhập từ khóa cần tìm:")
        keyword_label.pack(anchor=tk.W)
        
        self.keyword_entry = ttk
