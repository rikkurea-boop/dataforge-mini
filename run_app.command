#!/bin/zsh
set -e
cd "$(dirname "$0")"

echo "=== Đang khởi động DataForge Mini ==="

PYTHON_BIN=""
if [ -x "/opt/homebrew/bin/python3.13" ]; then
    PYTHON_BIN="/opt/homebrew/bin/python3.13"
elif command -v python3.13 >/dev/null 2>&1; then
    PYTHON_BIN="$(command -v python3.13)"
elif command -v python3 >/dev/null 2>&1; then
    PYTHON_BIN="$(command -v python3)"
else
    echo "Lỗi: Không tìm thấy Python 3 trên máy."
    read -k 1 "?Nhấn phím bất kỳ để đóng..."
    exit 1
fi

if [ ! -x ".venv/bin/python" ]; then
    echo "Đang tạo môi trường ảo (.venv) và cài đặt thư viện lần đầu..."
    "$PYTHON_BIN" -m venv .venv
    .venv/bin/python -m pip install -r requirements.txt
fi

echo "Đang mở ứng dụng trên trình duyệt (http://localhost:8501)..."
echo "(Nhấn Ctrl + C tại cửa sổ này khi muốn tắt ứng dụng)"
.venv/bin/python -m streamlit run app.py
