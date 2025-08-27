import streamlit as st
import base64

# ------------------------
# Configurações da página
# ------------------------
st.set_page_config(
    page_title="Currículo - Carlos Gabriel Ribeiro",
    page_icon=":mortar_board:",
    layout="wide"
)

# ------------------------
# Estilo customizado
# ------------------------
st.markdown("""
    <style>
    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #f0f2f6;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 3px 3px 10px rgba(0,0,0,0.1);
    }

    /* Título da sidebar */
    .css-1d391kg h2, .css-1d391kg h3 {
        color: #2f4f4f;
        font-weight: 700;
        text-align: center;
        margin-bottom: 20px;
    }

    /* Botão de download */
    div.stDownloadButton > button {
        background-color: #4a90e2;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 10px 15px;
        border: none;
        width: 100%;
        transition: 0.3s;
    }
    div.stDownloadButton > button:hover {
        background-color: #357abd;
        cursor: pointer;
    }

    /* PDF container com fundo suave */
    .pdf-container {
        display: flex;
        justify-content: center;
        margin-top: 15px;
        padding: 10px;
        background: linear-gradient(to bottom right, #ffffff, #e6f0ff);
        border-radius: 15px;
    }

    iframe {
        width: 95% !important;
        height: 95vh;
        border: 2px solid #ccc;
        border-radius: 15px;
        box-shadow: 4px 4px 15px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

# ------------------------
# Barra lateral
# ------------------------
st.sidebar.title("📄 Currículo")
st.sidebar.markdown("Confira meu currículo ou baixe-o para seu dispositivo.")

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

# ------------------------
# PDF em tela cheia
# ------------------------
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
