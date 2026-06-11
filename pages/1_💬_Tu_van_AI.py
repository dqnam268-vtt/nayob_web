import streamlit as st
import requests
import json

# ==========================================
# 1. CẤU HÌNH TRANG
# ==========================================
st.set_page_config(page_title="Tư vấn Tuyển sinh AI - NaYoB", page_icon="💬", layout="centered")

st.markdown("""
    <style>
    .title-text { color: #005088; font-family: 'Merriweather', serif; font-size: 32px; font-weight: bold; text-align: center; margin-bottom: 10px; }
    .subtitle-text { color: #11caa0; font-size: 18px; text-align: center; font-style: italic; margin-bottom: 20px; }
    .footer { text-align: center; color: #94a3b8; font-style: italic; margin-top: 50px; border-top: 1px solid #e2e8f0; padding-top: 15px; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title-text">Trợ lý AI Tư vấn Tuyển sinh NaYoB</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle-text">Tư vấn lộ trình học Toán 24/7 cùng Thầy Đinh Quốc Nam</div>', unsafe_allow_html=True)
st.markdown("---")

# ==========================================
# 2. XỬ LÝ API KEY
# ==========================================
API_KEY = None
if "GEMINI_API_KEY" in st.secrets:
    API_KEY = st.secrets["GEMINI_API_KEY"]

if not API_KEY:
    st.error("⚠️ **Hệ thống chưa kết nối được với não bộ AI (Thiếu API Key)!**")
    st.stop()

# ==========================================
# 3. "BỘ NÃO" TRI THỨC CỦA AI
# ==========================================
KNOWLEDGE_BASE = """
BẠN LÀ: Một trợ lý tuyển sinh cực kỳ thân thiện, chuyên nghiệp, lịch sự và thấu hiểu tâm lý của Lớp Toán Thầy Đinh Quốc Nam (Thương hiệu NaYoB - Navigate Yourself).

NHIỆM VỤ CỦA BẠN:
1. Chào hỏi thân thiện và hỏi xem phụ huynh/học sinh cần tư vấn cho khối lớp mấy.
2. Cung cấp thông tin chính xác về lịch học, học phí.
3. Nhấn mạnh vào hồ sơ chuyên môn vượt trội của Thầy Nam để tạo niềm tin.
4. Hướng dẫn phụ huynh liên hệ Zalo 0356015268 hoặc điền form để đăng ký giữ chỗ.

--- THÔNG TIN CHUYÊN MÔN CỦA THẦY ĐINH QUỐC NAM ---
- Hơn 11 năm kinh nghiệm giảng dạy tại THCS Võ Trường Toản (TP.HCM).
- Học vấn: Thạc sĩ Lý luận & Phương pháp dạy học Toán, Cử nhân Sư phạm Toán - Tin (Xuất sắc), Cử nhân Ngôn ngữ Anh.
- Thành tích: 9 năm liên tiếp bồi dưỡng học sinh giỏi Toán cấp Thành phố.
- Phương pháp dạy "Navigate Yourself": Tuyệt đối không dạy học vẹt, rèn luyện tư duy tự định hướng.

--- THÔNG TIN KHÓA HỌC & HỌC PHÍ ---
* Học phí chung cho tất cả các lớp THCS (6, 7, 8, 9) là: 1.000.000 VNĐ/tháng.
* Lớp Toán 6: Thứ 3 & Thứ 5 (18h15 - 19h45)
* Lớp Toán 7: Thứ 2 & Thứ 4 (17h00 - 18h30)
* Lớp Toán 8: Thứ 3 & Thứ 5 (17h00 - 18h30)
* Lớp Toán 9 (Trọng tâm ôn thi vào 10): Thứ 2 & Thứ 4 (18h15 - 19h45)
"""

# ==========================================
# 4. GIAO DIỆN CHAT (SỬ DỤNG GIAO THỨC TRỰC TIẾP API)
# ==========================================
if "messages" not in st.session_state:
    st.session_state.messages = [{
        "role": "assistant", 
        "content": "Chào thầy Nam, chào Quý phụ huynh! Tôi là trợ lý AI của NaYoB. Tôi