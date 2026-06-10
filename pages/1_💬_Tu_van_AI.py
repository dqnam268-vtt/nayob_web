import streamlit as st
import google.generativeai as genai

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
# 2. XỬ LÝ API KEY (BẢO MẬT TUYỆT ĐỐI)
# ==========================================
API_KEY = None

try:
    # Lấy Key từ "két sắt" Secrets
    if "GEMINI_API_KEY" in st.secrets:
        API_KEY = st.secrets["GEMINI_API_KEY"]
except:
    pass

# Cảnh báo chi tiết nếu không tìm thấy Key
if not API_KEY:
    st.error("⚠️ **Hệ thống chưa kết nối được với não bộ AI (Thiếu API Key)!**")
    st.info("""
    💡 **Hướng dẫn khắc phục:**
    * **Nếu trang này đang chạy trên mạng (Streamlit Cloud):** Thầy hãy vào phần *Settings > Secrets* và dán mã `GEMINI_API_KEY = "mã_key_mới_của_thầy"` vào.
    * **Nếu trang này đang chạy trên máy tính của thầy:** Thầy cần tạo một thư mục tên là `.streamlit` nằm cùng chỗ với file `app.py`. Bên trong thư mục đó, tạo một file tên là `secrets.toml` và dán mã Key vào y như trên Cloud.
    """)
    st.stop()

# KẾT NỐI CHÌA KHÓA CHUẨN VỚI HỆ THỐNG
genai.configure(api_key=API_KEY)

# ==========================================
# 3. "BỘ NÃO" TRI THỨC CỦA AI (SYSTEM INSTRUCTION)
# ==========================================
KNOWLEDGE_BASE = """
BẠN LÀ: Một trợ lý tuyển sinh cực kỳ thân thiện, chuyên nghiệp, lịch sự và thấu hiểu tâm lý của Lớp Toán Thầy Đinh Quốc Nam (Thương hiệu NaYoB - Navigate Yourself).

NHIỆM VỤ CỦA BẠN:
1. Chào hỏi thân thiện và hỏi xem phụ huynh/học sinh cần tư vấn cho khối lớp mấy.
2. Cung cấp thông tin chính xác về lịch học, học phí dựa trên dữ liệu bên dưới.
3. Nhấn mạnh vào hồ sơ chuyên môn vượt trội của Thầy Nam để tạo niềm tin.
4. Hướng dẫn phụ huynh liên hệ Zalo hoặc điền form để đăng ký giữ chỗ.

--- THÔNG TIN CHUYÊN MÔN CỦA THẦY ĐINH QUỐC NAM ---
- Hơn 11 năm kinh nghiệm giảng dạy tại THCS Võ Trường Toản (TP.HCM).
- Học vấn: Thạc sĩ Lý luận & Phương pháp dạy học Toán, Cử nhân Sư phạm Toán - Tin (Xuất sắc), Cử nhân Ngôn ngữ Anh.
- Thành tích: 9 năm liên tiếp bồi dưỡng học sinh giỏi Toán cấp Thành phố.
- Chuyên môn đặc biệt: Chuyên gia bồi dưỡng kỹ năng giải toán trắc nghiệm nhanh bằng máy tính cầm tay Casio.
- Phương pháp dạy "Navigate Yourself": Tuyệt đối không dạy học vẹt, rèn luyện tư duy tự định hướng, giảm áp lực, giúp học sinh yêu Toán hơn.

--- THÔNG TIN KHÓA HỌC & HỌC PHÍ ---
* Học phí chung cho tất cả các lớp THCS (6, 7, 8, 9) là: 1.000.000 VNĐ/tháng.

* Lịch học cụ thể:
1. Lớp Toán 6: Thứ 3 & Thứ 5 (18h15 - 19h45)
2. Lớp Toán 7: Thứ 2 & Thứ 4 (17h00 - 18h30)
3. Lớp Toán 8: Thứ 3 & Thứ 5 (17h00 - 18h30)
4. Lớp Toán 9 (Trọng tâm ôn thi vào 10): Thứ 2 & Thứ 4 (18h15 - 19h45)

--- THÔNG TIN LIÊN HỆ ĐĂNG KÝ ---
- Hotline/Zalo trực tiếp Thầy Nam: 0356015268
- Địa điểm: TP. Hồ Chí Minh (Phụ huynh vui lòng gọi hotline để nhận định vị cơ sở chính xác).
- Link Form Đăng ký: Truy cập trang Đăng ký trên menu bên trái để điền thông tin.
------------------------------------
LƯU Ý KHI TRẢ LỜI: Trả lời ngắn gọn, súc tích, chia đoạn rõ ràng. Khéo léo mời phụ huynh cung cấp thêm thông tin về học lực của học sinh để tư vấn sâu hơn.
"""

# Khởi tạo mô hình AI (Sử dụng bản Flash chuẩn và ổn định nhất)
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction=KNOWLEDGE_BASE
)

# ==========================================
# 4. GIAO DIỆN KHUNG CHAT
# ==========================================
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append({
        "role": "assistant", 
        "content": "Kính chào Quý phụ huynh và các em học sinh! 👋\n\nTôi là trợ lý AI của trung tâm Toán NaYoB (Thầy Đinh Quốc Nam). Tôi có thể giúp anh/chị tra cứu lịch học, học phí, hoặc tư vấn lộ trình học cho các em khối THCS. Anh/chị cần hỗ trợ thông tin gì ạ?"
    })

# Hiển thị các tin nhắn cũ
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Xử lý tin nhắn mới
if prompt := st.chat_input("Nhập tin nhắn để tư vấn (VD: Thầy tư vấn giúp lớp 9)..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        message_placeholder.markdown("*(Đang suy nghĩ...)*")
        
        try:
            # Lọc lịch sử chat để gửi cho AI (BỎ QUA LỜI CHÀO ĐẦU TIÊN CỦA BOT ĐỂ KHÔNG BỊ LỖI)
            history = [
                {"role": "user" if m["role"] == "user" else "model", "parts": [m["content"]]} 
                for m in st.session_state.messages[1:-1]
            ]
            chat = model.start_chat(history=history)
            
            # Gửi tin nhắn và nhận phản hồi
            response = chat.send_message(prompt)
            full_response = response.text
            
            message_placeholder.markdown(full_response)
            st.session_state.messages.append({"role": "assistant", "content": full_response})
            
        except Exception as e:
            st.error(f"Lỗi: {e}")
            message_placeholder.markdown(f"Xin lỗi, hệ thống đang bận. Quý phụ huynh vui lòng liên hệ trực tiếp qua Zalo **0356015268** để được hỗ trợ nhanh nhất ạ.")

# ==========================================
# 5. FOOTER
# ==========================================
st.markdown('<div class="footer">Made by NamY</div>', unsafe_allow_html=True)