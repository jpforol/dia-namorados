import streamlit as st
from streamlit_autorefresh import st_autorefresh

st.set_page_config(page_title="Feliz Dia dos Namorados 💖", layout="centered")

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
    img.responsive {
        max-width: 90vw;
        height: auto;
        border-radius: 15px;
        box-shadow: 0px 4px 20px rgba(0,0,0,0.3);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("💘 Um momento especial com você")

foto1 = st.secrets["images"]["foto1"]
foto2 = st.secrets["images"]["foto2"]
foto3 = st.secrets["images"]["foto3"]

images = [
    (foto1, "Juntos em todos os momentos ❤️"),
    (foto2, "Um dia tranquilo, do jeito que a gente gosta 💑"),
    (foto3, "Só nós dois e o resto do mundo lá fora ❤️"),
]

count = st_autorefresh(interval=5000, limit=None, key="auto_refresh")

index = count % len(images)

img_base64, caption = images[index]

st.markdown(
    f"""
    <div style="display: flex; justify-content: center;">
        <img class="responsive" src="data:image/jpeg;base64,{img_base64}" />
    </div>
    <div class='caption'>{caption}</div>
    """,
    unsafe_allow_html=True,
)

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
