import streamlit as st
import pandas as pd
from datetime import datetime, time

st.set_page_config(page_title="📑个人简历生成器", page_icon="", layout="wide")

st.title('📑个人简历生成器')
c1, c2 = st.columns([1, 2])

with c1:
    st.subheader('🖊个人信息表单')
    name = st.text_input('姓名', autocomplete='name', key='name_input')
    job = st.text_input('职位', autocomplete='job', key='job_input')
    phone = st.text_input('电话', autocomplete='phone', key='phone_input')
    email = st.text_input('邮箱', autocomplete='email', key='email_input')
    birthday = st.text_input('出生日期', autocomplete='birthday', key='birthday_input')
    
    def my_format_func(option):
        return f'{option}'
    
    gender = st.radio('选择你的性别：', ['男', '女', '其他'], format_func=my_format_func)
    
    if gender == '男':
        st.write('你的性别是:**男**')
    elif gender == '女':
        st.write('你的性别是:**女**')
    else:
        st.write('你的性别是:**其他**')
    
    education = st.selectbox(
        '学历：', 
        ['小学', '初中', '高中', '大学', '研究生', '博士生'], 
        format_func=my_format_func, 
        index=2
    )
    
    language_options = st.multiselect(
        '语言能力',
        ['中文', '英语', '法语', '西班牙语', '德语', '泰语'],
        format_func=my_format_func,
    )
    
    skills = st.multiselect(
        '技能',
        ['python', 'SQL', '数据分析', '项目管理', 'Java', 'JavaScript'],
        format_func=my_format_func,
    )
    
    experience = st.slider('工作经验（年）', 0, 30, 25)
    
    money = st.slider(
        '期望薪资范围(美元)',
        6000, 55000, (10000, 25000)
    )
    
    introduce = st.text_area(
        label='个人简介：', 
        placeholder='请简要介绍您的专业背景、职业目标和个人特点...'
    )
    
    contact_time = st.time_input("每日最佳联系时间段")  # 避免与导入的time重名
    
    uploaded_file = st.file_uploader("上传你的照片")
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()  # 修复拼写错误


with c2:
    st.subheader('🖊简历实时预览')
    a1, a2 = st.columns(2)
    with a1:      
        st.write('你的姓名是：', name)
        if uploaded_file is not None:
            st.image(uploaded_file, caption='个人照片', width=150)  
        else:
            st.write('未上传照片')  
        st.write('你的职位是：', job)
        st.write('你的电话是：', phone)
        st.write('你的邮箱是：', email)
        st.write('你的出生日期是：', birthday)
        st.write('你的每日最佳联系时间段是：', contact_time)
    with a2:      
        st.write('你的性别是：', gender)
        st.write('你的学历是：', education)
        st.write('你的语言能力是：', language_options)
        st.write('你的技能是：', skills)
        st.write('你的工作经验是：', experience)
        st.write('你的期望薪资范围是：', money)
       
    st.write('你的个人简介是：', introduce)














