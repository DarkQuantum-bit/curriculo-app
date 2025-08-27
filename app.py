import streamlit as st
import base64

# ------------------------
# Configurações da página
# ------------------------
st.set_page_config(
    page_title="Currículo - Carlos Gabriel Ribeiro",
    page_icon=":mortar_board:",
    layout="wide"  # layout ocupa a largura total
)

# ------------------------
# Barra lateral
# ------------------------
st.sidebar.title("Currículo")

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
st.sidebar.image("qr_code.jpeg", caption="Escaneie para acessar meu CV", use_container_width=True)
# coloque o arquivo qr_code.png na mesma pasta do app

# ------------------------
# PDF em tela cheia
# ------------------------
with open(pdf_file, "rb") as f:
    base64_pdf = base64.b64encode(f.read()).decode('utf-8')

pdf_display = f'''
<iframe 
    src="data:application/pdf;base64,{base64_pdf}" 
    style="width: 100%; height: 100vh; border: none;">
</iframe>
'''

st.markdown(pdf_display, unsafe_allow_html=True)
