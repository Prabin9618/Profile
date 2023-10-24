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
    st.markdown("<h3 style='text-align: center;'>KPMG Global Services</h3>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center;'>2022-Present</h5>", unsafe_allow_html=True)
    st.markdown(
            """
            - Worked for one of the biggest retail sector firm, developing a spam classification bot with language translation, embedded images etc. blockers
            - Creation of raw dataset by email extraction from client mailbox using Python scripts, building various ML/DL models, deploying over Azure DevOps pipeline to Azure Web App and integration in Logic apps workflow
            - Utilizing Azure tools such as Azure ML, Cognitive Services for same purpose
            - Comparing all solutions by performance, efficiency and security aspects
            - Reduction of manual workload by 83%
            """
            )
    st.markdown("####")
    st.markdown("####")
    st.markdown("---")
    st.markdown(
            """
            - Worked in Pharmaceutical sales domain to create Analytics Insights dashboard displaying multi-item(multiple orgs/products) Sales Forecasting and Anomaly Detection on Sales data over past timeperiod
            - Extraction of raw data from SAP HANA database, copying to Azure Storage via Azure Data Factory, importing to Azure ML Studio and building models using various methods such as Automated ML
            - Consuming model in PowerBI to create dashboard and setting up refresh
            - Setting up AutoML feature to retrain ML model at certain frequency
            """
            )

with col_exp2:
    st.markdown("<h3 style='text-align: center;'>Tata Consultancy Services(TCS)</h3>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: center;'>2018-2022</h6>", unsafe_allow_html=True)
    st.markdown(
            """
            - Worked for one of the biggest banks in Australia, developing a Document Image Processing and intelligent text extraction project, reducing human workload by completing real time work usually done in 3-5 business days to 30 minutes            - Creation of raw dataset by email extraction from client mailbox using Python scripts, building various ML/DL models, deploying over Azure DevOps pipeline to Azure Web App and integration in Logic apps workflow
            - Classifying documents using state-of-the-art algorithms(88.89%), process and extract scanned/printed text using OCR, data and document comparison using fuzzy matching and regex algorithm to highlight key differences
            - Extract information from structured/unstructured texts automatically, review the exceptions and recommend updates in the model for improved extraction
            - Deploying model into client's docker platform and integration in UI
            """
            )
    st.markdown("---")
    st.markdown(
            """
            - Worked for one of the biggest banks in Australia, in Payments domain, utilizing skills such as Python, Oracle, Unix            
            - Extracting huge chunks of data from Oracle database, analyzing them using Python Data Analysis tools, providing insights to clients
            - Analyzing transactional processing data, implementing forecasting models to forecast weekly, monthly and quarterly expected loads, which helps reduce system downtime by 78%
            - Trend Forecasting, Capacity report analysis, Dashboard preparation for monthly/quarterly processing and highlighting performance issues
            - Developing cost/benefit analysis for business solutions
            """
            )