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

# 토픽별 감성 키워드 분포 (일렬 정렬)
st.subheader("토픽별 감성 키워드 분석")
topic_sentiment_counts = df.groupby(["Topic", "Sentiment"]).size().reset_index(name="Tweet Count")
fig = px.box(topic_sentiment_counts, x="Topic", y="Tweet Count", color="Sentiment", title="Sentiment Distribution by Topic", points="all")
st.plotly_chart(fig)

# 토픽별 감성 키워드 분포 (일렬 정렬)
st.subheader("토픽별 감성 키워드 분석")
topic_sentiment_counts = df.groupby(["Topic", "Sentiment"]).size().reset_index(name="Tweet Count")
fig = px.box(topic_sentiment_counts, x="Topic", y="Tweet Count", color="Sentiment", title="Sentiment Distribution by Topic", points="all")
st.plotly_chart(fig)
