import streamlit as st
import base64

st.set_page_config(
    page_title="Currículo - Carlos Gabriel Ribeiro",
    page_icon=":mortar_board:",
    layout="wide"
)

st.markdown("""
    <style>
    /* Cor de fundo da sidebar */
    .css-1d391kg {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
    }
    /* Título da sidebar */
    .css-1v3fvcr h2 {
        color: #2f4f4f;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

st.sidebar.title("📄 Currículo")

# Botão de download
pdf_file = "CV.pdf"
with open(pdf_file, "rb") as f:
    st.sidebar.download_button(
        label="⬇️ Baixar Currículo",
        data=f,
        file_name="Carlos_Ribeiro_CV.pdf",
        mime="application/pdf"
    )

# QR code
st.sidebar.image("qrcode.png", caption="Escaneie para acessar meu CV", use_container_width=True)

with open(pdf_file, "rb") as f:
    base64_pdf = base64.b64encode(f.read()).decode('utf-8')

pdf_display = f'''
<div style="display: flex; justify-content: center; margin-top: 10px;">
    <iframe 
        src="data:application/pdf;base64,{base64_pdf}" 
        style="width: 90%; height: 95vh; border: 2px solid #ddd; border-radius: 10px;">
    </iframe>
</div>
'''

st.markdown(pdf_display, unsafe_allow_html=True)
