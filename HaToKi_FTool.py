import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
import threading

class HaToKiFTool:
    def __init__(self, root):
        self.root = root
        self.root.title("HaToKi FTool")
        self.root.geometry("600x400")
        self.root.resizable(False, False)
        
        # Thiết lập màu sắc cho theme tối
        self.bg_color = "#2b2b2b"
        self.fg_color = "#ffffff"
        self.accent_color = "#007acc"
        self.secondary_bg = "#3c3c3c"
        
        # Cấu hình style
        self.setup_styles()
        
        # Tạo giao diện
        self.create_widgets()
        
    def setup_styles(self):
        """Thiết lập style cho các widget với theme tối"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Cấu hình style cho các widget
        style.configure("TFrame", background=self.bg_color)
        style.configure("TLabel", background=self.bg_color, foreground=self.fg_color, font=("Segoe UI", 10))
        style.configure("TButton", 
                        background=self.accent_color, 
                        foreground=self.fg_color,
                        font=("Segoe UI", 10, "bold"),
                        focuscolor="none")
        style.map("TButton", 
                 background=[('active', self.accent_color), ('pressed', self.accent_color)],
                 foreground=[('active', self.fg_color), ('pressed', self.fg_color)])
        style.configure("TEntry", 
                        fieldbackground=self.secondary_bg, 
                        foreground=self.fg_color,
                        insertcolor=self.fg_color)
        
    def create_widgets(self):
        """Tạo các widget cho giao diện người dùng"""
        # Frame chính
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Tiêu đề ứng dụng
        title_label = ttk.Label(main_frame, text="HaToKi FTool", font=("Segoe UI", 18, "bold"))
        title_label.pack(pady=(0, 20))
        
        # Phần 1: Chọn file đầu vào
        file_frame = ttk.Frame(main_frame)
        file_frame.pack(fill=tk.X, pady=10)
        
        file_label = ttk.Label(file_frame, text="Chọn file đầu vào (.txt):")
        file_label.pack(anchor=tk.W)
        
        file_input_frame = ttk.Frame(file_frame)
        file_input_frame.pack(fill=tk.X, pady=5)
        
        self.file_path = tk.StringVar()
        self.file_entry = ttk.Entry(file_input_frame, textvariable=self.file_path, state="readonly")
        self.file_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        
        browse_btn = ttk.Button(file_input_frame, text="Duyệt", command=self.browse_file)
        browse_btn.pack(side=tk.RIGHT)
        
        # Phần 2: Nhập từ khóa
        keyword_frame = ttk.Frame(main_frame)
        keyword_frame.pack(fill=tk.X, pady=10)
        
        keyword_label = ttk.Label(keyword_frame, text="Nhập từ khóa cần tìm:")
        keyword_label.pack(anchor=tk.W)
        
        self.keyword_var = tk.StringVar()
        keyword_entry = ttk.Entry(keyword_frame, textvariable=self.keyword_var)
        keyword_entry.pack(fill=tk.X, pady=5)
        
        # Nút Find
        find_btn = ttk.Button(main_frame, text="Find", command=self.start_filtering)
        find_btn.pack(pady=10)
        
        # Thanh tiến trình
        self.progress = ttk.Progressbar(main_frame, mode='determinate')
        self.progress.pack(fill=tk.X, pady=10)
        
        # Label hiển thị trạng thái
        self.status_label = ttk.Label(main_frame, text="Sẵn sàng", font=("Segoe UI", 9))
        self.status_label.pack(pady=5)
        
        # Nút mở thư mục kết quả
        self.open_folder_btn = ttk.Button(main_frame, text="Mở thư mục chứa kết quả", 
                                         command=self.open_result_folder, state="disabled")
        self.open_folder_btn.pack(pady=10)
        
        # Thông tin footer
        footer_label = ttk.Label(main_frame, text="HaToKi FTool - Công cụ lọc file txt chuyên nghiệp", 
                                font=("Segoe UI", 8), foreground="#aaaaaa")
        footer_label.pack(side=tk.BOTTOM, pady=10)
        
    def browse_file(self):
        """Mở hộp thoại để chọn file txt"""
        file_path = filedialog.askopenfilename(
            title="Chọn file txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if file_path:
            self.file_path.set(file_path)
            
    def start_filtering(self):
        """Bắt đầu quá trình lọc file trong một thread riêng"""
        # Kiểm tra đầu vào
        if not self.file_path.get():
            messagebox.showerror("Lỗi", "Vui lòng chọn file đầu vào!")
            return
            
        if not self.keyword_var.get():
            messagebox.showerror("Lỗi", "Vui lòng nhập từ khóa!")
            return
            
        # Vô hiệu hóa nút Find trong khi xử lý
        self.find_button_state = "disabled"
        
        # Khởi chạy thread để xử lý file
        thread = threading.Thread(target=self.filter_file)
        thread.daemon = True
        thread.start()
        
    def filter_file(self):
        """Lọc file theo từ khóa và ghi kết quả ra file output.txt"""
        try:
            input_file = self.file_path.get()
            keyword = self.keyword_var.get().lower()  # Chuyển về chữ thường để so sánh không phân biệt hoa thường
            output_file = "output.txt"
            
            # Đếm tổng số dòng để thiết lập thanh tiến trình
            total_lines = 0
            with open(input_file, 'r', encoding='utf-8') as f:
                for _ in f:
                    total_lines += 1
            
            # Reset và thiết lập thanh tiến trình
            self.progress['value'] = 0
            self.progress['maximum'] = total_lines
            
            # Mở file để đọc và ghi
            with open(input_file, 'r', encoding='utf-8') as infile, \
                 open(output_file, 'w', encoding='utf-8') as outfile:
                
                lines_processed = 0
                matches_found = 0
                
                # Đọc từng dòng và kiểm tra từ khóa
                for line in infile:
                    if keyword in line.lower():  # So sánh không phân biệt hoa thường
                        outfile.write(line)
                        matches_found += 1
                    
                    lines_processed += 1
                    # Cập nhật thanh tiến trình
                    progress_percent = (lines_processed / total_lines) * 100
                    self.root.after(0, self.update_progress, progress_percent, lines_processed, total_lines, matches_found)
            
            # Hoàn thành
            self.root.after(0, self.filter_complete, matches_found)
            
        except Exception as e:
            self.root.after(0, self.filter_error, str(e))
    
    def update_progress(self, value, current, total, matches):
        """Cập nhật thanh tiến trình và trạng thái"""
        self.progress['value'] = value
        self.status_label.config(text=f"Đang xử lý: {current}/{total} dòng - Tìm thấy: {matches} kết quả")
        
    def filter_complete(self, matches_found):
        """Xử lý khi quá trình lọc hoàn tất"""
        self.progress['value'] = 100
        self.status_label.config(text=f"Hoàn thành! Tìm thấy {matches_found} kết quả phù hợp")
        messagebox.showinfo("Thành công", f"Đã tạo file output.txt thành công.\nTìm thấy {matches_found} dòng phù hợp.")
        
        # Kích hoạt nút mở thư mục
        self.open_folder_btn.config(state="normal")
        
    def filter_error(self, error_msg):
        """Xử lý khi có lỗi xảy ra"""
        self.status_label.config(text="Đã xảy ra lỗi!")
        messagebox.showerror("Lỗi", f"Đã xảy ra lỗi khi xử lý file:\n{error_msg}")
        
    def open_result_folder(self):
        """Mở thư mục chứa file kết quả"""
        result_path = os.path.abspath("output.txt")
        folder_path = os.path.dirname(result_path)
        
        # Mở thư mục trong file explorer
        if os.name == 'nt':  # Windows
            os.system(f'explorer /select,"{result_path}"')
        elif os.name == 'posix':  # macOS, Linux
            if os.uname().sysname == 'Darwin':  # macOS
                os.system(f'open -R "{result_path}"')
            else:  # Linux
                os.system(f'xdg-open "{folder_path}"')

def main():
    root = tk.Tk()
    app = HaToKiFTool(root)
    root.mainloop()

if __name__ == "__main__":
    main()
