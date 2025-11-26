import streamlit as st
import joblib
import pandas  as pd

model=joblib.load("spam_clf.pkl")

st.set_page_config(layout="wide")

st.sidebar.image("flag.jpg")
st.sidebar.title("👤About Us")
st.sidebar.text("jdshfjjsdfjrusdkjnfkjfrvjkjfrhgvkjnkjfngvjfvnkjfnh")
st.sidebar.title("📞Contact Us")
st.sidebar.text("6909665856")



st.markdown("""
    <div style="background: linear-gradient(to right, #673AB7, #512DA8);
                padding: 15px;
                border-radius: 10px;
                text-align: center;">
        <h1 style="color: white; font-weight: bold;">
            🚫Spam Classifier Project
        </h1>
    </div>
""", unsafe_allow_html=True)


st.text("")
col1,col2=st.columns([1.5,2],gap="large")
with col1:
    st.markdown("""
<div style="background-color:#E3F2FD; padding:10px;
border-radius:10px; text-align:center;">
    <h2 style="color:#0D47A1; font-weight:800;">
        Single Msg Prediction
    </h2>
</div>
""", unsafe_allow_html=True)


    text=st.text_input("Enter MSG")
    if st.button("Predict"):
        result = model.predict([text])
        if result=="spam":
            st.error("Spam->Irrelevant❌")
        else:
            st.success("Ham->Relevant✔")

with col2:
    st.markdown("""
<div style="background-color:#E3F2FD; padding:10px;
border-radius:10px; text-align:center;">
    <h2 style="color:#0D47A1; font-weight:800;">
        Bulk Msg Prediction
    </h2>
</div>
""", unsafe_allow_html=True)
    file=st.file_uploader("select file containing bulk msgs",type=['txt','csv'])
    
    if file!=None:
        df=pd.read_csv(file.name,header=None,names=["Msg"])
        place=st.empty()
        place.dataframe(df)
        if st.button("Predict",key="b2"):
            df['result']=model.predict(df.Msg)
            place.dataframe(df)
            
            
    
