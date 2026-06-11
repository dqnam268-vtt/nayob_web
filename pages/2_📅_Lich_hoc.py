import streamlit as st
import pandas as pd

# ==========================================
# 1. CẤU HÌNH TRANG
# ==========================================
st.set_page_config(page_title="Lịch học và Học phí - NaYoB", page_icon="📅", layout="centered")

# Custom CSS đồng bộ giao diện
st.markdown("""
    <style>
    .title-text { color: #005088; font-family: 'Merriweather', serif; font-size: 36px; font-weight: bold; text-align: center; margin-bottom: 5px; }
    .subtitle-text { color: #11caa0; font-size: 18px; text-align: center; font-style: italic; margin-bottom: 30px; }
    .section-header { color: #005088; border-bottom: 2px solid #11caa0; padding-bottom: 10px; margin-top: 30px; margin-bottom: 20px; }
    .price-tag { font-size: 32px; font-weight: bold; color: #d97706; text-align: center; background-color: #fef3c7; padding: 15px; border-radius: 10px; border: 1px solid #fde68a; margin-bottom: 30px;}
    .footer { text-align: center; color: #94a3b8; font-style: italic; margin-top: 50px; border-top: 1px solid #e2e8f0; padding-top: 15px; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title-text">Bảng Thời Khóa Biểu & Học Phí</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle-text">Hệ thống Lớp Toán THCS NaYoB — Thầy Đinh Quốc Nam</div>', unsafe_allow_html=True)

# ==========================================
# 2. THÔNG TIN HỌC PHÍ CHUNG
# ==========================================
st.markdown('<h3 class="section-header">💎 Chính sách Học phí</h3>', unsafe_allow_html=True)
st.markdown('<div class="price-tag">1.000.000 VNĐ / Tháng</div>', unsafe_allow_html=True)
st.markdown("""
* **Áp dụng đồng giá** cho tất cả các khối lớp (Từ lớp 6 đến lớp 9).
* Mức phí này đã bao gồm toàn bộ tài liệu học tập thiết kế riêng , hệ thống bài tập rèn luyện tư duy và kiểm tra định kỳ.
""")

# ==========================================
# 3. BẢNG THỜI KHÓA BIỂU
# ==========================================
st.markdown('<h3 class="section-header">📅 Lịch học chi tiết</h3>', unsafe_allow_html=True)

# Tạo dữ liệu bảng bằng Pandas để hiển thị đẹp mắt trên Streamlit
data = {
    "Khối Lớp": ["Toán 6", "Toán 7", "Toán 8", "Toán 9 (Ôn thi vào 10)"],
    "Ngày Học": ["Thứ 3 và Thứ 5", "Thứ 2 và Thứ 4", "Thứ 3 và Thứ 5", "Thứ 2 và Thứ 4"],
    "Khung Giờ": ["18h45 - 20h15", "17h00 - 18h30", "17h00 - 18h30", "18h45 - 20h15"],
    "Mục Tiêu Trọng Tâm": ["Lấy gốc và Bồi dưỡng tư duy", "Phát triển tư duy logic", "Tăng cường kỹ năng giải bài", "Luyện đề bám sát cấu trúc thi"]
}

df_schedule = pd.DataFrame(data)

# Hiển thị bảng không có index (số thứ tự ở cột đầu)
st.table(df_schedule.set_index("Khối Lớp"))

# ==========================================
# 4. THÔNG TIN ĐỊA ĐIỂM & LIÊN HỆ
# ==========================================
st.markdown('<h3 class="section-header">📍 Địa điểm và Đăng ký</h3>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.info("""
    **Cơ sở học tập:**
    Khu vực TP. Hồ Chí Minh.
    
    *(Để đảm bảo sắp xếp lớp phù hợp với vị trí địa lý của học sinh, Quý phụ huynh vui lòng liên hệ trực tiếp để nhận định vị cơ sở chính xác).*
    """)
with col2:
    st.success("""
    **Liên hệ trực tiếp Thầy Nam:**
    * 📞 **Hotline/Zalo:** 0356015268
    * 💬 Hoặc sử dụng tính năng **Trợ lý AI** trên thanh menu bên trái để được tư vấn tự động 24/7.
    """)

# ==========================================
# 5. FOOTER
# ==========================================
st.markdown('<div class="footer">Made by NamY</div>', unsafe_allow_html=True)