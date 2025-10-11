#!/bin/sh
echo "🔧 Đang chuẩn bị môi trường iSH..."

# Cập nhật hệ thống
apk update && apk upgrade

# Cài Python 3.12 + pip + virtualenv
echo "📦 Đang cài Python 3.12 và pip..."
apk add python3 py3-pip py3-virtualenv --no-cache

# Nếu gói không có sẵn thì tải thủ công từ mirror Alpine
if [ $? -ne 0 ]; then
    echo "⚠️ Không tìm thấy gói Python, tải thủ công..."
    wget https://dl-cdn.alpinelinux.org/alpine/v3.20/main/aarch64/python3-3.12.3-r0.apk
    apk add --allow-untrusted python3-3.12.3-r0.apk
    apk add py3-pip py3-virtualenv
fi

# Kiểm tra cài đặt
echo "✅ Kiểm tra phiên bản:"
python3 --version
pip3 --version

# Tạo thư mục test
mkdir -p ~/python_test
cd ~/python_test
echo "print('✅ Python hoạt động trong iSH!')" > test.py

# Chạy thử
echo "▶️ Chạy thử file test.py:"
python3 test.py

echo "🎉 Hoàn tất! Python 3.12 + pip đã sẵn sàng trên iSH."
