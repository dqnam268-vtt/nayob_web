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
# 2. KHỞI TẠO AI (CẤU HÌNH CHUẨN)
# ==========================================
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    # Sử dụng model gốc, không thêm đuôi nếu không cần thiết
    model = genai.GenerativeModel('gemini-1.5-flash')
else:
    st.error("Chưa cấu hình API Key trong Streamlit Secrets!")
    st.stop()

# ==========================================
# 3. GIAO DIỆN CHAT
# ==========================================
if "messages" not in st.session_state:
    st.session_state.messages = [{
        "role": "assistant", 
        "content": "Chào thầy Nam, chào Quý phụ huynh! Tôi là trợ lý AI của NaYoB. Tôi có thể giúp gì cho anh/chị hôm nay ạ?"
    }]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Nhập câu hỏi..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        
        try:
            # Chuyển đổi lịch sử chat sang định dạng của Gemini
            history = [
                {"role": "user" if m["role"] == "user" else "model", "parts": [m["content"]]} 
                for m in st.session_state.messages[:-1]
            ]
            chat = model.start_chat(history=history)
            response = chat.send_message(prompt)
            
            message_placeholder.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error("Hệ thống AI đang tạm nghỉ, thầy vui lòng kiểm tra lại kết nối hoặc thử lại sau.")
            st.write(f"Chi tiết lỗi: {e}")

# ==========================================
# 4. FOOTER
# ==========================================
st.markdown('<div class="footer">Made by NamY</div>', unsafe_allow_html=True)