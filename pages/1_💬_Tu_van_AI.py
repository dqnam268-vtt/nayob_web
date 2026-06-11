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
# 2. XỬ LÝ API KEY TỪ SECRETS
# ==========================================
API_KEY = None
if "GEMINI_API_KEY" in st.secrets:
    API_KEY = st.secrets["GEMINI_API_KEY"]

if not API_KEY:
    st.error("⚠️ **Hệ thống chưa kết nối được với API Key. Thầy vui lòng kiểm tra lại thiết lập Secrets.**")
    st.stop()

# ==========================================
# 3. TRI THỨC CỦA AI
# ==========================================
KNOWLEDGE_BASE = """
BẠN LÀ: Một trợ lý tuyển sinh cực kỳ thân thiện, chuyên nghiệp, lịch sự và thấu hiểu tâm lý của Lớp Toán Thầy Đinh Quốc Nam (Thương hiệu NaYoB - Navigate Yourself).

NHIỆM VỤ:
1. Chào hỏi thân thiện và hỏi phụ huynh cần tư vấn cho khối lớp mấy.
2. Cung cấp thông tin lịch học, học phí (1.000.000 VNĐ/tháng).
3. Hướng dẫn phụ huynh liên hệ Zalo 0356015268 để đăng ký.

THÔNG TIN LỊCH HỌC:
- Lớp 6: Thứ 3 & Thứ 5 (18h15 - 19h45)
- Lớp 7: Thứ 2 & Thứ 4 (17h00 - 18h30)
- Lớp 8: Thứ 3 & Thứ 5 (17h00 - 18h30)
- Lớp 9: Thứ 2 & Thứ 4 (18h15 - 19h45)
"""

# ==========================================
# 4. GIAO DIỆN CHAT TRỰC TIẾP QUA REST API
# ==========================================
if "messages" not in st.session_state:
    st.session_state.messages = [{
        "role": "assistant", 
        "content": (
            "Chào thầy Nam, chào Quý phụ huynh! "
            "Tôi là trợ lý AI của NaYoB. Tôi có thể giúp tra cứu lịch học, "
            "học phí hoặc tư vấn lộ trình học Toán. Anh/chị cần hỗ trợ thông tin gì ạ?"
        )
    }]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Nhập câu hỏi tại đây..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        message_placeholder.markdown("*(Đang suy nghĩ...)*")
        
        try:
            # Gom lịch sử hội thoại
            contents = []
            for m in st.session_state.messages[1:]:
                role = "user" if m["role"] == "user" else "model"
                contents.append({
                    "role": role,
                    "parts": [{"text": m["content"]}]
                })

            # Đóng gói dữ liệu
            payload = {
                "systemInstruction": {"parts": [{"text": KNOWLEDGE_BASE}]},
                "contents": contents
            }
            
            url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"
            headers = {"Content-Type": "application/json"}
            
            # Gửi yêu cầu qua requests
            response = requests.post(url, headers=headers, data=json.dumps(payload))
            
            if response.status_code == 200:
                result = response.json()
                bot_reply = result["candidates"][0]["content"]["parts"][0]["text"]
                
                message_placeholder.markdown(bot_reply)
                st.session_state.messages.append({"role": "assistant", "content": bot_reply})
            else:
                st.error(f"Lỗi phản hồi từ Google: {response.text}")
                message_placeholder.markdown("Xin lỗi, máy chủ AI đang bảo trì. Quý phụ huynh vui lòng liên hệ Zalo 0356015268 để được hỗ trợ ạ.")
                
        except Exception as e:
            st.error(f"Lỗi kết nối mạng: {e}")
            message_placeholder.markdown("Xin lỗi, hệ thống đang bận. Quý phụ huynh vui lòng liên hệ Zalo 0356015268 để được hỗ trợ ạ.")

# ==========================================
# 5. FOOTER
# ==========================================
st.markdown('<div class="footer">Made by NamY</div>', unsafe_allow_html=True)