import streamlit as st
import random
import string

# 定义生成密码的函数
def generate_password(length, use_chars):
    characters = ''
    if '小写字母' in use_chars:
        characters += string.ascii_lowercase
    if '大写字母' in use_chars:
        characters += string.ascii_uppercase
    if '数字' in use_chars:
        characters += string.digits
    if '特殊字符' in use_chars:
        characters += string.punctuation
    return ''.join(random.choice(characters) for i in range(length))

# Streamlit应用界面
st.title('随机密码生成器')

# 用户输入
password_length = st.slider('选择密码长度', min_value=6, max_value=128, value=12)
use_chars = st.multiselect('选择使用的字符类型', ['小写字母', '大写字母', '数字', '特殊字符'], default=['小写字母', '大写字母'])

# 生成密码按钮
if st.button('生成密码'):
    generated_password = generate_password(password_length, use_chars)
    st.text_input("生成的密码", generated_password, disabled=True)
