import streamlit as st
import base64

st.set_page_config(
    page_title="Currículo - Carlos Gabriel Ribeiro",
    page_icon=":mortar_board:",
    layout="wide"
)

st.markdown("""
    <style>
    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
    }

    /* Título da sidebar */
    .css-1d391kg h2, .css-1d391kg h3 {
        color: #2f4f4f;
        font-weight: bold;
    }

    /* PDF container centralizado */
    .pdf-container {
        display: flex;
        justify-content: center;
        margin-top: 10px;
        padding: 5px;
    }

    /* iframe responsivo */
    iframe {
        width: 100% !important;
        height: 95vh;
        border: 2px solid #ddd;
        border-radius: 10px;
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
<div class="pdf-container">
    <iframe 
        src="data:application/pdf;base64,{base64_pdf}">
    </iframe>
</div>
'''

st.markdown(pdf_display, unsafe_allow_html=True)

