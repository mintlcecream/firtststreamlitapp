import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# 데이터 로드
def load_data():
    file_path = "twitter_training.csv"
    columns = ["ID", "Topic", "Sentiment", "Text"]
    df = pd.read_csv(file_path, names=columns, skiprows=1)  # 첫 번째 행 스킵 (컬럼명 없음)
    return df

df = load_data()

# 스트림릿 앱 설정
st.title("Twitter Sentiment Analysis")


# 토픽별 감성 분석 요약 표 & 그래프
st.subheader("토픽별 감성 분석 요약")
topic_summary = df.groupby(["Topic", "Sentiment"]).size().unstack(fill_value=0)
st.dataframe(topic_summary)
fig = px.bar(topic_summary, barmode="group", title="Sentiment Count per Topic")
st.plotly_chart(fig)
