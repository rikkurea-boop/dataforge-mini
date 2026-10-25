# DataForge Mini

**Tên đề tài:** Xây dựng ứng dụng xử lý, phân tích và trực quan hóa dữ liệu bằng Python.

Project độc lập phục vụ bài tập **Chương 5.5 – NumPy, Pandas, Matplotlib**. Tiêu chí cao nhất: **tối giản, đúng trọng tâm, chạy được, và người học giải thích được toàn bộ cấu trúc cùng code**.

**Trạng thái:** R01–R05 đã hoàn thành nghiên cứu trên branch PR #1; R06 là bước tiếp theo. **Chưa triển khai ứng dụng**. Mọi file code trong cây dưới đây chỉ là kế hoạch.

## Hướng dẫn cho AI mới
Đọc theo thứ tự: [AGENTS.md](AGENTS.md) → [RULEBOOK.md](RULEBOOK.md) → [PROJECT_SPEC.md](PROJECT_SPEC.md) → [docs/REQUIREMENTS.md](docs/REQUIREMENTS.md) → [docs/PLAN.md](docs/PLAN.md) → [docs/STATUS_HANDOFF.md](docs/STATUS_HANDOFF.md). Sau đó đọc code/test thực tế (nếu có) và tiếp tục task đầu tiên chưa hoàn thành. Không được nhận định tính năng đã xong chỉ vì có trong tài liệu.

## Cấu trúc code dự kiến (không phải file đã có)
```text
dataforge-mini/
├── app.py               # Streamlit UI: tối thiểu, dễ thuyết trình
├── analysis.py          # pandas + numpy: load, clean, statistics
├── charts.py            # matplotlib plots
├── sample_data.csv      # dataset học tập tổng hợp
├── requirements.txt
├── tests/
│   └── test_analysis.py
├── README.md
├── AGENTS.md
├── RULEBOOK.md
├── PROJECT_SPEC.md
└── docs/
    ├── PLAN.md
    ├── REQUIREMENTS.md
    └── STATUS_HANDOFF.md
```

Không thêm module/class/layer chỉ để "đẹp kiến trúc". Chỉ tách file khi giúp code dễ giải thích hơn.

## Mối quan hệ với DataForge gốc
Repo [Data-Forge](https://github.com/rikkurea-boop/Data-Forge) là training-data factory riêng; **không sửa, không import, không bắt DataForge Mini phụ thuộc vào nó**. Dự án này là bài tập độc lập.
