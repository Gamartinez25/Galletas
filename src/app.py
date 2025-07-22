import streamlit as st
import pandas as pd
from PIL import Image

# Load cookie data
@st.cache
def load_data():
    data = pd.read_csv('src/data/cookies.csv')
    return data

# Main function to run the app
def main():
    st.title("Cookie Catalog")
    st.sidebar.header("Filter Cookies")
    
    # Load data
    cookies = load_data()
    
    # Display cookie catalog
    for index, row in cookies.iterrows():
        image_path = f"src/utils/images/{row['cookie_name']}.jpg"
        try:
            image = Image.open(image_path)
            st.image(image, use_container_width=True)
        except FileNotFoundError:
            st.warning(f"Image not found for {row['cookie_name']}")
        st.subheader(row['cookie_name'])
        st.write(row['cookie_description'])
        st.write(f"Price: ${row['cookie_price']:.2f}")
        st.markdown("---")

if __name__ == "__main__":
    main()
