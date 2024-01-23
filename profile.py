import streamlit as st
import base64
from PIL import Image

st.set_page_config(layout="wide")

with open("style.css") as f:
    css = f.read()

st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

st.markdown("""<style>img{border-radius: 50%;}</style>""", unsafe_allow_html=True)

# Resume PDF file
with open("PD Resume.pdf", "rb") as pdf_file:
    PDFbyte = pdf_file.read()

col1, col2, col3 = st.columns([20,80,20])

with col1:
    st.write("")
    st.write("")
    st.image("Photo.jpg", width=180)

with col2:
    st.markdown("<h1>PRABIN DASH</h1>", unsafe_allow_html=True)
    st.markdown("Data Scientist")
    st.markdown("Bhubaneswar, India")
    st.download_button(
        label="Download Resume",
        data=PDFbyte,
        file_name="Resume_PrabinDash.pdf",
        mime="application/octet-stream",
    )

with col3:
    collink1, collink2 = st.columns(spec=[0.1, 0.9])
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

st.write(
    "I am a technology geek interested in exploring ML and AI domain. With over 5 years into Data Science and more than 2 years working in Cloud, I am interested in exploring fields such as Natural Language Processing and Generative AI. I have extensive hands-on experience in end-to-end implementation of projects as well as deploying them over Docker or Cloud platforms"
)

tab_ex, tab_cert, tab_skills, tab_ed = st.tabs(
    ["Experience", "Certifications", "Skills", "Education"]
)

with tab_ex:
    with st.expander("KPMG Global Services"):
        st.markdown("<h5>2022-Present</h5>", unsafe_allow_html=True)
        st.markdown(
            """
                - Working in developing a Generative AI POC, building systems using ChatGPT API
                - Utilizing internal AI API and prompt engineering concepts to create a POC on document validation as per terms and conditions, building end-to-end system and using Streamlit for building U
                """
        )
        st.markdown("---")
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

    with st.expander("Tata Consultancy Services(TCS)"):
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

with tab_cert:
    colcert1, colcert2 = st.columns(spec=[1,49])
    with colcert1:
        st.image("imgs/azure.png", width=28)
        st.image("imgs/azure.png", width=28)
    with colcert2:
        st.write("Microsoft Azure Fundamentals - AZ900", unsafe_allow_html=True)
        st.write("Microsoft Azure Data Scientist Associate - DP100", unsafe_allow_html=True)

with tab_skills:
    colskills1, colskills2, colskills3, colskills4 = st.columns(spec=[1,24,1,24])
    with colskills1:
        st.image("imgs/python.png", width=28)
        st.image("imgs/azure.png", width=28)
        st.image("imgs/tf.png", width=28)
        st.image("imgs/pytorch.png", width=28)
        st.image("imgs/nlp.jpg", width=28)
        st.image("imgs/docker.png", width=28)
    with colskills2:
        st.write("Python", unsafe_allow_html=True)
        st.write("Azure Cloud", unsafe_allow_html=True)
        st.write("Tensorflow/Keras", unsafe_allow_html=True)
        st.write("PyTorch", unsafe_allow_html=True)
        st.write("NLP", unsafe_allow_html=True)
        st.write("Docker", unsafe_allow_html=True)
    with colskills3:
        st.image("imgs/sql.png", width=28)
        st.image("imgs/pbi.png", width=28)
        st.image("imgs/flask.png", width=28)
        st.image("imgs/streamlit.png", width=28)
        st.image("imgs/unix.png", width=28)
        st.image("imgs/git.png", width=28)
    with colskills4:
        st.write("SQL", unsafe_allow_html=True)
        st.write("Tableau/Power BI", unsafe_allow_html=True)
        st.write("Flask", unsafe_allow_html=True)
        st.write("Streamlit", unsafe_allow_html=True)
        st.write("Unix/Linux", unsafe_allow_html=True)
        st.write("Git/GitHub", unsafe_allow_html=True)

with tab_ed:
    colcert1, colcert2 = st.columns(spec=[1,20])
    with colcert1:
        st.write("")
        st.write("")
        st.image("imgs/graduation.png", width=56)
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.image("imgs/graduation.png", width=56)
        st.write("")
    with colcert2:
        st.write("B.Tech (2014-2018)", unsafe_allow_html=True)
        st.write("College of Engineering and Technology", unsafe_allow_html=True)
        st.write("Instrumentation and Electronics Engineering", unsafe_allow_html=True)
        st.write("AISSCE (2012-2014)", unsafe_allow_html=True)
        st.write("Mother's Public School", unsafe_allow_html=True)
        st.write("CBSE", unsafe_allow_html=True)

st.markdown("<h2>PERSONAL PROJECTS</h2>", unsafe_allow_html=True)

col_pp1, col_pp2 = st.columns([0.29, 0.71])

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
    st.markdown(
        f'<img src="data:image/gif;base64,{data_url}" style="{style_image2}">',
        unsafe_allow_html=True,
    )

with col_pp2:
    st.markdown("<h5>Game Recommender System</h5>", unsafe_allow_html=True)
    st.markdown("Domain: Recreation")
    st.markdown("Skills: NLP, ML, Streamlit")
    # st.write(f'''
    # <a target="_blank" href="https://huggingface.co/spaces/prabin9618/game-recommender">
    #     <button>
    #         Try this out
    #     </button>
    # </a>
    # ''',
    # unsafe_allow_html=True
    # )
    URL_STRING = "https://huggingface.co/spaces/prabin9618/game-recommender"

    st.markdown(
        f'<a href="{URL_STRING}" style="display: inline-block; padding: 8px 10px; background-color: #4CAF50; color: white; text-align: center; text-decoration: none; font-size: 16px; border-radius: 4px;">Try it out</a>',
        unsafe_allow_html=True,
    )
