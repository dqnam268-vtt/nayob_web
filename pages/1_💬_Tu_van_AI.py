import streamlit as st
import requests
import json

# ==========================================
# 1. CẤU HÌNH TRANG
# ==========================================
st.set_page_config(page_title="Tư vấn Tuyển sinh - NaYoB", page_icon="💬", layout="centered")

st.markdown("""
    <style>
    .title-text { color: #005088; font-family: 'Merriweather', serif; font-size: 32px; font-weight: bold; text-align: center; margin-bottom: 5px; }
    .subtitle-text { color: #11caa0; font-size: 16px; text-align: center; font-style: italic; margin-bottom: 15px; }
    div[data-testid="stButton"] > button { border-radius: 20px; font-size: 13px; color: #0f172a; background-color: #f8fafc; border: 1px solid #cbd5e1; padding: 4px 10px; }
    div[data-testid="stButton"] > button:hover { border-color: #005088; color: #005088; background-color: #e0f2fe; }
    .footer { text-align: center; color: #94a3b8; font-size: 12px; margin-top: 40px; border-top: 1px solid #e2e8f0; padding-top: 10px; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title-text">Trợ lý AI - Thầy Đinh Quốc Nam</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle-text">Tư vấn Lộ trình & Lịch học Toán (Hệ thống NaYoB)</div>', unsafe_allow_html=True)
st.markdown("---")

# ==========================================
# 2. ĐƯỜNG DẪN PROXY APPS SCRIPT CỦA THẦY
# ==========================================
APPS_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbzi8UZVwXnrY_8AEBnwbLUAxEAz6xzeDAJP24kO8wBd9c5g0mdmhx6Qpg0JQkNJuCOg/exec"

# ==========================================
# 3. TRI THỨC CỦA AI (ĐÃ CẬP NHẬT ĐỊA CHỈ HỌC)
# ==========================================
KNOWLEDGE_BASE = """
BẠN LÀ: Trợ lý AI của Thầy Đinh Quốc Nam (NaYoB).
YÊU CẦU TỐI THƯỢNG: Trả lời RẤT NGẮN GỌN, ĐÚNG TRỌNG TÂM, KHÔNG DÀI DÒNG (tối đa 3-4 câu). Dùng gạch đầu dòng cho dễ đọc. Tự suy luận linh hoạt dựa trên ngữ cảnh.

THÔNG TIN THẦY NAM & CHUYÊN MÔN:
- Nơi công tác: Thầy Nam hiện đang công tác tại Trường THCS Võ Trường Toản.
- Học vấn: Thạc sĩ Toán học, Cử nhân Sư phạm xuất sắc. 11 năm kinh nghiệm, 9 năm luyện thi HSG.
- Phương pháp dạy: "Navigate Yourself" (Tự định hướng). Sĩ số tối đa: 15 HS/lớp.

CHƯƠNG TRÌNH & HỌC PHÍ (1.000.000 VNĐ/tháng):
- Lớp 6 (T3 & T5, 18h45 - 20h15): Số học, Hình trực quan.
- Lớp 7 (T2 & T4, 17h00 - 18h30): Số hữu tỉ, Tam giác.
- Lớp 8 (T3 & T5, 17h00 - 18h30): Đại số, Tứ giác, Định lý Thalès.
- Lớp 9 (T2 & T4, 18h45 - 20h15): Ôn thi TS10 TP.HCM. Trọng tâm giải Toán thực tế, Vi-et, Đồ thị, Hình phẳng.

ĐỊA ĐIỂM HỌC & LIÊN HỆ: 
- TUYỆT ĐỐI KHÔNG CUNG CẤP ĐỊA CHỈ TRƯỜNG LÀM ĐỊA CHỈ HỌC THÊM. 
- Nếu phụ huynh hỏi địa chỉ học ở đâu, hãy báo phụ huynh kết bạn Zalo 0356015268 để Thầy Nam thông báo địa điểm lớp học chi tiết và xếp lớp phù hợp.
"""

# ==========================================
# 4. GIAO DIỆN CHAT 
# ==========================================
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Kính chào Quý phụ huynh! 👋 Tôi là trợ lý của Thầy Đinh Quốc Nam. Anh/chị cần tư vấn lịch học, học phí hay thông tin gì ạ?"}]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- BỘ QUÉT NGỮ CẢNH ---
recent_context = " ".join([m["content"].lower() for m in st.session_state.messages[-2:]])

goi_y = []
if "lớp 6" in recent_context:
    goi_y = ["Địa điểm học ở đâu?", "Lịch & Học phí lớp 6", "Phương pháp dạy của Thầy"]
elif "lớp 9" in recent_context or "ts 10" in recent_context:
    goi_y = ["Đề TS10 khó chỗ nào?", "Lịch ôn Lớp 9", "Địa điểm học Lớp 9"]
elif "thầy nam" in recent_context or "địa chỉ" in recent_context or "ở đâu" in recent_context:
    goi_y = ["Thành tích của Thầy?", "Địa điểm lớp học thêm ở đâu?", "Thầy Nam công tác trường nào?"]
else:
    goi_y = ["Địa điểm học ở đâu?", "Lịch học Lớp 9", "Học phí và sĩ số lớp?"]

# --- HIỂN THỊ NÚT ---
st.markdown("<div style='text-align: center; margin-bottom: 5px; margin-top: 10px; color: #64748b; font-size: 13px;'>💡 <i>Gợi ý câu hỏi:</i></div>", unsafe_allow_html=True)
cols = st.columns(3)
for i, cau_hoi in enumerate(goi_y):
    with cols[i]:
        if st.button(cau_hoi, use_container_width=True):
            st.session_state.quick_prompt = cau_hoi

prompt = st.chat_input("Nhập câu hỏi tại đây...")

if "quick_prompt" in st.session_state and st.session_state.quick_prompt:
    prompt = st.session_state.quick_prompt
    st.session_state.quick_prompt = None

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        message_placeholder.markdown("*(Đang suy nghĩ...)*")
        
        try:
            contents_payload = []
            
            for msg in st.session_state.messages[1:-1]:
                role = "user" if msg["role"] == "user" else "model"
                contents_payload.append({
                    "role": role,
                    "parts": [{"text": msg["content"]}]
                })
            
            contents_payload.append({
                "role": "user",
                "parts": [{"text": prompt}]
            })
            
            payload = {
                "action": "solve",
                "contents": contents_payload,
                "systemInstruction": {"parts": [{"text": KNOWLEDGE_BASE}]}
            }
            
            response = requests.post(
                APPS_SCRIPT_URL,
                headers={"Content-Type": "text/plain;charset=utf-8"},
                data=json.dumps(payload),
                allow_redirects=True
            )
            
            if response.status_code == 200:
                data = response.json()
                bot_reply = data.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "")
                
                if not bot_reply:
                    bot_reply = "Xin lỗi, hiện tại hệ thống bận."
                    
                message_placeholder.markdown(bot_reply)
                st.session_state.messages.append({"role": "assistant", "content": bot_reply})
                st.rerun() 
            else:
                st.error("Lỗi đường truyền trung gian.")
                
        except Exception as e:
            st.error(f"Lỗi hệ thống: {e}")
            message_placeholder.markdown("Hệ thống đang bận. Quý phụ huynh vui lòng liên hệ Zalo 0356015268 ạ.")

# ==========================================
# 5. FOOTER
# ==========================================
st.markdown('<div class="footer">Made by NamY</div>', unsafe_allow_html=True)