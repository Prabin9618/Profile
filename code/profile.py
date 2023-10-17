import streamlit as st

st.set_page_config(layout='wide')

st.markdown("""<style>img{border-radius: 50%;}</style>""", unsafe_allow_html=True)

col1, col2, col3= st.columns(3)

with col1:
    st.image("Photo.jpg", width=180)

with col2:
    st.title("PRABIN DASH")
    st.markdown("Data Scientist")
    st.markdown("Bhubaneswar, India")

with col3:
    collink1, collink2 = st.columns(spec=[0.1,0.9])
    with collink1:
        st.markdown("")
        st.image("linkedin.png", width=28)
        st.image("github.png", width=28)
        st.image("mail.png", width=28)
        st.image("phone.png", width=28)
    with collink2:
        st.markdown("")
        st.markdown("[LinkedIn](https://www.linkedin.com/in/prabin-dash-00a281137/)")
        st.markdown("[GitHub](https://github.com/Prabin9618)")
        st.markdown("prabindash135@gmail.com")
        st.markdown("+91 9778841064")