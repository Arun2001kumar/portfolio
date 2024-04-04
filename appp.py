import streamlit as st

# Sidebar
st.sidebar.title('Arunkumar H V')
st.sidebar.header('Contact')
st.sidebar.write("Email: arunkumarhv14@gmail.com")
st.sidebar.write("github: [Arun2001kumar](https://github.com/arun2001kumar)")
st.sidebar.write("LinkedIn: [Arunkumar H V](https://www.linkedin.com/in/arunkumar-h-v-5812b8232/)")
st.sidebar.header('Skills')
skills = ['Python', 'Machine Learning', 'Data Analysis', 'Power BI','Tableau', 'SQL', 'Statistical Modeling','AWS GLUE','AWS QuickSight','AWS DynamoDB','AZURE DataBrick','Azure Data Pipeline','Pyspark']
for skill in skills:
    st.sidebar.write(skill)

st.markdown(
    """
    <style>
    .main {
        background: linear-gradient(to right, #FFB6C1, #87CEFA);
        color: black;
        padding: 20px;
        margin: 20px;
        border-radius: 10px;
    }
    .headline {
        color: #003366;
    }
    .sidebar .sidebar-content {
        background: linear-gradient(to right, #FFE4B5, #87CEEB);
        color: white;
        padding: 20px;
        margin: 20px;
        border-radius: 10px;
    }
    .sidebar .sidebar-content p {
        margin: 0;
    }
    .project-name, .education {
        color: purple;
        font-size: 24px; /* Adjust the font size as desired */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# About Me Section
st.markdown("<h2 class='headline'>About Me</h2>", unsafe_allow_html=True)
st.write("I am a passionate Software engineer data scientist with expertise in machine learning, data analysis, and visualization. I hold a Master degree in Computer Science and have experience working with various industries.")

# Experience Section
st.markdown("<h2 class='headline'>Experience</h2>", unsafe_allow_html=True)
st.write("Data Analyst Intern at Elementure Pvt Ltd (June 2023 - septumber 2023)")
st.write("- Utilized data acquisition techniques to gather information from Aquesa smart water meters, ensuring a comprehensive dataset for analysis")
st.write("- Employed data preprocessing methods to clean, transform, and organize raw data, enhancing its quality and usability for analysis purposes.")
st.write("- Leveraged statistical analysis and visualization techniques to extract insights from the collected data, enabling informed decision-making for water efficiency improvements and leak detection")
st.write("- Applied analytical models to identify patterns and trends in water usage data, facilitating the optimization of water distribution systems and the implementation of strategies for enhancing water conservation efforts.")
st.write("- Developed machine learning models for predictive maintenance")
st.write("- Conducted data analysis to identify key insights for business strategy")

# Projects Section
st.markdown("<h2 class='headline'>Projects</h2>", unsafe_allow_html=True)

# Project 1: E-commerce Sales Prediction
st.markdown("<h3 class='project-name'>Project 1: Al-based learning platform is developed using  Django (Python)</h3>", unsafe_allow_html=True)
st.write("- Utilized HTML, CSS, JavaScript, and Django (Python) to create an AI-based learning platform.")
st.write("- Incorporated OpenAI API GPT-4 to generate scripts and quizzes dynamically, enhancing the learning experience with interactive content")
st.write("- Implemented D-ID API to generate videos featuring user-created avatars and voices, providing a personalized touch to the learning process.")
st.write("- By leveraging AI capabilities, the platform offers dynamic and interactive content, catering to individual learning preferences and improving engagement.")
st.write("- Combining AI-driven content generation with personalized videos, the platform provides a comprehensive learning environment, fostering both knowledge retention and user engagement.")

# Project 2: Customer Churn Analysis
st.markdown("<h3 class='project-name'>Project 2: Fake News Detection using Machine Learning</h3>", unsafe_allow_html=True)
st.write("- Developed a machine learning system to detect fake news by identifying and verifying false or misleading information in news articles and online content.")
st.write("- Implemented Naïve Bayes, Decision Tree, Logistic Regression, and Gradient Boosting algorithms to classify news articles as fake or genuine based on various features.")
st.write("- Preprocessed the news data to extract relevant features such as word frequency, sentiment analysis, and credibility of sources")
st.write("- Evaluated the performance of each algorithm using metrics like accuracy, precision, recall, and F1-score to determine the most effective approach.")
st.write("- By automating the detection process, the system contributes to maintaining information accuracy and integrity, thereby mitigating the spread of misinformation and promoting trustworthy sources.")

# Project 3: Sentiment Analysis on Twitter Data
st.markdown("<h3 class='project-name'>Project 3: Multi-stage Continuous-flow Manufacturing Process Prediction</h3>", unsafe_allow_html=True)
st.write("- Utilized real process data from a continuous manufacturing line spanning several hours.")
st.write("- Aimed to predict certain properties of the factory output based on various input data collected during the production run.")
st.write("- Addressed the challenges of predicting output properties in a high-speed, continuous manufacturing process with parallel and series stages.")
st.write("- Engineered features from the input data to capture relevant information about the manufacturing process, such as temperature, pressure, and flow rates.")
st.write("- Developed predictive models using machine learning techniques such as regression or time series analysis to forecast factory output properties, aiding in process optimization and quality control.")

# Education Section
st.markdown("<h2 class='headline'>Education</h2>", unsafe_allow_html=True)
st.markdown("<h3 class='education'>Master of Computer Application (MCA)</h3>", unsafe_allow_html=True)
st.write("- krupanidhi group of Institution (Bengaluru North University )") 
st.write("- January 2022-Octomber 2023(Bengaluru North University")
st.markdown("<h3 class='education'>Bachelor of Science(B.sc)</h3>", unsafe_allow_html=True)
st.write("- Sarada Vilas College Mysore (MYSORE UNIVERSITY)") 
st.write("- Jun 2018 – sept 2021")
# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.write("Thank you for visiting my portfolio! Feel free to reach out for collaborations or inquiries.")
