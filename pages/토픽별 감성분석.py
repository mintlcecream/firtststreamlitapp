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

# 데이터 미리보기
st.subheader("데이터 미리보기")
st.dataframe(df.head())

# 감성 분포 시각화
st.subheader("감성 분포")
sentiment_counts = df["Sentiment"].value_counts()
fig = px.pie(sentiment_counts, names=sentiment_counts.index, values=sentiment_counts.values, title="Sentiment Distribution")
st.plotly_chart(fig)

# 특정 키워드 감성 비교
st.subheader("키워드별 감성 분석")
keyword = st.text_input("키워드를 입력하세요:")
if keyword:
    filtered_df = df[df["Text"].str.contains(keyword, case=False, na=False)]
    st.write(f"'{keyword}'이 포함된 트윗 개수: {len(filtered_df)}")
    if not filtered_df.empty:
        keyword_sentiment_counts = filtered_df["Sentiment"].value_counts()
        fig = px.bar(x=keyword_sentiment_counts.index, y=keyword_sentiment_counts.values, labels={'x': 'Sentiment', 'y': 'Count'}, title=f"Sentiment Analysis for '{keyword}'")
        st.plotly_chart(fig)
    else:
        st.write("해당 키워드를 포함하는 트윗이 없습니다.")

# 토픽별 감성 키워드 분포
st.subheader("토픽별 감성 키워드 분석")
fig = px.box(df, x="Topic", y=df.index, color="Sentiment", title="Sentiment Distribution by Topic")
st.plotly_chart(fig)

