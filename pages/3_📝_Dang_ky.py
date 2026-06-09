import streamlit as st
import streamlit.components.v1 as components

# ==========================================
# 1. CẤU HÌNH TRANG
# ==========================================
st.set_page_config(page_title="Đăng ký Ghi danh - NaYoB", page_icon="📝", layout="centered")

# Custom CSS đồng bộ giao diện
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
# 2. NHÚNG GOOGLE FORM
# ==========================================
# THẦY DÁN LINK GOOGLE FORM VÀO ĐÂY (Lưu ý: Link gốc, không dùng link rút gọn bit.ly cho iframe)
GOOGLE_FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLScXAAXLN-FXWc9n4888GLyMhqHp8TUMNhUGjkiG8AM1VnhUjw/viewform?usp=header"

if GOOGLE_FORM_URL == "https://docs.google.com/forms/d/e/1FAIpQLScXAAXLN-FXWc9n4888GLyMhqHp8TUMNhUGjkiG8AM1VnhUjw/viewform?usp=header":
    st.warning("⚠️ **Lưu ý dành cho Thầy Nam:** Thầy vui lòng mở file `3_📝_Dang_ky.py` và dán đường link Google Form của thầy vào biến `GOOGLE_FORM_URL` để biểu mẫu hiện ra nhé.")
else:
    # Nếu link chưa có tham số embedded=true, hệ thống sẽ tự thêm vào để form hiển thị đẹp hơn
    if "?embedded=true" not in GOOGLE_FORM_URL:
        if "?" in GOOGLE_FORM_URL:
            GOOGLE_FORM_URL += "&embedded=true"
        else:
            GOOGLE_FORM_URL += "?embedded=true"

    # Nhúng Iframe Google Form với chiều cao 800px để hiển thị đầy đủ
    components.iframe(GOOGLE_FORM_URL, width=700, height=800, scrolling=True)
    
    # Nút dự phòng trong trường hợp trình duyệt điện thoại của phụ huynh chặn iFrame
    st.markdown("---")
    st.markdown("<div style='text-align: center; color: #64748b; font-size: 14px;'>Nếu biểu mẫu phía trên không tải được, Quý phụ huynh vui lòng bấm vào nút dưới đây:</div>", unsafe_allow_html=True)
    
    st.markdown(f"""
        <div style="text-align: center; margin-top: 15px;">
            <a href="{GOOGLE_FORM_URL.replace('?embedded=true', '')}" target="_blank" 
               style="background-color: #005088; color: white; padding: 12px 25px; text-decoration: none; border-radius: 8px; font-weight: bold; display: inline-block;">
               Mở Biểu Mẫu Trên Cửa Sổ Mới
            </a>
        </div>
    """, unsafe_allow_html=True)

# ==========================================
# 3. FOOTER
# ==========================================
st.markdown('<div class="footer">Made by NamY</div>', unsafe_allow_html=True)