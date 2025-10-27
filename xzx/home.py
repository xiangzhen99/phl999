import streamlit as st
st.title("欢迎来到phl and hqx 主页")
st.write("这个页面来自home.py文件,请单击左侧👈页面,导航到相应页面")
st.set_page_config(page_title='奇思妙想',page_icon='🐈')
images = [{'utl':"https://wallup.net/wp-content/uploads/2018/10/06/520307-pomeranian-dog-dogs.jpg",
           'parm':'摆烂拜拜拜'},
          {'utl': "https://img.keaitupian.cn/newupload/04/1682416672559498.jpg",
           'parm':'!?'},
          {'utl': "https://img.keaitupian.cn/newupload/12/1672138519149011.jpg",
           'parm':'我是笨蛋'},
          {'utl': 'https://n.sinaimg.cn/sinakd20220826s/335/w600h535/20220826/e854-ee2800b519b08a845ffeefe4920f7a8d.png',
           'parm':'好累'},
          {'utl': 'https://img.keaitupian.cn/newupload/02/1675413307459841.jpg',
           'parm':'疯掉了'}]

st.subheader("🐧奇思妙想")
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

