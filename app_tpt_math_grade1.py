import streamlit as st
import random

def generate_number_bonds(n, max_val):
    problems = []
    for _ in range(n):
        whole = random.randint(5, max_val)
        part1 = random.randint(1, whole - 1)
        part2 = whole - part1
        problems.append({"whole": whole, "part1": part1, "part2": part2})
    return problems

# --- UI Setup ---
st.set_page_config(page_title="G.1 Math Worksheet Generator", page_icon="✏️")
st.title("🧮 G.1 Math Worksheet Generator")
st.write("สร้างโจทย์คณิตศาสตร์สำหรับ Grade 1 เพื่อนำไปทำใบงานขายบน TpT")

with st.sidebar:
    st.header("Settings")
    topic = st.selectbox("เลือกหัวข้อโจทย์", ["Number Bonds", "Basic Addition (Up to 20)"])
    num_questions = st.slider("จำนวนโจทย์", 5, 20, 10)
    max_value = st.number_input("ค่าตัวเลขสูงสุด", value=20)
    generate_btn = st.button("Generate Questions")

if generate_btn:
    st.subheader(f"หัวข้อ: {topic}")
    
    if topic == "Number Bonds":
        data = generate_number_bonds(num_questions, max_value)
        
        # แสดงผลแบบ Grid เพื่อให้ดูง่าย
        cols = st.columns(2)
        for i, item in enumerate(data):
            with cols[i % 2]:
                st.info(f"Set {i+1}")
                st.latex(rf"\text{{Whole: }} {item['whole']}")
                st.latex(rf"\text{{Part 1: }} {item['part1']} \quad | \quad \text{{Part 2: ?? (Ans: {item['part2']})}}")
                st.divider()

    elif topic == "Basic Addition (Up to 20)":
        for i in range(num_questions):
            a = random.randint(1, max_value - 5)
            b = random.randint(1, 5)
            st.write(f"### {i+1}) {a} + {b} = \_\_\_\_")

    st.success("สุ่มโจทย์ใหม่สำเร็จ! คุณสามารถคัดลอกตัวเลขไปใส่ใน Canva หรือ Word ได้เลย")
else:
    st.info("👈 ปรับแต่งการตั้งค่าที่แถบด้านข้างแล้วกด Generate")
