import streamlit as st
import streamlit as st
import pandas as pd

st.title("🥧南宁美食探索")

st.header("🧭南宁美食地图")
restaurants_data = {
    "餐厅": ["六叔烤鱼", "廖哥土鲫鱼", "顺兴川味馆", "甘家界柠檬鸭", "瑶王府"],
    "类型": ["中餐", "中餐", "快餐", "中餐", "中餐"],
    "评分": [4.2, 4.5, 4.0, 4.7, 4.3],
    "人均消费(元)": [100,160,170,190,120],
    "latitude": [22.810903,22.834839,22.845473,22.794860,22.838686],
    "longitude": [108.323087,108.290574,108.232036,108.362962,108.266088]
}
map_data = {
    'latitude': [22.810903,22.834839,22.845473,22.794860,22.838686],
    'longitude':[108.323087,108.290574,108.232036,108.362962,108.266088]

    }
st.map(pd.DataFrame(map_data))

st.title("🥧各餐厅评分数据")
data = {
    '餐馆':["六叔烤鱼", "廖哥土鲫鱼", "顺兴川味馆", "甘家界柠檬鸭", "瑶王府"],
    '评分':[4.2, 4.5, 4.0, 4.7, 4.3],
    }
df = pd.DataFrame(data)
index = pd.Series([1, 2, 3,4,5], name='餐馆评分')
st.subheader("餐馆评分")
st.bar_chart(df, x='餐馆')
df.set_index('餐馆',inplace=True)



data = {
    '月份':['01月', '02月', '03月','04月','05月','06月', '07月', '08月','09月','10月','11月','12月'],
    '六叔烤鱼'  :[200,150,180,190,230,160,170,165,175,156,178,188],
    '廖哥土鲫鱼':[120,160,123,155,166,150,180,190,230,160,170,165],
    '顺兴川味馆':[110,100,160,170,190,120,160,123,155,166,150,180],
    '甘家界牌柠檬鸭':[110,100,160,110,170,180,190,230,160,170,165,175],
    '瑶王府':[110,100,160,180,190,100,160,110,170,180,190,230],
}
df = pd.DataFrame(data)
index = pd.Series([1, 2, 3,4,5,6,7,8,9,10,11,12], name='序号')
df.index = index
st.header('🧮门店数据')
st.write(df)
st.header('💻折线图')
st.subheader("🔋门店月度销售额走势对比")
st.line_chart(df,x='月份')


df.set_index('月份', inplace=True)
st.subheader("💡餐馆对比")
st.line_chart(df, y=["六叔烤鱼"])
st.line_chart(df, y=["六叔烤鱼", "廖哥土鲫鱼"])
st.subheader('🥯餐馆价格条形图')
st.bar_chart(df)
st.subheader('🌭餐馆价格面积图')
st.area_chart(df)
data = {
    '时间':['11点', '12点','13点','14点','15点'],
    '六叔烤鱼'  :[30,50,50,60,70],
    '廖哥土鲫鱼':[40,50,60,70,70],
    '顺兴川味馆':[50,50,50,60,80],
    '甘家界牌柠檬鸭':[60,50,70,50,90],
    '瑶王府':[80,50,80,50,70]
}
df = pd.DataFrame(data)
index = pd.Series([1, 2, 3,4,5], name='序号')
df.index = index
st.header('🔔用餐时间')
st.write(df)
st.header('📝面积图')
st.subheader('🎹用餐时间对比')
st.area_chart(df,x='时间')
import streamlit as st
import time
st.header("当前拥挤程度")
progress_text_1 = ("正在排队中")
my_bar = st.progress(0, text=progress_text_1)
time.sleep(0.5)

for percent in range(80):
    time.sleep(0.1)
    my_bar.progress(percent+1,text=f'{progress_text_1},当前拥挤程度{percent}%:hourglass:')

for percent in range(80,100):
    time.sleep(0.05)
    my_bar.progress(percent + 1,text=f'程序马上就要完成了,当前进度{percent}%:hourglass:')






