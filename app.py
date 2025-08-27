import streamlit as st
import base64
import sys

# Para converter PDF em imagens
from pdf2image import convert_from_path

st.set_page_config(
    page_title="Currículo - Carlos Gabriel Ribeiro",
    page_icon=":mortar_board:",
    layout="wide"
)

# ------------------------
# Estilo
# ------------------------
st.markdown("""
<style>
/* Botão de download da sidebar */
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

/* Container do PDF */
.pdf-container {
    display: flex;
    justify-content: center;
    margin-top: 15px;
    padding: 10px;
    background: linear-gradient(to bottom right, #ffffff, #e6f0ff);
    border-radius: 15px;
    box-shadow: 4px 4px 15px rgba(0,0,0,0.1);
}

/* iframe do PDF */
iframe {
    width: 95% !important;
    height: 95vh;
    border: 2px solid #ccc;
    border-radius: 15px;
}

/* QR code na sidebar */
.sidebar-image img {
    border-radius: 10px;
    box-shadow: 2px 2px 8px rgba(0,0,0,0.1);
}
</style>
""", unsafe_allow_html=True)

# ------------------------
# Barra lateral
# ------------------------
st.sidebar.title("📄 Currículo")
st.sidebar.markdown("Confira meu currículo ou baixe-o para seu dispositivo.")

pdf_file = "CV.pdf"
with open(pdf_file, "rb") as f:
    st.sidebar.download_button(
        label="⬇️ Baixar currículo",
        data=f,
        file_name="Carlos_Ribeiro_CV.pdf",
        mime="application/pdf"
    )

st.sidebar.markdown('<div class="sidebar-image">', unsafe_allow_html=True)
st.sidebar.image("qrcode.png", caption="Escaneie para acessar meu CV", use_container_width=True)
st.sidebar.markdown('</div>', unsafe_allow_html=True)

# ------------------------
# Detectar mobile
# ------------------------
user_agent = st.runtime.scriptrunner.get_script_run_ctx().client.session_state.get("user_agent", "")
is_mobile = "Mobile" in user_agent or "iPhone" in user_agent or "Android" in user_agent

# ------------------------
# Exibir PDF
# ------------------------
if is_mobile:
    st.markdown("### 📄 Visualização do PDF (Mobile-friendly)")
    # Converter PDF em imagens
    pages = convert_from_path(pdf_file, dpi=150)
    for page in pages:
        st.image(page, use_container_width=True)
else:
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
