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
    .suggestion-btn { background-color: #f1f5f9; color: #0f172a; border: 1px solid #cbd5e1; border-radius: 20px; padding: 6px 12px; font-size: 13px; margin: 4px; display: inline-block; cursor: pointer; transition: 0.3s; }
    .suggestion-btn:hover { background-color: #e2e8f0; border-color: #94a3b8; }
    .footer { text-align: center; color: #94a3b8; font-style: italic; margin-top: 50px; border-top: 1px solid #e2e8f0; padding-top: 15px; }
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
# 3. TRI THỨC CỦA AI (ĐÃ CẬP NHẬT CHI TIẾT TỪNG LỚP)
# ==========================================
KNOWLEDGE_BASE = """
BẠN LÀ: Trợ lý tuyển sinh chuyên nghiệp của Lớp Toán Thầy Đinh Quốc Nam (Thương hiệu giáo dục NaYoB - Navigate Yourself). Giọng điệu thân thiện, chuyên môn cao, xưng "tôi" và gọi "anh/chị" hoặc "phụ huynh".

CHƯƠNG TRÌNH HỌC (Bám sát SGK Kết nối tri thức):
- Lớp 6: Số tự nhiên, Phân số, Số thập phân, Hình học trực quan (Hình phẳng, Khối không gian), Tính đối xứng, Thống kê & Xác suất.
- Lớp 7: Số hữu tỉ, Số thực, Góc & Đường thẳng song song, Tam giác bằng nhau, Đại lượng tỉ lệ, Biểu thức đại số.
- Lớp 8: Đa thức, Hằng đẳng thức đáng nhớ, Tứ giác, Định lí Thalès, Tam giác đồng dạng, Hàm số & Đồ thị.
- Lớp 9 (Trọng tâm Ôn thi TS 10): Phương trình & Hệ phương trình, Căn bậc hai/ba, Hệ thức lượng trong tam giác vuông, Đường tròn. Bổ sung liên tục các chuyên đề luyện thi (Vi-ét, Giải toán lập phương trình, Hình học phẳng tổng hợp).

THÔNG TIN LỊCH HỌC & HỌC PHÍ:
- Học phí chung các khối: 1.000.000 VNĐ/tháng.
- Lớp 6: Thứ 3 & Thứ 5 (18h45 - 20h15)
- Lớp 7: Thứ 2 & Thứ 4 (17h00 - 18h30)
- Lớp 8: Thứ 3 & Thứ 5 (17h00 - 18h30)
- Lớp 9: Thứ 2 & Thứ 4 (18h45 - 20h15)

KỸ NĂNG DẪN DẮT (QUAN TRỌNG): 
- Nếu phụ huynh hỏi chung chung, bạn hãy chủ động mồi thêm câu hỏi: "Anh/chị muốn tìm hiểu thêm về *Trọng tâm kiến thức lớp...* hay *Phương pháp dạy học định hướng* của Thầy Nam không ạ?"
- Luôn kết thúc bằng việc mời phụ huynh liên hệ Zalo 0356015268 để được xếp lớp.
"""

# ==========================================
# 4. GIAO DIỆN CHAT VÀ TỪ KHÓA GỢI Ý
# ==========================================
# Khởi tạo tin nhắn chào mừng và các nút gợi ý
if "messages" not in st.session_state:
    loi_chao = (
        "Kính chào Quý phụ huynh! 👋 Tôi là trợ lý AI của hệ thống Toán NaYoB.\n\n"
        "Tôi có thể hỗ trợ anh/chị các thông tin sau:\n"
        "1️⃣ **Lịch học & Học phí** các khối THCS.\n"
        "2️⃣ **Trọng tâm kiến thức** theo bộ sách Kết nối tri thức.\n"
        "3️⃣ **Lộ trình ôn thi Tuyển sinh 10** (Khối 9).\n\n"
        "Anh/chị quan tâm đến khối lớp mấy hoặc cần tôi tư vấn chủ đề gì ạ?"
    )
    st.session_state.messages = [{"role": "assistant", "content": loi_chao}]

# In lịch sử tin nhắn
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Hiển thị các từ khóa mồi (chỉ hiện khi chưa có nhiều tin nhắn để giao diện gọn gàng)
if len(st.session_state.messages) <= 3:
    st.markdown("<div style='text-align: center; margin-bottom: 10px; color: #64748b; font-size: 14px;'>💡 <i>Gợi ý câu hỏi thường gặp:</i></div>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Lịch học lớp 9 ôn TS 10?", use_container_width=True):
            st.session_state.quick_prompt = "Xin tư vấn lịch học và lộ trình lớp 9 ôn thi Tuyển sinh 10."
    with col2:
        if st.button("Học phí và Lịch lớp 6?", use_container_width=True):
            st.session_state.quick_prompt = "Cho tôi hỏi học phí và lịch học của khối lớp 6."
    with col3:
        if st.button("Trọng tâm kiến thức lớp 8?", use_container_width=True):
            st.session_state.quick_prompt = "Chương trình lớp 8 sách Kết nối tri thức học những nội dung gì trọng tâm?"

# Xử lý input từ người dùng (nhập tay hoặc bấm nút)
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
            # Chế tạo lịch sử hội thoại
            history_text = ""
            for msg in st.session_state.messages[-4:-1]:
                nguoi_gui = "Phụ huynh" if msg["role"] == "user" else "Trợ lý"
                history_text += f"{nguoi_gui}: {msg['content']}\n"

            full_prompt = f"""
            Lịch sử trò chuyện gần đây:
            {history_text}
            
            Câu hỏi mới của phụ huynh: {prompt}
            """
            
            # Gửi qua Apps Script
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
            else:
                st.error("Lỗi đường truyền trung gian.")
                
        except Exception as e:
            st.error(f"Lỗi hệ thống.")
            message_placeholder.markdown("Hệ thống đang bận. Quý phụ huynh vui lòng liên hệ Zalo 0356015268 ạ.")

# ==========================================
# 5. FOOTER
# ==========================================
st.markdown('<div class="footer">Made by NamY</div>', unsafe_allow_html=True)