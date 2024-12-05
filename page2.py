import streamlit as st

name = st.text_input('請輸入你的名字')
if name:
    st.write(f'你好, {name}!')

st.divider()

password = st.text_input('請輸入密碼', type='password')
if password:
    st.write(f'你的密碼是: {password}')

st.divider()

paragraph = st.text_area('請輸入一些文字')

st.divider()
age = st.number_input('請輸入你的年齡',value=20, min_value=1, max_value=100, step=3)
st.write(f'你的年齡是: {age}')

st.divider()
checked = st.checkbox('我同意條款')
if checked:
    st.write('你已經同意條款')

st.divider()
submitted = st.button('送出')
if submitted:
    st.write('已送出')