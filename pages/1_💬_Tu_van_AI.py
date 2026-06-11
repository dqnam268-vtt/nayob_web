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
    /* Chỉnh nút gợi ý cho mềm mại, giống phong cách chat UI hiện đại */
    div[data-testid="stButton"] > button { border-radius: 20px; color: #0f172a; border-color: #cbd5e1; background-color: #f8fafc;}
    div[data-testid="stButton"] > button:hover { border-color: #005088; color: #005088; background-color: #f0f8ff;}
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title-text">Trợ lý AI Tư vấn Tuyển sinh NaYoB</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle-text">Tư vấn lộ trình học Toán 24/7 cùng Thầy Đinh Quốc Nam</div>', unsafe_allow_html=True)
st.markdown("---")

# ==========================================
# 2. ĐƯỜNG DẪN PROXY (GOOGLE APPS SCRIPT)
# ==========================================
APPS_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbzi8UZVwXnrY_8AEBnwbLUAxEAz6xzeDAJP24kO8wBd9c5g0mdmhx6Qpg0JQkNJuCOg/exec"

# ==========================================
# 3. TRI THỨC CỦA AI (CẬP NHẬT THÊM SĨ SỐ)
# ==========================================
KNOWLEDGE_BASE = """
BẠN LÀ: Trợ lý tuyển sinh chuyên nghiệp của Lớp Toán Thầy Đinh Quốc Nam (Thương hiệu giáo dục NaYoB - Navigate Yourself). Giọng điệu thân thiện, chuyên môn cao, xưng "tôi" và gọi "anh/chị" hoặc "phụ huynh".

CHƯƠNG TRÌNH HỌC (Sách Kết nối tri thức) & MÔI TRƯỜNG:
- Lớp 6: Số tự nhiên, Phân số, Số thập phân, Hình học trực quan, Khối không gian, Tính đối xứng.
- Lớp 7: Số hữu tỉ, Số thực, Góc & Đường thẳng song song, Tam giác bằng nhau, Đại lượng tỉ lệ.
- Lớp 8: Đa thức, Hằng đẳng thức, Tứ giác, Định lí Thalès, Tam giác đồng dạng.
- Sĩ số lớp học: Giới hạn tối đa 15 học sinh/lớp để Thầy Nam có thể theo sát, kèm cặp từng em và định hướng tư duy cá nhân hóa.

ĐẶC BIỆT KHỐI 9 (TRỌNG TÂM ÔN THI TS10 TẠI TP.HCM):
- Đề thi Toán Tuyển sinh 10 tại TP.HCM rất đặc thù. Trọng tâm cực kỳ lớn (chiếm 4.5/10 điểm) rơi vào các bài TOÁN THỰC TẾ đòi hỏi đọc hiểu dài, lập phương trình, lãi suất. Kèm theo Vi-et, Đồ thị, Hình phẳng.
- Lộ trình: Rèn luyện phương pháp "Navigate Yourself" giúp học sinh tự phân tích đề dài, bóc tách dữ liệu để mô hình hóa bài toán thực tế mà không bị tâm lý e ngại.

THÔNG TIN LỊCH HỌC & HỌC PHÍ:
- Học phí chung các khối: 1.000.000 VNĐ/tháng.
- Lớp 6: Thứ 3 & Thứ 5 (18h45 - 20h15)
- Lớp 7: Thứ 2 & Thứ 4 (17h00 - 18h30)
- Lớp 8: Thứ 3 & Thứ 5 (17h00 - 18h30)
- Lớp 9: Thứ 2 & Thứ 4 (18h45 - 20h15)

KỸ NĂNG DẪN DẮT: 
- Luôn trả lời ngắn gọn, xuống dòng rõ ràng.
- Khéo léo mời phụ huynh liên hệ Zalo 0356015268 để Thầy Nam trực tiếp kiểm tra năng lực đầu vào và xếp lớp.
"""

# ==========================================
# 4. GIAO DIỆN CHAT VÀ NÚT TÒ MÒ ĐỘNG
# ==========================================
if "messages" not in st.session_state:
    loi_chao = (
        "Kính chào Quý phụ huynh! 👋 Tôi là trợ lý AI của hệ thống Toán NaYoB.\n\n"
        "Anh/chị đang quan tâm lịch học, học phí hay chương trình đào tạo của khối lớp mấy ạ?"
    )
    st.session_state.messages = [{"role": "assistant", "content": loi_chao}]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- BỘ QUÉT NGỮ CẢNH: CHỌN NÚT GỢI Ý ĐỘNG ---
# Lấy nội dung 2 tin nhắn gần nhất để phân tích đang nói về chủ đề gì
recent_context = " ".join([m["content"].lower() for m in st.session_state.messages[-2:]])

goi_y = []
if "lớp 6" in recent_context:
    goi_y = ["Sĩ số một lớp 6 là bao nhiêu?", "Chương trình lớp 6 học những gì?", "Lịch học & Học phí lớp 6"]
elif "lớp 7" in recent_context:
    goi_y = ["Trọng tâm kiến thức Lớp 7", "Sĩ số lớp 7", "Lịch học & Học phí"]
elif "lớp 8" in recent_context:
    goi_y = ["Hình học lớp 8 khó không?", "Lịch học & Học phí lớp 8", "Sĩ số lớp"]
elif "lớp 9" in recent_context or "tuyển sinh" in recent_context or "ts 10" in recent_context:
    goi_y = ["Cấu trúc Toán TS10 TP.HCM", "Lộ trình ôn thi Lớp 9", "Sĩ số lớp 9"]
else:
    # Mặc định khi mới vào hoặc hỏi chung chung
    goi_y = ["Tư vấn giúp tôi Lớp 6", "Tư vấn chương trình Lớp 9 Ôn TS10", "Sĩ số lớp học của Thầy Nam?"]

# --- HIỂN THỊ NÚT GỢI Ý ---
st.markdown("<div style='text-align: center; margin-bottom: 5px; margin-top: 10px; color: #64748b; font-size: 14px;'>💡 <i>Gợi ý cho Quý phụ huynh:</i></div>", unsafe_allow_html=True)
cols = st.columns(3)
for i, cau_hoi in enumerate(goi_y):
    with cols[i]:
        if st.button(cau_hoi, use_container_width=True):
            st.session_state.quick_prompt = cau_hoi

# --- KHUNG NHẬP CHAT ---
prompt = st.chat_input("Nhập câu hỏi của Quý phụ huynh tại đây...")

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
            history_text = ""
            for msg in st.session_state.messages[-4:-1]:
                nguoi_gui = "Phụ huynh" if msg["role"] == "user" else "Trợ lý"
                history_text += f"{nguoi_gui}: {msg['content']}\n"

            full_prompt = f"""
            Lịch sử trò chuyện gần đây:
            {history_text}
            
            Câu hỏi mới của phụ huynh: {prompt}
            """
            
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
            
            if response.status_code == 200:
                data = response.json()
                bot_reply = data.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "")
                
                if not bot_reply:
                    bot_reply = "Xin lỗi, hiện tại hệ thống chưa xử lý kịp câu hỏi này."
                    
                message_placeholder.markdown(bot_reply)
                st.session_state.messages.append({"role": "assistant", "content": bot_reply})
                st.rerun() # Tải lại trang ngay lập tức để cập nhật bộ nút gợi ý mới
            else:
                st.error("Lỗi đường truyền trung gian.")
                
        except Exception as e:
            st.error(f"Lỗi hệ thống.")
            message_placeholder.markdown("Hệ thống đang bận. Quý phụ huynh vui lòng liên hệ Zalo 0356015268 ạ.")

# ==========================================
# 5. FOOTER
# ==========================================
st.markdown('<div class="footer">Made by NamY</div>', unsafe_allow_html=True)