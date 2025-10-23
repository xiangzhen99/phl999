import streamlit as st

st.text("小猫咪喵喵喵")
st.image("https://img95.699pic.com/photo/60063/8518.jpg_wh860.jpg", caption='小猫')
import streamlit as st
st.set_page_config(page_title='小猫咪',page_icon='🐈')
images = [{'utl':"https://i.pinimg.com/originals/fe/10/4f/fe104f1e3ecd77bbffc4167160e09b9c.jpg",
           'parm':'小猫1'},
          {'utl': "https://www.holidaysmart.com/sites/default/files/dailyimage/og/2022/cat-scottish-fold-day.jpg",
           'parm':'小猫2'},
          {'utl': "https://images2.alphacoders.com/121/1213770.jpg",
           'parm':'小猫3'},
          {'utl': 'https://www.thehappycatsite.com/wp-content/uploads/2020/12/What-does-it-mean-if-a-cat-winks-at-you-HC-long.jpg',
           'parm':'小猫4'},
          {'utl': 'https://www.ajdesigner.com/fl_cat_age/cat_1200_630.png',
           'parm':'小猫5'}]

st.subheader("展示多个图片")
if'ind' not in st.session_state:
    st.session_state['ind']=0
    
def nextIMG():
   st.session_state['ind']=(st.session_state['ind']+1)%len(images)
st.image(images[st.session_state['ind']]['utl'],caption=images[st.session_state['ind']]['parm'])   
    
def prevIMG():
   st.session_state['ind']=(st.session_state['ind']-1)%len(images)
col1,col2=st.columns(2)
with col1:
     st.button('上一张',on_click=prevIMG,use_container_width=True)
with col2:
     st.button('下一张',on_click=nextIMG,use_container_width=True)

