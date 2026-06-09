import streamlit as st

# ==========================================
# 1. CẤU HÌNH TRANG WEB
# ==========================================
st.set_page_config(
    page_title="Lớp Toán Thầy Đinh Quốc Nam - NaYoB",
    page_icon="🧮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS để tối ưu giao diện theo tone màu chuyên nghiệp
st.markdown("""
    <style>
    .main-title { color: #005088; font-family: 'Merriweather', serif; font-size: 42px; font-weight: bold; text-align: center; margin-bottom: 5px; }
    .subtitle { color: #11caa0; font-size: 22px; text-align: center; font-style: italic; margin-bottom: 30px; }
    .section-header { color: #005088; border-left: 5px solid #11caa0; padding-left: 15px; margin-top: 30px; margin-bottom: 20px; }
    .footer { text-align: center; color: #94a3b8; font-style: italic; margin-top: 50px; border-top: 1px solid #e2e8f0; padding-top: 15px; }
    .highlight-box { background-color: #f1f5f9; padding: 20px; border-radius: 10px; border-left: 4px solid #005088; margin-bottom: 15px; }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 2. BANNER & TIÊU ĐỀ CHÍNH
# ==========================================
st.markdown('<div class="main-title">LỚP TOÁN THẦY ĐINH QUỐC NAM</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Thương hiệu Giáo dục NaYoB — Navigate Yourself</div>', unsafe_allow_html=True)

# ==========================================
# 3. THÔNG TIN LIÊN HỆ & TỔNG QUAN
# ==========================================
col1, col2 = st.columns([1, 2.2])

with col1:
    st.info("💡 **HƯỚNG DẪN:**\n\nSử dụng thanh menu bên trái để chuyển sang trang **💬 Tư vấn AI** hoặc xem **📅 Lịch học & Học phí**.")
    st.markdown("### 📞 Thông tin liên hệ")
    st.success("**Hotline / Zalo:** 0356015268\n\n**Email:** dqnam268@gmail.com\n\n**Địa điểm:** TP. Hồ Chí Minh *(Liên hệ để nhận địa chỉ cơ sở chi tiết)*")

with col2:
    st.markdown('<h3 class="section-header" style="margin-top: 0;">🎓 Chuyên gia Giáo dục & Nhà sáng lập NaYoB</h3>', unsafe_allow_html=True)
    st.markdown("""
    Với hơn **11 năm kinh nghiệm** tận tâm trong ngành giáo dục cấp THCS, Thầy **Đinh Quốc Nam** (hiện đang công tác tại Trường THCS Võ Trường Toản, TP.HCM) luôn tiên phong tích hợp công nghệ và học liệu số vào giảng dạy Toán học.
    
    **Nền tảng học vấn vững chắc:**
    * 🎓 **Thạc sĩ** Lý luận và Phương pháp dạy học môn Toán (Đại học Sài Gòn).
    * 🎓 **Cử nhân Sư phạm Toán - Tin học** (Đại học Cần Thơ) — Tốt nghiệp loại **Xuất sắc**.
    * 🎓 **Cử nhân Ngôn ngữ Anh** (Đại học Cửu Long) — Cung cấp tư duy song ngữ và khả năng khai thác các phương pháp giáo dục quốc tế.
    """)

# ==========================================
# 4. KINH NGHIỆM & THÀNH TÍCH NỔI BẬT
# ==========================================
st.markdown('<h3 class="section-header">🏆 Bề dày Thành tích & Nghiên cứu khoa học</h3>', unsafe_allow_html=True)

col_achieve, col_research = st.columns(2)

with col_achieve:
    st.markdown('<div class="highlight-box">', unsafe_allow_html=True)
    st.markdown("""
    **Thành tích Đào tạo & Công tác:**
    * 🥇 **9 năm liên tiếp** bồi dưỡng học sinh đạt Giải Học sinh giỏi Toán cấp Thành phố.
    * 🏅 Nhận **Bằng khen của Ủy ban Nhân dân TP.HCM** vì những đóng góp xuất sắc cho phong trào thi đua của Thành phố (Năm học 2021-2022 và 2022-2023).
    * 🌟 Đạt danh hiệu **Giáo viên Chủ nhiệm Giỏi** (2023-2026) và Lao động Tiên tiến 9 năm liền.
    * 🧮 **Chuyên gia máy tính cầm tay:** Nhiều năm kinh nghiệm bồi dưỡng học sinh giải toán nhanh bằng Casio, tối ưu điểm số thi trắc nghiệm.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

with col_research:
    st.markdown('<div class="highlight-box">', unsafe_allow_html=True)
    st.markdown("""
    **Nghiên cứu & Xuất bản Khoa học:**
    
    Tác giả của các bài báo khoa học trên **Tạp chí Khoa học Giáo dục Việt Nam (2025)**, khẳng định sự đầu tư nghiêm túc về học thuật:
    * 📚 *Thiết kế và Đánh giá hệ thống VisuoGeometry-Trainer: Hệ thống học tập thích ứng ứng dụng Truy vết Kiến thức Bayes cho hình học trực quan lớp 7.*
    * 📚 *Ứng dụng học liệu số trong dạy học các hình khối thực tiễn môn Toán lớp 8.*
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# 5. TRIẾT LÝ GIÁO DỤC NAYOB
# ==========================================
st.markdown('<h3 class="section-header">🎯 Triết lý Giáo dục: "Navigate Yourself"</h3>', unsafe_allow_html=True)
st.markdown("""
Tại **NaYoB**, chúng tôi tin rằng vai trò của người thầy không chỉ là truyền đạt công thức, mà là **định hướng giúp học sinh tự khai phá năng lực của chính mình**. 
* **Học hiểu bản chất, không học vẹt:** Rèn luyện tư duy logic để học sinh tự thiết lập sơ đồ giải quyết cho mọi dạng bài.
* **Môi trường thấu hiểu:** Kỷ luật nhưng luôn đồng hành, giúp các em học sinh giảm bớt áp lực tâm lý và thực sự yêu thích môn Toán.
""")

# ==========================================
# 6. CHÂN TRANG (FOOTER CHUẨN)
# ==========================================
st.markdown('<div class="footer">Made by NamY</div>', unsafe_allow_html=True)