import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="EDA Project Dashboard", page_icon="📊", layout="wide")

st.title("📊 Exploratory Data Analysis Dashboard")
st.write("Explore patterns, trends, correlations, and key factors influencing student performance.")

df = pd.read_csv("student_performance.csv")

st.sidebar.header("Filters")
min_att = st.sidebar.slider("Minimum Attendance (%)", 40, 100, 40)
max_att = st.sidebar.slider("Maximum Attendance (%)", 40, 100, 100)
filtered = df[(df["Attendance_Percent"] >= min_att) & (df["Attendance_Percent"] <= max_att)]

st.subheader("Dataset Overview")
c1, c2, c3, c4 = st.columns(4)
c1.metric("Records", len(filtered))
c2.metric("Average Final Score", f"{filtered['Final_Score'].mean():.2f}")
c3.metric("Average Attendance", f"{filtered['Attendance_Percent'].mean():.2f}%")
c4.metric("Average Study Hours", f"{filtered['Study_Hours'].mean():.2f}")

st.subheader("Statistical Summary")
st.dataframe(filtered.describe().round(2), use_container_width=True)

col1, col2 = st.columns(2)

with col1:
    st.subheader("Study Hours vs Final Score")
    fig, ax = plt.subplots()
    sns.scatterplot(data=filtered, x="Study_Hours", y="Final_Score", ax=ax)
    ax.set_title("Study Hours and Final Score")
    st.pyplot(fig)

with col2:
    st.subheader("Attendance vs Final Score")
    fig, ax = plt.subplots()
    sns.scatterplot(data=filtered, x="Attendance_Percent", y="Final_Score", ax=ax)
    ax.set_title("Attendance and Final Score")
    st.pyplot(fig)

st.subheader("Distribution of Final Scores")
fig, ax = plt.subplots()
sns.histplot(filtered["Final_Score"], bins=20, kde=True, ax=ax)
ax.set_xlabel("Final Score")
st.pyplot(fig)

st.subheader("Correlation Heatmap")
numeric = filtered.select_dtypes(include="number")
fig, ax = plt.subplots(figsize=(9, 5))
sns.heatmap(numeric.corr(), annot=True, fmt=".2f", cmap="coolwarm", ax=ax)
st.pyplot(fig)

st.subheader("Key Insights")
corr = filtered.corr(numeric_only=True)["Final_Score"].drop("Final_Score").sort_values(ascending=False)
for feature, value in corr.items():
    direction = "positive" if value > 0 else "negative"
    st.write(f"- **{feature}** has a **{direction} correlation** with Final Score ({value:.2f}).")

st.subheader("Filtered Data")
st.dataframe(filtered, use_container_width=True)
