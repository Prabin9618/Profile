import streamlit as st
import base64
import webbrowser

st.set_page_config(layout='wide')

with open('style.css') as f:
    css = f.read()

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

st.markdown("""<style>img{border-radius: 50%;}</style>""", unsafe_allow_html=True)

# Resume PDF file
with open("PD Resume.pdf", "rb") as pdf_file:
    PDFbyte = pdf_file.read()

col1, col2, col3= st.columns([0.2,0.55,0.25])

with col1:
    st.image("Photo.jpg", width=180)

with col2:
    st.title("PRABIN DASH")
    st.markdown("Data Scientist")
    st.markdown("Bhubaneswar, India")
    st.download_button(label="Download Resume",
                    data=PDFbyte,
                    file_name="Resume_PrabinDash.pdf",
                    mime='application/octet-stream')

with col3:
    collink1, collink2 = st.columns(spec=[0.1,0.9])
    with collink1:
        st.markdown("")
        st.image("linkedin.png", width=28)
        st.image("github.png", width=28)
        st.image("huggingface.png", width=28)
        st.image("mail.png", width=28)
        st.image("phone.png", width=28)
    with collink2:
        st.markdown("")
        st.markdown("[LinkedIn](https://www.linkedin.com/in/prabin-dash-00a281137/)")
        st.markdown("[GitHub](https://github.com/Prabin9618)")
        st.markdown("[Hugging Face](https://huggingface.co/prabin9618)")
        st.markdown("prabindash135@gmail.com")
        st.markdown("+91 9778841064")

st.markdown("####")

st.write("I am a technology geek interested in exploring ML and AI domain. With 4+ years into Data Science and 2+ years working in Azure Cloud, I am interested in exploring fields such as Natural Language Processing and Generative AI. I have experience in building models as well as deploying them over Docker or Cloud platforms")

st.markdown("####")
st.markdown("####")

col_ed1, col_ed2, col_ed3, col_ed4 = st.columns(4)

with col_ed1:
    st.markdown("<h4>EDUCATION</h3>", unsafe_allow_html=True)
    st.markdown("<div>B.Tech (2014-2018)</div>", unsafe_allow_html=True)
    st.write("<div>College of Engineering and Technology</div>", unsafe_allow_html=True)
    st.markdown("<h6>Instrumentation and Electronics Engineering</h6>", unsafe_allow_html=True)
    st.markdown("<div>AISSCE (2012-2014)</div>", unsafe_allow_html=True)
    st.write("<div>Mother's Public School</div>", unsafe_allow_html=True)
    st.markdown("<h6>CBSE</h6>", unsafe_allow_html=True)

with col_ed2:
    st.markdown("<h4>SKILLS</h3>", unsafe_allow_html=True)
    col_skills1, col_skills2 = st.columns([0.5,0.5])
    with col_skills1:
        st.write("<div>Python</div>", unsafe_allow_html=True)
        st.write("<div>Azure Cloud</div>", unsafe_allow_html=True)
        st.write("<div>Tensorflow/Keras</div>", unsafe_allow_html=True)
        st.write("<div>PyTorch</div>", unsafe_allow_html=True)
        st.write("<div>NLP</div>", unsafe_allow_html=True)
        st.write("<div>Docker</div>", unsafe_allow_html=True)
    with col_skills2:
        st.write("<div>SQL</div>", unsafe_allow_html=True)
        st.write("<div>Tableau/Power BI</div>", unsafe_allow_html=True)
        st.write("<div>Flask</div>", unsafe_allow_html=True)
        st.write("<div>Streamlit</div>", unsafe_allow_html=True)
        st.write("<div>Unix/Linux</div>", unsafe_allow_html=True)
        st.write("<div>Git/GitHub</div>", unsafe_allow_html=True)

with col_ed3:
    st.markdown("<h4>CERTIFICATIONS</h3>", unsafe_allow_html=True)
    st.markdown("")
    st.write("<div>AZ900: Azure Fundamentals</div>", unsafe_allow_html=True)
    st.markdown("")
    st.write("<div>DP100: Azure Data Scientist Associate</div>", unsafe_allow_html=True)

with col_ed4:
    st.markdown("<h4>YEARS OF EXPERIENCE</h3>", unsafe_allow_html=True)
    st.write("<div>Total IT Experience: 5 yrs</div>", unsafe_allow_html=True)    
    st.write("<div>Python: 4.5 yrs</div>", unsafe_allow_html=True)
    st.write("<div>Data Science: 4 yrs</div>", unsafe_allow_html=True)
    st.write("<div>SQL: 4 yrs</div>", unsafe_allow_html=True)
    st.write("<div>Cloud(Azure, AWS): 2 yrs</div>", unsafe_allow_html=True)

st.markdown("<h2>EXPERIENCE</h2>", unsafe_allow_html=True)

col_exp1, col_exp2 = st.columns(2)

with col_exp1:
    st.markdown("<h4>KPMG Global Services</h3>", unsafe_allow_html=True)
    st.markdown("<h5>2022-Present</h5>", unsafe_allow_html=True)
    st.markdown(
            """
            - Worked for one of the biggest retail sector firm, developing a spam classification bot
            - Creation of raw dataset by email extraction from client mailbox using Python scripts
            - Building various ML/DL models(Naive Bayes, XGBoost, LSTM) and creating Flask app
            - Deploying Flask app over Azure DevOps pipeline to Azure Web App and integration in Logic apps workflow
            - Implementing solutions to blockers such as non-English language emails using Language Translation, extracting text from embedded images using Image Captioning
            - Utilizing Azure tools such as Azure Machine Learning, Cognitive Services for performance and speed improvement
            - Implemented end-to-end project and deployed to Production including fixing issues during deployment, this solution reduces manual workload by 83%
            """
            )
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
    st.markdown("<h4>Tata Consultancy Services(TCS)</h3>", unsafe_allow_html=True)
    st.markdown("<h5>2018-2022</h5>", unsafe_allow_html=True)
    st.markdown(
            """
            - Worked for one of the biggest banks in Australia, developing a Document Image Processing and intelligent text extraction project, reducing human workload by completing real time work usually done in 3-5 business days to 30 minutes
            - Classifying documents using state-of-the-art Image Classification algorithms like EfficientNet(88.89%), process and extract scanned/printed text using OCR
            - Data and document comparison using fuzzy matching and regex algorithm to highlight key differences
            - Extract text from scanned/searchable PDFs and images using python libraries
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

st.markdown("<h2>PERSONAL PROJECTS</h2>", unsafe_allow_html=True)

col_pp1, col_pp2 = st.columns([0.29,0.71])

with col_pp1:
    # Project 1
    file_ = open("gamerec.gif", "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()

    style_image2 = """
    width: auto;
    max-width: 700px;
    height: auto;
    max-height: 800px;
    display: block;
    justify-content: center;
    border-radius: 5%;
    """
    st.markdown(f'<img src="data:image/gif;base64,{data_url}" style="{style_image2}">',unsafe_allow_html=True)

with col_pp2:
    st.markdown("<h5>Game Recommender System</h5>", unsafe_allow_html=True)
    st.markdown('Domain: Recreation')
    st.markdown('Skills: NLP, ML, Streamlit')
    if st.button("Try it out"):
        webbrowser.open_new_tab("https://huggingface.co/spaces/prabin9618/game-recommender")
