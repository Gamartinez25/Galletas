import streamlit as st
import pandas as pd
from PIL import Image
import os

#PAGE_TITLE = "" # This will appear in the browser tab title
#PAGE_ICON = "🍪"  # Puedes usar un emoji o la ruta a una imagen .png

#st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

st.title('Nuestro Catálogo de Delicias') # This will be the main title displayed on your page
st.write("Bienvenido a nuestro catálogo de cookies 🍪")


# --- Carga eficiente de datos ---
@st.cache_data
def load_cookie_data():
    try:
        data = pd.read_csv('src/data/cookies.csv')
        return data
    except FileNotFoundError:
        st.error("Error: 'cookies.csv' no encontrado. Por favor colócalo en 'src/data/'.")
        st.stop()
    except Exception as e:
        st.error(f"Error cargando los datos: {e}")
        st.stop()

# --- Estilos modernizados ---
st.markdown("""
<style>
    body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        background: #fff2e6;
        color: #333;
    }

    /* Ocultar sidebar completamente y franja decorativa */
    [data-testid="stSidebar"], 
    section[data-testid="stSidebarContent"],
    .css-6qob1r.e1fqkh3o3 {
        display: none !important;
    }

    .catalog-wrapper {
        background: linear-gradient(135deg, #fffff 0%, #ffffff 100%);
        border-radius: 25px;
        padding: 40px 50px;
        max-width: 950px;
        margin: 3rem auto 5rem auto;
    }

    h1 {
        font-weight: 800 !important;
        font-size: 3rem !important;
        color: #d35400;
        margin-bottom: 2rem !important;
        text-align: center;
        letter-spacing: 1.5px;
        text-shadow: 1px 1px 5px rgba(211, 84, 0, 0.25);
    }

    .cookie-card {
        display: flex;
        align-items: center;
        gap: 30px;
        padding: 24px 0;
        border-bottom: 1px solid #f0d9b5;
        transition: background-color 0.3s ease;
    }
    .cookie-card:last-child {
        border-bottom: none;
        padding-bottom: 0;
    }
    .cookie-card:hover {
        background-color: #fff3e0;
        border-radius: 20px;
        box-shadow: 0 8px 22px rgba(211, 84, 0, 0.15);
    }

    .cookie-img {
        border-radius: 18px;
        box-shadow: 0 6px 20px rgba(230, 126, 34, 0.35);
        width: 100%;
        height: auto;
        object-fit: cover;
    }

    .cookie-text-content h4 {
        font-size: 1.8rem;
        font-weight: 900;
        margin-bottom: 0.6rem;
        color: #9b4514;
    }
    .cookie-text-content p {
        font-size: 1.05rem;
        color: #7a4e15;
        margin-bottom: 1.2rem;
        line-height: 1.6;
        font-weight: 500;
    }
    .cookie-price {
        font-size: 1.4rem;
        font-weight: 800;
        color: #d35400;
        margin-bottom: 14px;
    }

    .stButton>button {
        background: #d35400;
        color: white;
        font-weight: 800;
        border-radius: 14px;
        padding: 12px 26px;
        border: none;
        transition: background-color 0.3s ease;
        box-shadow: 0 6px 20px rgba(211, 84, 0, 0.4);
        cursor: pointer;
        font-size: 1.1rem;
    }
    .stButton>button:hover {
        background-color: #b44500;
        box-shadow: 0 8px 28px rgba(180, 69, 0, 0.55);
    }
</style>
""", unsafe_allow_html=True)

# --- Lógica principal ---
def main():
    cookies = load_cookie_data()
    if cookies is None:
        return
    if cookies.empty:
        st.info("No hay cookies disponibles en el catálogo.")
    else:
        for index, row in cookies.iterrows():
            #image_filename = f"{row['cookie_name']}.jpg"
            image_filename = "Chocolate Chip.jpg"
            image_path = os.path.join("src", "utils", "images", image_filename)

            st.markdown('<div class="cookie-card">', unsafe_allow_html=True)
            cols = st.columns([0.35, 0.65])

            with cols[0]:
                try:
                    image = Image.open(image_path)
                    st.image(image, use_container_width=True)
                except FileNotFoundError:
                    placeholder = Image.new('RGB', (160, 160), color='#f0f0f0')
                    st.image(placeholder, caption="Imagen no disponible", use_container_width=True)

            with cols[1]:
                st.markdown('<div class="cookie-text-content">', unsafe_allow_html=True)
                st.markdown(f"<h4>{row['cookie_name']}</h4>", unsafe_allow_html=True)
                st.markdown(f"<div class='cookie-price'>${row['cookie_price']:.2f}</div>", unsafe_allow_html=True)

                if f"show_details_{index}" not in st.session_state:
                    st.session_state[f"show_details_{index}"] = False

                btn_text = "Ocultar Detalles" if st.session_state[f"show_details_{index}"] else "Ver Detalles"
                if st.button(btn_text, key=f"btn_{index}"):
                    st.session_state[f"show_details_{index}"] = not st.session_state[f"show_details_{index}"]

                if st.session_state[f"show_details_{index}"]:
                    st.markdown(f"<p>{row['cookie_description']}</p>", unsafe_allow_html=True)

                st.markdown('</div>', unsafe_allow_html=True)

            st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
