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
# 2. ĐƯỜNG DẪN PROXY (GOOGLE APPS SCRIPT)
# ==========================================
# Sử dụng trực tiếp đường link trung gian của thầy thay cho API Key
APPS_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbzi8UZVwXnrY_8AEBnwbLUAxEAz6xzeDAJP24kO8wBd9c5g0mdmhx6Qpg0JQkNJuCOg/exec"

# ==========================================
# 3. TRI THỨC CỦA AI
# ==========================================
KNOWLEDGE_BASE = """
BẠN LÀ: Trợ lý tuyển sinh của Lớp Toán Thầy Đinh Quốc Nam (NaYoB).

THÔNG TIN LỊCH HỌC & HỌC PHÍ:
- Học phí chung: 1.000.000 VNĐ/tháng.
- Lớp 6: Thứ 3 & Thứ 5 (18h15 - 19h45)
- Lớp 7: Thứ 2 & Thứ 4 (17h00 - 18h30)
- Lớp 8: Thứ 3 & Thứ 5 (17h00 - 18h30)
- Lớp 9: Thứ 2 & Thứ 4 (18h15 - 19h45)

LIÊN HỆ: 
- Hướng dẫn phụ huynh liên hệ Hotline/Zalo trực tiếp Thầy Nam: 0356015268.
"""

# ==========================================
# 4. GIAO DIỆN CHAT 
# ==========================================
if "messages" not in st.session_state:
    st.session_state.messages = [{
        "role": "assistant", 
        "content": "Chào thầy Nam, chào Quý phụ huynh! Tôi là trợ lý AI của NaYoB. Anh/chị cần tra cứu lịch học, học phí cho khối lớp mấy ạ?"
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
            # 1. Chế tạo lịch sử hội thoại
            history_text = ""
            for msg in st.session_state.messages[-4:-1]:
                nguoi_gui = "Phụ huynh" if msg["role"] == "user" else "Trợ lý"
                history_text += f"{nguoi_gui}: {msg['content']}\n"

            full_prompt = f"""
            Lịch sử trò chuyện gần đây:
            {history_text}
            
            Câu hỏi mới của phụ huynh: {prompt}
            """
            
            # 2. Đóng gói dữ liệu gửi thẳng qua link Apps Script của thầy
            payload = {
                "action": "solve",
                "contents": [{"parts": [{"text": full_prompt}]}],
                "systemInstruction": {"parts": [{"text": KNOWLEDGE_BASE}]}
            }
            
            response = requests.post(
                APPS_SCRIPT_URL,
                headers={"Content-Type": "text/plain;charset=utf-8"},
                data=json.dumps(payload),
                allow_redirects=True
            )
            
            # 3. Xử lý câu trả lời trả về
            if response.status_code == 200:
                data = response.json()
                bot_reply = data.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "")
                
                if not bot_reply:
                    bot_reply = "Xin lỗi, hiện tại AI chưa thể xử lý câu hỏi này."
                    
                message_placeholder.markdown(bot_reply)
                st.session_state.messages.append({"role": "assistant", "content": bot_reply})
            else:
                st.error(f"Lỗi đường truyền trung gian: Máy chủ phản hồi mã {response.status_code}")
                
        except Exception as e:
            st.error(f"Lỗi hệ thống: {e}")
            message_placeholder.markdown("Xin lỗi, hệ thống đang bận. Quý phụ huynh vui lòng liên hệ Zalo 0356015268 ạ.")

# ==========================================
# 5. FOOTER
# ==========================================
st.markdown('<div class="footer">Made by NamY</div>', unsafe_allow_html=True)