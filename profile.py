import streamlit as st

st.set_page_config(layout='wide')

st.markdown("""<style>img{border-radius: 50%;}</style>""", unsafe_allow_html=True)

# Resume PDF file
with open("PD Resume.pdf", "rb") as pdf_file:
    PDFbyte = pdf_file.read()

col1, col2, col3, col4= st.columns([0.25,0.2,0.3,0.25])

with col1:
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

with col2:
    st.image("Photo.jpg", width=180)

with col3:
    st.title("PRABIN DASH")
    st.markdown("Data Scientist")
    st.markdown("Bhubaneswar, India")
    st.download_button(label="Download Resume",
                    data=PDFbyte,
                    file_name="Resume_PrabinDash.pdf",
                    mime='application/octet-stream')

with col4:
    st.markdown("<h3 style='text-align: center;'>EDUCATION</h3>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: center;'>B.Tech (2014-2018)</div>", unsafe_allow_html=True)
    st.write("<div style='text-align: center;'>College of Engineering and Technology</div>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: center;'>Instrumentation and Electronics Engineering</h6>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: center;'>AISSCE (2012-2014)</div>", unsafe_allow_html=True)
    st.write("<div style='text-align: center;'>Mother's Public School</div>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: center;'>CBSE</h6>", unsafe_allow_html=True)

st.markdown("####")
st.markdown("####")
st.markdown("####")

col_ed1, col_ed2, col_ed3 = st.columns(3)

with col_ed1:
    st.markdown("<h3 style='text-align: center;'>SKILLS</h3>", unsafe_allow_html=True)
    col_skills1, col_skills2 = st.columns([0.5,0.5])
    with col_skills1:
        st.write("<div style='text-align: center;'>Python</div>", unsafe_allow_html=True)
        st.write("<div style='text-align: center;'>Azure Cloud</div>", unsafe_allow_html=True)
        st.write("<div style='text-align: center;'>Tensorflow/Keras/PyTorch</div>", unsafe_allow_html=True)
        st.write("<div style='text-align: center;'>NLP</div>", unsafe_allow_html=True)
        st.write("<div style='text-align: center;'>Docker</div>", unsafe_allow_html=True)
    with col_skills2:
        st.write("<div style='text-align: center;'>SQL</div>", unsafe_allow_html=True)
        st.write("<div style='text-align: center;'>Tableau/Power BI</div>", unsafe_allow_html=True)
        st.write("<div style='text-align: center;'>Flask/Streamlit</div>", unsafe_allow_html=True)
        st.write("<div style='text-align: center;'>Unix/Linux</div>", unsafe_allow_html=True)
        st.write("<div style='text-align: center;'>Git/GitHub</div>", unsafe_allow_html=True)

with col_ed2:
    st.markdown("<h3 style='text-align: center;'>CERTIFICATIONS</h3>", unsafe_allow_html=True)
    st.markdown("")
    st.write("<div style='text-align: center;'>AZ900: Azure Fundamentals</div>", unsafe_allow_html=True)
    st.markdown("")
    st.write("<div style='text-align: center;'>DP100: Azure Data Scientist Associate</div>", unsafe_allow_html=True)

with col_ed3:
    st.markdown("<h3 style='text-align: center;'>YEARS OF EXPERIENCE</h3>", unsafe_allow_html=True)
    st.write("<div style='text-align: center;'>Total IT Experience: 5 yrs</div>", unsafe_allow_html=True)    
    st.write("<div style='text-align: center;'>Python: 4.5 yrs</div>", unsafe_allow_html=True)
    st.write("<div style='text-align: center;'>Data Science: 4 yrs</div>", unsafe_allow_html=True)
    st.write("<div style='text-align: center;'>SQL: 4 yrs</div>", unsafe_allow_html=True)
    st.write("<div style='text-align: center;'>Cloud(Azure, AWS): 2 yrs</div>", unsafe_allow_html=True)

st.markdown("####")
st.markdown("####")
st.markdown("####")

st.markdown("<h2 style='text-align: center;'>SHORT INTRODUCTION</h2>", unsafe_allow_html=True)
st.write("I am a technology geek interested in exploring ML and AI domain. With 4+ years into DataScience and 2+ years working in Azure Cloud, I am interested in exploring fields such as Natural Language Processing and Generative AI. I have experience in building models as well as deploying them over Docker or Cloud platforms")

st.markdown("####")
st.markdown("####")

st.markdown("<h2 style='text-align: center;'>EXPERIENCE</h2>", unsafe_allow_html=True)

col_exp1, col_exp2 = st.columns(2)

with col_exp1:
    