import streamlit as st

# ==========================================
# 1. CẤU HÌNH TRANG
# ==========================================
st.set_page_config(page_title="Đăng ký Ghi danh - NaYoB", page_icon="📝", layout="centered")

st.markdown("""
    <style>
    .title-text { color: #005088; font-family: 'Merriweather', serif; font-size: 36px; font-weight: bold; text-align: center; margin-bottom: 5px; }
    .subtitle-text { color: #11caa0; font-size: 18px; text-align: center; font-style: italic; margin-bottom: 20px; }
    .instruction-text { text-align: center; color: #334155; font-size: 16px; margin-bottom: 30px; }
    .footer { text-align: center; color: #94a3b8; font-style: italic; margin-top: 50px; border-top: 1px solid #e2e8f0; padding-top: 15px; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title-text">Phiếu Đăng Ký Ghi Danh</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle-text">Hệ sinh thái Toán học NaYoB — Thầy Đinh Quốc Nam</div>', unsafe_allow_html=True)
st.markdown('<div class="instruction-text">Quý phụ huynh vui lòng điền đầy đủ thông tin vào biểu mẫu dưới đây. Thầy Nam sẽ liên hệ lại qua Zalo/Điện thoại để xác nhận và thông báo địa điểm học chi tiết.</div>', unsafe_allow_html=True)

# ==========================================
# 2. NHÚNG GOOGLE FORM BẰNG HTML GỐC (CHỐNG LỖI 100%)
# ==========================================
# Nhúng Form trực tiếp bằng iframe HTML thay vì dùng thư viện Streamlit
st.markdown("""
    <iframe src="https://docs.google.com/forms/d/e/1FAIpQLScXAAXLN-FXWc9n4888GLyMhqHp8TUMNhUGjkiG8AM1VnhUjw/viewform?embedded=true" 
    width="100%" height="800" frameborder="0" marginheight="0" marginwidth="0">Đang tải…</iframe>
""", unsafe_allow_html=True)

# Nút dự phòng
st.markdown("---")
st.markdown("<div style='text-align: center; color: #64748b; font-size: 14px;'>Nếu biểu mẫu phía trên không tải được, Quý phụ huynh vui lòng bấm vào nút dưới đây:</div>", unsafe_allow_html=True)

clean_url = "https://docs.google.com/forms/d/e/1FAIpQLScXAAXLN-FXWc9n4888GLyMhqHp8TUMNhUGjkiG8AM1VnhUjw/viewform"
st.markdown(f"""
    <div style="text-align: center; margin-top: 15px;">
        <a href="{clean_url}" target="_blank" 
           style="background-color: #005088; color: white; padding: 12px 25px; text-decoration: none; border-radius: 8px; font-weight: bold; display: inline-block;">
           Mở Biểu Mẫu Trên Cửa Sổ Mới
        </a>
    </div>
""", unsafe_allow_html=True)

st.markdown('<div class="footer">Made by NamY</div>', unsafe_allow_html=True)