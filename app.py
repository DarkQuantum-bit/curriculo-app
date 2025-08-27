import streamlit as st
import base64

st.set_page_config(
    page_title="Currículo - Carlos Gabriel Ribeiro",
    page_icon=":mortar_board:",
    layout="wide"
)

pdf_file = "CV.pdf"

# Botão de download na sidebar
with open(pdf_file, "rb") as f:
    st.sidebar.download_button(
        label="⬇️ Baixar currículo",
        data=f,
        file_name="Carlos_Ribeiro_CV.pdf",
        mime="application/pdf"
    )

# QR code
st.sidebar.image("qrcode.png", caption="Escaneie para acessar meu CV", use_container_width=True)

# PDF em iframe (desktop/tablet) ou link (mobile)
with open(pdf_file, "rb") as f:
    base64_pdf = base64.b64encode(f.read()).decode('utf-8')

st.markdown(f"""
<div style="display:flex; flex-direction:column; align-items:center; margin-top:15px;">
  <iframe
    src="data:application/pdf;base64,{base64_pdf}"
    style="width:95%; height:95vh; border:2px solid #ccc; border-radius:15px;"
  ></iframe>
  <p style="text-align:center; margin-top:10px;">
    <a href="{pdf_file}" target="_blank">Abrir PDF</a>
  </p>
</div>
""", unsafe_allow_html=True)

