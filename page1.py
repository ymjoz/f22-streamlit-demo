import streamlit as st
import pandas as pd

st.title('測試網站 🇯🇵 🇰🇷')
st.write('## Page1,下午好！')
st.image('./baseball.png', width=200)

df = pd.DataFrame({"學號": ["004","008","018", "093", "052"],
              "班級": ["12班", "1班", "4班", "7班", "6班"],
              "成績": [92, 68, 95, 43, 77],
              "隊伍": ["巨人", "養樂多", "巨人", "火腿", "歐力士"]})

# st.write('---')
st.divider()
st.dataframe(df)