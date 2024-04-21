import streamlit as st
import base64
from annotated_text import annotated_text, annotation
from htbuilder import styles

st.set_page_config(layout="wide")

with open("style.css") as f:
    css = f.read()

st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

st.markdown("""<style>img{border-radius: 50%;}</style>""", unsafe_allow_html=True)

# Resume PDF file
with open("PD Resume.pdf", "rb") as pdf_file:
    PDFbyte = pdf_file.read()

col1, col2 = st.columns([30,70])

with col1:
    colleft1, colleft2, colleft3 = st.columns(spec=[0.25,0.5,0.25])
    with colleft2:
        st.image('Photo.jpg', width=180)
        st.download_button(
            label="Download Resume",
            data=PDFbyte,
            file_name="Resume_PrabinDash.pdf",
            mime="application/octet-stream",
        )

    space1, space2, collink1, collink2 = st.columns(spec=[0.1,0.1,0.1,0.7])
    with collink1:
        st.image("imgs/linkedin.png",width=24)
        st.image("imgs/github.png",width=24)
        st.image("imgs/huggingface.png",width=24)
        st.image("imgs/mail.png",width=24)
        st.image("imgs/phone.png",width=24)
    with collink2:
        st.markdown("[LinkedIn](https://www.linkedin.com/in/prabin-dash-00a281137/)")
        st.markdown("[GitHub](https://github.com/Prabin9618)")
        st.markdown("[Hugging Face](https://huggingface.co/prabin9618)")
        st.markdown("prabindash135@gmail.com")
        st.markdown("+91 9778841064")

with col2:
    font_css = """
    <style>
    button[data-baseweb="tab"] > div[data-testid="stMarkdownContainer"] > p {
    font-size: 18px;
    }
    </style>
    """
    st.write(font_css, unsafe_allow_html=True)

    tab_about, tab_ex, tab_cert, tab_skills, tab_ed, tab_works = st.tabs(
        ["About Me","Experience", "Certifications", "Skills", "Education", "Projects"]
    )

    with tab_about:
        intro1, intro2 = st.columns(2)
        with intro1:
            annotated_text(annotation("Hi! I am","","#ffffff",font_family="sans-serif",font_size="30px"))
            annotated_text(annotation("Prabin Dash","","#ffffff",font_family="sans-serif",font_size="30px"))
        with intro2:
            st.markdown("")
            annotated_text(annotation("Data Scientist","","#0099ff","#ffffff",font_family="sans-serif",font_size="50px"))
        
        st.markdown("")
        annotated_text(annotation('''I am a technology geek interested in exploring ML and AI domain. With over 5 years into Data Science 
                            and more than 3 years working in Cloud, I am interested in exploring fields such as Natural Language Processing 
                            and Generative AI. I have extensive hands-on experience in end-to-end implementation of projects as well as 
                            deploying them over Docker or Cloud platforms''',"","#ffffff",font_family="sans-serif",font_size="20px"))
    with tab_ex:
        with st.expander("KPMG Global Services"):
            st.markdown("<h5>2022-Present</h5>", unsafe_allow_html=True)
            st.markdown(
                """
                    - Type - Generative AI (POC)
                    - Domain - Business/Resourcing
                    - Skills Utilized - Prompt Engineering, OpenAI API, Streamlit
                    - Deployment - Streamlit UI
                    - Summary - Built Gen AI POCs via Prompt Engineering, Building systems using ChatGPT API and deployed in Streamlit UI
                    - Real-life impact - Business Teams(BAs, HRs etc.)
                    """
            )
            st.markdown("---")
            st.markdown(
                """
                    - Type - Text Classification(Machine Learning/Deep Learning)
                    - Domain - Retail
                    - Skills Utilized - Machine Learning/Deep Learning, Azure Machine Learning, Azure DevOps, Azure Cognitive Services, Flask
                    - Deployment - Azure Web App, Azure Container Instances, Azure Cognitive Services
                    - Summary - Building a Spam Classification bot, utilizing various Azure Services for accuracy and efficiency, integration with primary pipeline in Azure Logic Apps and deploying to Production
                    - Blockers - Implementing solutions to blockers such as non-English language emails using Language Translation, extracting text from embedded images using Image Captioning
                    - Real-life impact - Reducing manual workload by 83%
                    """
            )
            st.markdown("---")
            st.markdown(
                """
                    - Type - Time Series Forecasting/Anomaly Detection(Machine Learning/Deep Learning)
                    - Domain - Pharmaceutical sales
                    - Skills Utilized - Machine Learning/Deep Learning, Azure Machine Learning, Azure Data Factory, PowerBI
                    - Deployment - Azure Container Instances, models consumed in PowerBI
                    - Summary - Implementing a multi-item/multi-org sales forecasting model for SAP, building an Anomaly detection model for detecting anomalous sales records
                    - Real-life impact - Analytics Insights Dashboard
                    """
            )

        with st.expander("Tata Consultancy Services(TCS)"):
            st.markdown("<h5>2018-2022</h5>", unsafe_allow_html=True)
            st.markdown(
                """
                    - Type - Document Image Processing and text extraction(Computer Vision)
                    - Domain - Banking and Financial Services(BFSI)
                    - Skills Utilized - Deep Learning(CNN, SOTA), OCR, PDF processing
                    - Deployment - Docker (Client Environment)
                    - Summary - Classifying documents using state-of-the-art Image Classification algorithms like EfficientNet(88.89%), process and extract scanned/printed text using OCR, Data and document comparison using fuzzy matching and regex algorithm to highlight key differences, Extract text from scanned/searchable PDFs and images using python libraries, Extract information from structured/unstructured texts automatically, review the exceptions and recommend updates in the model for improved extraction
                    - Real-life impact - Reducing human workload by completing real time work usually done in 3-5 business days to 30 minutes
                    """
            )
            st.markdown("---")
            st.markdown(
                """
                    - Type - Time Series Forecasting(Machine Learning)
                    - Domain - Banking and Financial Services(BFSI)
                    - Skills Utilized - Python, Oracle Database, Unix
                    - Deployment - Analytics Dashboard
                    - Summary - Extracting huge chunks of data from Oracle database, analyzing them using Python Data Analysis tools, providing insights to clients, Analyzing transactional processing data, implementing forecasting models to forecast weekly, monthly and quarterly expected loads, which helps reduce system downtime by 78%, Trend Forecasting, Capacity report analysis, Dashboard preparation for monthly/quarterly processing and highlighting performance issues
                    - Real-life impact - Analytics Insights, Internal Teams
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

    with tab_works:
        col_pp1, col_pp2 = st.columns(2)

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
