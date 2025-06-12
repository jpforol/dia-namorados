import streamlit as st
import time
import base64

st.set_page_config(page_title="Feliz Dia dos Namorados 💖", layout="centered")

# Estilo da página
st.markdown(
    """
    <style>
    body {
        background-color: #3B0A2A;
        color: #E0BCCF;
    }
    .stApp {
        background-color: #3B0A2A;
        color: #E0BCCF;
    }
    .caption {
        text-align: center;
        font-size: 20px;
        margin-top: 10px;
        font-weight: bold;
        color: #D88AA0;
    }
    h1, h2, h3, h4 {
        color: #FFD6E8;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("💘 Um momento especial com você")

foto1 = st.secrets["images"]["foto1"]
foto2 = st.secrets["images"]["foto2"]
foto3 = st.secrets["images"]["foto3"]

# Lista de imagens e legendas
images = [
    (foto1, "Juntos em todos os momentos ❤️"),
    (foto2, "Um dia tranquilo, do jeito que a gente gosta 💑"),
    (foto3, "Só nós dois e o resto do mundo lá fora ❤️"),
]

# Controla o índice da imagem
if "index" not in st.session_state:
    st.session_state.index = 0

# Pega imagem atual e legenda
img_base64, caption = images[st.session_state.index]

# Exibe imagem com tamanho fixo centralizado via HTML
st.markdown(
    f"""
    <div style="display: flex; justify-content: center;">
        <img src="data:image/jpeg;base64,{img_base64}" 
             style="width: 650px; height: 850px; object-fit: cover; border-radius: 15px; box-shadow: 0px 4px 20px rgba(0,0,0,0.3);" />
    </div>
    <div class='caption'>{caption}</div>
    """,
    unsafe_allow_html=True,
)

# Mensagem final
st.markdown(
    """
    <div style="text-align: center; margin-top: 40px; font-size: 18px; color: #E0BCCF;">
        Feliz Dia dos Namorados! ❤️<br>
        Tenho sorte de estar comemorando mais um, e melhor ainda por saber que ainda virão muitos outros.<br><br>
        ❤️ EU TE AMO ❤️<br><br>
        Tentei colocar música no site, mas eu ainda estou aprendendo a fazer isso aqui:<br>
        <a href="https://open.spotify.com/intl-pt/track/0Flkg211OzPzT2fss5sfSn?si=4aeb7cf5c145444d" target="_blank" style="color:#FFD6E8; text-decoration: underline;">
            Ouve aqui
        </a>
    </div>
    """,
    unsafe_allow_html=True,
)


# Espera e troca
time.sleep(5)
st.session_state.index = (st.session_state.index + 1) % len(images)
st.rerun()
